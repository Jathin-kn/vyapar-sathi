# Vyapar Sathi

An AI-powered conversational reporting and decision guidance system for MSMEs (Micro, Small & Medium Enterprises) using secure natural language queries.

## Features

- 🤖 **AI-Powered Queries**: Ask business questions in natural language and get instant insights
- 📊 **Smart Reporting**: Generate dynamic reports based on your business data
- 💡 **Decision Guidance**: Get recommendations and explanations for business decisions
- 🔒 **Secure**: Enterprise-grade security for sensitive business data
- ⚡ **Real-time Processing**: Instant responses to your queries

## Tech Stack

### Backend
- **Python 3.x** with Flask/FastAPI
- **Groq API** for AI-powered query processing
- Intent extraction and validation system
- Query and why-engine for intelligent responses

### Frontend
- **React** with Vite
- **Modern UI Components** for seamless user experience
- Real-time chat interface
- Data visualization and table views

## Project Structure

```
vyapar-sathi/
├── backend/
│   └── app/
│       ├── main.py              # Application entry point
│       ├── api/
│       │   └── query.py         # Query API endpoints
│       └── services/
│           ├── groq_client.py   # Groq API integration
│           ├── intent_extractor.py
│           ├── intent_validator.py
│           ├── query_engine.py
│           └── why_engine.py
├── frontend/
│   ├── src/
│   │   ├── pages/               # Page components
│   │   ├── components/          # Reusable components
│   │   └── api/                 # API client methods
│   └── vite.config.js
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Groq API key

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create a .env file with your configuration
GROQ_API_KEY=your_api_key_here
```

5. Run the server:
```bash
python app/main.py
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Build for production:
```bash
npm run build
```

## Usage

1. Start the backend server
2. Start the frontend development server
3. Open your browser to `http://localhost:5173` (or the URL shown in terminal)
4. Ask business questions in natural language:
   - "What's my revenue this month?"
   - "Show me top-selling products"
   - "Why did sales drop last week?"

## API Endpoints

### Queries
- `POST /api/query` - Submit a natural language query
- `GET /api/query/{id}` - Retrieve query results

### Why Explanations
- `POST /api/why` - Get explanations for insights

## Configuration

Update `.env` files in both backend and frontend directories with appropriate settings:

**Backend (.env):**
```
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

**Frontend (.env):**
```
VITE_API_URL=http://localhost:8000
```

## Development

### Running Tests
```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm test
```

### Code Quality
```bash
# Backend linting
pylint app/

# Frontend linting
npm run lint
```

## Contributing

1. Create a feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@vyaparsathi.com or create an issue in the repository.

## Acknowledgments

- Built with Groq API for powerful AI processing
- React and Vite for modern frontend development
- Python ecosystem for robust backend services
