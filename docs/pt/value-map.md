# Mapa de Valor

O Mapa de Valor é a forma do Value-First desenhar uma iniciativa em uma página. Ele pega emprestada a ideia que tornou o [modelo C4](https://c4model.com/) popular em arquitetura de software: poucos níveis de zoom, uma notação mínima e desenhos que qualquer pessoa faz num quadro branco, sem ferramenta especial (Simon Brown, c4model.com).

Use quando uma iniciativa for grande demais para uma única Value Spec. Para um item só, vá direto à [Value Spec](../../templates/pt/value-spec.md).

## Três níveis de zoom

| Nível | Mostra | Responde | Quem mais lê |
|---|---|---|---|
| **1. Resultado** | A iniciativa: problema, para quem, uma métrica, o que fica de fora | Por que estamos fazendo isso, e como saberemos? | Todos, inclusive a liderança |
| **2. Fatias** | As Value Specs que movem o resultado, em ordem | O que entregamos primeiro, e em que estamos apostando? | Par de Valor, time, stakeholders |
| **3. Critérios** | Os critérios de sucesso (SC-n) de uma fatia e o que verifica cada um | Como sabemos que esta fatia funciona? | Time e agentes de código |

Existe um quarto nível, o **código**, que não se desenha. Testes e pull requests citam os IDs dos SC, e ferramentas e agentes o produzem. Como o nível de código no C4, ele é opcional no papel.

## Notação: quatro regras

1. **Toda caixa tem tipo, nome e uma frase.**
2. **Toda caixa de Resultado e de Fatia tem uma métrica ou um sinal.** Se não dá para nomear, ainda não está pronta.
3. **Toda seta tem um verbo**, como "contribui para" ou "é verificado por".
4. **Um desenho por nível.** Aproxime só onde precisar.

Tipos de caixa:

- **Resultado:** problema · para quem · métrica (linha de base → meta, até quando) · fora do escopo.
- **Fatia (VS-xxx):** o que entrega · como move a métrica · aposta mais arriscada, de valor ou técnica · status.
- **Critério (SC-n):** o enunciado em EARS ou Dado/Quando/Então · o que o verifica (teste, dashboard, revisão).

## Exemplo

*Fictício e ilustrativo. Amplia o [exemplo da VS-014](../../templates/pt/value-spec-example.md).*

- **Nível 1, Resultado:** *Clientes obtêm as próprias faturas.* Contatos financeiros pedem faturas ao suporte. Métrica: tickets de fatura de ~120 para ≤ 40 por semana, 6 semanas após o lançamento. Fora do escopo: pagamento, edição de faturas.
- **Nível 2, Fatias:**
  - **VS-014** Baixar faturas no portal. Aposta: clientes usariam o portal em vez de mandar e-mail ao suporte (validada, 5 de 6). *Em construção.*
  - **VS-015** Filtrar faturas por data. Aposta: auditorias precisam de intervalos de datas (2 de 6 pediram). *Próxima.*
  - **VS-016** Fatura mensal por e-mail. Aposta: receber é melhor que procurar (não validada). *Talvez.*
- **Nível 3, Critérios da VS-014:** SC-1 listar 24 meses → teste ponta a ponta · SC-2 PDF sem alterações → teste de integração · SC-3 403 sem `billing_admin` → teste de segurança · SC-4 p95 < 1 s → teste de carga.

A página do site desenha este exemplo. Também há um [mapa em branco para imprimir](https://andrelaf.github.io/deliver-value-methodology/pt/map.html).

## Como conduzir (cerca de 60 minutos)

1. **Nível 1 juntos (15 min).** Produto e Tech Lead, com um ou dois stakeholders. Se não houver acordo sobre uma métrica, pare: provavelmente são duas iniciativas.
2. **Nível 2 (30 min).** Liste as fatias. Cada uma deve conseguir mover a métrica sozinha. Escreva a aposta mais arriscada de cada uma e ordene pelo que vocês vão aprender primeiro, não pelo tamanho.
3. **Cada fatia vira uma Value Spec.** O nível 3 é escrito na spec, não no workshop.
4. **Mantenha vivo.** Depois de cada verificação de valor, marque a fatia como entregue, não entregue ou aposentada, e refaça a ordem.

## Guardando no repositório

Uma foto do quadro branco resolve. Se quiser que pessoas e agentes leiam, guarde em Markdown junto das specs, por exemplo em `specs/README.md`. Use o [template de Mapa de Valor](../../templates/pt/value-map.md).

---

**Da v1.** O Mapa de Valor substitui o Canvas de Alinhamento Valor-Tecnologia. A maior parte dos 12 blocos do canvas agora vive na Value Spec, então o mapa guarda só o que a spec não tem: o resultado acima das specs e a ordem entre elas. O canvas original está em [docs/archive/v1/pt/canvas](../archive/v1/pt/canvas/value-technology-alignment-canvas.svg).
