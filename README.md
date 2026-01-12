# What2Buy 🛒

**What2Buy** is an AI-powered web application that helps users find and compare the best product offers across multiple marketplaces simultaneously.
The project was created as part of a bachelor's thesis and presents a modern full-stack architecture using:

- **FastAPI (Python)** – the backend API
- **LangChain + ChatGPT** – an AI agent for searching and structuring data
- **Quasar + Vue 3** – the frontend
- **Docker + Docker Compose** – containerization and execution of the entire system
<br><br>
**The application enables:**

- searching for products using a natural language query,
- selecting marketplaces (Amazon, Allegro, MediaExpert, etc.),
- obtaining structured results,
- comparing products in pairs with the same specifications,
- quickly navigating to offers.

---
## 🧱 Architecture
**what2buy**/<br>
├─ backend/ - FastAPI + LangChain + MCP<br>
├─ frontend/ - Quasar / Vue 3<br>
└─ docker/ - Dockerfiles + docker-compose.yml<br>

- The backend runs in a separate container and provides an API (`:8000`)
- The frontend is built for a static application and served by nginx (`:8080`)
- Communication is via HTTP (REST)

---

## 🚀 Project Launch

**Requirements:**
- Docker
- Docker Compose

```bash
cd docker
docker compose build
docker compose up
```
**After launch:**

Frontend: http://localhost:8080

Backend (Swagger): http://localhost:8000/docs
<br><br><br>
**In the backend/ directory, there is an .env file where you should set the API keys:**

```
OPENAI_API_KEY=...
MCP_API_KEY=...
MCP_SCRAPING_BROWSER_USER=...
MCP_ULOCKER_ZONE=...
```

---

## 🧠 Technologies Used
**Backend:**
- Python 3.11
- FastAPI
- LangChain
- OpenAI ChatGPT
- MCP (BrightData)
- Pydantic

**Frontend:**
- Vue 3
- Quasar Framework
- Pinia
- Axios

**DevOps:**
- Docker
- Docker Compose
- Nginx