export default function Editor({ code, setCode }) {
    return (
        <textarea
            style={{ width: "100%", height: "200px" }}
            value={code}
            onChange={(e) => setCode(e.target.value)}
        />
    );
}
