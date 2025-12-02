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
                marginBottom: 10
            }}>
                {tabs.map(t => (
                    <button
                        key={t}
                        onClick={() => setTab(t)}
                        style={{
                            padding: "8px 16px",
                            background: tab === t ? "#1976D2" : "#eee",
                            color: tab === t ? "white" : "black",
                            border: "none",
                            borderRadius: "6px",
                            cursor: "pointer"
                        }}
                    >
                        {t}
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
                maxHeight: "350px"
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
                        borderRadius: 8
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
                        borderRadius: 8
                    }}>
                        {result.phases.execution.output}
                    </pre>
                </>
            )}
        </div>
    );
}
