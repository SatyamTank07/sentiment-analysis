# 🚀 # Sentiment Analysis Web Application - Fine-tuned on IMDb Dataset

A complete **Sentiment Analysis** product built using **FastAPI**, **React.js**, **Transformers**, and **Docker** — fully containerized and deployed on **Render (free hosting)**.

## ✨ Live Demo

- **Frontend**: [https://frontend-wmo8.onrender.com/](https://frontend-wmo8.onrender.com/)
- **Backend API**: [https://backend-phgn.onrender.com/](https://backend-phgn.onrender.com/)


## 🛠 Tech Stack

- **Frontend**: React.js (Vite)
- **Backend**: FastAPI (Python)
- **NLP Model**: Huggingface Transformers (BERT Fine-tuned)
- **Containerization**: Docker, Docker-Compose
- **Deployment**: Render.com

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/SatyamTank07/sentiment-analysis.git
cd sentiment-analysis
```

### 2. Run with Docker Compose

```bash
docker-compose up --build
```
- Frontend will be available at [http://localhost:3000](http://localhost:3000)
- Backend will be available at [http://localhost:8000](http://localhost:8000)


## 🌐 Deployment Instructions (Render)
### Backend (FastAPI)
  - Create a new Web Service on Render.
  - Connect your GitHub repository.
  - Settings:
      - Environment: Docker
      - Dockerfile path: backend/Dockerfile
      - Port: 8000

### Frontend (React)
  - Create another Web Service.
  - Settings:
      - Environment: Docker
      - Dockerfile path: frontend/Dockerfile
      - Port: 3000
   
### 🧑‍💻 Author
Satyam Tank — [GitHub Profile](https://github.com/SatyamTank07)

### 🎯 Notes:
- This project uses free Render hosting — it may take few seconds to wake up after idle time.
