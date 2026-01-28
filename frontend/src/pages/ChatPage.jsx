import { useState } from 'react';
import ChatInput from '../components/ChatInput';
import MessageBubble from '../components/MessageBubble';
import WhyPanel from '../components/WhyPanel';
import TableView from '../components/TableView';
import { askQuestion } from '../api/queryApi';

function ChatPage() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (question) => {
    setError(null);
    setLoading(true);
    try {
      const response = await askQuestion(question);
      setData(response);
    } catch (err) {
      setError(err?.message || 'Something went wrong');
      setData(null);
    } finally {
      setLoading(false);
    }
  };

  const hasWhy = Array.isArray(data?.why) && data.why.length > 0;
  const hasTable = Array.isArray(data?.table) && data.table.length > 0;

  return (
    <section id="chat" className="layout chat-section">
      <header className="hero">
        <p className="eyebrow">Insights assistant</p>
        <h1>Ask your business anything</h1>
        <p className="subtext">Type a question, get an answer, and see the why behind the change.</p>
      </header>

      <section className="card shell">
        <ChatInput onSubmit={handleSubmit} />

        {loading && <div className="pill pill-warn">Thinking...</div>}
        {error && <div className="pill pill-error">{error}</div>}

        {data && (
          <div className="stack">
            {data.answer && <MessageBubble text={data.answer} />}
            {hasWhy && <WhyPanel why={data.why} />}
            {hasTable && <TableView rows={data.table} />}
          </div>
        )}
      </section>
    </section>
  );
}

export default ChatPage;
