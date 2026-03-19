<h1 align="center">AI CUSTOMER SUPPORT CHATBOT</h1>
<h3 align="center">An AI Chatbot that can handle most of your customer's repetitive questions instantly</h3>

<img width="1835" height="936" alt="{F0E9B500-F027-4E7A-B045-1373351F94AF}" src="https://github.com/user-attachments/assets/d1828b06-7da8-4cd6-afd0-ce72b036a62b" />


## What it does: 
Every business receives the same customer questions over and over concerning opening hours, pricing, order status, return policies. Each one takes time to answer manually and pulls your team away from work that actually matters.

This chatbot handles all of it automatically by responding to customers instantly at any hour of the day without any human intervention.

The results are faster response times and overall happier customers


## Video Demo

https://github.com/user-attachments/assets/1e617f23-e335-4572-acdb-c22d8996cc03


## Live link: try it out for yorself
**NB**: the chatbot was deployed on a random sites as a chat widget for demo purposes only, here's the link

https://gocart-production-dfb2.up.railway.app/



## Use Cases

- **E-commerce Support**: Order status, returns, product questions
- **SaaS Help Desk**: Account issues, feature questions, troubleshooting
- **Service Businesses**: Appointment scheduling, service inquiries
- **General Customer Service**: FAQs, policies, general information


## Tech Stack

- **Agent Framework**: LangChain (for agent orchestration and tool management)
- **Language Model**: LangChain Chat Model (powered by OpenAI)
- **Embeddings**: OpenAI Embedding Model
- **Query Engine**: LangChain RAG pipeline
- **Memory System**: LangChain conversation memory
- **API Framework**: FastAPI    
- **Tools**: LangChain tools for extensible agent capabilities



## Run Locally

1. Clone the repository
```bash
git clone https://github.com/amvvr1/demo-chatbot.git
cd support chatbot
```

2. Install dependencies with UV
```bash
uv sync
```


3. Set up environment variables
```bash
# Create .env file
OPENAI_API_KEY=your_openai_api_key_here
```

4. Run the FastAPI application
```bash
uv run uvicorn main:app --reload
```

Or with standard Python:
```bash
uvicorn main:app --reload
```

5. Access the API
- API: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs


## Contact
**Email:**  scholarammar@gmail.com
