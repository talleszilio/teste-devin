"""
Script 3: Agente Simples com Tool Use
Objetivo: Criar agente que usa ferramentas
Dia do plano: Dia 5
"""

import os
import json
import requests
from datetime import datetime
from typing import Dict, List, Any
from anthropic import Anthropic

# Configuração
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


class Tool:
    """Classe base para ferramentas que o agente pode usar"""
    
    def __init__(self, name: str, description: str, parameters: Dict):
        self.name = name
        self.description = description
        self.parameters = parameters
    
    def execute(self, **kwargs) -> Any:
        """Executa a ferramenta com os parâmetros fornecidos"""
        raise NotImplementedError


class WeatherTool(Tool):
    """Ferramenta para obter clima (simulada)"""
    
    def __init__(self):
        super().__init__(
            name="get_weather",
            description="Obtém o clima atual para uma cidade",
            parameters={
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Nome da cidade"
                    }
                },
                "required": ["city"]
            }
        )
    
    def execute(self, city: str) -> Dict:
        """Simula obter clima (em produção, usaria API real)"""
        # Simulação - em produção usar API como OpenWeatherMap
        weather_data = {
            "São Paulo": {"temp": 25, "condition": "Parcialmente nublado", "humidity": 65},
            "Rio de Janeiro": {"temp": 28, "condition": "Ensolarado", "humidity": 70},
            "New York": {"temp": 15, "condition": "Chuvoso", "humidity": 80},
            "Tokyo": {"temp": 20, "condition": "Limpo", "humidity": 55},
        }
        
        if city in weather_data:
            return {
                "city": city,
                **weather_data[city],
                "timestamp": datetime.now().isoformat()
            }
        else:
            return {
                "city": city,
                "error": "Cidade não encontrada na base de dados simulada"
            }


class CalculatorTool(Tool):
    """Ferramenta para cálculos matemáticos"""
    
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Executa operações matemáticas básicas",
            parameters={
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                        "description": "Operação a executar"
                    },
                    "a": {"type": "number", "description": "Primeiro número"},
                    "b": {"type": "number", "description": "Segundo número"}
                },
                "required": ["operation", "a", "b"]
            }
        )
    
    def execute(self, operation: str, a: float, b: float) -> Dict:
        """Executa cálculo"""
        operations = {
            "add": a + b,
            "subtract": a - b,
            "multiply": a * b,
            "divide": a / b if b != 0 else "Erro: divisão por zero"
        }
        
        result = operations.get(operation, "Operação inválida")
        
        return {
            "operation": operation,
            "operands": [a, b],
            "result": result
        }


class SearchTool(Tool):
    """Ferramenta para busca na web (simulada)"""
    
    def __init__(self):
        super().__init__(
            name="search",
            description="Busca informações na web",
            parameters={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Termo de busca"
                    }
                },
                "required": ["query"]
            }
        )
    
    def execute(self, query: str) -> Dict:
        """Simula busca na web"""
        # Simulação - em produção usar Google API, Bing API, etc.
        fake_results = [
            {
                "title": f"Resultado sobre {query}",
                "url": f"https://example.com/{query.replace(' ', '-')}",
                "snippet": f"Esta é uma informação simulada sobre {query}."
            }
        ]
        
        return {
            "query": query,
            "results": fake_results,
            "total_results": 1
        }


class SimpleAgent:
    """Agente simples com tool use"""
    
    def __init__(self, tools: List[Tool]):
        self.tools = {tool.name: tool for tool in tools}
        self.anthropic = Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None
        self.conversation_history = []
    
    def get_tools_schema(self) -> List[Dict]:
        """Retorna schema das ferramentas para o modelo"""
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.parameters
            }
            for tool in self.tools.values()
        ]
    
    def execute_tool(self, tool_name: str, tool_input: Dict) -> str:
        """Executa uma ferramenta e retorna resultado"""
        if tool_name not in self.tools:
            return f"Erro: Ferramenta {tool_name} não encontrada"
        
        tool = self.tools[tool_name]
        try:
            result = tool.execute(**tool_input)
            return json.dumps(result, ensure_ascii=False)
        except Exception as e:
            return f"Erro executando {tool_name}: {str(e)}"
    
    def process_message(self, user_message: str) -> str:
        """
        Processa mensagem do usuário com loop de tool use
        
        Args:
            user_message: Mensagem do usuário
        
        Returns:
            Resposta final do agente
        """
        if not self.anthropic:
            return "API Key da Anthropic não configurada"
        
        # Adicionar mensagem do usuário ao histórico
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        max_iterations = 5  # Evitar loops infinitos
        iteration = 0
        
        while iteration < max_iterations:
            iteration += 1
            
            # Chamar modelo com histórico e ferramentas
            response = self.anthropic.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1024,
                tools=self.get_tools_schema(),
                messages=self.conversation_history
            )
            
            # Processar resposta
            assistant_message = {"role": "assistant", "content": []}
            
            for block in response.content:
                if block.type == "text":
                    print(f"🤖 Agente: {block.text}")
                    assistant_message["content"].append({"type": "text", "text": block.text})
                
                elif block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input
                    
                    print(f"🔧 Usando ferramenta: {tool_name}")
                    print(f"   Input: {tool_input}")
                    
                    # Executar ferramenta
                    tool_result = self.execute_tool(tool_name, tool_input)
                    print(f"   Resultado: {tool_result}")
                    
                    # Adicionar tool use ao histórico
                    assistant_message["content"].append({
                        "type": "tool_use",
                        "id": block.id,
                        "name": tool_name,
                        "input": tool_input
                    })
                    
                    # Adicionar resultado da ferramenta ao histórico
                    self.conversation_history.append(assistant_message)
                    self.conversation_history.append({
                        "role": "user",
                        "content": [
                            {
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": tool_result
                            }
                        ]
                    })
                    
                    # Continuar loop para dar ao modelo chance de usar o resultado
                    assistant_message = {"role": "assistant", "content": []}
                    continue
            
            # Se não houver tool use, adiciona mensagem e finaliza
            if assistant_message["content"]:
                self.conversation_history.append(assistant_message)
            
            # Extrair texto final
            final_text = ""
            for block in response.content:
                if block.type == "text":
                    final_text = block.text
                    break
            
            return final_text
        
        return "Máximo de iterações atingido"
    
    def reset(self):
        """Limpa histórico de conversação"""
        self.conversation_history = []


