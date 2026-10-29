# Princípios

Seis princípios definem o Value-First. Se um time abre mão de um deles, está fazendo outra coisa. Isso pode estar tudo bem, mas não é Value-First.

## 1. O valor fica explícito antes de o trabalho começar

Todo trabalho relevante começa dizendo qual problema resolve, para quem, que valor deve gerar e como vamos saber. Prazos e escopo continuam importando. Eles servem ao valor, e não o contrário.

*Baseado em:* o primeiro princípio ágil, "entrega antecipada e contínua de software de valor" ([agilemanifesto.org](https://agilemanifesto.org/principles.html)), e o trabalho de produto orientado a resultados ([Cagan](https://www.svpg.com/product-vs-feature-teams/); Seiden, *Outcomes Over Output*, 2019).

## 2. A spec é um contrato de valor, e ela é viva

Uma spec não é um documento que você entrega e esquece. É um acordo curto sobre problema, valor, critérios de sucesso e restrições. É versionada com o código e muda quando o código ou o feedback nos ensinam algo. Com agentes de código, ela também é entrada executável: o que não está escrito, o agente adivinha.

*Baseado em:* os "documentos vivos" de Specification by Example ([Adzic, 2011](https://gojko.net/books/specification-by-example/)); o desenvolvimento "spec-anchored" ([Böckeler, 2025](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)).

## 3. Valide antes de construir

Antes de se comprometer, reduza a maior incerteza da forma mais barata: uma conversa, um spike técnico ou um protótipo. Um protótipo pode ser gerado com IA e é descartável por padrão. O que ele ensina vai para a spec.

*Baseado em:* o shaping do Shape Up ([Singer, 2019](https://basecamp.com/shapeup)); o teste de premissas da descoberta contínua ([Torres](https://www.producttalk.org/2021/08/product-discovery/)).

## 4. Produto e Tecnologia especificam juntos

A spec tem dois donos. Produto é dono do problema e do valor. O Tech Lead é dono da viabilidade, das restrições e de tornar a spec construível, por pessoas e por agentes. O trabalho de tradução que o Tech Lead já faz ganha um nome e um parceiro.

*Baseado em:* o princípio ágil "pessoas de negócio e desenvolvedores devem trabalhar juntos diariamente" ([agilemanifesto.org](https://agilemanifesto.org/principles.html)); o trio de produto (produto, design, engenharia) da descoberta contínua ([Torres](https://www.producttalk.org/2021/08/product-discovery/)).

## 5. Um plano que muda é informação, não fracasso

O que é fixo e o que é flexível é combinado no início. Quando a realidade muda, a mudança vai para a spec, com o seu motivo, e todos conseguem ver. Sem contratos, sem comitês: um registro curto e visível.

*Baseado em:* "responder a mudanças mais que seguir um plano" ([Manifesto Ágil](https://agilemanifesto.org/)); apetite e escopo variável no Shape Up.

## 6. Pessoas são donas do resultado; a IA acelera

Agentes ajudam a especificar, prototipar e construir. Decisões, revisão de código, segurança e dívida técnica continuam sendo responsabilidades humanas. Medimos resultados (outcomes), não a quantidade de código ou de tickets.

*Baseado em:* a constatação do DORA de que a IA amplifica o sistema em que é inserida, e de que a estabilidade de entrega piorou com o aumento da adoção de IA, mesmo quando a vazão melhorou ([DORA 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report), [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).

---

**Da v1.** Estes seis substituem os cinco princípios da v1. "Valor sobre Prazo" virou o #1, "Tradução Eficiente" virou o #2 e "Avaliação Técnica Preliminar" virou o #3. "Renegociação Formal" e "Transparência Contínua" se fundiram no #5. O #4 substitui o papel de "Analista de Valor" da v1 por uma dupla (veja [papéis](./roles-and-artifacts.md)). O #6 é novo. O texto da v1 está em [docs/archive/v1](../archive/v1/pt/principles.md).
