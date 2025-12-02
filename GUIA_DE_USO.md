✅ Cómo usar tu Mini-Compilador Web
1️⃣ Escribe código en el cuadro grande

Ejemplo simple para probar:

int x = 10;
int y = 20;
int z = x + y;
print(z);

2️⃣ Presiona el botón “Compilar”

El frontend enviará tu código al servidor Flask en:

http://localhost:5000/compile

3️⃣ Te aparecerán resultados abajo

React mostrará esto en <Results />:

✔ Tokens del análisis léxico

✔ AST (árbol sintáctico)

✔ Tabla de símbolos

✔ Cuádruplos generados

✔ Cuádruplos optimizados

✔ Código ejecutado (si hay salida)

Todos esos datos deben aparecer automáticamente cuando compilas.

========================================================================================================


PARA CORRER AMBOS SERVICIOS DE FLASK Y REACT SIN NECESIDAD DE ABRIR DOS TERMINALES VAMOS A POCIOCIONARLOS EN "C:\Users\casim\Documents\mini-compilador>"

NOTA RECUERDA QUE TIENES QUE ESTAR POCICIONADO EN LA TERMINAL DESDE LA CARPETA RAIZ.

EN SEGUIDA EJECUTAR EL CODIGO:

".\run_all.bat"