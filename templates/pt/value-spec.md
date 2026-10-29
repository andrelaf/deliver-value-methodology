---
# Value Spec — Value-First Development
# Legível por pessoas e por agentes de código. Mantenha curta: se não couber em algumas telas, divida.
id: VS-000                     # ID estável; tarefas, commits e PRs fazem referência a ele
title: "<título curto, orientado a resultado>"
status: draft                  # draft | validating | ready | in-build | delivered | measured | retired
version: 0.1.0                 # minor sobe em mudança de escopo/critérios, patch em ajuste de redação
owners:
  product: "<nome>"            # dono do problema, do valor e da métrica
  tech: "<nome>"               # Tech Lead: dono das restrições, da testabilidade dos critérios e do contexto dos agentes
created: AAAA-MM-DD
updated: AAAA-MM-DD
links:
  prototype: ""                # URL do protótipo de validação, se houver
  issue: ""                    # épico/issue no tracker
  design: ""                   # design/plano gerado depois (ex.: plan.md do Spec Kit, design.md do Kiro)
  agent_context: "AGENTS.md"   # ou CLAUDE.md / .cursor/rules / .kiro/steering
  dashboard: ""                # onde a métrica de valor é observada
---

# <título>

<!-- Como usar: produto e Tech Lead preenchem juntos, em uma sessão de trabalho.
     Escrevam o que se sabe; coloquem o que não se sabe em Perguntas em aberto, em vez de adivinhar.
     Esta spec é o contrato de valor. Planos, tarefas e código são produzidos depois, a partir dela. -->

## 1. Problema
<!-- 2 a 4 frases. O que dói hoje, para quem, e a evidência (dados, tickets, entrevistas). Nada de solução aqui. -->

## 2. Quem e contexto
<!-- Usuários/personas principais, a situação em que estão e os sistemas ou processos envolvidos. -->
- **Usuários principais:**
- **Contexto / gatilho:**
- **Sistemas envolvidos:**

## 3. Valor esperado
<!-- Um resultado. Se você tem três resultados, provavelmente tem três specs. -->
| Resultado (outcome) | Métrica | Linha de base | Meta | Até quando | Método de medição |
|---|---|---|---|---|---|
| <mudança de comportamento ou de negócio que queremos> | <nome da métrica> | <valor atual + fonte> | <valor-alvo> | <data / N semanas após o lançamento> | <consulta, evento, pesquisa; quem verifica> |

## 4. Critérios de sucesso
<!-- Mensuráveis e testáveis. Cada um recebe um ID que tarefas, testes e PRs citam.
     Critérios de comportamento: EARS ("Quando <gatilho>, o <sistema> deve <resposta>";
       também Enquanto <estado> / Se <condição indesejada>, então ... / Onde <funcionalidade>)
     ou Given / When / Then. Critérios não comportamentais: um limite que possa ser verificado. -->
- **SC-1** (EARS): Quando <gatilho>, o <sistema> deve <resposta>.
- **SC-2** (Given/When/Then): Dado <contexto>, quando <ação>, então <resultado observável>.
- **SC-3** (limite): <ex.: latência p95 de X < 300 ms sob N rps>.

## 5. Escopo, fora do escopo e flexibilidade
- **No escopo:**
- **Fora do escopo (explicitamente não faremos agora):**
<!-- O que está fora do escopo importa mais ainda para agentes: impede que o agente "ajude" acrescentando coisas. -->
- **Fixo (não muda sem os dois donos):** <!-- ex.: o resultado, uma data legal, uma restrição de segurança -->
- **Flexível (pode mudar para proteger o resultado):** <!-- ex.: detalhes de escopo, UI, data de entrega dentro de uma janela -->
- **Revisite esta spec se:** <!-- gatilhos, ex.: um protótipo invalida A-1, uma estimativa dobra, uma dependência atrasa -->

## Checagem de prontidão
<!-- Não comecem a construir (pessoas ou agentes) até que as cinco tenham resposta. -->
- [ ] Que problema estamos resolvendo? (§1)
- [ ] Para quem? (§2)
- [ ] Que valor esperamos? (§3)
- [ ] Como vamos medir? (§3–4)
- [ ] O que é fixo e o que é flexível? (§5)

