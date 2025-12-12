// Componente Editor.
//
// Props:
// 1. code: Código fuente actual.
// 2. setCode: Función para actualizar el código fuente.
//
// Renderizado:
// - Muestra un área de texto donde el usuario puede escribir el código fuente.

export default function Editor({ code, setCode }) {
    return (
        <textarea
            style={{ width: "100%", height: "200px" }}
            value={code}
            onChange={(e) => setCode(e.target.value)}
        />
    );
}
