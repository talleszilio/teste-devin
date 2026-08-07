# Scripts de IA - Ambiente de Desenvolvimento

Guia para configurar e executar os scripts práticos do plano de estudo.

## 🚀 Configuração Rápida

### 1. Instalar Python
Certifique-se de ter Python 3.9+ instalado:
```bash
python --version
```

### 2. Criar Ambiente Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar API Keys

#### Opção A: Variáveis de Ambiente (Recomendado)
```bash
# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="sua-chave-aqui"
$env:OPENAI_API_KEY="sua-chave-aqui"

# Windows (CMD)
set ANTHROPIC_API_KEY=sua-chave-aqui
set OPENAI_API_KEY=sua-chave-aqui

# Linux/Mac
export ANTHROPIC_API_KEY="sua-chave-aqui"
export OPENAI_API_KEY="sua-chave-aqui"
```

#### Opção B: Arquivo .env
Crie arquivo `.env`:
```
ANTHROPIC_API_KEY=sua-chave-aqui
OPENAI_API_KEY=sua-chave-aqui
```

E adicione ao início dos scripts:
```python
from dotenv import load_dotenv
load_dotenv()
```

### 5. Obter API Keys

#### Anthropic (Claude)
1. Acesse: https://console.anthropic.com/
2. Crie conta
3. Vá em "API Keys"
4. Crie nova key
5. Créditos grátis disponíveis para testes

#### OpenAI (GPT)
1. Acesse: https://platform.openai.com/
2. Crie conta
3. Vá em "API Keys"
4. Crie nova key
5. Adicione créditos (mínimo $5)

---

## 📁 Estrutura de Scripts

```
scripts_ia/
├── 01_api_basica.py           # Uso básico de APIs de LLM
├── 02_rag_simples.py          # Sistema RAG completo
├── 03_agente_simples.py       # Agente com tool use
├── requirements.txt           # Dependências
└── README.md                  # Este arquivo
```

---

## 🎯 Scripts e Objetivos

### 1. API Básica (`01_api_basica.py`)
**Dia do plano**: Dia 4

**O que aprende**:
- Fazer chamadas a APIs de LLM
- Usar streaming para respostas em tempo real
- Entender parâmetros (temperature, max_tokens)
- Estimar custos por tokens
- System prompts e personas

**Como executar**:
```bash
python 01_api_basica.py
```

**Pré-requisitos**:
- ANTHROPIC_API_KEY configurada
- OPENAI_API_KEY (opcional, para exemplos GPT)

---

### 2. RAG Simples (`02_rag_simples.py`)
**Dia do plano**: Dia 6

**O que aprende**:
- Chunking de documentos
- Embeddings com SentenceTransformers
- Vector database com ChromaDB
- Retrieval por similaridade
- Geração com contexto (RAG)

**Como executar**:
```bash
python 02_rag_simples.py
```

**Pré-requisitos**:
- ANTHROPIC_API_KEY configurada
- Downloads automáticos de modelo e dependências

**Saída**:
- Banco de dados ChromaDB em `./chroma_db`
- Documentos indexados e recuperáveis

---

### 3. Agente Simples (`03_agente_simples.py`)
**Dia do plano**: Dia 5

**O que aprende**:
- Tool use (function calling)
- Loop de agente (pensar → agir → observar)
- Múltiplas ferramentas
- Chain-of-thought
- Especialização de agentes

**Como executar**:
```bash
python 03_agente_simples.py
```

**Pré-requisitos**:
- ANTHROPIC_API_KEY configurada

**Ferramentas incluídas**:
- WeatherTool (clima simulado)
- CalculatorTool (cálculos matemáticos)
- SearchTool (busca simulada)

---

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError"
**Solução**: Instale as dependências:
```bash
pip install -r requirements.txt
```

### Erro: "ANTHROPIC_API_KEY not configured"
**Solução**: Configure a variável de ambiente:
```bash
export ANTHROPIC_API_KEY="sua-chave"
```

### Erro: "ChromaDB initialization error"
**Solução**: Verifique permissões de escrita no diretório atual

### Download lento de modelo SentenceTransformers
**Solução**: O modelo é baixado na primeira execução (~100MB). Seja paciente ou use VPN se necessário.

### Erro de quota/limite da API
**Solução**: 
- Verifique seu saldo no console da API
- Espere reset de rate limits
- Use modelo menor se disponível

---

## 💡 Dicas de Uso

### Para Desenvolvimento
- Use `print()` extensivamente para debugar
- Comece com temperature baixa (0.1-0.3) para respostas mais previsíveis
- Limpe o banco de dados ChromaDB periodically: `rm -rf ./chroma_db`

### Para Produção
- Nunca commit API keys
- Use logging em vez de print
- Implemente retry logic para chamadas de API
- Monitore custos com contagem de tokens

### Para Aprendizado
- Leia o código antes de executar
- Modifique parâmetros e veja resultados
- Adicione suas próprias ferramentas ao agente
- Indexe seus próprios documentos no RAG

---

## 📚 Recursos Adicionais

### Documentação
- [Anthropic API Docs](https://docs.anthropic.com/)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [ChromaDB Docs](https://docs.trychroma.com/)
- [SentenceTransformers](https://www.sbert.net/)

### Comunidades
- Discord: LangChain, LlamaIndex
- Reddit: r/MachineLearning, r/LocalLLM

---

## 🚀 Próximos Passos

Após executar os scripts básicos:

1. **Estender o RAG**:
   - Adicionar seus próprios documentos
   - Experimentar diferentes chunk sizes
   - Implementar re-ranking

2. **Melhorar o Agente**:
   - Adicionar ferramentas reais (APIs de clima, busca)
   - Implementar memória persistente
   - Criar agentes multi-especialistas

3. **Integrar Frameworks**:
   - Experimentar LangChain
   - Testar LlamaIndex
   - Explorar CrewAI

---

## 📝 Notas

- Os scripts usam APIs pagas. Monitore seus custos!
- SentenceTransformers roda localmente (sem custo após download)
- ChromaDB é local e gratuito
- Em produção, considere vector databases gerenciados (Pinecone, Weaviate)

---

## 🆘 Suporte

Se encontrar problemas:
1. Verifique se Python é 3.9+
2. Confirme que todas dependências estão instaladas
3. Valide suas API keys
4. Consulte documentação oficial das APIs

Boa sorte com seus estudos de IA! 🎓
