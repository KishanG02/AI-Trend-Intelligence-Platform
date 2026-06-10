<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00D4FF&height=200&section=header&text=AI%20Trend%20Intelligence%20Platform&fontSize=36&fontColor=ffffff&fontAlignY=38&desc=Real-Time%20Technology%20Trend%20Monitoring%20%7C%20Kafka%20%7C%20Airflow%20%7C%20Groq%20LLM%20%7C%20Streamlit&descAlignY=58&descSize=14" alt="Header"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)](https://kafka.apache.org/)
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)](https://airflow.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq%20LLM-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com/)
[![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white)](https://min.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/KrishanG02/ai-trend-intelligence-platform?style=flat-square&color=yellow)](https://github.com/KrishanG02/ai-trend-intelligence-platform/stargazers)
[![Forks](https://img.shields.io/github/forks/KrishanG02/ai-trend-intelligence-platform?style=flat-square&color=blue)](https://github.com/KrishanG02/ai-trend-intelligence-platform/network)
[![Issues](https://img.shields.io/github/issues/KrishanG02/ai-trend-intelligence-platform?style=flat-square&color=red)](https://github.com/KrishanG02/ai-trend-intelligence-platform/issues)

<br/>

> **An end-to-end Real-Time AI Trend Intelligence Platform** that continuously monitors emerging technology trends from News APIs and YouTube, processes streams through Kafka and Airflow, performs sentiment analysis, forecasts future trends, and surfaces AI-powered executive summaries — all through a single interactive Streamlit dashboard.

<br/>

[🚀 Quick Start](#-quick-start) · [🏗️ Architecture](#️-architecture) · [✨ Features](#-features) · [📊 Dashboard](#-dashboard-modules) · [🛠️ Tech Stack](#️-tech-stack) · [🤝 Contributing](#-contributing)

</div>

---

## 📌 Why This Project?

Organizations today are overwhelmed with technology signals — news, YouTube, social feeds — but lack the infrastructure to turn that noise into actionable intelligence. This platform closes that gap.

| Problem | Solution |
|---|---|
| Technology trends move fast | Real-time ingestion via Kafka + News/YouTube APIs |
| Raw data is unstructured | NLP sentiment analysis + unified trend scoring |
| Hard to forecast what's next | ML-powered trend forecasting engine |
| Reports take too long to write | Groq LLM generates executive summaries automatically |
| No single source of truth | MinIO data lake centralizes all analytics |
| Complex to navigate | Interactive Streamlit dashboard with 7 modules |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                                 │
│                                                                     │
│          📰 News API                    🎬 YouTube Data API         │
│               │                                │                   │
│               ▼                                ▼                   │
│       ┌──────────────┐              ┌──────────────────┐           │
│       │ News Producer│              │ YouTube Producer │           │
│       └──────┬───────┘              └────────┬─────────┘           │
└──────────────┼──────────────────────────────┼─────────────────────┘
               │                              │
               ▼                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    ⚡ APACHE KAFKA STREAMING                        │
│                     (Real-Time Message Bus)                         │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   🔄 APACHE AIRFLOW ORCHESTRATION                   │
│                                                                     │
│   Fetch News → Validate → Sentiment → Scoring → Leaderboard        │
│       → Unified Trends → History → Forecasting → AI Summary        │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
               ┌──────────────┼──────────────┐
               ▼              ▼              ▼
        🤖 Groq LLM    📈 ML Forecast   📊 Analytics
        (Summaries)    (Predictions)    (Scoring)
               │              │              │
               └──────────────┼──────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    🗄️ MINIO DATA LAKE                               │
│                  (S3-Compatible Storage)                            │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    🖥️ STREAMLIT DASHBOARD                           │
│   Overview │ Trends │ History │ Forecast │ Sentiment │ AI Insights  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ✨ Features

<details>
<summary><b>📡 Real-Time Data Collection</b></summary>

<br/>

- **News API Integration** — Pulls breaking technology news headlines and articles in real time
- **YouTube Data API v3** — Fetches trending tech video metadata, titles, and channel signals
- **Technology Keyword Extraction** — Automatically identifies and tracks emerging tech terms
- **Automated Ingestion Pipelines** — No manual triggers; continuous polling on configurable intervals

</details>

<details>
<summary><b>⚙️ Data Engineering Pipeline</b></summary>

<br/>

- **Apache Kafka Streaming** — Decoupled, fault-tolerant message streaming between producers and consumers
- **Apache Airflow Orchestration** — DAG-based pipeline scheduling, monitoring, and retry logic
- **Dockerized Infrastructure** — All services (Kafka, Airflow, MinIO) spin up with a single `docker compose up`
- **MinIO S3-Compatible Data Lake** — Persistent, queryable storage for all raw and processed analytics

</details>

<details>
<summary><b>🤖 AI-Powered Analytics</b></summary>

<br/>

- **VADER Sentiment Analysis** — Fast, lexicon-based sentiment scoring on every article and video
- **Unified Trend Scoring** — Combines news frequency, video views, and sentiment into a single score
- **Trend Leaderboards** — Auto-ranks the hottest technologies by composite score
- **Groq LLM Executive Summaries** — Generates natural language trend reports for business stakeholders

</details>

<details>
<summary><b>📈 Predictive Analytics</b></summary>

<br/>

- **Historical Trend Tracking** — Stores time-series data for every monitored technology
- **ML Trend Forecasting Engine** — Uses scikit-learn to project future trend scores
- **Growth Analysis** — Quantifies week-over-week and month-over-month technology momentum
- **Forward-Looking Predictions** — Surfaces which technologies are about to trend before they peak

</details>

---

## 📊 Dashboard Modules

| Module | Description |
|---|---|
| 🏠 **Overview** | High-level trend intelligence snapshot with top movers |
| 🔥 **Unified Trends** | Combined News + YouTube scores in one leaderboard |
| 📅 **Trend History** | Time-series evolution of any tracked technology |
| 🔮 **Forecast Analytics** | ML-powered future trend predictions with confidence ranges |
| 💬 **Sentiment Analytics** | Positive/Negative/Neutral breakdown across tech topics |
| 🤖 **AI Insights** | Groq-generated executive summaries and narrative reports |
| 🩺 **Pipeline Health** | Live status monitoring for Kafka, Airflow, and analytics jobs |

---

## 🛠️ Tech Stack

```
┌─────────────────┬────────────────────────────────────────────────┐
│ Layer           │ Technologies                                   │
├─────────────────┼────────────────────────────────────────────────┤
│ Data Ingestion  │ News API · YouTube Data API v3                 │
│ Streaming       │ Apache Kafka · Docker                          │
│ Orchestration   │ Apache Airflow                                 │
│ Storage         │ MinIO (S3-Compatible Data Lake)                │
│ AI / LLM        │ Groq (llama3-70b-8192) · VADER Sentiment       │
│ ML / Forecasting│ Scikit-Learn · NumPy · Pandas                  │
│ Visualization   │ Streamlit · Plotly                             │
│ Language        │ Python 3.10+                                   │
└─────────────────┴────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
ai-trend-engine/
│
├── 📁 airflow/
│   ├── dags/                    # Airflow DAG definitions
│   └── docker-compose.yml       # Airflow Docker setup
│
├── 📁 analytics/
│   ├── trend_scoring.py         # Composite trend scoring logic
│   ├── leaderboard.py           # Trend leaderboard generator
│   ├── trend_history.py         # Historical time-series tracker
│   └── trend_forecast.py        # ML forecasting engine
│
├── 📁 ai/
│   ├── sentiment_analyzer.py    # VADER sentiment pipeline
│   └── trend_report_generator.py # Groq LLM summary generator
│
├── 📁 dashboard/
│   └── app.py                   # Streamlit dashboard (7 modules)
│
├── 📁 storage/
│   └── minio_uploader.py        # MinIO data lake uploader
│
├── 📁 streaming/
│   ├── news_producer.py         # Kafka news producer
│   └── youtube_producer.py      # Kafka YouTube producer
│
├── 📁 config/                   # Configuration files
├── 📁 data-lake/                # Local data lake artifacts
├── 📄 requirements.txt
└── 📄 .env.example
```

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:

- Python 3.10+
- Docker & Docker Compose
- API keys for [News API](https://newsapi.org/), [YouTube Data API v3](https://developers.google.com/youtube/v3), and [Groq](https://console.groq.com/)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/KrishanG02/ai-trend-intelligence-platform.git
cd ai-trend-intelligence-platform
```

### Step 2 — Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
NEWS_API_KEY=your_news_api_key_here
YOUTUBE_API_KEY=your_youtube_api_key_here
GROQ_API_KEY=your_groq_api_key_here
KAFKA_BROKER=localhost:9092
```

### Step 5 — Start Kafka

```bash
docker compose up -d
```

### Step 6 — Start Airflow

```bash
cd airflow
docker compose up -d
```

> Access Airflow UI at: `http://localhost:8080`

### Step 7 — Launch Dashboard

```bash
streamlit run dashboard/app.py
```

> Access Dashboard at: `http://localhost:8501`

---

## 📈 Analytics Pipeline Flow

```
① Fetch News & YouTube Data
         ↓
② Validate & Clean Payloads
         ↓
③ VADER Sentiment Analysis
         ↓
④ Unified Trend Scoring
         ↓
⑤ Leaderboard Generation
         ↓
⑥ Trend History Logging
         ↓
⑦ ML Trend Forecasting
         ↓
⑧ Groq AI Summary Generation
         ↓
⑨ Upload to MinIO Data Lake
         ↓
⑩ Render in Streamlit Dashboard
```

---

## 🎯 Use Cases

| Domain | Application |
|---|---|
| 🏢 **Enterprise Intelligence** | Monitor competitor technology adoption in real time |
| 📊 **Market Research** | Track AI, cloud, and DevOps trend momentum |
| 🔍 **Competitive Analysis** | Benchmark technology topics against industry peers |
| 📝 **Executive Reporting** | Auto-generate weekly trend briefings with Groq LLM |
| 🎓 **Data Engineering Portfolio** | Demonstrates Kafka + Airflow + MinIO + LLM in a single project |
| ☁️ **Cloud Technology Tracking** | Follow AWS, GCP, Azure, and Kubernetes trend trajectories |

---

## 🔮 Future Enhancements

- [ ] Apache Spark integration for distributed processing
- [ ] Databricks support for large-scale analytics
- [ ] Real-time streaming analytics dashboard
- [ ] LLM-based technology recommendation engine
- [ ] Vector Search & RAG for semantic trend retrieval
- [ ] Multi-cloud deployment (AWS / GCP / Azure)
- [ ] Automated alerting system (Slack / email notifications)

---

## 👨‍💻 Author

<div align="center">

**Krishna Gupta**

*Cloud Engineering · Data Engineering · Generative AI*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/krishnag0211)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KrishanG02)

</div>

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "feat: add your feature description"

# 4. Push to your branch
git push origin feature/your-feature-name

# 5. Open a Pull Request
```

---

## ⭐ Support

If this project helped you, please consider:

- ⭐ **Starring** the repository
- 🍴 **Forking** it to build your own version
- 🐛 **Opening issues** for bugs or feature requests
- 📢 **Sharing** it with your network

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00D4FF&height=100&section=footer" alt="Footer"/>

*Built with ❤️ by Krishna Gupta — Turning data streams into actionable intelligence.*

</div>
