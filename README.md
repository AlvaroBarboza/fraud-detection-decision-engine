# 🛡️ Fraud Detection & Decision Engine (Risk Analysis & API)

[![Python 3.9+](https://img.shields.io/badge/python-3.9%25+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%25+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/status-production_ready-success.svg)]()

> **Case sênior de engenharia de dados e risco antifraude**, unindo rigor metodológico (*Point-in-Time*), arquitetura de baixa latência em microsserviço (FastAPI) e conteinerização (Docker) para o ciclo completo de decisão transacional.

---

## 📋 Sumário Executivo
Este projeto evolui de uma análise exploratória de 3.199 transações (Nov/Dez 2019, R$ 2,45M em GMV) para um **serviço de decisão antifraude executável**. O objetivo é equilibrar a mitigação severa de prejuízos financeiros (taxa base de chargeback de 23,14% em valor) com o controle rigoroso da fricção operacional.

---

## 🏗️ Arquitetura e Engenharia do Projeto

1. **Análise Exploratória & Baseline:** Identificação de severidade financeira e assimetria de tickets.
2. **Engenharia Point-in-Time:** Ordenação cronológica estrita por usuário para evitar *data leakage* em features temporais (`minutes_since_last_txn`).
3. **Motor de Decisão Multifator:** Combinação de lojistas de alto risco, janelas de velocidade crítica (*Hit and Run* de 30 min a 24h) e onboardings de alto valor.
4. **Serviço de Baixa Latência (FastAPI):** Exposição das regras de negócio em um endpoint REST orientado a respostas em $p99 < 100ms$.
5. **Conteinerização (Docker):** Empacotamento isolado do ambiente e dependências para reprodutibilidade total em infraestrutura.

---

## 🚀 Como Subir o Serviço via Docker

### 1. Construir a Imagem Docker
Na raiz do repositório, execute o comando de build:
```bash
docker build -t fraud-engine-api .

2. Executar o Container
Suba o container mapeando a porta padrão 8000:

Bash
docker run -d -p 8000:8000 --name fraud-api-container fraud-engine-api
🔌 Documentação da API (/predict)
O microsserviço recebe uma carga transacional via JSON e retorna a decisão analítica com explainability instantânea e métrica de latência.

Exemplo de Requisição (cURL)
Bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "merchant_id": 830,
  "transaction_amount": 1500.0,
  "minutes_since_last_txn": 15,
  "is_first_purchase": false
}'
Exemplo de Resposta da API
JSON
{
  "decision": "BLOCK",
  "fraud_score": 0.95,
  "regras_acionadas": [
    "HIGH_RISK_MERCHANT",
    "VELOCITY_WINDOW_HIT_AND_RUN"
  ],
  "latencia_ms": 1.42
}
⚠️ Notas Técnicas e Limitações
Validação In-Sample: O histórico de risco dos lojistas foi mapeado sobre o período total da amostra; em ambientes de produção corporativa, esta feature requer janelas deslizantes (rolling windows).

Censura à Direita (Right-Censoring): A janela de fechamento em dezembro/2019 introduz atraso de maturação de chargebacks (lag), exigindo o uso de curvas de atraso em cenários reais para evitar subestimação do risco na cauda recente.

Desenvolvido com rigor técnico de engenharia de dados e risco.