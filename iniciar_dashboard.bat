@echo off
echo ========================================================
echo        Iniciando o Planning BI - Dashboards Locais
echo ========================================================
echo.

echo [1] Iniciando Servidor Back-end (FastAPI / BigQuery) na porta 8000...
start "Planning BI - Backend" cmd /c "cd backend && python main.py"

echo [2] Iniciando Servidor Front-end (HTML/JS) na porta 3000...
start "Planning BI - Frontend" cmd /c "cd html-final && python -m http.server 3000"

echo.
echo Aguardando inicializacao dos servidores (3 segundos)...
timeout /t 3 /nobreak > nul

echo.
echo [3] Abrindo o Dashboard no seu navegador padrao...
start http://localhost:3000/ebitda.html

echo.
echo ========================================================
echo Tudo pronto! Você pode fechar as janelas pretas (CMD) 
echo quando quiser desligar o sistema.
echo ========================================================
pause
