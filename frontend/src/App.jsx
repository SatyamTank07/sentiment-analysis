import { useState } from 'react';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!text.trim()) return;
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/predict', { text });
      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Error connecting to backend.");
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>🎬 Movie Review Sentiment Analyzer</h1>
      <textarea
        rows="6"
        cols="50"
        placeholder="Type your movie review here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        style={{ display: 'block', marginBottom: '1rem' }}
      />
      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? 'Analyzing...' : 'Analyze Sentiment'}
      </button>

      {result && (
        <div style={{ marginTop: '2rem' }}>
          <h2>Result:</h2>
          <p><strong>Sentiment:</strong> {result.label}</p>
          <p><strong>Confidence:</strong> {result.probability}%</p>
        </div>
      )}
    </div>
  );
}

export default App;

// docker run -P sentiment-frontend
// docker ps