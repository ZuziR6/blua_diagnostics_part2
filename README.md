# BluaDiagnostics - Sprint 2

## Arquitetura

Sistema multi-agente utilizando LangGraph:

- Supervisor Agent
- Triage Agent
- Prescription Agent
- Escalation Agent

Fluxo:

Supervisor → Triagem | Prescrição | Escalada Humana

## Tecnologias

- LangChain
- LangGraph
- ChromaDB
- OpenAI
- Streamlit

## Como executar

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Configurar variáveis

Criar arquivo `.env`

```env
OPENAI_API_KEY=sua_chave
```

### Gerar Vector Store

```bash
python -m src.rag.ingest
```

### Rodar aplicação

```bash
streamlit run app/streamlit_app.py
```

### Rodar evals

```bash
python evals/eval_runner.py
```

## Guardrails

- Red flag detection
- Escalada automática
- Out-of-scope rejection

## Métricas

- Accuracy por categoria
- Tempo médio de resposta
- Taxa de escalada correta

## Trade-offs

- Uso de modelo OpenAI ao invés de local
- ChromaDB pela simplicidade
- RAG básico sem reranking
