#!/bin/bash
# Script de setup rápido para ambiente de desenvolvimento de IA

echo "🚀 Configurando ambiente de desenvolvimento de IA..."
echo ""

# Verificar Python
echo "📦 Verificando Python..."
python --version
if [ $? -ne 0 ]; then
    echo "❌ Python não encontrado. Instale Python 3.9+"
    exit 1
fi

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "🔧 Criando ambiente virtual..."
    python -m venv venv
fi

# Ativar ambiente virtual
echo "🔌 Ativando ambiente virtual..."
source venv/bin/activate

# Atualizar pip
echo "⬆️  Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo "📥 Instalando dependências..."
pip install -r requirements.txt

# Criar arquivo .env se não existir
if [ ! -f ".env" ]; then
    echo "📝 Criando arquivo .env..."
    cp .env.example .env
    echo "⚠️  Edite o arquivo .env com suas API keys"
fi

# Criar diretórios necessários
mkdir -p chroma_db
mkdir -p logs

echo ""
echo "✅ Setup concluído!"
echo ""
echo "📋 Próximos passos:"
echo "1. Edite o arquivo .env com suas API keys"
echo "2. Ative o ambiente: source venv/bin/activate"
echo "3. Execute os scripts: python 01_api_basica.py"
echo ""
echo "📚 Veja README.md para mais detalhes"
