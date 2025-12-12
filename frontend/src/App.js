import { useState } from "react";
import Editor from "./Editor";
import Results from "./Results";
import { compileCode } from "./api";

// Componente principal de la aplicación React.
//
// Secciones principales:
// 1. Estados:
//    - code: Almacena el código fuente ingresado por el usuario.
//    - result: Almacena los resultados de la compilación.
//
// 2. Función handleCompile():
//    - Propósito: Enviar el código al backend y actualizar el estado con los resultados.
//
// 3. Renderizado:
//    - Incluye el editor de código, botón de compilación y resultados.

export default function App() {
    const [code, setCode] = useState("");
    const [result, setResult] = useState(null);

    const handleCompile = async () => {
        try {
            const data = await compileCode(code);
            setResult(data);
        } catch (err) {
            console.error("Error al compilar", err);
        }
    };

    return (
        <div style={{ padding: 20 }}>
            <h1>Mini Compilador Web</h1>
            <Editor code={code} setCode={setCode} />
            <button onClick={handleCompile}>Compilar</button>
            {result && <Results result={result} />}
        </div>
    );
}
