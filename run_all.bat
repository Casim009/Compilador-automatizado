@echo off
echo === INICIANDO BACKEND Y FRONTEND ===

start cmd /k "cd backend && venv\Scripts\activate && python app.py"

start cmd /k "cd frontend && npm start"

echo Todo iniciado.