def exemplo_agente_simples():
    """Exemplo de agente com múltiplas ferramentas"""
    print("=" * 60)
    print("Exemplo: Agente com Múltiplas Ferramentas")
    print("=" * 60)
    
    # Criar ferramentas
    tools = [
        WeatherTool(),
        CalculatorTool(),
        SearchTool()
    ]
    
    # Criar agente
    agent = SimpleAgent(tools)
    
    # Lista de tarefas para o agente
    tasks = [
        "Qual o clima em São Paulo?",
        "Quanto é 1234 multiplicado por 567?",
        "Busque informações sobre inteligência artificial",
        "Está frio em Nova York? (considere frio abaixo de 20°C)"
    ]
    
    for task in tasks:
        print(f"\n{'=' * 60}")
        print(f"👤 Usuário: {task}")
        print(f"{'=' * 60}")
        
        response = agent.process_message(task)
        print(f"\n✅ Resposta final: {response}")
        
        # Resetar entre tarefas
        agent.reset()


def exemplo_chain_of_thought():
    """Exemplo forçando chain-of-thought"""
    print("\n" + "=" * 60)
    print("Exemplo: Chain-of-Thought Explícito")
    print("=" * 60)
    
    tools = [CalculatorTool()]
    agent = SimpleAgent(tools)
    
    task = """
    Preciso calcular o custo total de um projeto:
    - Desenvolvimento: 150 horas a $50/hora
    - Design: 40 horas a $60/hora
    - Testes: 30 horas a $45/hora
    
    Pense passo a passo e calcule o total.
    """
    
    print(f"👤 Usuário: {task}")
    response = agent.process_message(task)
    print(f"\n✅ Resposta: {response}")


def exemplo_agente_especializado():
    """Exemplo de agente com persona específica"""
    print("\n" + "=" * 60)
    print("Exemplo: Agente Especializado (Assistente Financeiro)")
    print("=" * 60)
    
    tools = [CalculatorTool()]
    agent = SimpleAgent(tools)
    
    # Definir system prompt para especialização
    system_prompt = """
    Você é um assistente financeiro especializado.
    Sempre que fizer cálculos, mostre o passo a passo.
    Arredonde valores para 2 casas decimais.
    Seja preciso e profissional.
    """
    
    # Adicionar system prompt ao primeiro mensaje
    agent.conversation_history.append({
        "role": "user",
        "content": system_prompt + "\n\nAgora, ajude com o seguinte:"
    })
    
    task = """
    Quero calcular o retorno de investimento:
    Investimento inicial: $10,000
    Retorno após 1 ano: $12,500
    Qual foi o percentual de retorno?
    """
    
    print(f"👤 Usuário: {task}")
    response = agent.process_message(task)
    print(f"\n✅ Resposta: {response}")


def main():
    """Executa todos os exemplos"""
    print("=" * 60)
    print("Script 3: Agente Simples com Tool Use")
    print("=" * 60)
    
    if not ANTHROPIC_API_KEY:
        print("⚠️  ANTHROPIC_API_KEY não configurada")
        print("Sete com: export ANTHROPIC_API_KEY='sua-chave'")
        return
    
    try:
        # Exemplo 1: Agente com múltiplas ferramentas
        exemplo_agente_simples()
        
        # Exemplo 2: Chain-of-thought
        exemplo_chain_of_thought()
        
        # Exemplo 3: Agente especializado
        exemplo_agente_especializado()
        
        print("\n" + "=" * 60)
        print("✅ Todos os exemplos de agentes executados!")
        print("=" * 60)
        print("\n💡 Próximos passos:")
        print("- Adicionar mais ferramentas (API reais, banco de dados)")
        print("- Implementar memória de longo prazo")
        print("- Criar agentes multi-especialistas")
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
