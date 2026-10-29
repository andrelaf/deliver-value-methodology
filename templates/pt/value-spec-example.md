---
# Exemplo fictício e ilustrativo. Empresa, nomes e números são inventados.
id: VS-014
title: "Clientes baixam as próprias faturas"
status: ready
version: 1.1.0
owners:
  product: "Marina (Product Manager)"
  tech: "Rafael (Tech Lead)"
created: 2026-09-01
updated: 2026-09-12
links:
  prototype: "<link para o protótipo clicável>"
  issue: "BILL-231"
  design: "specs/014-invoice-download/plan.md"
  agent_context: "AGENTS.md"
  dashboard: "<link para o dashboard de suporte>"
---

# Clientes baixam as próprias faturas

## 1. Problema
Clientes B2B não conseguem obter faturas antigas pelo portal. Eles abrem tickets de suporte, e "me mande a fatura X" é a principal categoria de tickets no nosso helpdesk (relatório interno, ago. 2026). O suporte gasta tempo com uma tarefa que não exige nenhum julgamento, e os clientes ficam esperando.

## 2. Quem e contexto
- **Usuários principais:** contatos financeiros nas contas de clientes (papel `billing_admin`).
- **Contexto / gatilho:** fechamento de mês, auditorias.
- **Sistemas envolvidos:** portal do cliente (web), serviço de faturamento (os PDFs das faturas já estão armazenados).

## 3. Valor esperado
| Resultado (outcome) | Métrica | Linha de base | Meta | Até quando | Método de medição |
|---|---|---|---|---|---|
| Clientes obtêm as faturas por conta própria | Tickets semanais de "pedido de fatura" | ~120/semana (tag do helpdesk, ago. 2026, ilustrativo) | ≤ 40/semana | 6 semanas após o lançamento | Relatório da tag no helpdesk, revisado semanalmente pela Marina |

## 4. Critérios de sucesso
- **SC-1** (EARS): Quando um `billing_admin` abrir *Faturamento › Faturas*, o portal deve listar as faturas daquela conta dos últimos 24 meses, das mais recentes para as mais antigas.
- **SC-2** (EARS): Quando o usuário selecionar *Baixar* em uma fatura, o portal deve entregar o PDF armazenado sem alterações.
- **SC-3** (EARS): Se um usuário sem `billing_admin` solicitar a URL de uma fatura, então o portal deve retornar 403 e registrar a tentativa.
- **SC-4** (limite): A lista de faturas carrega em menos de 1 s no p95 para contas com até 500 faturas.
- **SC-5** (instrumentação): Quando um download terminar, o portal deve registrar um evento `invoice_downloaded` com o ID da conta, exibido no dashboard de suporte ao lado da contagem de tickets.

## 5. Escopo, fora do escopo e flexibilidade
- **No escopo:** listagem + download dos PDFs existentes.
- **Fora do escopo:** edição de faturas, pagamento, exportação em CSV, faturas com mais de 24 meses, filtro por data (VS-015).
- **Fixo:** o resultado (menos tickets de fatura); acesso restrito à conta; nenhum acesso direto ao bucket.
- **Flexível:** o layout da lista; a janela de 24 meses (pode diminuir se o SC-4 estiver em risco); a data de lançamento dentro de setembro.
- **Revisite esta spec se:** os tickets não caírem até a semana 3, ou se a API de faturamento não conseguir atender ao SC-4.

## Checagem de prontidão
- [x] Problema · [x] Para quem · [x] Valor esperado · [x] Como medir · [x] Fixo vs. flexível

## 6. Restrições
- **Técnicas:** ler os PDFs pela API do serviço de faturamento. Nenhum acesso direto ao bucket a partir do portal.
- **Segurança e privacidade:** as URLs assinadas de download expiram em 5 min. As faturas são filtradas por ID da conta no servidor.
- **Compliance:** os eventos de download são retidos conforme a política de auditoria (veja AGENTS.md › Audit).
- **Lançamento e reversão:** atrás de uma feature flag por conta. 10% das contas na semana 1, depois todas. Desligar a flag volta ao fluxo atual (pedir ao suporte).

## 7. Premissas e riscos
| ID | Premissa ou risco | Impacto se estiver errado | Como validamos | Status |
|---|---|---|---|---|
| A-1 | Os contatos financeiros usariam o portal em vez de mandar e-mail para o suporte | Alto: o valor não se realiza | Protótipo mostrado a 6 clientes | validated (5/6) |
| A-2 | A API de faturamento consegue servir listas de 500 itens com rapidez suficiente | Médio: SC-4 em risco | Spike de 1 dia | validated |

## 8. Perguntas em aberto
- *(nenhuma em aberto; a Q-1 sobre filtros de data foi resolvida, veja as decisões)*

## 9. Plano de validação
- **Premissa mais arriscada:** A-1.
- **Protótipo:** fluxo clicável gerado por IA com dados falsos, timebox de 1 dia.
- **Evidência para seguir em frente:** ≥ 4 de 6 clientes dizem que deixariam de mandar e-mail para o suporte.
- **Resultado:** 5/6 sim. Dois pediram filtro por data (adiado, veja o registro de decisões, 2026-09-12).

## 10. Registro de decisões
| Data | Decisão | Por quê | Decidido por | Afeta |
|---|---|---|---|---|
| 2026-09-08 | Usar URLs assinadas, com expiração de 5 min | Evitar expor o bucket; está de acordo com a linha de base de segurança | Rafael + segurança | SC-2, restrições |
| 2026-09-12 | Filtro por data adiado para a VS-015 | Não é necessário para reduzir os tickets; mantém a fatia pequena | Marina + Rafael | Escopo |

## 11. Registro de mudanças
| Versão | Data | Mudança | Motivo | Aprovado por |
|---|---|---|---|---|
| 1.0.0 | 2026-09-08 | Pronta para construção | O protótipo validou a A-1 | Marina, Rafael |
| 1.1.0 | 2026-09-12 | Adicionado o SC-3 (403 + log); filtro por data → fora do escopo | Revisão de segurança; feedback do protótipo | Marina, Rafael |

## 12. Verificação de valor
- *(Agendada para 6 semanas após o lançamento. Ainda não preenchida.)*

## 13. Instruções para agentes
> Siga as instruções padrão para agentes da Value Spec (seção 13 do template). Específico desta funcionalidade: nunca acesse o bucket de armazenamento diretamente. Todo PR cita `Spec: VS-014@1.1.0` e os IDs de SC que cobre.
