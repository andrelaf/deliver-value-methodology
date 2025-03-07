# Práticas Recomendadas para o (DV)

Este documento detalha as práticas recomendadas para implementação efetiva do Deliver-Value Framework (DV). Estas práticas foram compiladas a partir de experiências reais e são adaptáveis a diferentes contextos organizacionais.

## Sumário

- [Práticas Gerais](#práticas-gerais)
- [Práticas para Discovery](#práticas-para-discovery)
- [Práticas para Planejamento](#práticas-para-planejamento)
- [Práticas para Execução](#práticas-para-execução)
- [Práticas para Validação](#práticas-para-validação)
- [Práticas para Resolução de Conflitos](#práticas-para-resolução-de-conflitos)
- [Práticas para Escalar o Framework](#práticas-para-escalar-o-framework)

## Práticas Gerais

### 1. Estabeleça um Vocabulário Comum

**O que**: Crie e mantenha um glossário compartilhado entre as áreas de negócio e tecnologia.

**Como implementar**:
- Realize workshops para alinhar terminologias entre áreas
- Mantenha um documento vivo com definições claras dos termos específicos do domínio
- Revise periodicamente para garantir que novas terminologias sejam incluídas

**Benefícios**:
- Reduz mal-entendidos causados por interpretações diferentes dos mesmos termos
- Acelera reuniões e discussões ao eliminar a necessidade de explicações repetitivas
- Facilita a integração de novos membros à equipe

### 2. Cultura de Transparência Técnica

**O que**: Promova uma cultura onde limitações técnicas possam ser discutidas abertamente, sem julgamentos.

**Como implementar**:
- Realize "Tech Shares" regulares onde desafios técnicos são apresentados para a área de negócio
- Incentive a equipe técnica a explicar "por quê" algo é complexo, não apenas afirmar que é
- Crie um ambiente seguro onde ninguém é penalizado por trazer problemas à tona

**Benefícios**:
- Antecipa riscos antes que se tornem problemas
- Cria empatia entre áreas com diferentes perspectivas
- Permite ajustes de expectativas mais realistas

### 3. Documentação Mínima Viável

**O que**: Defina e implemente um conjunto mínimo de documentação que equilibre agilidade e rastreabilidade.

**Como implementar**:
- Para cada tipo de projeto, identifique quais documentos agregam valor real
- Automatize a geração de documentação técnica sempre que possível
- Foque na documentação de decisões ("decision records") mais que em especificações detalhadas

**Benefícios**:
- Reduz sobrecarga administrativa sem perder informações essenciais
- Mantém a rastreabilidade de decisões importantes
- Permite que novos membros compreendam o histórico do projeto

### 4. Modelos de Diagramas Padronizados

**O que**: Utilize notações padronizadas de diagramas para facilitar a comunicação entre equipes e documentar aspectos do sistema.

**Como implementar**:
- **C4 Model**: Para documentação de arquitetura em diferentes níveis de abstração (Contexto, Contêineres, Componentes e Código)
- **BPMN (Business Process Model and Notation)**: Para representação de processos de negócio
- **UML**: Para documentação detalhada de componentes e interações quando necessário
- **Entity-Relationship Diagrams (ERD)**: Para modelagem de dados
- **Diagramas de Sequência**: Para fluxos de interação complexos
- **Mermaid ou PlantUML**: Para diagramas mantidos como código junto à documentação

**Benefícios**:
- Estabelece um padrão visual comum para toda a organização
- Facilita a compreensão rápida de estruturas complexas
- Permite diferentes níveis de abstração para diferentes públicos
- Integra-se com práticas de documentação como código

**Recomendações de uso**:
- Use C4 Model para visões arquiteturais com stakeholders técnicos
- Use BPMN para discussões de processos com a área de negócio
- Mantenha diagramas simples e focados em um aspecto específico
- Considere ferramentas que permitam versionar diagramas junto com código

## Práticas para Discovery

### 1. Workshop de Valor do Produto

**O que**: Sessão colaborativa para identificar e quantificar o valor central que o produto/projeto deve entregar.

**Como implementar**:
- Reúna representantes de negócio, tecnologia e UX
- Utilize técnicas como Impact Mapping ou Value Proposition Canvas
- Documente claramente o valor em termos de outcomes (resultados), não outputs (entregas)

**Benefícios**:
- Alinha todas as áreas em torno do verdadeiro propósito do projeto
- Fornece um norte claro para decisões futuras
- Permite priorização baseada em valor real

### 2. Domain Storytelling

**O que**: Técnica colaborativa onde especialistas de domínio narram histórias sobre seus processos de negócio, enquanto um facilitador os documenta visualmente.

**Como implementar**:
- Convide especialistas de domínio que conhecem profundamente o processo
- Utilize uma notação visual simples (atores, objetos de trabalho, atividades)
- Capture histórias reais, não processos idealizados
- Documente o vocabulário específico do domínio durante as sessões

**Benefícios**:
- Cria uma linguagem compartilhada entre negócio e tecnologia
- Revela detalhes sutis dos processos que não aparecem em documentações formais
- Identifica pontos de dor e oportunidades de melhoria no fluxo atual
- Facilita a criação de um modelo de domínio mais preciso

### 3. Event Storming

**O que**: Workshop colaborativo para modelar processos de negócio complexos usando eventos de domínio em uma linha de tempo.

**Como implementar**:
- Utilize um espaço grande (parede ou quadro) com post-its coloridos
- Comece pelos eventos de domínio (geralmente em laranja)
- Adicione comandos, atores, agregados e políticas em iterações sucessivas
- Identifique bounded contexts e possíveis subdivisões do domínio

**Benefícios**:
- Cria um entendimento compartilhado do fluxo de eventos do negócio
- Revela complexidades e gargalos no processo atual
- Ajuda a identificar fronteiras naturais para divisão do sistema
- Facilita a transição para uma arquitetura orientada a eventos ou microserviços

### 4. Avaliação Técnica Exploratória

**O que**: Período dedicado à exploração de viabilidade técnica antes do comprometimento formal com estimativas.

**Como implementar**:
- Permita que o Especialista Técnico forme um pequeno grupo para exploração
- Documente claramente premissas e incertezas
- Construa protótipos de conceito para aspectos de maior risco

**Benefícios**:
- Reduz riscos de estimativas irrealistas
- Identifica desafios técnicos antecipadamente
- Permite ajuste de escopo antes do início formal do projeto

### 5. Mapeamento de Dependências

**O que**: Identificação sistemática de todas as dependências internas e externas que podem impactar o projeto.

**Como implementar**:
- Crie um diagrama visual de dependências
- Classifique dependências por criticidade e controle (dentro ou fora do controle da equipe)
- Defina estratégias para mitigar riscos em dependências críticas

**Benefícios**:
- Previne surpresas desagradáveis durante a execução
- Permite planejamento de contingências para dependências de alto risco
- Identifica gargalos potenciais antecipadamente

## Práticas para Planejamento

### 1. Criação Colaborativa da Matriz de Valor

**O que**: Desenvolvimento conjunto da Matriz de Valor que relaciona funcionalidades com o valor para o negócio.

**Como implementar**:
- Realize sessões com participação ativa de negócio e tecnologia
- Utilize técnicas de priorização como RICE (Reach, Impact, Confidence, Effort)
- Documente claramente critérios de aceitação focados em valor

**Benefícios**:
- Cria um entendimento compartilhado das prioridades
- Permite decisões objetivas quando tradeoffs forem necessários
- Mantém o foco no que realmente importa para o sucesso do projeto

### 2. Contratos de Flexibilidade

**O que**: Estabelecimento formal de parâmetros fixos e flexíveis para o projeto.

**Como implementar**:
- Identifique claramente o que é não-negociável (ex: requisitos regulatórios)
- Estabeleça formalmente o que pode ser flexibilizado (escopo, prazo, recursos)
- Defina gatilhos e processos para renegociação

**Benefícios**:
- Cria expectativas claras sobre o que pode ser ajustado
- Permite adaptação sem conflitos desnecessários
- Formaliza um processo para lidar com mudanças inevitáveis

### 3. Planejamento em Ondas

**O que**: Abordagem de planejamento que detalha o curto prazo e mantém o longo prazo mais flexível.

**Como implementar**:
- Planeje em detalhe apenas as próximas 2-3 sprints
- Mantenha planos de médio prazo com granularidade intermediária
- Use roadmaps temáticos para longo prazo, sem detalhar features específicas

**Benefícios**:
- Equilibra previsibilidade com adaptabilidade
- Reduz replanejamento excessivo
- Permite ajustes baseados em aprendizados sem perder a direção

## Práticas para Execução

### 1. Tech Alignment Sessions

**O que**: Reuniões regulares para alinhar visão técnica e resolver impedimentos técnicos.

**Como implementar**:
- Realize encontros curtos (30-45 min) envolvendo especialistas técnicos
- Foque em decisões arquiteturais e desbloqueio de impedimentos
- Documente decisões importantes e compartilhe com a equipe

**Benefícios**:
- Mantém consistência técnica no projeto
- Resolve rapidamente bloqueios técnicos
- Dissemina conhecimento entre diferentes especialistas

### 2. Checkpoints de Valor

**O que**: Verificações regulares para garantir que o valor planejado está sendo criado.

**Como implementar**:
- Realize checkpoints a cada 2-3 sprints
- Envolva representantes de negócio e tecnologia
- Avalie progresso em termos de valor, não apenas funcionalidades entregues

**Benefícios**:
- Permite correções de curso rápidas
- Mantém o foco no valor real sendo criado
- Identifica quando o valor planejado não está sendo alcançado

### 3. Showcases Orientados a Valor

**O que**: Demonstrações de progresso focadas no valor entregue, não apenas em funcionalidades.

**Como implementar**:
- Estruture demonstrações em torno de jornadas de usuário ou casos de negócio
- Destacue explicitamente o valor gerado por cada incremento
- Convide stakeholders diversos para obter feedback variado

**Benefícios**:
- Mantém stakeholders conectados ao progresso real
- Facilita feedback significativo e contextualizado
- Reforça a cultura de foco no valor

## Práticas para Validação

### 1. Validação Contínua em Ciclos Curtos

**O que**: Verificação frequente com usuários reais ou representantes de negócio sobre o valor sendo entregue.

**Como implementar**:
- Estabeleça ciclos curtos de feedback (1-2 semanas)
- Utilize técnicas como testes de usabilidade, entrevistas ou A/B testing
- Documente insights e implemente melhorias rapidamente

**Benefícios**:
- Evita desenvolvimento prolongado na direção errada
- Mantém o produto alinhado às necessidades reais dos usuários
- Permite iterações rápidas baseadas em feedback concreto

### 2. Métricas de Validação Objetiva

**O que**: Conjunto de métricas específicas para verificar se o valor planejado está sendo realizado.

**Como implementar**:
- Estabeleça KPIs claros ligados aos objetivos de valor
- Implemente instrumentação para coletar dados automaticamente
- Revise métricas regularmente com a equipe e stakeholders

**Benefícios**:
- Fornece evidências objetivas do valor entregue
- Permite decisões baseadas em dados, não opiniões
- Identifica rapidamente quando os objetivos não estão sendo atingidos

### 3. Retrospectivas Centradas em Valor

**O que**: Retrospectivas que focam não apenas em processos, mas no valor entregue e percebido.

**Como implementar**:
- Adicione perguntas específicas sobre valor nas retrospectivas
- Convide ocasionalmente representantes do negócio para participar
- Documente aprendizados relacionados à entrega de valor

**Benefícios**:
- Mantém a equipe focada no propósito maior do projeto
- Identifica oportunidades para melhorar a entrega de valor
- Cria alinhamento contínuo entre execução e objetivos

## Práticas para Resolução de Conflitos

### 1. Escalonamento Baseado em Dados

**O que**: Processo estruturado para resolução de conflitos usando dados objetivos.

**Como implementar**:
- Estabeleça um framework claro para decisões (ex: matriz de impacto/esforço)
- Exija que posições conflitantes sejam apoiadas por dados ou evidências
- Documente premissas por trás de cada posição

**Benefícios**:
- Despersonaliza conflitos, focando em dados e não em opiniões
- Facilita decisões mais objetivas e menos emocionais
- Cria precedentes úteis para situações futuras

### 2. Comitê de Priorização

**O que**: Grupo multidisciplinar responsável por resolver conflitos de priorização.

**Como implementar**:
- Forme um comitê com representantes de diferentes áreas
- Estabeleça critérios claros para priorização
- Realize reuniões regulares ou sob demanda para resolver conflitos

**Benefícios**:
- Fornece um mecanismo formal para resolver impasses
- Equilibra diferentes perspectivas nas decisões
- Aumenta a transparência do processo decisório

### 3. Acordos de Compromisso

**O que**: Documentos formais que registram compromissos quando ajustes são necessários.

**Como implementar**:
- Crie um template simples para registrar acordos
- Documente claramente o que cada parte está comprometendo
- Estabeleça prazos e critérios para revisão

**Benefícios**:
- Evita mal-entendidos sobre o que foi acordado
- Fornece referência clara para acompanhamento
- Cria accountability para todas as partes envolvidas

## Práticas para Escalar o Framework

### 1. Comunidades de Prática

**O que**: Grupos informais que promovem compartilhamento de conhecimento e padronização de práticas.

**Como implementar**:
- Crie comunidades para papéis específicos (ex: Analistas de Valor, Especialistas Técnicos)
- Promova encontros regulares para troca de experiências
- Incentive a documentação de padrões e melhores práticas

**Benefícios**:
- Dissemina conhecimento entre equipes
- Padroniza práticas mantendo espaço para adaptação
- Cria suporte entre pares para desafios comuns

### 2. Framework de Adaptação Contextual

**O que**: Diretrizes claras sobre como adaptar o (DV) para diferentes contextos.

**Como implementar**:
- Crie uma matriz de adaptação baseada em variáveis como tamanho do projeto, criticidade, etc.
- Documente exemplos de adaptações bem-sucedidas
- Permita que equipes customizem com justificativa clara

**Benefícios**:
- Evita aplicação rígida do framework em contextos inadequados
- Fornece orientação para adaptações sem perder princípios essenciais
- Permite evolução orgânica das práticas baseada em aprendizados

### 3. Métricas de Adoção e Maturidade

**O que**: Sistema para avaliar o nível de adoção e maturidade na implementação do (DV).

**Como implementar**:
- Desenvolva um modelo de maturidade com níveis claros
- Crie ferramentas de auto-avaliação para equipes
- Realize revisões periódicas para identificar áreas de melhoria

**Benefícios**:
- Fornece visibilidade sobre a adoção real do framework
- Identifica áreas que precisam de mais suporte ou treinamento
- Permite celebrar avanços na implementação

---

## Adaptando Práticas ao Seu Contexto

É fundamental ressaltar que estas práticas são recomendações, não regras rígidas. Cada organização deve adaptar estas práticas ao seu contexto específico, considerando:

- Cultura organizacional existente
- Maturidade das equipes
- Natureza dos projetos
- Restrições específicas do domínio

O sucesso do (DV) não está na aplicação literal de todas estas práticas, mas na incorporação de seus princípios fundamentais de uma forma que faça sentido para sua realidade.

Recomendamos começar com um subconjunto destas práticas, avaliar os resultados, e gradualmente incorporar mais elementos conforme a equipe ganha experiência com o framework.
