@echo off
REM Script de setup rápido para ambiente de desenvolvimento de IA (Windows)

echo 🚀 Configurando ambiente de desenvolvimento de IA...
echo.

REM Verificar Python
echo 📦 Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado. Instale Python 3.9+
    exit /b 1
)

REM Criar ambiente virtual se não existir
if not exist "venv" (
    echo 🔧 Criando ambiente virtual...
    python -m venv venv
)

REM Ativar ambiente virtual
echo 🔌 Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Atualizar pip
echo ⬆️  Atualizando pip...
python -m pip install --upgrade pip

REM Instalar dependências
echo 📥 Instalando dependências...
pip install -r requirements.txt

REM Criar arquivo .env se não existir
if not exist ".env" (
    echo 📝 Criando arquivo .env...
    copy .env.example .env
    echo ⚠️  Edite o arquivo .env com suas API keys
)

REM Criar diretórios necessários
if not exist "chroma_db" mkdir chroma_db
if not exist "logs" mkdir logs

echo.
echo ✅ Setup concluído!
echo.
echo 📋 Próximos passos:
echo 1. Edite o arquivo .env com suas API keys
echo 2. Ative o ambiente: venv\Scripts\activate.bat
echo 3. Execute os scripts: python 01_api_basica.py
echo.
echo 📚 Veja README.md para mais detalhes
