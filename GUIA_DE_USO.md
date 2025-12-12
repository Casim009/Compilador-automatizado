✅ Cómo usar tu Mini-Compilador Web
1️⃣ Escribe código en el cuadro grande

Ejemplo simple para probar:

int x = 10;
int y = 20;
int z = x + y;
print(z);


Aquí tienes varios ejemplos organizados por secciones, desde fáciles hasta más avanzados.

✅ 1. Operaciones aritméticas básicas
➤ Suma, resta, multiplicación y división
int a = 5;
int b = 3;
int suma = a + b;
int resta = a - b;
int multi = a * b;

int divi = a / b;
print(suma);
print(resta);
print(multi);
print(divi);

✅ 2. Asignaciones encadenadas
int x = 4;
int y = x;
int z = y + 6;
print(z);

✅ 3. Uso de variables temporales

Tu compilador genera temporales como t1, t2.
Este ejemplo produce varias operaciones internas:

int x = 8;
int y = 12;
int r = (x + y) * 2;
print(r);

✅ 4. Ejemplo con muchas operaciones juntas
int a = 10;
int b = 4;
int c = a * b + a - b;
print(c);

✅ 5. Ejemplo con valores negativos (si tu compilador los soporta)
int x = -3;
int y = 7;
int r = x + y;
print(r);

✅ 6. Ejemplo estilo “programa completo”
int base = 5;
int altura = 8;
int area = base * altura;
print(area);

🧪 7. Ejemplo para probar optimización

(Forma redundante)

int x = 2;
int y = 3;
int r = x * y * 1;
print(r);

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