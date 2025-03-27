import React, { useEffect, useState } from "react";

function Results() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/results/")
      .then((res) => res.json())
      .then((data) => setResults(data));
  }, []);

  return (
    <div>
      <h2>Screening Results</h2>
      <ul>
        {results.map((r) => (
          <li key={r.id}>
            <strong>{r.filename}</strong> - {r.skills}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Results;
