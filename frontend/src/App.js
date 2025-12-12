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
      alert("Ocurrió un error al compilar el código.");
    }
  };

  return (
    <div style={{
      padding: "20px",
      maxWidth: "1200px",
      margin: "0 auto",
      fontFamily: "'Poppins', sans-serif",
      color: "#fff",
      minHeight: "100vh",
      background: "linear-gradient(135deg, #0f2027, #203a43, #2c5364)"
    }}>
      {/* Encabezado */}
      <header style={{ textAlign: "center", marginBottom: 40 }}>
        <h1 style={{ fontSize: "2.5rem", color: "#00d8ff", textShadow: "0 2px 10px rgba(0,0,0,0.5)" }}>
          Mini Compilador Web
        </h1>
        <p style={{ color: "#c0c0c0", marginTop: 5 }}>
          Escribe tu código y compílalo en tiempo real
        </p>
      </header>

      {/* Editor y botón de compilación */}
      <div style={{
        display: "flex",
        flexDirection: "column",
        gap: "15px",
        marginBottom: 30
      }}>
        <Editor code={code} setCode={setCode} />

        <button
          onClick={handleCompile}
          style={{
            alignSelf: "flex-start",
            padding: "12px 30px",
            background: "linear-gradient(90deg, #1976D2, #00d8ff)",
            color: "#fff",
            border: "none",
            borderRadius: "12px",
            fontWeight: 600,
            cursor: "pointer",
            transition: "all 0.3s ease",
            boxShadow: "0 8px 20px rgba(0,0,0,0.3)",
            fontSize: "1rem"
          }}
          onMouseEnter={e => e.target.style.filter = "brightness(1.2)"}
          onMouseLeave={e => e.target.style.filter = "brightness(1)"}
        >
          Compilar
        </button>
      </div>

      {/* Resultados */}
      {result && <Results result={result} />}
    </div>
  );
}
