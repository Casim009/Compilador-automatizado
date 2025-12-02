 # 🖥️ Mini-Compilador Web  
Lenguajes y Autómatas II — Tecnológico Nacional de México (ITIZ)  
Autor: **Casimiro Velasco Christian Aarón**

Antes de comenzar, asegúrate de tener instalado:

### Windows
1. **Python 3.8 o superior**
   - Descargar de: https://www.python.org/downloads/
   - ✅ Marcar "Add Python to PATH" durante la instalación

2. **Node.js 14 o superior**
   - Descargar de: https://nodejs.org/
   - Incluye npm automáticamente

### Mac/Linux
```bash
# Python (normalmente ya está instalado)
python3 --version

# Node.js
# Mac: brew install node
# Linux: sudo apt install nodejs npm
```

## 📘 Descripción General

El **Mini-Compilador Web** es una aplicación completa que implementa las fases principales de un compilador tradicional:

- **Análisis Léxico**
- **Análisis Sintáctico**
- **Generación de AST**
- **Tabla de Símbolos**
- **Código Intermedio (Cuádruplos)**
- **Optimización Básica**
- **Generación de Código en Python**

Incluye:

✅ **Backend en Python (Flask)**  
✅ **Frontend en React**  
✅ **Compilación en tiempo real desde el navegador**  
✅ **Ejecución con un solo clic usando un script `.bat`**

Es ideal para fines educativos, prácticas de laboratorio y demostraciones.

---

## 📂 Estructura del Proyecto


mini-compilador/
│
├── backend/
│ ├── app.py
│ ├── lexer.py
│ ├── parser.py
│ ├── optimizer.py
│ ├── codegen.py
│ ├── semantic.py
│ ├── intermediate.py
│ ├── parsetab.py
│ └── requirements.txt
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── App.js
│ │ ├── Editor.js
│ │ ├── Results.js
│ │ ├── api.js
│ │ └── index.js
│ ├── package.json
│
└── run_all.bat ← Inicia todo el proyecto automáticamente



---

## 🚀 Instalación y Ejecución

### 🔧 Requisitos previos
- Python 3.10+
- Node.js 16+
- npm
- Windows (para usar `run_all.bat`)

---

## ⚙️ Configuración del Backend

1. Abrir consola en la carpeta `/backend/`
2. Crear entorno virtual:

```bash
python -m venv venv

Activarlo:

venv\Scripts\activate o venv/Scripts/activate

Instalar dependencias:

pip install -r requirements.txt


Ejecutar servidor:

python app.py


El backend corre en:

http://localhost:5000

🎨 Configuración del Frontend

Abrir consola en /frontend/

Instalar dependencias:

npm install


Ejecutar:

npm start


El frontend abrirá automáticamente:

http://localhost:3000

▶️ EJECUTAR TODO AUTOMÁTICAMENTE (RECOMENDADO)

Este proyecto incluye un script run_all.bat que inicia:

backend (Flask)

frontend (React)

al mismo tiempo.

Cómo ejecutarlo:

Ir a la carpeta raíz:

cd mini-compilador


Ejecutar:

.\run_all.bat


Se abrirán dos ventanas y se levantará automáticamente el compilador web.

🧪 ¿Cómo usar el compilador?

Escribe código como:

a = 5 + 3
b = a * 2


Presiona Compilar

Obtendrás:

🔹 AST

🔹 Tokens (si implementas análisis léxico)

🔹 Tabla de Símbolos

🔹 Cuádruplos

🔹 Código Optimizado

🔹 Código Python

📡 API del Backend
POST /compile

Envías:

{ "code": "a = 3 + 5" }


Recibes:

{
  "ast": {},
  "symbols": {},
  "quadruples": [],
  "optimized": [],
  "python": "a = 8"
}

💡 Características Técnicas

Lexer basado en PLY

Parser LALR usando PLY

Optimización constante (constant folding)

Generación de cuádruplos tipo TAC

Clean architecture

Frontend modular (React components)

Proxy integrado para evitar CORS

🏫 Proyecto Escolar

Este proyecto fue realizado como parte de la materia:

Lenguajes y Autómatas II

Tecnológico Nacional de México — Campus Iztapalapa (ITIZ)

🛠️ Autor **

Casimiro Velasco Christian Aarón