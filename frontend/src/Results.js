import { useState } from "react";

export default function Results({ result }) {
  const [tab, setTab] = useState("lexical");

  if (!result || !result.phases) {
    return <div>No hay resultados</div>;
  }

  const tabs = Object.keys(result.phases);

  const getPretty = (obj) => JSON.stringify(obj, null, 2);

  return (
    <div style={{ marginTop: 20 }}>
      <h2>Resultados de la Compilación</h2>

      {/* Tabs */}
      <div style={{
        display: "flex",
        gap: 10,
        marginBottom: 15,
        flexWrap: "wrap"
      }}>
        {tabs.map(t => (
          <button
            key={t}
            onClick={() => setTab(t)}
            style={{
              padding: "10px 20px",
              background: tab === t ? "#1976D2" : "#f0f0f0",
              color: tab === t ? "white" : "#333",
              border: "2px solid #1976D2",
              borderRadius: "8px",
              cursor: "pointer",
              fontWeight: "600",
              transition: "all 0.3s ease",
            }}
            onMouseEnter={e => {
              if (tab !== t) e.target.style.background = "#e0e0e0";
            }}
            onMouseLeave={e => {
              if (tab !== t) e.target.style.background = "#f0f0f0";
            }}
          >
            {t.charAt(0).toUpperCase() + t.slice(1)}
          </button>
        ))}
      </div>

      {/* Panel */}
      <pre style={{
        background: "#111",
        color: "#0f0",
        padding: 15,
        borderRadius: 8,
        overflow: "auto",
        maxHeight: "350px",
        fontFamily: "'Fira Code', monospace"
      }}>
        {getPretty(result.phases[tab])}
      </pre>

      {/* Métricas */}
      {result.metrics && (
        <>
          <h3>Métricas</h3>
          <pre style={{
            background: "#222",
            color: "#0af",
            padding: 15,
            borderRadius: 8,
            fontFamily: "'Fira Code', monospace"
          }}>
            {getPretty(result.metrics)}
          </pre>
        </>
      )}

      {/* Output */}
      {result.phases.execution?.output && (
        <>
          <h3>Salida del Programa</h3>
          <pre style={{
            background: "#000",
            color: "#0ff",
            padding: 15,
            borderRadius: 8,
            fontFamily: "'Fira Code', monospace"
          }}>
            {result.phases.execution.output}
          </pre>
        </>
      )}
    </div>
  );
}
