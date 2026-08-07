# Biblioteca de Prompts Reutilizáveis

Coleção de prompts otimizados para tarefas comuns em IA.

---

## 🎯 Categorias de Prompts

- [Análise de Código](#análise-de-código)
- [Escrita e Documentação](#escrita-e-documentação)
- [Dados e Análise](#dados-e-análise)
- [Debugging e Troubleshooting](#debugging-e-troubleshooting)
- [Arquitetura e Design](#arquitetura-e-design)
- [Aprendizado e Explicação](#aprendizado-e-explicação)

---

## 🔍 Análise de Código

### Review de Código
```
Você é um engenheiro de software sênior especializado em code review.

Analise o seguinte código considerando:
1. Bugs e edge cases
2. Performance e otimizações
3. Segurança
4. Legibilidade e maintainability
5. Boas práticas da linguagem

Forneça:
- Lista de problemas encontrados (severidade: alta/média/baixa)
- Sugestões específicas de melhoria
- Código refatorado se necessário

Código a analisar:
```{linguagem}
{codigo}
```
```

### Explicação de Código
```
Explique o seguinte código em {nível_de_detalhe}:

```{linguagem}
{codigo}
```

Para cada parte do código, explique:
- O que faz
- Por que foi implementado assim
- Possíveis problemas ou melhorias

Seja {estilo}: {conciso/detalhado/técnico/iniciante}
```

### Refatoração
```
Refatore o seguinte código para melhorar:
- Legibilidade
- Performance
- Maintainability
- Segurança

Mantenha a mesma funcionalidade. Explique cada mudança feita.

Código original:
```{linguagem}
{codigo}
```
```

### Geração de Testes
```
Gere testes unitários completos para o seguinte código usando {framework}.

Inclua:
- Testes de happy path
- Testes de edge cases
- Testes de erro
- Mocks quando necessário

Código:
```{linguagem}
{codigo}
```
```

---

## ✍️ Escrita e Documentação

### Documentação de Código
```
Gere documentação completa para o seguinte código usando formato {formato}.

Inclua:
- Descrição geral do módulo/classe/função
- Parâmetros com tipos e descrições
- Valores de retorno
- Exceções levantadas
- Exemplos de uso
- Notas de implementação se relevante

Código:
```{linguagem}
{codigo}
```
```

### README de Projeto
```
Gere um README.md profissional para este projeto.

Estrutura sugerida:
1. Título e descrição curta
2. Features principais
3. Pré-requisitos
4. Instalação
5. Uso básico
6. Exemplos
7. Configuração
8. Contribuindo
9. Licença

Use markdown e mantenha tom profissional e acolhedor.

Informações do projeto:
{informações}
```

### Commit Messages
```
Gere uma mensagem de commit seguindo conventional commits para as seguintes mudanças:

{mudanças}

Formato:
<tipo>(<escopo>): <descrição>

Tipos comuns: feat, fix, docs, style, refactor, test, chore
```

### Email Profissional
```
Escreva um email profissional sobre {assunto}.

Contexto:
{contexto}

Destinatário: {destinatário}
Tom: {formal/informal/profissional/amigável}

Inclua:
- Assunto claro
- Saudação apropriada
- Contexto necessário
- Call-to-action se necessário
- Despedida profissional
```

---

## 📊 Dados e Análise

### Análise de Dados
```
Analise os seguintes dados e forneça insights:

{dados}

Considerando:
- Tendências principais
- Outliers
- Correlações
- Recomendações

Apresente resultados em {formato}: {texto/tabela/gráfico_description}
```

### SQL Queries
```
Escreva uma query SQL para {objetivo}.

Schema do banco de dados:
{schema}

Requisitos:
{requisitos}

Otimize para performance se necessário.
```

### Limpeza de Dados
```
Descreva um processo de limpeza para os seguintes dados:

{dados_amostra}

Identifique:
- Valores faltantes
- Dados duplicados
- Inconsistências
- Formatos incorretos

Forneça:
- Estratégia para cada problema
- Código Python/pandas para implementar
```

### Visualização de Dados
```
Sugira o melhor tipo de gráfico para visualizar {tipo_de_dado}.

Dados disponíveis:
{dados}

Justifique sua escolha considerando:
- Tipo de dados
- Mensagem a comunicar
- Público-alvo
- Limitações de cada tipo de gráfico
```

---

## 🐛 Debugging e Troubleshooting

### Debugging
```
Ajude a debugar o seguinte problema:

{descrição_do_problema}

Código:
```{linguagem}
{codigo}
```

Erro/Mensagem:
{erro}

Ambiente:
{ambiente}

Forneça:
- Possíveis causas
- Como diagnosticar
- Soluções específicas
- Como prevenir no futuro
```

### Otimização de Performance
```
Analise o seguinte código para problemas de performance:

```{linguagem}
{codigo}
```

Contexto:
- Tamanho dos dados: {tamanho}
- Requisitos de performance: {requisitos}
- Ambiente: {ambiente}

Identifique:
- Bottlenecks
- Complexidade de tempo/espaço
- Oportunidades de otimização

Forneça código otimizado com explicações.
```

### Memory Leaks
```
Ajude a identificar possíveis memory leaks no seguinte código:

```{linguagem}
{codigo}
```

Forneça:
- Análise de alocação/liberação de memória
- Ferramentas para diagnosticar
- Correções específicas
```

---

## 🏗️ Arquitetura e Design

### Design de Sistema
```
Desenhe a arquitetura para um sistema que:

{requisitos}

Considere:
- Escalabilidade
- Disponibilidade
- Segurança
- Maintainability
- Custos

Forneça:
- Diagrama de arquitetura (descritivo)
- Componentes principais
- Fluxo de dados
- Trade-offs considerados
- Tecnologias recomendadas
```

### Design de API
```
Desenhe uma API REST para {domínio}.

Endpoints necessários:
{endpoints}

Forneça para cada endpoint:
- Método HTTP
- Path
- Parâmetros
- Request body schema
- Response schema
- Códigos de status
- Autenticação/autorização

Siga REST principles e boas práticas.
```

### Design de Database
```
Desenhe o schema de banco de dados para {domínio}.

Entidades e relacionamentos:
{entidades}

Forneça:
- Diagrama ER (descritivo)
- Tabelas com colunas e tipos
- Chaves primárias e estrangeiras
- Índices recomendados
- Considerações de performance
```

### Padrões de Design
```
Sugira padrões de design apropriados para:

{contexto}

Para cada padrão sugerido:
- Nome do padrão
- Quando usar
- Como implementar
- Trade-offs
- Exemplo de código se aplicável
```

---

## 🎓 Aprendizado e Explicação

### Explicação de Conceito
```
Explique {conceito} para {nível}: {iniciante/intermediário/avançado}.

Use analogias se apropriado.
Inclua exemplos práticos.
Mencione aplicações reais.
Seja {estilo}: {conciso/detalhado/técnico}
```

### Comparação
```
Compare {opção_a} vs {opção_b} considerando:

Critérios:
{critérios}

Para cada critério:
- Como cada opção performa
- Vantagens e desvantagens
- Quando escolher cada uma

Conclusão com recomendação baseada em {contexto}.
```

### Tutorial Passo a Passo
```
Crie um tutorial passo a passo para {tarefa}.

Público-alvo: {público}
Pré-requisitos: {pré-requisitos}
Ferramentas necessárias: {ferramentas}

Estrutura:
1. Introdução e objetivos
2. Pré-requisitos e setup
3. Passos numerados detalhados
4. Exemplos de cada passo
5. Troubleshooting comum
6. Próximos passos

Seja claro e inclua comandos/código quando necessário.
```

### Quiz/Perguntas de Estudo
```
Gere {n} perguntas de estudo sobre {tópico}.

Nível de dificuldade: {fácil/médio/difícil}
Tipo de perguntas: {múltipla escolha/verdadeiro ou falso/resposta curta}

Para cada pergunta:
- Enunciado claro
- Opções (se múltipla escolha)
- Resposta correta
- Explicação da resposta
```

---

## 🤖 Prompts Específicos para IA

### System Prompts

#### Assistente Técnico
```
Você é um assistente técnico especializado em {domínio}.
Seja preciso, técnico e conciso.
Quando não souber, diga explicitamente.
Forneça exemplos de código quando relevante.
Sempre explique o "porquê" das suas recomendações.
```

#### Code Reviewer
```
Você é um code reviewer sênior com 15+ anos de experiência.
Seja construtivo mas direto.
Priorize: segurança > performance > legibilidade.
Forneça exemplos de código correto.
Explique o impacto de cada problema encontrado.
```

#### Arquiteto de Software
```
Você é um arquiteto de software experiente.
Considere trade-offs explicitamente.
Pense em escalabilidade, maintainability e custos.
Justifique cada decisão arquitetural.
Mencione alternativas e quando usá-las.
```

#### Professor/Instrutor
```
Você é um paciente e claro professor.
Explique conceitos complexos de forma simples.
Use analogias e exemplos do dia a dia.
Verifique entendimento antes de avançar.
Adapte explicação ao nível do aluno.
```

---

## 🛠️ Prompts de Automação

### Geração de Boilerplate
```
Gere boilerplate para {tipo} em {linguagem}.

Inclua:
- Estrutura de pastas recomendada
- Arquivos principais
- Configuração básica
- Exemplos de uso
- Comentários explicativos

Siga melhores práticas da comunidade.
```

### Migração de Código
```
Migre o seguinte código de {linguagem_origem} para {linguagem_destino}:

```{linguagem_origem}
{codigo}
```

Preserve:
- Funcionalidade
- Performance
- Tratamento de erros
- Comentários relevantes

Adapte para idiomas e padrões da linguagem destino.
```

### Script de Deploy
```
Gere um script de deploy para {aplicação}.

Ambiente: {ambiente}
Requisitos:
{requisitos}

Inclua:
- Setup inicial
- Instalação de dependências
- Configuração
- Build/compile
- Testes
- Deploy
- Rollback se falhar

Use {ferramenta}: {bash/docker/k8s/terraform}
```

---

## 📝 Prompts de Negócios

### Análise de Requisitos
```
Analise os seguintes requisitos de negócio:

{requisitos}

Identifique:
- Requisitos funcionais
- Requisitos não-funcionais
- Ambiguidades
- Conflitos
- Missing information

Forneça perguntas esclarecedoras para o stakeholder.
```

### User Stories
```
Converta os seguintes requisitos em user stories:

{requisitos}

Formato:
Como um [tipo de usuário],
Eu quero [ação],
Para que [benefício].

Critérios de aceitação:
- [critério 1]
- [critério 2]

Priorize: {alta/média/baixa}
```

### Estimativa de Esforço
```
Estime o esforço para implementar:

{tarefa/descrição}

Considere:
- Complexidade técnica
- Incertezas
- Dependências
- Riscos

Forneça:
- Estimativa em horas/dias
- Nível de confiança (alta/média/baixa)
- Fatores que impactam a estimativa
- Como reduzir incerteza
```

---

## 🎨 Prompts Criativos

### Brainstorming
```
Gere {n} ideias para {problema/oportunidade}.

Restrições:
{restrições}

Critérios:
- Inovação
- Viabilidade
- Impacto

Para cada ideia:
- Descrição breve
- Vantagens
- Desafios
- Como validar
```

### Naming
```
Sugira {n} nomes para {produto/projeto}.

Contexto:
{contexto}

Critérios:
- Memorável
- Fácil de soletrar
- Disponível como domínio (verificar)
- Apropriado para o público

Forneça:
- Nome
- Significado/relevância
- Domínio sugerido
- Tagline opcional
```

### Copywriting
```
Escreva copy para {produto/serviço}.

Público-alvo: {público}
Objetivo: {objetivo}
Tom: {tom}

Forneça:
- Headline principal
- Subheadline
- Body copy
- Call-to-action
- Variações A/B se aplicável
```

---

## 🔒 Prompts de Segurança

### Análise de Segurança
```
Analise o seguinte código para vulnerabilidades de segurança:

```{linguagem}
{codigo}
```

Contexto:
{contexto}

Verifique:
- Injection attacks
- Authentication/authorization
- Data validation
- Cryptography issues
- Sensitive data exposure
- XSS/CSRF se aplicável

Forneça:
- Vulnerabilidades encontradas (severidade)
- Como explorar (alto nível)
- Como corrigir
- Como prevenir no futuro
```

### Security Checklist
```
Gere um checklist de segurança para {tipo de aplicação}.

Considere:
- OWASP Top 10
- Específico do domínio
- Compliance se aplicável

Organize por:
- Development
- Testing
- Deployment
- Monitoring
```

---

## 📊 Métricas e Avaliação

### Avaliação de Qualidade
```
Avalie a qualidade do seguinte {artefato}:

{artefato}

Critérios:
{critérios}

Forneça:
- Nota para cada critério (1-10)
- Justificativa para cada nota
- Pontos fortes
- Pontos fracos
- Recomendações específicas
- Nota geral
```

### A/B Testing
```
Desenhe um teste A/B para:

{objetivo}

Hipótese:
{hipótese}

Forneça:
- Variáveis a testar
- Métricas de sucesso
- Tamanho de amostra recomendado
- Duração do teste
- Como analisar resultados
- Critérios de decisão
```

---

## 🌐 Prompts Multilíngues

### Tradução Técnica
```
Traduza o seguinte texto técnico de {idioma_origem} para {idioma_destino}:

{texto}

Mantenha:
- Terminologia técnica consistente
- Precisão técnica
- Tom apropriado
- Formatação se relevante

Notas de contexto:
{notas}
```

### Localização
```
Localize o seguinte conteúdo para {região/idioma}:

{conteúdo}

Considere:
- Culturalmente apropriado
- Formatos de data/número
- Moeda
- Idiomas formais vs informais
- Referências locais
```

---

## 🎯 Prompts de Especialização

### Persona Específica
```
Você é um {profissão/role} com {anos} anos de experiência em {especialidade}.

Estilo de comunicação: {estilo}
Nível de detalhe: {nível}
Foco: {foco}

Responda à seguinte questão/tarefa:
{questão}
```

### Framework Específico
```
Responda usando {framework/linguagem}.

Siga:
- Best practices do framework
- Convenções da comunidade
- Padrões de projeto comuns
- Versão: {versão} se relevante

Tarefa:
{tarefa}
```

---

## 💡 Dicas de Uso

### Para Melhores Resultados

1. **Seja Específico**: Mais contexto = melhores respostas
2. **Use Exemplos**: Mostre o formato desejado
3. **Defina Restrições**: Limite o escopo quando necessário
4. **Itere**: Refine o prompt baseado nos resultados
5. **Componha**: Combine prompts para tarefas complexas

### Estrutura de Prompt Bem-Sucedido

```
[ROLE/PERSONA]
[CONTEXTO]
[TAREFA ESPECÍFICA]
[REQUISITOS/RESTRIÇÕES]
[FORMATO DE SAÍDA]
[EXEMPLOS SE RELEVANTE]
```

### Exemplo de Composição

```
Você é um code reviewer sênior. [ROLE]

Analise este código de uma API REST em Python. [CONTEXTO]

Código:
```python
{codigo}
```

Foque em segurança, performance e boas práticas. [TAREFA]

Forneça:
- Lista de problemas (severidade)
- Código corrigido
- Explicação das mudanças [FORMATO]
```

---

## 📝 Template Vazio

```
ROLE: {role}

CONTEXTO:
{contexto}

TAREFA:
{tarefa}

REQUISITOS:
{requisitos}

RESTRIÇÕES:
{restrições}

FORMATO DE SAÍDA:
{formato}

EXEMPLOS:
{exemplos}
```

---

## 🔄 Variações por Nível de Detalhe

### Nível Iniciante
```
Explique {tópico} como se eu tivesse 10 anos de experiência em tecnologia,
mas nenhuma em {domínio específico}.
Use analogias do dia a dia.
Evite jargão técnico.
Forneça exemplos simples.
```

### Nível Intermediário
```
Explique {tópico} para alguém com conhecimento básico em {domínio}.
Assuma familiaridade com conceitos fundamentais.
Use terminologia apropriada.
Forneça exemplos práticos.
Mencione trade-offs.
```

### Nível Avançado
```
Explique {tópico} em profundidade para especialistas em {domínio}.
Inclua detalhes de implementação.
Discuta edge cases.
Mencione research state-of-the-art.
Compare abordagens alternativas.
Forneça referências.
```

---

## 📚 Como Estender Esta Biblioteca

1. **Categorize**: Organize por domínio/tipo de tarefa
2. **Versione**: Mantenha histórico de mudanças
3. **Teste**: Valide prompts com casos reais
4. **Documente**: Adicione notas de uso e exemplos
5. **Compartilhe**: Contribua com a equipe

---

## 🆘 Troubleshooting de Prompts

### Resposta Genérica
- Adicione mais contexto específico
- Defina persona mais precisa
- Adicione exemplos do formato desejado

### Resposta Muito Longa
- Adicione limite de palavras/tokens
- Seja mais específico sobre o que incluir
- Use formato estruturado

### Resposta Incorreta
- Verifique se o prompt é claro
- Adicione exemplos de saída correta
- Divida em prompts menores

### Alucinação
- Adicione "Se não souber, diga explicitamente"
- Forneça contexto/background
- Peça para citar fontes se aplicável

---

Esta biblioteca é um documento vivo. Adicione seus próprios prompts conforme descobrir o que funciona melhor para seu contexto! 🚀
