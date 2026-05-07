# Smart Travel Planner — Agentic RAG System

A fully local, multi-agent AI travel planning system built using CrewAI, Ollama, ChromaDB, n8n, Streamlit, and Docker.

The system generates budget-aware travel itineraries using local LLM inference, Retrieval-Augmented Generation (RAG), and automated travel-intelligence pipelines — without relying on paid cloud AI APIs.

---

# Features

* Multi-agent AI workflow using CrewAI
* Fully local LLM inference via Ollama
* RAG pipeline using ChromaDB
* Automated ETL/data-refresh workflows using n8n
* Budget-aware itinerary generation
* Weather and currency integration
* Dockerized deployment
* Streamlit-based interactive dashboard
* Local-first architecture with zero SaaS dependency

---

# Architecture

```text
                           ┌─────────────────────┐
                           │      User Input     │
                           │ Destination/Budget  │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │     Streamlit UI    │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │    CrewAI Agents    │
                           │─────────────────────│
                           │ • Research Agent    │
                           │ • Budget Analyst    │
                           │ • Itinerary Planner │
                           └──────────┬──────────┘
                                      │
                        ┌─────────────┴─────────────┐
                        ▼                           ▼
             ┌─────────────────┐         ┌─────────────────┐
             │   ChromaDB RAG  │         │ Ollama + Llama3 │
             │ Vector Retrieval│         │ Local Inference │
             └─────────────────┘         └─────────────────┘
                        ▲
                        │
             ┌─────────────────────┐
             │   Travel Knowledge  │
             │ Wikivoyage/Kaggle   │
             │ Weather/Currency    │
             └─────────────────────┘
                        ▲
                        │
             ┌─────────────────────┐
             │    n8n Workflows    │
             │ Automated ETL/Data  │
             └─────────────────────┘
```

---

# Tech Stack

## AI & Agents

* Python
* CrewAI
* Ollama
* Llama 3 / Mistral

## RAG & Storage

* ChromaDB
* Sentence Transformers

## Automation & ETL

* n8n
* Pandas
* BeautifulSoup

## Frontend

* Streamlit

## Deployment

* Docker
* Docker Compose

---

# Project Structure

```text
smart-travel-planner/
│
├── app/
│   ├── streamlit_app.py
│   ├── crew.py
│   ├── rag.py
│   ├── prompts.py
│   └── config.py
│
├── scripts/
│   ├── ingest_weather.py
│   ├── ingest_currency.py
│   ├── ingest_wikivoyage.py
│   └── build_vector_db.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── chroma/
│
├── n8n/
│   └── workflows/
│
├── screenshots/
├── docs/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# How It Works

## 1. Data Ingestion

Travel-related information is collected from:

* Wikivoyage
* Open-Meteo
* Frankfurter API
* Kaggle datasets

---

## 2. Data Processing

Data is cleaned and normalized using:

* Pandas
* BeautifulSoup
* Python ETL scripts

---

## 3. Vector Database

Processed travel knowledge is embedded and stored in ChromaDB for semantic retrieval.

---

## 4. Agentic Workflow

CrewAI orchestrates multiple specialized agents:

### Research Agent

Retrieves travel information from the RAG knowledge base.

### Budget Analyst Agent

Analyzes travel costs based on user budget and duration.

### Itinerary Planner Agent

Generates a structured day-by-day itinerary.

---

## 5. Local LLM Inference

Ollama runs Llama 3 locally for:

* itinerary generation
* travel recommendations
* summarization
* reasoning

No cloud APIs are required.

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/smart-travel-planner.git
cd smart-travel-planner
```

---

## 2. Install Ollama

Install Ollama from:

[Ollama Official Website](https://ollama.com?utm_source=chatgpt.com)

Start Ollama:

```bash
ollama serve
```

Pull a model:

```bash
ollama pull llama3.1:8b
```

Alternative lightweight model:

```bash
ollama pull mistral
```

---

## 3. Start Docker

Make sure Docker Desktop is running.

Install Docker from:

[Docker Official Website](https://www.docker.com/products/docker-desktop/?utm_source=chatgpt.com)

---

## 4. Build Containers

```bash
docker compose build
```

---

## 5. Start Application

```bash
docker compose up
```

Run in detached mode:

```bash
docker compose up -d
```

---

# Application URLs

| Service   | URL                                            |
| --------- | ---------------------------------------------- |
| Streamlit | [http://localhost:8501](http://localhost:8501) |
| n8n       | [http://localhost:5678](http://localhost:5678) |

---

# Running the Streamlit App Manually

```bash
streamlit run app/streamlit_app.py
```

---

# Example Usage

Input:

```text
Destination: Paris
Days: 5
Budget: 800 EUR
Style: Cultural
```

Output:

* Budget estimation
* Suggested attractions
* Weather notes
* Currency insights
* Day-by-day itinerary
* Travel tips

---

# n8n Workflows

The project includes automated workflows for:

* Weather data refresh
* Currency updates
* Knowledge base rebuilding
* Scheduled ingestion pipelines

Workflow exports are stored in:

```text
n8n/workflows/
```

---

# Docker Services

## Streamlit Container

Runs the frontend dashboard and CrewAI workflow.

## n8n Container

Handles automation and ETL orchestration.

## Ollama

Runs locally on the host machine for optimized Apple Silicon performance.

---

# Screenshots

## Dashboard

Add screenshot here.

## Generated Itinerary

Add screenshot here.

## n8n Workflow

Add screenshot here.

---

# Demo Video

Add your demo video link here.

Example:

```text
https://youtube.com/your-demo-video
```

---

# Future Improvements

* Flight API integration
* Hotel recommendation engine
* Interactive maps
* Voice assistant support
* Persistent user memory
* Vision-language model support
* Multi-language itinerary generation

---

# Why This Project Matters

This project demonstrates:

* Agentic AI system design
* Retrieval-Augmented Generation (RAG)
* Local LLM deployment
* Automated ETL pipelines
* Multi-agent orchestration
* Dockerized AI systems engineering

---

# Author

Nauman Ahmed

* LinkedIn: Add link
* GitHub: Add link
* Portfolio: Add link

---

# License

This project is licensed under the MIT License.
