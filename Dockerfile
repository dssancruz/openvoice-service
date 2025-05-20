# Usa imagem leve com Python 3.10
FROM python:3.10-slim

# Instala o git para permitir instalação via git+https
RUN apt-get update && apt-get install -y git

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Expõe a porta que o Flask usará
EXPOSE 5000

# Comando padrão para iniciar o Flask
CMD ["python", "app.py"]