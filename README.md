# 🔐 Auth-page

A full-stack authentication system built with **Flask** (Python) on the backend and **React** on the frontend. It uses **JWT (JSON Web Tokens)** for secure user sessions and **SQLAlchemy** as the ORM to interact with a **PostgreSQL database running in Docker**.

---

## Prerequisites 
- Python: 3.13.3
- Flask: 3.1.1
- Node.js: v22.15.0
- React: 19.1.0
- Vite: 6.3.5
- Docker: 28.2.2
- postgres:17.5-alpine

## 🛠 Technologies

- **Backend**: Python + Flask  
- **Frontend**: React  
- **Database**: PostgreSQL + SQLAlchemy + Docker  



## Instalations

### clone repository
git clone https://github.com/msg019/auth-page.git     
cd auth-page  

### set up docker container  
docker compose up -d  

### set up Backend
cd backend  
python -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt     
python3 main.py  

### set up Frontend  
cd frontend  
npm install  
npm run dev  

