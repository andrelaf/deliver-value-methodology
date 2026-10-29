# Cenários ilustrativos

> **Estes são cenários fictícios**, escritos para mostrar como as práticas se encaixam. Não são estudos de caso e não têm resultados medidos. Se você já usou o Value-First em um time real, [compartilhe sua experiência](../../CONTRIBUTING.md). Vamos publicá-la com sua permissão e com a fonte.

---

## 1. Um prazo regulatório com escopo incerto

**Situação.** Uma loja online precisa atender a uma nova regra tributária até uma data legal fixa. O primeiro ticket de Produto diz "adaptar o checkout à nova regra".

**Com Value-First.**
- O Par de Valor escreve uma Value Spec. **Fixo:** a data legal e a conformidade. **Flexível:** todo o resto, incluindo o acabamento da interface e os meios de pagamento menos usados.
- O Tech Lead acrescenta as restrições que o ticket deixou de fora: qual serviço tributário usar, como arredondar os valores e como manter a trilha de auditoria.
- Um spike de dois dias mostra que um dos provedores de pagamento não consegue suportar a regra a tempo. Isso entra na spec como risco, com um plano alternativo.
- Quando a data do provedor atrasa, o registro de mudanças documenta o acionamento do plano alternativo. Os stakeholders ficam sabendo no mesmo dia.

**O que a prática tornou visível:** a diferença entre o que não pode mudar e o que pode. Sem isso, tudo parece igualmente urgente.

## 2. Agentes de código em uma funcionalidade com intenção vaga

**Situação.** Um time que usa agentes de código recebe uma história: "permitir que os clientes exportem seus dados". Um agente produz uma exportação completa em CSV em uma tarde. Na revisão, o time descobre que a necessidade real era um relatório mensal para um auditor, em um formato específico.

**Com Value-First.**
- A checagem de prontidão falha em "Que valor esperamos?" e "Como vamos medir?".
- Produto conversa com dois clientes e descobre o requisito do auditor. A Value Spec agora informa o formato e quem recebe o relatório. Um item em "fora do escopo" diz: "exportação de uso geral".
- O próximo plano do agente associa cada tarefa a um critério de sucesso e para no limite do que está fora do escopo.

**O que a prática tornou visível:** o agente não errou. Ele fez exatamente o que a história dizia. A lacuna estava na spec, então a correção também estava na spec.

## 3. Um produto interno com muitos stakeholders

**Situação.** Três departamentos querem coisas diferentes de uma ferramenta interna de aprovações. Cada um vê o próprio pedido como prioridade.

**Com Value-First.**
- Uma sessão opcional de Mapa de Valor coloca um resultado compartilhado no topo e gera quatro Value Specs candidatas, cada uma com a sua aposta mais arriscada.
- Cada spec declara o valor esperado com uma métrica fornecida pelo próprio departamento, como o tempo de aprovação ou os pedidos de retrabalho.
- Uma tabela simples ordena as quatro por valor esperado e esforço. Duas são construídas primeiro.
- As verificações de valor após o lançamento mostram que uma das entregas não mexeu na sua métrica. O time aposenta a spec de continuação em vez de estendê-la.

**O que a prática tornou visível:** uma forma compartilhada de comparar pedidos, e permissão para parar de investir onde o valor não apareceu.

---

**Da v1.** A v1 apresentava dois estudos de caso "reais" com percentuais e valores precisos, mas sem organizações, datas ou fontes, e as versões em PT e EN traziam números diferentes. Eles foram removidos pela regra "toda afirmação factual precisa de fonte" ([Decisão D6](../../DECISIONS.md)). O texto original está em [docs/archive/v1](../archive/v1/pt/case-studies.md).
