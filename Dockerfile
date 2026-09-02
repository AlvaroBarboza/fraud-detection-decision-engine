# Usamos uma imagem oficial e leve de Python
FROM python:3.9-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Instala as dependências necessárias
RUN pip install --no-cache-dir fastapi uvicorn pydantic pandas

# Copia o código da aplicação para dentro do container
COPY app.py /app/app.py

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Comando para rodar a aplicação via Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]