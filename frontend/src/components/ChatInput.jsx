import { useState } from 'react';

function ChatInput({ onSubmit }) {
  const [text, setText] = useState('');

  const handleSubmit = () => {
    if (!text.trim()) return;
    onSubmit(text);
    setText('');
  };

  return (
    <div className="chat-input">
      <input
        className="chat-input__field"
        type="text"
        placeholder="Ask about revenue, orders, growth..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter') handleSubmit();
        }}
      />
      <button className="chat-input__button" onClick={handleSubmit} disabled={!text.trim()}>
        Ask
      </button>
    </div>
  );
}

export default ChatInput;
