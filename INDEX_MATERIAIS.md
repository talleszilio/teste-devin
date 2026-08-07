# 📚 Índice de Materiais - Plano de Estudo de IA

Todos os materiais criados para seu plano de 2 semanas de estudo de IA.

---

## 🎯 Visão Geral

Você tem agora um conjunto completo de materiais para se tornar referência em IA na sua equipe:

- ✅ **Glossário técnico** (50+ termos explicados)
- ✅ **Scripts práticos** (API, RAG, Agentes)
- ✅ **Templates de prompts** (biblioteca reutilizável)
- ✅ **Ambiente configurado** (Python + dependências)
- ✅ **Recursos em português** (cursos, canais, comunidades)

---

## 📁 Estrutura de Arquivos

```
C:\Users\talle\
├── glossario_ia_completo.md          # Glossário técnico detalhado
├── recursos_portugues.md              # Recursos em português
├── INDEX_MATERIAIS.md                # Este arquivo
│
├── scripts_ia/                       # Ambiente de desenvolvimento
│   ├── 01_api_basica.py             # Script de APIs de LLM
│   ├── 02_rag_simples.py            # Script de RAG
│   ├── 03_agente_simples.py         # Script de Agentes
│   ├── requirements.txt             # Dependências Python
│   ├── .env.example                 # Exemplo de configuração
│   ├── setup.bat                    # Setup automático (Windows)
│   ├── setup.sh                     # Setup automático (Linux/Mac)
│   ├── README.md                    # Documentação dos scripts
│   └── GUIA_SETUP.md                # Guia de setup detalhado
│
└── templates_prompts/
    └── prompts_reutilizaveis.md     # Biblioteca de prompts
```

---

## 🚀 Como Começar

### Passo 1: Configurar Ambiente (10 minutos)
```bash
cd scripts_ia
# Windows
setup.bat

# Linux/Mac
bash setup.sh
```

