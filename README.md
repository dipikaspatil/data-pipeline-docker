# Data Pipeline in Docker
Creating a simple data pipeline in Docker involves defining a few key stages that simulate data flow — e.g., ingestion → transformation → storage — and running each stage as a containerized service.

An example pipeline:

Ingest data using a Python script (e.g., CSV or API).
Transform data with another Python service.
Store data into a lightweight database like PostgreSQL or just a file.

# 🐳 Dockerized Data Pipeline (Ingest → Transform)

This is a simple data pipeline built using **Python** and **Docker Compose**. It simulates a two-step process:

1. **Ingest:** A Python script writes sample data to `raw.csv`
2. **Transform:** Another script reads that file, modifies it, and writes to `clean.csv`

---

## 📂 Project Structure

data-pipeline-docker/
├── docker-compose.yml
├── Dockerfiles/
│ ├── Dockerfile.ingest
│ └── Dockerfile.transform
├── ingest/
│ └── ingest.py
├── transform/
│ └── transform.py
├── shared_data/
└── README.md


---

## ▶️ How to Run

> 🧰 Requirements: Docker & Docker Compose installed on your system

```bash
# Build the containers
docker-compose build

# Run the pipeline
docker-compose up

After running, you'll find the output in the shared_data/ folder:

raw.csv → created by the ingest step

clean.csv → created by the transform step

# Clean up after run

docker-compose down

