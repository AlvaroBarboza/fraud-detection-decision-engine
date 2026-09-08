from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import time

app = FastAPI(
    title="Fraud Detection Decision Engine API",
    description="API de baixa latência para motor de decisão de risco antifraude",
    version="1.0.0"
)

# Modelo de Dados de Entrada (Payload da Transação)
class TransactionPayload(BaseModel):
    merchant_id: int = Field(..., description="ID do lojista")
    transaction_amount: float = Field(..., description="Valor da transação em BRL")
    minutes_since_last_txn: float = Field(..., description="Tempo em minutos desde a última transação do usuário (-1 se primeira)")
    is_first_purchase: bool = Field(..., description="Flag indicando se é a primeira compra do usuário")

# A lista de lojistas de alto risco identificada na análise exploratória do case
RISKY_MERCHANTS = [830, 1445, 879, 710, 1341]

@app.post("/predict")
def evaluate_fraud_risk(transaction: TransactionPayload):
    start_time = time.time()
    
    # Aplicação da Engine de Fraud
    is_risky_merchant = transaction.merchant_id in RISKY_MERCHANTS
    is_high_velocity_window = (0 <= transaction.minutes_since_last_txn <= 60) and (transaction.transaction_amount > 1000)
    is_risky_onboarding = transaction.is_first_purchase and (transaction.transaction_amount > 2500)
    
    # Decisão final baseada no motor composto
    predicted_fraud = is_risky_merchant or is_high_velocity_window or is_risky_onboarding
    
    # Definição de regras acionadas para auditoria
    triggered_rules = []
    if is_risky_merchant:
        triggered_rules.append("HIGH_RISK_MERCHANT")
    if is_high_velocity_window:
        triggered_rules.append("VELOCITY_WINDOW_HIT_AND_RUN")
    if is_risky_onboarding:
        triggered_rules.append("HIGH_VALUE_ONBOARDING")
        
    decision = "BLOCK" if predicted_fraud else "APPROVE"
    score = 0.95 if predicted_fraud else 0.05
    
    latency_ms = (time.time() - start_time) * 1000
    
    return {
        "decision": decision,
        "fraud_score": score,
        "regras_acionadas": triggered_rules,
        "latencia_ms": round(latency_ms, 2)
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "engine": "active"}