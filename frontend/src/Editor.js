export default function Editor({ code, setCode }) {
  return (
    <div
      style={{
        background: "rgba(255, 255, 255, 0.05)",
        backdropFilter: "blur(10px)",
        borderRadius: "12px",
        padding: "15px",
        boxShadow: "0 8px 20px rgba(0,0,0,0.2)",
        width: "100%",
        minHeight: "220px",
        display: "flex",
        flexDirection: "column",
        gap: "10px",
      }}
    >
      <label style={{ fontWeight: 600, marginBottom: 5, color: "#fff" }}>
        Editor de Código
      </label>
      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        spellCheck="false"
        style={{
          width: "100%",
          flexGrow: 1,
          background: "#1e1e1e",
          color: "#0f0",
          fontFamily: "'Fira Code', monospace",
          fontSize: "14px",
          border: "none",
          borderRadius: "8px",
          padding: "12px",
          resize: "vertical",
          minHeight: "150px",
          overflow: "auto",
          outline: "none",
        }}
        placeholder="Escribe tu código aquí..."
      />
    </div>
  );
}
