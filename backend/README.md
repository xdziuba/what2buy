# What2Buy Backend

Backend of the **What2Buy** application built with **FastAPI**.  
It handles API requests from the frontend, communicates with the AI agent (LangChain + ChatGPT),
and returns structured product search results.

---

## Install the dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
**Make sure you have a .env file with required API keys.**

---

## Start the API in development mode
```bash
fastapi dev main.py
```

**The backend will be available at:**

http://127.0.0.1:8000


**API documentation (Swagger):**

http://127.0.0.1:8000/docs