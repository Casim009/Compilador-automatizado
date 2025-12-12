// Funciones principales:
// 1. compileCode(code):
//    - Entrada: Código fuente como cadena.
//    - Salida: Respuesta JSON del servidor.
//    - Propósito: Enviar el código al backend para su compilación.
//    - Implementación: Realiza una solicitud POST al endpoint `/compile` del backend.

export const compileCode = async (code) => {
    const res = await fetch("http://localhost:5000/compile", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code })
    });
    return await res.json();
};
