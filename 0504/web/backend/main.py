from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# 프로젝트의 절대 경로를 기반으로 템플릿 경로 설정
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(base_dir, 'frontend', 'templates'))

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    a = 5
    b = 10
    sum = a + b
    # 'index.html' 템플릿에 데이터를 전달
    return templates.TemplateResponse("index.html", {"request": request, "sum": sum})

@app.get("/chungeum", response_class=HTMLResponse)
async def chungeum(request: Request):
    message = "hello cheungeum!"
    return templates.TemplateResponse("chungeum.html", {"request": request, "message": message})

#####################################################################
#실행하는 방법

# 가상 환경 새로 생성
#python -m venv E:\study\0504\web\venv

# 가상 환경 활성화
### window
# .\venv\Scripts\Activate
### mac
# source venv/bin/activate

# 아래를 한 줄식 차레대로 설치
# pip install fastapi==0.74.1
# pip install "uvicorn[standard]"
# pip install jinja2

# uvicorn backend.main:app --reload