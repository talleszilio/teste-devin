"""
Script 1: API Básica - Como usar LLMs via API
Objetivo: Aprender a fazer chamadas básicas a APIs de LLM
Dia do plano: Dia 4
"""

import os
from anthropic import Anthropic
import openai

# Configuração - use variáveis de ambiente
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def exemplo_anthropic_basico():
    """Exemplo básico com Anthropic Claude"""
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Explique o que é um LLM em 2 parágrafos."
            }
        ]
    )
    
    print("Resposta do Claude:")
    print(message.content[0].text)
    return message.content[0].text

def exemplo_anthropic_streaming():
    """Exemplo com streaming (resposta token por token)"""
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    
    print("\nResposta com streaming:")
    with client.messages.stream(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[{
            "role": "user", 
            "content": "Conte uma história curta sobre IA."
        }]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    print()  # Nova linha ao final

def exemplo_openai_basico():
    """Exemplo básico com OpenAI GPT"""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente técnico conciso."
            },
            {
                "role": "user",
                "content": "O que é RAG?"
            }
        ],
        max_tokens=150,
        temperature=0.7
    )
    
    print("\nResposta do GPT-4:")
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def exemplo_com_parametros():
    """Exemplo mostrando diferentes parâmetros"""
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    
    # Temperature baixa = mais determinístico
    resposta_conservadora = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=100,
        temperature=0.1,  # Baixa temperatura
        messages=[{
            "role": "user",
            "content": "Gere um nome para um startup de IA."
        }]
    )
    
    # Temperature alta = mais criativo
    resposta_criativa = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=100,
        temperature=1.0,  # Alta temperatura
        messages=[{
            "role": "user",
            "content": "Gere um nome para um startup de IA."
        }]
    )
    
    print("\nTemperature 0.1 (conservador):")
    print(resposta_conservadora.content[0].text)
    
    print("\nTemperature 1.0 (criativo):")
    print(resposta_criativa.content[0].text)

def exemplo_contagem_tokens():
    """Exemplo de como estimar custos"""
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    
    # Texto de exemplo
    texto = "Explique o funcionamento de transformadores em redes neurais de forma detalhada." * 10
    
    # Estimar tokens (regra aproximada: 1 token ≈ 4 caracteres)
    tokens_estimados = len(texto) / 4
    
    print(f"\nEstimativa de tokens: {tokens_estimados:.0f}")
    print(f"Custo aproximado (Claude Sonnet): ${tokens_estimados/1000 * 0.003:.4f}")
    
    # Fazer a request para ver tokens reais
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[{"role": "user", "content": texto}]
    )
    
    print(f"Tokens input reais: {response.usage.input_tokens}")
    print(f"Tokens output: {response.usage.output_tokens}")

def exemplo_system_prompt():
    """Exemplo de system prompt para definir comportamento"""
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    
    system_prompts = {
        "dev": "Você é um desenvolvedor sênior. Seja técnico e conciso.",
        "professor": "Você é um professor paciente. Explique de forma simples.",
        "poeta": "Você é um poeta. Use linguagem criativa e metafórica."
    }
    
    pergunta = "O que é uma API?"
    
    for persona, system_prompt in system_prompts.items():
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=150,
            system=system_prompt,
            messages=[{"role": "user", "content": pergunta}]
        )
        
        print(f"\n--- Persona: {persona.upper()} ---")
        print(response.content[0].text)

def main():
    """Executa todos os exemplos"""
    print("=" * 60)
    print("Script 1: API Básica - Exemplos de Uso de LLMs")
    print("=" * 60)
    
    # Verificar se API keys estão configuradas
    if not ANTHROPIC_API_KEY:
        print("⚠️  ANTHROPIC_API_KEY não configurada")
        print("Sete com: export ANTHROPIC_API_KEY='sua-chave'")
        return
    
    try:
        # Exemplo 1: Chamada básica
        print("\n1. Chamada Básica")
        print("-" * 40)
        exemplo_anthropic_basico()
        
        # Exemplo 2: Streaming
        print("\n2. Streaming")
        print("-" * 40)
        exemplo_anthropic_streaming()
        
        # Exemplo 3: Diferentes parâmetros
        print("\n3. Diferentes Parâmetros (Temperature)")
        print("-" * 40)
        exemplo_com_parametros()
        
        # Exemplo 4: Contagem de tokens
        print("\n4. Estimativa de Custos")
        print("-" * 40)
        exemplo_contagem_tokens()
        
        # Exemplo 5: System prompts
        print("\n5. System Prompts")
        print("-" * 40)
        exemplo_system_prompt()
        
        # Exemplo OpenAI (se tiver key)
        if OPENAI_API_KEY:
            print("\n6. OpenAI GPT-4")
            print("-" * 40)
            exemplo_openai_basico()
        
        print("\n" + "=" * 60)
        print("✅ Todos os exemplos executados com sucesso!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("Verifique suas API keys e conexão com internet")

if __name__ == "__main__":
    main()
