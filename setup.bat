@echo off
@echo iniciando o programa Apache airflow
docker-compose up airflow-init -d
timeout /t 2 /nobreak
cls
if %ERRORLEVEL% neq 0(
    @echo ouve erro ao iniciar o Apache Airflow
    pause
    exit /b %ERRORLEVEL%
)else(
    @echo Subindo os containers
    docker-compose up -d
)
@echo Operação finalizada
pause
