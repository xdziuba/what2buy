# What2Buy – Docker Setup

This directory contains all Docker-related configuration for the **What2Buy** project.
It allows running the entire application (frontend + backend) using Docker Compose.

---

## Requirements

- Docker
- Docker Compose

---

## Build and run the application

**From this directory:**

```bash
docker compose build
docker compose up
```
---

## After startup

- Frontend: http://localhost:8080
- Backend API: http://localhost:8000
- Backend docs: http://localhost:8000/docs

**Services:**
- frontend – Quasar/Vue app served by Nginx
- backend – FastAPI application with AI agent

**Each service runs in its own container and communicates over Docker’s internal network.**

---

## Stop the application
```bash
docker compose down
```