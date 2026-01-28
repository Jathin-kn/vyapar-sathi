function MessageBubble({ text }) {
  const content = text ?? '';
  return <div className="message">{content}</div>;
}

export default MessageBubble;
