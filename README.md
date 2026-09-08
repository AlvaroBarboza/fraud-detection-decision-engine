# 🛡️ Fraud Detection & Decision Engine (Risk Analysis & API)

[![Python 3.9+](https://img.shields.io/badge/python-3.9%25+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%25+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/status-production_ready-success.svg)]()

> **Case de engenharia de dados e risco antifraude**, métodologia (*Point-in-Time*), arquitetura de baixa latência em microsserviço (FastAPI) e conteinerização (Docker) para o ciclo completo de decisão transacional.

---

## Resumo 
Este projeto evolui de uma análise exploratória de 3.199 transações (Nov/Dez 2019, R$ 2,45M em GMV) para um **serviço de decisão antifraude executável**. O objetivo é equilibrar a mitigação severa de prejuízos financeiros (taxa base de chargeback de 23,14% em valor) com o controle rigoroso da fricção operacional.

---

## Arquitetura e Engenharia do Projeto

1. **Análise Exploratória & Baseline:** Identificando severidade financeira e assimetria de tickets.
2. **Engenharia Point-in-Time:** Ordenação cronológica baseada usuário distinto para evitar *data leakage* em features temporais (`minutes_since_last_txn`).
3. **Motor de Decisão Multifator:** Combinação de lojistas de alto risco, janelas de velocidade crítica (*Hit and Run* de 30 min a 24h) e onboardings de alto valor.
4. **Serviço de Baixa Latência (FastAPI):** Exposição das regras de negócio em um endpoint REST orientado a respostas em $p99 < 100ms$.
5. **Conteinerização (Docker):** Empacotamento isolado do ambiente e dependências para reprodutibilidade total em infraestrutura.

---

