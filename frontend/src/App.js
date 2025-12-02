import { useState } from "react";
import Editor from "./Editor";
import Results from "./Results";
import { compileCode } from "./api";

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
