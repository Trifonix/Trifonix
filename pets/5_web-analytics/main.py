from fastapi import FastAPI, Request
from visits import Visit, visits_list
import matplotlib.pyplot as plt
from collections import Counter
from io import BytesIO
import base64
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Сервис статистики посещений работает"}

@app.get("/visit")
def record_visit(request: Request):
    ip = request.client.host
    user_agent = request.headers.get("user-agent", "unknown")
    visit = Visit(ip, user_agent)
    visits_list.append(visit)
    return {"message": "Посещение зафиксировано", "ip": ip, "user_agent": user_agent, "time": str(visit.time)}

@app.get("/stats")
def stats():
    ips = [v.ip for v in visits_list]
    counter = Counter(ips)

    plt.figure(figsize=(6,4))
    plt.bar(counter.keys(), counter.values())
    plt.xlabel("IP")
    plt.ylabel("Количество посещений")
    plt.title("Статистика посещений")
    
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()

    return {
        "visits_count": len(visits_list),
        "visits_per_ip": counter,
        "graph_base64": img_base64
    }
