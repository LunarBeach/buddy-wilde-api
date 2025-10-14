from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://buddywilde.com", "https://www.buddywilde.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DealReq(BaseModel):
    n_players: int

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/deal")
def deal(req: DealReq):
    return {"message": "dealt", "n_players": req.n_players}

