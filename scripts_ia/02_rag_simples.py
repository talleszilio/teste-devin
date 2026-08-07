"""
Script 2: RAG Simples - Retrieval-Augmented Generation
Objetivo: Implementar sistema RAG básico
Dia do plano: Dia 6
"""

import os
from typing import List, Dict
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from anthropic import Anthropic

# Configuração
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

class RAGSystem:
    """Sistema RAG simples usando ChromaDB e SentenceTransformers"""
    
    def __init__(self, collection_name: str = "meus_documentos"):
        """Inicializa o sistema RAG"""
        # Inicializa modelo de embeddings (local e gratuito)
        print("Carregando modelo de embeddings...")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Inicializa ChromaDB (vector database local)
        print("Inicializando ChromaDB...")
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )
        
        # Inicializa cliente Anthropic
        self.anthropic = Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None
        
        print("✅ Sistema RAG inicializado!")
    
    def chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """
        Divide texto em chunks com overlap
        
        Args:
            text: Texto para dividir
            chunk_size: Tamanho do chunk em caracteres
            overlap: Sobreposição entre chunks
        
        Returns:
            Lista de chunks
        """
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - overlap  # Overlap
        
        return chunks
    
    def add_documents(self, documents: List[Dict[str, str]]):
        """
        Adiciona documentos ao índice
        
        Args:
            documents: Lista de dicts com 'text' e 'metadata'
        """
        print(f"\nAdicionando {len(documents)} documentos...")
        
        all_chunks = []
        all_metadata = []
        all_ids = []
        
        for idx, doc in enumerate(documents):
            text = doc['text']
            metadata = doc.get('metadata', {})
            
            # Chunk o documento
            chunks = self.chunk_text(text)
            
            for chunk_idx, chunk in enumerate(chunks):
                all_chunks.append(chunk)
                all_metadata.append({
                    **metadata,
                    'doc_id': idx,
                    'chunk_id': chunk_idx
                })
                all_ids.append(f"doc_{idx}_chunk_{chunk_idx}")
        
        # Gerar embeddings
        print("Gerando embeddings...")
        embeddings = self.embedding_model.encode(all_chunks).tolist()
        
        # Adicionar ao ChromaDB
        self.collection.add(
            documents=all_chunks,
            embeddings=embeddings,
            metadatas=all_metadata,
            ids=all_ids
        )
        
        print(f"✅ {len(all_chunks)} chunks indexados!")
    
    def retrieve(self, query: str, n_results: int = 3) -> List[Dict]:
        """
        Recupera chunks relevantes para a query
        
        Args:
            query: Pergunta ou consulta
            n_results: Número de resultados a retornar
        
        Returns:
            Lista de chunks relevantes com metadata
        """
        # Gerar embedding da query
        query_embedding = self.embedding_model.encode([query]).tolist()
        
        # Buscar no ChromaDB
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        
        # Formatar resultados
        retrieved = []
        for i in range(len(results['documents'][0])):
            retrieved.append({
                'text': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i]
            })
        
        return retrieved
    
    def generate_response(self, query: str, context_chunks: List[Dict]) -> str:
        """
        Gera resposta usando LLM com contexto recuperado
        
        Args:
            query: Pergunta do usuário
            context_chunks: Chunks recuperados
        
        Returns:
            Resposta gerada
        """
        if not self.anthropic:
            return "API Key da Anthropic não configurada"
        
        # Construir prompt com contexto
        context_text = "\n\n".join([
            f"[Fragmento {i+1}]: {chunk['text']}"
            for i, chunk in enumerate(context_chunks)
        ])
        
        prompt = f"""Você é um assistente útil que responde perguntas baseado em contextos fornecidos.

CONTEXTO:
{context_text}

PERGUNTA: {query}

INSTRUÇÕES:
- Responda baseando-se APENAS no contexto fornecido
- Se a resposta não estiver no contexto, diga "Não consigo responder com as informações disponíveis"
- Seja conciso e direto
- Cite qual fragmento usou na resposta

RESPOSTA:"""
        
        # Chamar API
        response = self.anthropic.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
    
    def query(self, question: str, n_chunks: int = 3) -> Dict:
        """
        Faz query completa: retrieve + generate
        
        Args:
            question: Pergunta do usuário
            n_chunks: Número de chunks a recuperar
        
        Returns:
            Dict com chunks recuperados e resposta gerada
        """
        print(f"\n🔍 Processando pergunta: '{question}'")
        
        # Recuperar chunks relevantes
        print("Recuperando contexto...")
        chunks = self.retrieve(question, n_results=n_chunks)
        
        print(f"✅ {len(chunks)} chunks recuperados")
        
        # Gerar resposta
        print("Gerando resposta...")
        response = self.generate_response(question, chunks)
        
        return {
            'question': question,
            'retrieved_chunks': chunks,
            'answer': response
        }


