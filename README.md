## Arquitetura Final

O sistema BluaDiagnostics foi desenvolvido utilizando arquitetura multi-agente baseada em LangGraph, com foco em triagem clínica segura, modularidade e privacidade de dados.

### Componentes principais

- LangGraph para orquestração multi-agente
- Ollama para inferência local de LLM
- ChromaDB como vector store
- Sentence Transformers para embeddings
- Streamlit para interface visual
- Guardrails clínicos para segurança

### Fluxo do sistema

Supervisor → Triagem → Prescrição  
Supervisor → Escalada Humana (casos críticos)

### Agentes implementados

#### 1. TriageAgent
Responsável por:
- interpretar sintomas
- consultar RAG
- detectar contexto clínico

#### 2. PrescriptionAgent
Responsável por:
- gerar orientações clínicas seguras
- recomendar continuidade de tratamento
- sugerir acompanhamento médico

#### 3. CardiologyAgent
Responsável por:
- analisar sintomas cardiovasculares
- avaliar hipertensão
- identificar risco cardíaco

#### 4. EscalationAgent
Responsável por:
- escalada automática de red flags
- interrupção segura do fluxo
- encaminhamento humano

### RAG Pipeline

O pipeline RAG utiliza:

- chunking com RecursiveCharacterTextSplitter
- embeddings locais via sentence-transformers
- ChromaDB como banco vetorial
- retriever integrado aos agentes

### Segurança

O sistema possui:
- detecção de red flags clínicas
- bloqueio de jailbreaks
- validação de escopo médico
- moderação básica de conteúdo

### Privacidade e LGPD

A utilização do Ollama permite execução local do modelo, reduzindo exposição de dados clínicos sensíveis e alinhando o sistema às boas práticas de privacidade e LGPD.