### Passo 2: Obter API Keys (5 minutos)
1. [Anthropic Console](https://console.anthropic.com/) - grátis
2. Copie API key e configure em `.env`

### Passo 3: Executar Primeiro Script (5 minutos)
```bash
# Ativar ambiente
venv\Scripts\activate.bat  # Windows
source venv/bin/activate   # Linux/Mac

# Executar
python 01_api_basica.py
```

### Passo 4: Começar Estudo Estruturado
Siga o plano de 2 semanas (veja abaixo)

---

## 📖 Conteúdo Detalhado

### 1. Glossário de IA (`glossario_ia_completo.md`)

**Conteúdo**: 50+ termos técnicos explicados detalhadamente

**Seções**:
- Fundamentos (AI, ML, DL, GenAI)
- Arquitetura (Transformer, Attention, Token)
- Treinamento (Pre-training, Fine-tuning, RLHF)
- Inferência (Temperature, Streaming, Latency)
- APIs (Rate limits, Chunking, Batching)
- Agentes (Tool use, Memory, Chain-of-Thought)
- RAG (Vector DB, Embeddings, Retrieval)
- Avaliação (Benchmarks, Metrics, Hallucination)
- Produção (Serverless, Caching, Observability)
- Segurança (Prompt Injection, Guardrails)
- Ferramentas (LangChain, LlamaIndex)
- Casos de Uso (Chatbots, Code Assistants)

**Como usar**:
- Marque termos que domina com ✓
- Adicione exemplos próprios
- Use como referência durante estudos

---

### 2. Scripts Práticos (`scripts_ia/`)

#### **01_api_basica.py** - Dia 4 do plano
**O que aprende**:
- Fazer chamadas a APIs de LLM
- Usar streaming
- Entender parâmetros (temperature, max_tokens)
- Estimar custos
- System prompts

**Exemplos incluídos**:
- Chamada básica Anthropic
- Streaming em tempo real
- Comparação de parâmetros
- Contagem de tokens
- System prompts diferentes

#### **02_rag_simples.py** - Dia 6 do plano
**O que aprende**:
- Chunking de documentos
- Embeddings com SentenceTransformers
- Vector database com ChromaDB
- Retrieval por similaridade
- Geração com contexto (RAG)

**Exemplos incluídos**:
- Sistema RAG completo
- Indexação de documentos
- Busca semântica
- Geração com contexto
- Teste de chunking

#### **03_agente_simples.py** - Dia 5 do plano
**O que aprende**:
- Tool use (function calling)
- Loop de agente (pensar → agir → observar)
- Múltiplas ferramentas
- Chain-of-thought
- Especialização de agentes

**Ferramentas incluídas**:
- WeatherTool (clima simulado)
- CalculatorTool (cálculos)
- SearchTool (busca simulada)

---

### 3. Templates de Prompts (`templates_prompts/prompts_reutilizaveis.md`)

**Categorias**:
- Análise de Código (review, refatoração, testes)
- Escrita e Documentação (README, commit messages)
- Dados e Análise (SQL, limpeza, visualização)
- Debugging (errors, performance, memory)
- Arquitetura (sistemas, APIs, databases)
- Aprendizado (explicações, comparações, tutoriais)
- Automação (boilerplate, migração, deploy)
- Negócios (requisitos, user stories, estimativas)
- Criativos (brainstorming, naming, copywriting)
- Segurança (análise, checklist)

**Como usar**:
- Copie e adapte para suas necessidades
- Adicione seus próprios prompts
- Versione prompts que funcionam bem

---

### 4. Ambiente de Desenvolvimento (`scripts_ia/`)

**Configurado com**:
- Python 3.14.6
- Ambiente virtual (`venv/`)
- Todas as dependências instaladas
- Scripts de setup automático
- Documentação completa

**Dependências principais**:
- `anthropic` - API Claude
- `openai` - API GPT
- `chromadb` - Vector database
- `sentence-transformers` - Embeddings
- `pandas`, `numpy` - Processamento de dados

**Guias disponíveis**:
- `README.md` - Documentação dos scripts
- `GUIA_SETUP.md` - Guia passo a passo
- `setup.bat/sh` - Setup automático

---

### 5. Recursos em Português (`recursos_portugues.md`)

**Categorias**:
- 📺 YouTube (canais brasileiros)
- 📝 Blogs e sites (Medium, Dev.to)
- 🎓 Cursos online (gratuitos e pagos)
- 📚 Livros (traduzidos)
- 🎙️ Podcasts (tech e Data Science)
- 💻 Comunidades (Telegram, Discord)
- 📰 Notícias (tecnologia)
- 🏢 Empresas brasileiras de IA
- 🎯 Eventos e conferências
- 📱 Apps e ferramentas
- 🎓 Instituições de ensino

**Destaques**:
- Canais: Mario Filho, Felipe Deschamps, Dunossauro
- Cursos: Alura, DIO, Coursera (com legendas)
- Comunidades: Python Brasil, ML Brasil
- Eventos: PyBR, TDC, Data Science Brasil

---

## 🗓️ Plano de 2 Semanas - Resumo

### Semana 1: Fundamentos
- **Dia 1**: Fundamentos ML/LLMs + glossário
- **Dia 2**: Modelos e empresas + script API
- **Dia 3**: Arquitetura (transformers, embeddings)
- **Dia 4**: APIs + prática (script 01)
- **Dia 5**: Agentes + prática (script 03)
- **Dia 6**: RAG + prática (script 02)
- **Dia 7**: Revisão + glossário completo

### Semana 2: Aplicações
- **Dia 8**: Prompt engineering + templates
- **Dia 9**: Avaliação e benchmarking
- **Dia 10**: Deploy e produção
- **Dia 11**: Segurança e ética
- **Dia 12**: Ferramentas ecossistema
- **Dia 13**: Casos de uso e arquiteturas
- **Dia 14**: Apresentação e plano de ação

---

## 🎯 Checklist de Início Rápido

### Hoje (1 hora)
- [ ] Ler glossário (seções fundamentais)
- [ ] Configurar ambiente (setup.bat)
- [ ] Obter API key Anthropic
- [ ] Executar `01_api_basica.py`
- [ ] Inscrever-se em 2 canais YouTube

### Esta Semana (5 horas)
- [ ] Completar glossário (marcar termos conhecidos)
- [ ] Executar todos os 3 scripts
- [ ] Ler recursos em português
- [ ] Entrar em 1 comunidade (Telegram)
- [ ] Assistir 1 playlist completa

### Próxima Semana (10 horas)
- [ ] Seguir plano de estudo dias 1-7
- [ ] Modificar e estender scripts
- [ ] Criar 3 prompts próprios
- [ ] Ler 1 livro/capítulo
- [ ] Participar de 1 comunidade

---

## 💡 Dicas de Uso

### Para Estudo Eficiente
1. **Siga o plano**: 2-3 horas por dia
2. **Pratique ativamente**: Modifique os scripts
3. **Documente**: Anote o que aprendeu
4. **Ensine**: Explique para colegas
5. **Construa**: Crie projetos próprios

### Para Referência Rápida
- **Termo técnico**: Glossário
- **Como fazer X**: Scripts + README
- **Prompt para Y**: Templates
- **Recurso em PT**: Recursos portugueses
- **Problema técnico**: GUIA_SETUP.md

### Para Compartilhar
- Use o glossário para alinhar vocabulário da equipe
- Compartilhe scripts para práticas em grupo
- Use templates para padronizar prompts
- Indique recursos portugueses para colegas

---

## 📊 Medição de Progresso

### Semana 1
- [ ] 50+ termos do glossário compreendidos
- [ ] 3 scripts executados com sucesso
- [ ] 3 APIs testadas (Anthropic, OpenAI, etc.)
- [ ] 1 sistema RAG funcionando
- [ ] 1 agente com tool use funcionando

### Semana 2
- [ ] 10 prompts criados e testados
- [ ] 1 arquitetura desenhada
- [ ] 1 avaliação de modelos realizada
- [ ] 1 checklist de segurança criado
- [ ] 1 apresentação preparada

---

## 🆘 Suporte

### Problemas Técnicos
- **Scripts não rodam**: Veja `GUIA_SETUP.md`
- **API keys**: Veja seção configuração
- **Dependências**: Reinstale com `pip install -r requirements.txt`

### Dúvidas de Conteúdo
- **Termos técnicos**: Consulte glossário
- **Como fazer X**: Veja scripts e README
- **Recursos adicionais**: Veja recursos portugueses

### Comunidade
- **Python Brasil**: Telegram e Discord
- **Stack Overflow PT**: pt.stackoverflow.com
- **Reddit**: r/pythonbrasil

---

## 🎉 Próximos Passos Após o Plano

1. **Construir projeto próprio**: Aplicar conhecimento
2. **Contribuir open source**: Compartilhar aprendizado
3. **Apresentar para equipe**: Tornar-se referência
4. **Especializar-se**: Escolher área (RAG, agentes, etc.)
5. **Manter atualizado**: Newsletters, papers, eventos

---

## 📝 Notas

Este conjunto de materiais foi criado para ser:
- **Prático**: Scripts funcionais imediatamente
- **Completo**: Cobre todo o ecossistema
- **Atualizado**: Tecnologias atuais (2024)
- **Acessível**: Recursos em português
- **Adaptável**: Modifique conforme necessário

**Lembre-se**: O melhor material é aquele que você usa e adapta para suas necessidades!

---

## 🚀 Comece Agora!

Seu próximo passo imediato:

1. Abra `scripts_ia/GUIA_SETUP.md`
2. Siga os passos de configuração
3. Execute `python 01_api_basica.py`
4. Comece o plano de estudo dia 1

Boa sorte na jornada para se tornar referência em IA! 🎓✨
