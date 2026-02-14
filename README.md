# 🚀 EventForge

EventForge is a lightweight **event ingestion service** built with **FastAPI**.
It is designed to demonstrate **backend system design**, **API development**, **data modeling**, and **reliability fundamentals** used in modern production systems.

> 🛠 **Status:** In Progress — actively developed as a hands-on backend engineering portfolio project.

---

## ✨ Why EventForge?

Many backend systems need a reliable way to **ingest, store, and query events** coming from multiple sources
(e.g. application activity, background jobs, system notifications).

EventForge is intentionally scoped to highlight **core backend engineering decisions** — not UI complexity.

**What this project emphasizes:**
- Clean and explicit API design
- Strong input validation and data modeling
- Production-oriented service structure
- Reliability, observability, and debuggability
- Developer-friendly local setup

---

## 🧩 Core Features

### ✅ Implemented (Current)
- FastAPI application skeleton
- Health check endpoint
- Project structure suitable for scaling
- Interactive API documentation via Swagger

### 🛣 Planned
- Event ingestion endpoints (`POST /events`, `GET /events/{id}`)
- Persistent storage with PostgreSQL
- Database migrations
- Pagination and filtering
- Structured logging and request correlation
- Rate limiting or retry-safe ingestion
- Automated tests and CI pipeline
- Containerized local development (Docker)

---

## 🏗 Architecture Overview

EventForge follows a simple, service-oriented architecture:

- **FastAPI** — API layer
- **PostgreSQL** — persistent event storage (planned)
- **Alembic** — database migrations (planned)

The design prioritizes **clarity, maintainability, and production-aligned patterns**.

---

## ⚙️ Getting Started (Local Development)

### Prerequisites
- Python 3.10+
- Git

### Setup
```bash
git clone https://github.com/GhazalSadeghpour/EventForge.git
cd EventForge

python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

```



```md
> If PowerShell blocks venv activation, run:  
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
```
### Run the API (development mode)


    python -m uvicorn app.main:app --reload

### Verify it works


    Health check: http://127.0.0.1:8000/health


### API docs (Swagger): http://127.0.0.1:8000/docs

Example:

    curl http://127.0.0.1:8000/health


### Expected response:

    {"status":"ok"}


### Run the tests:

         pytest -q
