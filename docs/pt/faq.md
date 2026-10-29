# FAQ

### O que é o Value-First Development, em uma frase?
Uma camada leve sobre a forma como você já trabalha. Ela torna o valor de cada trabalho explícito, compartilhado e mensurável antes que alguém o construa, para que pessoas e agentes de código construam a coisa certa. Veja [Por que Value-First](./why.md).

### Ele substitui o Scrum ou o Kanban?
Não. Você mantém sua cadência, seus eventos e seu quadro. As Value Specs melhoram o que entra em uma sprint ou em uma coluna, e a verificação de valor olha para o que sai. Veja a [comparação](./comparison.md).

### É só para times que usam IA?
Não. Todos os princípios funcionam sem agentes. Os agentes deixam a necessidade mais visível, porque executam o que está escrito e não conseguem preencher lacunas como um colega faria.

### Isso não é só escrever mais documentos?
Não deveria ser. Uma Value Spec cabe em cerca de uma página, cobre um item de valor e fica junto ao código. Se passar de duas páginas, divida. O objetivo é descobrir mais cedo o que vale a pena construir e registrar só isso. Veja a crítica sobre o modelo cascata em [Specs na era da IA](./ai-and-specs.md#limites-e-riscos).

### Quem escreve a Value Spec?
O Par de Valor: Produto e o Tech Lead, juntos. O time revisa. Veja os [papéis](./roles-and-artifacts.md).

### Nosso Tech Lead já faz isso. O que muda?
O trabalho passa a ser visível, planejado e compartilhado. Produto divide a responsabilidade, então ele deixa de depender da memória e das noites de uma única pessoa.

### O que aconteceu com o Analista de Valor da v1?
Deixou de ser um cargo, porque um terceiro papel entre Produto e Tecnologia acrescenta uma passagem de bastão, e toda passagem de bastão perde contexto. A análise de valor continua sendo uma habilidade que qualquer pessoa pode trazer. Veja os [papéis](./roles-and-artifacts.md#o-que-aconteceu-com-o-analista-de-valor).

### Todo ticket precisa de uma Value Spec?
Não. Só itens com incerteza real sobre valor ou viabilidade, ou itens construídos principalmente por agentes. Correções de bugs e trabalho de rotina não precisam. Veja [quando não usar](./adoption.md#quando-não-usar).

### E se não conseguirmos medir o valor?
Comece com um sinal observável com o qual todos concordem, mesmo que aproximado: tickets de suporte, uma etapa de um funil, o tempo gasto em uma tarefa. Se nada puder ser observado, transforme isso na primeira pergunta em aberto.

### Como usar com Spec Kit, Kiro ou ferramentas parecidas?
Uma Value Spec pode ser a entrada da etapa `specify` do Spec Kit ou da fase de requisitos do Kiro. Suas restrições podem alimentar uma constitution do Spec Kit, arquivos de steering ou o AGENTS.md. O Value-First decide *o quê e por quê*. As ferramentas cuidam de *spec → código*.

### Funciona em ambientes regulados?
Sim. Os requisitos de compliance entram na seção "Restrições" e ficam fixos. O registro de decisões e o registro de mudanças servem como trilha de auditoria.

### Existe evidência de que funciona?
Ainda não na forma de dados de resultado sobre o próprio Value-First. O framework se apoia em pesquisas publicadas (DORA, literatura de Agile e de produto, listadas nas [fontes](./sources.md)) e na prática. Se você adotar, gostaríamos de saber o que aconteceu: [CONTRIBUTING](../../CONTRIBUTING.md).

### Posso usar e adaptar?
Sim. A licença é MIT. Use o que ajudar e conte para nós o que você mudou.
