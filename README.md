# Financial Simulation

Template de dashboard de exemplo.

## Instalação

Certifique-se de ter o Python 3.11 e o pip instalados em seu sistema. Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto. Siga as etapas abaixo para configurar o ambiente e instalar os requisitos:

```bash
# Clone o repositório
git clone https://github.com/BaltasarMR/financialsimulation_STREAMLIT.git

# Navegue até o diretório do projeto
cd financialsimulation_STREAMLIT

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv env

# Ative o ambiente virtual (no Windows)
.\env\Scripts\activate.ps1

#Case apresente algum erro utilize esse comando no Windows

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Ative o ambiente virtual (no macOS/Linux)
source venv/bin/activate

# Instale as dependências do projeto
pip install -r requirements.txt

#Depois que finalizar
deactivate