def exemplo_uso():
    """Exemplo completo de uso do sistema RAG"""
    
    # Documentos de exemplo
    documentos = [
        {
            'text': """
            A Amazon Web Services (AWS) é uma plataforma de computação em nuvem 
            oferecida pela Amazon. Lançada em 2006, a AWS fornece serviços como 
            computação (EC2), armazenamento (S3), bancos de dados (RDS) e muito mais.
            É a líder de mercado em computação em nuvem com participação de cerca de 32%.
            
            Principais serviços da AWS:
            - EC2: Elastic Compute Cloud para computação
            - S3: Simple Storage Service para armazenamento
            - RDS: Relational Database Service para bancos de dados
            - Lambda: Computação serverless
            """,
            'metadata': {'source': 'aws_overview.txt', 'topic': 'aws'}
        },
        {
            'text': """
            O Google Cloud Platform (GCP) é o serviço de computação em nuvem do Google.
            Oferece serviços de computação, armazenamento, machine learning e big data.
            O GCP é conhecido por suas capacidades em IA/ML e preços competitivos.
            
            Principais serviços do GCP:
            - Compute Engine: Máquinas virtuais
            - Cloud Storage: Armazenamento de objetos
            - BigQuery: Data warehouse
            - Vertex AI: Plataforma de machine learning
            """,
            'metadata': {'source': 'gcp_overview.txt', 'topic': 'gcp'}
        },
        {
            'text': """
            Microsoft Azure é a plataforma de nuvem da Microsoft. Lançada em 2010,
            oferece integração forte com produtos Microsoft como Windows Server e Office 365.
            Azure é popular entre empresas enterprise.
            
            Principais serviços do Azure:
            - Virtual Machines: Computação
            - Blob Storage: Armazenamento
            - Azure SQL: Banco de dados
            - Azure Functions: Computação serverless
            """,
            'metadata': {'source': 'azure_overview.txt', 'topic': 'azure'}
        }
    ]
    
    # Inicializar sistema
    rag = RAGSystem()
    
    # Adicionar documentos
    rag.add_documents(documentos)
    
    # Fazer queries
    queries = [
        "Quais são os principais serviços da AWS?",
        "O que o Google Cloud oferece de Machine Learning?",
        "Qual nuvem é melhor para empresas que usam Microsoft?"
    ]
    
    for query in queries:
        print("\n" + "=" * 60)
        result = rag.query(query)
        
        print("\n📚 Contexto Recuperado:")
        for i, chunk in enumerate(result['retrieved_chunks']):
            print(f"\nFragmento {i+1} (distância: {chunk['distance']:.3f}):")
            print(chunk['text'][:200] + "...")
        
        print("\n💡 Resposta Gerada:")
        print(result['answer'])
        print("=" * 60)


def teste_chunking():
    """Testa diferentes estratégias de chunking"""
    print("\n" + "=" * 60)
    print("Teste de Chunking")
    print("=" * 60)
    
    texto = "A " * 100 + "Inteligência Artificial é transformadora. " * 50
    
    rag = RAGSystem()
    
    # Testar diferentes tamanhos
    tamanhos = [200, 500, 1000]
    
    for tamanho in tamanhos:
        chunks = rag.chunk_text(texto, chunk_size=tamanho, overlap=50)
        print(f"\nChunk size {tamanho}: {len(chunks)} chunks")
        print(f"Primeiro chunk: {chunks[0][:100]}...")
        print(f"Último chunk: {chunks[-1][:100]}...")


def main():
    """Executa exemplos"""
    print("=" * 60)
    print("Script 2: RAG Simples - Retrieval-Augmented Generation")
    print("=" * 60)
    
    try:
        # Exemplo principal
        exemplo_uso()
        
        # Teste de chunking
        teste_chunking()
        
        print("\n" + "=" * 60)
        print("✅ Exemplos RAG executados com sucesso!")
        print("=" * 60)
        print("\n💡 Dica: O banco de dados ChromaDB foi salvo em ./chroma_db")
        print("Você pode adicionar seus próprios documentos!")
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
