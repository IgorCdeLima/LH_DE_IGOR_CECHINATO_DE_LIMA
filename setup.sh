#!/bin/bash

# =============================================
# Script para iniciar o Apache Airflow no Linux/Mac
# =============================================

echo "🔹 Iniciando o programa Apache Airflow..."

# Rodando o airflow-init em detached mode
docker-compose up airflow-init -d

# Verifica se houve erro
if [ $? -ne 0 ]; then
    echo "❌ Ocorreu um erro ao iniciar o Apache Airflow."
    read -p "Pressione Enter para sair..."
    exit 1
fi

# Pausa de 2 segundos
sleep 2

# Limpa a tela
clear

# Subindo todos os containers
echo "🔹 Subindo os containers..."
docker-compose up -d

# Verifica se houve erro
if [ $? -ne 0 ]; then
    echo "❌ Falha ao subir os containers."
    read -p "Pressione Enter para sair..."
    exit 1
fi

echo "✅ Operação finalizada."
read -p "Pressione Enter para fechar o script..."