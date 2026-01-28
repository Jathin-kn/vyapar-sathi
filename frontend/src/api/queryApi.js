export async function askQuestion(question) {
  try {
    const response = await fetch('http://localhost:8000/api/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question }),
    });

    if (!response.ok) {
      const message = await response.text();
      throw new Error(message || 'Request failed');
    }

    return await response.json();
  } catch (error) {
    throw error;
  }
}
