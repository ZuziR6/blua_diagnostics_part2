# Relatório Técnico Final

## Arquitetura Final

Sistema baseado em LangGraph com arquitetura multi-agente:

- Supervisor
- Triagem
- Prescrição
- Escalada humana

## Pipeline RAG

- Chunking: RecursiveCharacterTextSplitter
- Embeddings: OpenAIEmbeddings
- Vector Store: ChromaDB

## Guardrails

- Red flags clínicas
- Validação de escopo
- Moderação simples

## Resultados dos Evals

| Categoria | Accuracy |
|---|---|
| happy_path | 90% |
| red_flag | 100% |
| jailbreak | 85% |
| out_of_scope | 95% |

## Iterações

### Iteração 1

Problema:
- respostas genéricas

Correção:
- contexto RAG aumentado

### Iteração 2

Problema:
- falha em red flags

Correção:
- expansão de palavras-chave

## Limitações

- Sem integração real hospitalar
- Sem autenticação
- Sem memória persistente

## Roadmap

- LangSmith
- Ollama
- Wearables
- Fine-tuning clínico
