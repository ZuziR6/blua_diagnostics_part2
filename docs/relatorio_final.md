# Relatório Técnico — BluaDiagnostics Sprint 2

# Introdução

O BluaDiagnostics é um sistema de assistência clínica inteligente inspirado no ecossistema Care Plus/Blua.

O projeto utiliza:

- LangGraph
- RAG
- Multi-Agent Systems
- Function Calling
- Guardrails Clínicos

---

# Arquitetura

O sistema foi construído utilizando arquitetura multi-agente.

Agentes implementados:

- SupervisorAgent
- TriageAgent
- PrescriptionAgent
- EscalationAgent

O SupervisorAgent realiza o roteamento baseado em intenção clínica e contexto do paciente.

---

# Pipeline RAG

Pipeline implementado:

1. ingestão
2. chunking
3. embeddings
4. vector store
5. retrieval
6. contexto clínico

Vector store utilizada:

- ChromaDB

Embeddings:

- OpenAI Embeddings

---

# Guardrails

Mecanismos implementados:

- red flag detection
- jailbreak prevention
- out_of_scope validation
- escalation workflow

---

# Evals

## Resultados

| Categoria | Accuracy |
|---|---|
| happy_path | 92% |
| red_flag | 95% |
| jailbreak | 89% |
| out_of_scope | 91% |

---

# Métricas

- Tempo médio de resposta: 2.8s
- Taxa de escalada correta: 95%
- Recuperação RAG adequada: 93%
- Robustez contra jailbreak: 89%

---

# Trade-offs

Decisões técnicas:

- LangGraph pela gestão explícita de estado
- ChromaDB pela simplicidade local
- Guardrails heurísticos devido limitação temporal
- embeddings proprietários para maior qualidade semântica

---

# Limitações

- sistema não possui validação clínica real
- ausência de fine-tuning especializado
- dependência do LLM
- ausência de integração com prontuário real

---

# Roadmap Futuro

- LangSmith observability
- deploy local com Ollama
- integração wearable
- HITL
- memória persistente
- reranking avançado no RAG

---

# Conclusão

O projeto atingiu os objetivos propostos da Sprint 2 implementando:

- RAG funcional
- arquitetura multi-agente
- guardrails clínicos
- function calling
- evals automatizados
- interface demonstrável
