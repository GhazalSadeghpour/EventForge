# 🚀 EventForge

**EventForge** is a lightweight **event ingestion service** built with **FastAPI** and **PostgreSQL**.  
It focuses on **backend system design**, **API development**, **data modeling**, and **reliability fundamentals** used in modern production systems.

> 🛠️ **Status:** In Progress  
> This project is actively being developed as a hands-on backend engineering project.

---

## ✨ Why EventForge?

Many systems require a reliable way to ingest, store, and query events coming from multiple sources.  
EventForge is intentionally scoped to highlight **core backend engineering decisions**, not UI complexity.

What this project emphasizes:

- Clean and explicit API design  
- Strong input validation and data modeling  
- Production-aligned database usage  
- Reliability, observability, and debuggability  
- Developer-friendly local setup  

---

## 🧩 Core Features

### ✅ Implemented / MVP
- REST API for event ingestion  
- Schema validation for incoming events  
- PostgreSQL persistence  
- Health check endpoint  
- Docker-based local development  

### 🛣️ Planned
- Idempotent event ingestion  
- Pagination and filtering  
- Structured logging with request correlation  
- Rate limiting or retry-safe ingestion  
- Basic metrics and monitoring  
- Automated tests and CI pipeline  

---

## 🏗️ Architecture Overview

EventForge follows a simple, service-oriented architecture:

- **FastAPI** — API layer  
- **PostgreSQL** — persistent event storage  
- **Docker Compose** — local orchestration  
- **Alembic** — database migrations  

The design prioritizes **clarity**, **maintainability**, and **production-aligned patterns**.

---

## 🗄️ Data Model (Initial)

### `events`

| Column       | Type      | Description                          |
|-------------|-----------|--------------------------------------|
| `id`        | UUID      | Primary key                          |
| `created_at`| timestamp | Event creation time                 |
| `event_type`| string    | Type/category of the event          |
| `source`    | string    | Origin of the event                 |
| `payload`   | JSONB     | Flexible event-specific data        |

Indexes will be added based on query patterns (e.g. `event_type`, `created_at`).

---

## ⚙️ Getting Started (Local Development)

### Prerequisites
- Docker  
- Docker Compose  

### Run locally
```bash
docker compose up --build
