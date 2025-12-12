@echo off
echo === INICIANDO BACKEND Y FRONTEND ===

echo [BACKEND] Activando entorno virtual y ejecutando Flask...
start cmd /k "cd backend && call venv\Scripts\activate && python app.py"

echo [FRONTEND] Iniciando servidor React...
start cmd /k "cd frontend && npm start"

echo === TODO INICIADO ===
pause
