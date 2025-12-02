# 🧪 Casos de Prueba - Mini-Compilador

## Casos de Prueba Exitosos

### Caso 1: Declaración Simple
**Código:**
```javascript
int x = 10;
print(x);
```

**Resultado Esperado:**
- ✅ Tokens: 6 tokens
- ✅ AST: Árbol con declaración y print
- ✅ Tabla de símbolos: x (int, 10)
- ✅ Cuádruplos: 2 cuádruplos
- ✅ Salida: `10`

---

### Caso 2: Operaciones Aritméticas
**Código:**
```javascript
int a = 5;
int b = 3;
int suma = a + b;
int resta = a - b;
int producto = a * b;
print(suma);
print(resta);
print(producto);
```

**Resultado Esperado:**
- ✅ Tokens: ~30 tokens
- ✅ Tabla de símbolos: a, b, suma, resta, producto
- ✅ Optimización: Plegado de constantes aplicado
- ✅ Salida:
```
8
2
15
```

---

### Caso 3: Condicional If Simple
**Código:**
```javascript
int x = 10;
if (x > 5) {
    print(1);
}
```

**Resultado Esperado:**
- ✅ AST: Nodo if con condición y bloque then
- ✅ Cuádruplos: Incluye IF_FALSE y LABEL
- ✅ Salida: `1`

---

### Caso 4: Condicional If-Else
**Código:**
```javascript
int edad = 15;
if (edad >= 18) {
    print(1);
} else {
    print(0);
}
```

**Resultado Esperado:**
- ✅ AST: Nodo if con bloques then y else
- ✅ Cuádruplos: Incluye IF_FALSE, GOTO y LABEL
- ✅ Salida: `0`

---

### Caso 5: Ciclo While
**Código:**
```javascript
int contador = 0;
while (contador < 3) {
    print(contador);
    contador = contador + 1;
}
```

**Resultado Esperado:**
- ✅ AST: Nodo while con condición y cuerpo
- ✅ Cuádruplos: Incluye LABEL, IF_FALSE y GOTO
- ✅ Salida:
```
0
1
2
```

---

### Caso 6: Tipos de Datos Mixtos
**Código:**
```javascript
int entero = 42;
float decimal = 3.14;
bool verdadero = true;
bool falso = false;
print(entero);
print(decimal);
```

**Resultado Esperado:**
- ✅ Tabla de símbolos: 4 variables con tipos correctos
- ✅ Sin errores semánticos
- ✅ Salida:
```
42
3.14
```

---

### Caso 7: Operadores Lógicos
**Código:**
```javascript
bool a = true;
bool b = false;
if (a && b) {
    print(1);
} else {
    print(2);
}
```

**Resultado Esperado:**
- ✅ Evaluación correcta de operador &&
- ✅ Salida: `2`

---

### Caso 8: Comparaciones
**Código:**
```javascript
int x = 10;
int y = 20;
if (x < y) {
    print(1);
}
if (x == 10) {
    print(2);
}
if (y != x) {
    print(3);
}
```

**Resultado Esperado:**
- ✅ Tres condiciones evaluadas correctamente
- ✅ Salida:
```
1
2
3
```

---

### Caso 9: Programa Completo
**Código:**
```javascript
int suma = 0;
int i = 1;

while (i <= 5) {
    suma = suma + i;
    i = i + 1;
}

print(suma);
```

**Resultado Esperado:**
- ✅ Cálculo correcto de suma 1+2+3+4+5
- ✅ Salida: `15`

---

### Caso 10: Optimización - Plegado de Constantes
**Código:**
```javascript
int resultado = 5 + 3 * 2;
print(resultado);
```

**Resultado Esperado:**
- ✅ Antes de optimización: múltiples cuádruplos
- ✅ Después de optimización: cuádruplos reducidos
- ✅ Reducción > 0%
- ✅ Salida: `11`

---

## Casos de Prueba con Errores Esperados

### Error 1: Variable No Declarada
**Código:**
```javascript
print(x);
```

**Error Esperado:**
```
Error: Variable 'x' no ha sido declarada
Fase: semantic
```

---

### Error 2: Incompatibilidad de Tipos
**Código:**
```javascript
int x = true;
```

**Error Esperado:**
```
Error de tipo: No se puede asignar bool a int en 'x'
Fase: semantic
```

---

### Error 3: Error de Sintaxis
**Código:**
```javascript
int x = 10
print(x);
```

**Error Esperado:**
```
Error de sintaxis: token inesperado...
Fase: syntax
```

---

### Error 4: Condición No Booleana
**Código:**
```javascript
int x = 10;
if (x) {
    print(1);
}
```