## 6. Restrições
<!-- O Tech Lead conduz esta seção. Regras duradouras, que valem para várias funcionalidades, vão no AGENTS.md / steering; liste aqui só o que é específico e faça link para o resto. -->
- **Técnicas / arquitetura:**
- **Não funcionais (desempenho, disponibilidade, acessibilidade):**
- **Segurança e privacidade:** <!-- classes de dados, autenticação/autorização, segredos, preocupações OWASP -->
- **Compliance / jurídico:**
- **Dependências:**

## 7. Premissas e riscos
| ID | Premissa ou risco | Impacto se estiver errado | Como validamos | Status |
|---|---|---|---|---|
| A-1 | <acreditamos que...> | <alto/médio/baixo + o que acontece> | <protótipo, consulta de dados, spike, entrevista> | open / validated / invalidated |

## 8. Perguntas em aberto
<!-- Agentes: se o seu trabalho tocar em uma destas, parem e perguntem. -->
- **Q-1:** <pergunta> — responsável: <nome> — necessária até: <data>

## 9. Plano de validação (protótipo → evidência)
<!-- Valide o valor antes de investir na construção. Protótipos são evidência, não entregáveis. -->
- **Premissa mais arriscada:** A-x
- **Protótipo / experimento:** <o quê, construído como (ex.: fluxo clicável gerado por IA), timebox>
- **Quem vê:** <usuários, stakeholders>
- **Evidência para seguir em frente:** <sinal + limite>
- **Evidência para parar ou pivotar:** <sinal>
- **Resultado:** <preenchido após a validação; link>

## 10. Registro de decisões
| Data | Decisão | Por quê | Decidido por | Afeta |
|---|---|---|---|---|
| AAAA-MM-DD | <decisão> | <justificativa / alternativas consideradas> | <nomes> | <IDs de SC/A/escopo> |

## 11. Registro de mudanças
<!-- Spec viva: toda mudança de valor, critérios, escopo ou restrições ganha uma linha. Mudanças de escopo ou de critérios são uma renegociação formal e precisam dos dois donos. -->
| Versão | Data | Mudança | Motivo (feedback, código, dados) | Aprovado por |
|---|---|---|---|---|
| 0.1.0 | AAAA-MM-DD | Rascunho inicial | — | produto + tech |

## 12. Verificação de valor
<!-- Preenchida após a entrega, na data da §3. Compare o resultado com a meta. -->
- **Data da verificação:**
- **Resultado vs. meta:** <métrica: linha de base → real (meta)>
- **Veredito:** valor entregue / em parte / não entregue
- **O que aprendemos e próximo passo:** <atualizar a spec, nova spec, parar>

## 13. Instruções para agentes
<!-- Mantenha este bloco. Ele diz aos agentes de código como usar esta spec. Regras duradouras do repositório ficam no AGENTS.md / CLAUDE.md. -->
> **Para agentes de código de IA que trabalham a partir desta spec:**
> 1. **Esta spec é a fonte da intenção.** Implemente apenas o necessário para atender aos critérios de sucesso (seção 4) dentro do escopo (seção 5). Não invente requisitos, funcionalidades ou "extras". O que está fora do escopo é um limite rígido.
> 2. **Pergunte, não adivinhe.** Se algo for ambíguo, contradisser o código ou tocar em uma Pergunta em aberto (seção 8), pare e pergunte aos donos. Não escolha uma interpretação em silêncio.
> 3. **Respeite as restrições.** A seção 6 e o arquivo de contexto de agentes do repositório (`links.agent_context`) são obrigatórios. Se uma restrição parecer bloquear um critério, relate o conflito. Não o contorne.
> 4. **Rastreie tudo.** Cada tarefa que você planejar deve corresponder a um ou mais IDs de critério (SC-n). Cada teste deve citar o SC que verifica. Trabalho sem critério está fora do escopo.
> 5. **Cite a spec nos PRs.** As descrições de PR incluem `Spec: <id>@<version>`, os IDs de SC cobertos, os SC ainda não cobertos e as premissas que você assumiu.
> 6. **Proponha, não edite, a intenção.** Se a implementação mostrar que a spec está errada ou incompleta, proponha uma mudança (decisão + entrada no registro de mudanças) aos donos. Não altere você mesmo as seções 3 a 6.
> 7. **Segurança em primeiro lugar.** Nunca enfraqueça autenticação, autorização, validação de entrada ou tratamento de segredos para fazer um critério passar. Sinalize o problema.
