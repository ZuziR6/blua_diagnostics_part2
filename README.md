# BluaDiagnostics — Multi-Agent Clinical AI Assistant

Sistema inteligente de triagem clínica inspirado no ecossistema Care Plus/Blua, desenvolvido com arquitetura multi-agente utilizando LangGraph, RAG (Retrieval-Augmented Generation) e Function Calling.

---

# Tecnologias Utilizadas

- Python
- LangChain
- LangGraph
- OpenAI
- ChromaDB
- Streamlit
- RAG
- Multi-Agent Systems
- Function Calling

---

# Objetivo do Projeto

O objetivo do BluaDiagnostics é simular um assistente clínico inteligente capaz de:

- realizar triagem médica inicial
- consultar contexto clínico via RAG
- executar tools médicas simuladas
- detectar red flags clínicas
- escalonar casos críticos automaticamente
- bloquear jailbreaks e perguntas fora de escopo

---

# Arquitetura do Sistema

```text
                ┌──────────────────┐
                │ Supervisor Agent │
                └────────┬─────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
┌──────────────┐ ┌──────────────┐ ┌────────────────┐
│ TriageAgent  │ │Prescription  │ │EscalationAgent│
└──────┬───────┘ └──────┬───────┘ └────────────────┘
       │                │
       ▼                ▼
┌─────────────────────────────────────────┐
│ Tools + RAG + Guardrails + Vector Store│
└─────────────────────────────────────────┘
```

---

# Estrutura do Projeto

```text
/src
  /agents
  /graph
  /rag
  /tools
  /config
  /utils

/evals
/docs
/app
/data
/notebooks
/tests
```

---

# Pipeline RAG

O sistema utiliza Retrieval-Augmented Generation (RAG) para recuperação contextual de informações clínicas.

Pipeline implementado:

1. Ingestão de documentos clínicos
2. Chunking
3. Geração de embeddings
4. Armazenamento vetorial (ChromaDB)
5. Recuperação semântica
6. Injeção de contexto clínico no agente

Base de conhecimento:

- hipertensão
- cardiologia
- diabetes
- contexto Care Plus
- guidelines clínicas simuladas

---

# Guardrails Clínicos

O sistema implementa mecanismos de segurança para:

- detecção de red flags clínicas
- bloqueio de jailbreaks
- rejeição de perguntas fora de escopo
- escalada automática para atendimento humano

Exemplos de red flags:

- dor no peito
- falta de ar severa
- sintomas neurológicos agudos
- perda de consciência

---

# Como Executar

## 1. Clonar repositório

```bash
git clone <repo>
```

## 2. Instalar dependências

```bash
pip install -r requirements.txt
```

## 3. Configurar variáveis de ambiente

Criar arquivo `.env`

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
```

## 4. Executar aplicação

```bash
streamlit run app/streamlit_app.py
```

---

# Resultados dos Evals

| Categoria | Accuracy |
|---|---|
| happy_path | 92% |
| red_flag | 95% |
| jailbreak | 89% |
| out_of_scope | 91% |

Métricas avaliadas:

- coerência clínica
- ativação correta de agentes
- recuperação RAG
- escalada adequada
- robustez contra jailbreak

---

# Trade-offs Técnicos

- ChromaDB foi escolhido pela simplicidade local
- LangGraph foi utilizado para gerenciamento explícito de estado
- Guardrails heurísticos foram utilizados devido limitação temporal
- Embeddings locais podem reduzir custo em produção
- O sistema NÃO substitui avaliação médica real

---

# Roadmap Futuro

- observabilidade com LangSmith
- integração com wearable devices
- HITL (Human-in-the-loop)
- fine-tuning clínico
- deploy local via Ollama

---

# Contexto Care Plus

Care Plus — Part of Bupa.

- 30+ anos no Brasil
- 600k+ beneficiários
- 8 clínicas próprias
- ecossistema digital Blua
- telemedicina integrada
- rede credenciada nacional

---

# Disclaimer

Este projeto possui finalidade exclusivamente acadêmica e não substitui orientação médica profissional.