**Error Esperado:**
```
Error: La condición del if debe ser booleana, no int
Fase: semantic
```

---

### Error 5: Carácter Ilegal
**Código:**
```javascript
int x = 10 @ 5;
```

**Error Esperado:**
```
Carácter ilegal '@'
Fase: lexical
```

---

## 📊 Tabla Resumen de Pruebas

| # | Caso | Tipo | Estado Esperado |
|---|------|------|-----------------|
| 1 | Declaración Simple | Exitoso | ✅ PASS |
| 2 | Operaciones Aritméticas | Exitoso | ✅ PASS |
| 3 | If Simple | Exitoso | ✅ PASS |
| 4 | If-Else | Exitoso | ✅ PASS |
| 5 | While | Exitoso | ✅ PASS |
| 6 | Tipos Mixtos | Exitoso | ✅ PASS |
| 7 | Operadores Lógicos | Exitoso | ✅ PASS |
| 8 | Comparaciones | Exitoso | ✅ PASS |
| 9 | Programa Completo | Exitoso | ✅ PASS |
| 10 | Optimización | Exitoso | ✅ PASS |
| E1 | Variable No Declarada | Error | ❌ ERROR (esperado) |
| E2 | Incompatibilidad Tipos | Error | ❌ ERROR (esperado) |
| E3 | Error Sintaxis | Error | ❌ ERROR (esperado) |
| E4 | Condición No Booleana | Error | ❌ ERROR (esperado) |
| E5 | Carácter Ilegal | Error | ❌ ERROR (esperado) |

---

## 🔍 Cómo Ejecutar las Pruebas

### Prueba Manual (Interfaz Web)
1. Inicia el backend y frontend
2. Copia cada caso de prueba en el editor
3. Presiona "Compilar"
4. Verifica que el resultado coincida con lo esperado

### Verificaciones por Fase

#### ✅ Análisis Léxico
- [ ] Todos los tokens identificados correctamente
- [ ] Números enteros y flotantes reconocidos
- [ ] Palabras reservadas identificadas
- [ ] Operadores correctos

#### ✅ Análisis Sintáctico
- [ ] AST construido sin errores
- [ ] Estructura correcta del árbol
- [ ] Nodos con información completa

#### ✅ Análisis Semántico
- [ ] Tabla de símbolos completa
- [ ] Tipos correctos asignados
- [ ] Errores de tipo detectados
- [ ] Variables no declaradas detectadas

#### ✅ Código Intermedio
- [ ] Cuádruplos generados correctamente
- [ ] Formato (op, arg1, arg2, result) correcto
- [ ] Labels y saltos bien formados

#### ✅ Optimización
- [ ] Plegado de constantes funcional
- [ ] Código muerto eliminado
- [ ] Reducción calculada correctamente

#### ✅ Código Objeto
- [ ] Código Python generado
- [ ] Sintaxis Python válida
- [ ] Variables correctamente nombradas

#### ✅ Ejecución
- [ ] Programa ejecuta sin errores
- [ ] Salida correcta
- [ ] Print funciona correctamente

---

## 📈 Métricas de Calidad

### Para el Informe Técnico

| Métrica | Objetivo | Resultado |
|---------|----------|-----------|
| Casos exitosos | 10/10 | ✅ |
| Errores detectados | 5/5 | ✅ |
| Optimización funcional | Sí | ✅ |
| Fases completas | 7/7 | ✅ |
| Interfaz funcional | Sí | ✅ |

---

## 🎯 Casos Adicionales para Demostración

### Demo 1: Fibonacci (Primeros 5)
```javascript
int a = 0;
int b = 1;
int i = 0;

print(a);
print(b);

while (i < 3) {
    int temp = a + b;
    a = b;
    b = temp;
    print(b);
    i = i + 1;
}
```

**Salida esperada:** `0 1 1 2 3`

---

### Demo 2: Factorial de 5
```javascript
int n = 5;
int factorial = 1;
int i = 1;

while (i <= n) {
    factorial = factorial * i;
    i = i + 1;
}

print(factorial);
```

**Salida esperada:** `120`

---

## ✅ Checklist de Pruebas Pre-Entrega

- [ ] Todos los casos exitosos funcionan
- [ ] Todos los errores son detectados correctamente
- [ ] La interfaz responde sin lag
- [ ] Los resultados son legibles y claros
- [ ] Las optimizaciones muestran reducción
- [ ] El código generado es ejecutable
- [ ] Las métricas son precisas
- [ ] Capturas de pantalla tomadas
- [ ] Video de demostración grabado (opcional)

---

**¡Proyecto listo para demostración! 🎓**