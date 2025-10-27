#!/bin/bash

# =============================================
# Script para iniciar o Apache Airflow no Linux/Mac
# =============================================

echo "🔹 Iniciando o programa Apache Airflow..."
docker-compose up airflow-init -d
clear
echo "🔹 Subindo os containers..."
docker-compose up -d
echo "✅ Operação finalizada."
read -p "Pressione Enter para fechar o script..."