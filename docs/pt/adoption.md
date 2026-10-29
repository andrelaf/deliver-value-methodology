# Adotando o Value-First

Como começar, como saber se vocês estão praticando e como evoluir.

## Vocês são Value-First se…

Um time pratica Value-First quando dá para **ver** estas coisas. São sinais no trabalho, não declarações de intenção:

- [ ] Todo item relevante em andamento (veja [quando não usar](#quando-não-usar)) aponta para uma Value Spec com pelo menos **um critério de sucesso mensurável**.
- [ ] Toda Value Spec tem **dois donos nomeados**: Produto e Tech Lead.
- [ ] As specs são **versionadas no repositório** e as instruções dos seus agentes (AGENTS.md, CLAUDE.md, rules) **apontam para elas**.
- [ ] Itens de alta incerteza têm um **protótipo ou spike registrado antes** do compromisso.
- [ ] Mudanças de escopo ou de data aparecem como **uma mudança na spec, com um motivo**, e não como um "atraso" descoberto numa reunião de status.
- [ ] **As verificações de valor acontecem** e são registradas. O time consegue citar entregas que **não** geraram o valor esperado.
- [ ] **Todo código gerado por IA é revisado por uma pessoa**, e a estabilidade é acompanhada junto com a velocidade (por exemplo, a taxa de falha de mudanças do DORA, [dora.dev](https://dora.dev/guides/dora-metrics-four-keys/)).

Se vocês marcarem os sete, estão praticando Value-First, seja qual for o seu quadro ou a sua cadência.

### Sinais de alerta

- Uma spec com mais de duas páginas que ninguém atualiza.
- "Valor" escrito como "melhorar a experiência", sem nenhuma métrica.
- O Tech Lead escrevendo a spec sozinho, de novo.
- A Value Spec virou mais um formulário de aprovação.
- Agentes produzindo código a partir do título de um ticket porque "a spec está na cabeça de alguém".

---

## Modelo de maturidade

Três níveis. Situem-se em cada linha separadamente: a maioria dos times está em níveis diferentes em linhas diferentes. O objetivo não é chegar ao nível 3 em tudo. É saber onde está o próximo passo.

| Dimensão | 1. Começando | 2. Praticando | 3. Incorporado |
|---|---|---|---|
| **Valor** | Os itens descrevem funcionalidades. O valor fica implícito. | A maioria dos itens declara o valor esperado e uma métrica. | Todo item relevante tem linha de base, meta e data de verificação. As prioridades mudam com base nas verificações de valor. |
| **Spec** | Tickets e conversas. O contexto vive na cabeça das pessoas. | Existem Value Specs para os itens maiores, escritas pela dupla. | As Value Specs são a entrada para pessoas e agentes. São versionadas, citadas nos PRs e mantidas atualizadas. |
| **Validação** | Construir primeiro, descobrir depois. | Spikes ou protótipos para os itens mais arriscados. | Protótipos respondem a uma pergunta de valor antes de todo compromisso de alta incerteza, e as decisões vão para a spec. |
| **Dupla** | Produto escreve e o TL traduz sozinho. | Produto e TL escrevem specs juntos para os itens grandes. | A dupla é o padrão. O time questiona as specs antes de construir. |
| **Mudança** | As mudanças aparecem como atrasos. | As mudanças são discutidas, mas não registradas. | As mudanças vão para a spec com um motivo e ficam visíveis para os stakeholders. |
| **Fechar o ciclo** | Ninguém olha para trás depois do lançamento. | Revisões ocasionais dos resultados. | As verificações de valor são agendadas e registradas, e alimentam o backlog. |
| **IA** | Uso pontual. Sem contexto compartilhado. | Existe um arquivo de contexto para agentes. A revisão de código cobre o que a IA produz. | Os agentes leem a Value Spec, perguntam sobre as questões em aberto e rastreiam o trabalho até os IDs dos critérios. A estabilidade é acompanhada. |

### Maturidade da spec em detalhe

As specs merecem uma escala própria, porque agora são a entrada a partir da qual os agentes agem:

| Nível | Como a spec é | O que um agente consegue fazer com ela |
|---|---|---|
| **0. Implícita** | O título de um ticket. O resto está na cabeça de alguém. | Adivinhar. |
| **1. Descrita** | Uma história de usuário com alguns critérios de aceite. | Construir algo plausível que pode deixar passar restrições e casos de borda. |
| **2. Recortada por valor** | Uma Value Spec: problema, métrica de valor, critérios testáveis, restrições, o que fica fora do escopo. | Planejar tarefas rastreadas até os critérios e parar no que está fora do escopo. |
| **3. Ancorada** | Nível 2, e além disso versionada ao lado do código, citada nos PRs, atualizada por decisões e verificações de valor. | Trabalhar a partir da intenção atual, sinalizar conflitos com o código e propor mudanças na spec. |

O nível 3 corresponde ao que Birgitta Böckeler chama de desenvolvimento *spec-anchored* ([martinfowler.com, 2025](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)). O Value-First não mira no *spec-as-source*, em que as pessoas editam apenas specs e nunca o código.

### Autoavaliação rápida

Deem uma nota de 1 a 3 a cada dimensão com o time, em 15 minutos. Não tirem a média. Escolham a linha **mais baixa** e melhorem essa primeiro. Uma conversa compartilhada sobre as notas vale mais do que os números.

---

## Comece em uma semana

1. **Escolha um item próximo** com valor de negócio real e alguma incerteza.
2. **Escrevam a Value Spec em dupla** com o [template](../../templates/pt/value-spec.md). Mantenham em uma página.
3. **Façam a checagem de prontidão.** Perguntas sem resposta vão para "Perguntas em aberto".
4. **Validem a premissa mais arriscada** com o protótipo ou spike mais barato que a responda.
5. **Adicionem o [snippet para agentes](../../templates/pt/agents-snippet.md)** ao seu AGENTS.md ou CLAUDE.md, se vocês usam agentes de código.
6. **Construam**, citando o ID da spec e os IDs dos critérios nos PRs.
7. **Agendem a verificação de valor** na data da spec. Depois, façam uma retro de 15 minutos: o que faltou na spec?

Depois de alguns itens, decidam juntos se a checagem de prontidão vira uma política do time.

## Quando não usar

- **Mudanças muito pequenas ou óbvias.** Correções de bugs, erros de digitação e manutenção de rotina não precisam de Value Spec.
- **Exploração pura ou spikes de pesquisa.** O resultado deles é aprendizado, então não precisam de métricas de sucesso de antemão. Registrem o que aprenderam na spec que eles alimentam.
- **Quando ninguém consegue medir valor de jeito nenhum.** Comecem combinando um sinal observável. Até lá, o Value-First vai parecer um formulário para preencher.
