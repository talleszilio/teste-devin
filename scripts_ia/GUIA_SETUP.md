# 🚀 Guia de Setup do Ambiente de Desenvolvimento

Ambiente configurado e pronto para uso! Siga este guia para começar.

---

## ✅ Status Atual

- ✅ Python 3.14.6 instalado
- ✅ Ambiente virtual criado (`venv/`)
- ✅ Dependências instaladas
- ✅ Scripts prontos para execução

---

## 🔑 Configuração de API Keys

### Passo 1: Obter API Keys

#### Anthropic (Claude) - **Necessário para scripts**
1. Acesse: https://console.anthropic.com/
2. Crie conta (grátis)
3. Vá em "API Keys"
4. Crie nova key
5. Copie a key (começa com `sk-ant-`)

#### OpenAI (GPT) - Opcional
1. Acesse: https://platform.openai.com/api-keys
2. Crie conta
3. Vá em "API Keys"
4. Crie nova key
5. Adicione créditos (mínimo $5)

### Passo 2: Configurar Variáveis de Ambiente

#### Opção A: Arquivo .env (Recomendado)
1. Copie o arquivo `.env.example` para `.env`:
```bash
cd scripts_ia
copy .env.example .env
```

2. Edite o arquivo `.env` e preencha suas keys:
```
ANTHROPIC_API_KEY=sk-ant-sua-key-aqui
OPENAI_API_KEY=sk-sua-key-aqui
```

#### Opção B: Variáveis de Ambiente (Windows PowerShell)
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-sua-key-aqui"
$env:OPENAI_API_KEY="sk-sua-key-aqui"
```

#### Opção C: Variáveis de Ambiente (Windows CMD)
```cmd
set ANTHROPIC_API_KEY=sk-ant-sua-key-aqui
set OPENAI_API_KEY=sk-sua-key-aqui
```

---

## 🎯 Como Usar

### Ativar Ambiente Virtual

#### Windows:
```bash
cd scripts_ia
venv\Scripts\activate.bat
```

#### Linux/Mac:
```bash
cd scripts_ia
source venv/bin/activate
```

### Executar Scripts

#### Script 1: API Básica
```bash
python 01_api_basica.py
```
**Aprende**: Uso de APIs, streaming, parâmetros, custos

#### Script 2: RAG Simples
```bash
python 02_rag_simples.py
```
**Aprende**: Chunking, embeddings, vector database, RAG

#### Script 3: Agente Simples
```bash
python 03_agente_simples.py
```
**Aprende**: Tool use, agentes, loop de decisão

---

## 📁 Estrutura de Arquivos

```
scripts_ia/
├── venv/                    # Ambiente virtual (ativado)
├── 01_api_basica.py         # Script de API
├── 02_rag_simples.py        # Script de RAG
├── 03_agente_simples.py     # Script de Agentes
├── requirements.txt         # Dependências
├── .env.example            # Exemplo de configuração
├── .env                    # Suas API keys (criar)
├── setup.bat               # Setup automático (Windows)
├── setup.sh                # Setup automático (Linux/Mac)
├── README.md               # Documentação completa
└── GUIA_SETUP.md           # Este arquivo
```

---

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError"
```bash
# Reinstalar dependências
pip install -r requirements.txt
```

### Erro: "ANTHROPIC_API_KEY not configured"
```bash
# Verificar se .env existe e está preenchido
# Ou configurar variável de ambiente
```

### Erro: "ChromaDB initialization error"
```bash
# Verificar permissões de escrita
# Deletar chroma_db e deixar script recriar
rm -rf chroma_db
```

### Download lento de modelo
- O modelo SentenceTransformers (~100MB) é baixado na primeira execução
- Seja paciente ou use VPN se necessário

### Erro de quota/limite
- Verifique saldo no console da API
- Espere reset de rate limits
- Use modelo menor se disponível

---

## 💰 Custos Estimados

### Anthropic Claude
- **Claude 3.5 Sonnet**: ~$0.003/1K input tokens, $0.015/1K output tokens
- **Executar todos os scripts uma vez**: ~$0.50-1.00
- **Desenvolvimento ativo (1 semana)**: ~$5-10

### OpenAI GPT
- **GPT-4**: ~$0.03/1K input tokens, $0.06/1K output tokens
- **Mais caro que Claude**

### Dicas para economizar:
- Use Claude 3 Haude para testes (mais barato)
- Implemente caching
- Limite `max_tokens` quando possível
- Use modelos locais (Llama via Ollama) para testes

---

## 📚 Recursos Adicionais

### Documentação
- [Anthropic API Docs](https://docs.anthropic.com/)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [ChromaDB Docs](https://docs.trychroma.com/)
- [SentenceTransformers](https://www.sbert.net/)

### Aprendizado
- Glossário completo: `../glossario_ia_completo.md`
- Templates de prompts: `../templates_prompts/prompts_reutilizaveis.md`
- Plano de estudo: Ver plano de 2 semanas

---

## 🎓 Plano de Estudo Sugerido

### Dia 1: Fundamentos
- Ler glossário (marcar termos conhecidos)
- Assistir "Intro to LLMs" (Andrej Karpathy)

### Dia 2: Modelos e Empresas
- Testar script `01_api_basica.py`
- Comparar Claude vs GPT-4
- Criar tabela comparativa

### Dia 3: Arquitetura
- Ler "The Illustrated Transformer"
- Entender embeddings e tokenização

### Dia 4: APIs (Prática)
- Executar `01_api_basica.py` completamente
- Implementar seu próprio script de API
- Medir latência e custos

### Dia 5: Agentes
- Executar `03_agente_simples.py`
- Criar seu próprio tool
- Implementar memória simples

### Dia 6: RAG
- Executar `02_rag_simples.py`
- Indexar seus próprios documentos
- Experimentar diferentes chunk sizes

### Dia 7: Revisão
- Revisar glossário
- Escrever resumo da semana
- Preparar apresentação

---

## 🚀 Próximos Passos

1. **Configurar API keys** (obter e configurar)
2. **Executar primeiro script** (`01_api_basica.py`)
3. **Estender exemplos** (modificar e experimentar)
4. **Construir projeto próprio** (aplicar conhecimento)
5. **Compartilhar com equipe** (ensinar o que aprendeu)

---

## 🆘 Suporte

Se encontrar problemas:

1. **Verificar logs**: Os scripts printam informações detalhadas
2. **Consultar README.md**: Documentação completa dos scripts
3. **Verificar documentação oficial**: Links acima
4. **Testar isoladamente**: Execute cada script separadamente

---

## ✅ Checklist de Setup

- [ ] Python 3.9+ instalado
- [ ] Ambiente virtual criado
- [ ] Dependências instaladas
- [ ] API keys obtidas
- [ ] .env configurado
- [ ] Script 01 executado com sucesso
- [ ] Script 02 executado com sucesso
- [ ] Script 03 executado com sucesso
- [ ] Glossário lido parcialmente
- [ ] Plano de estudo revisado

---

## 🎉 Você Está Pronto!

Ambiente configurado, scripts prontos, recursos disponíveis.

**Comece agora**: Configure suas API keys e execute `python 01_api_basica.py`

Boa sorte nos estudos! 🚀
