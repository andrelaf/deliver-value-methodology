
# Exemplos de Aplicação do FDCV

Este documento apresenta casos concretos de aplicação do Framework de Desenvolvimento Centrado em Valor (FDCV) em diferentes contextos. Cada exemplo ilustra como os princípios e práticas do framework podem ser adaptados para resolver desafios específicos.

## Sumário

- [Exemplo 1: Projeto de E-commerce com Prazo Regulatório](#exemplo-1-projeto-de-e-commerce-com-prazo-regulatório)
- [Exemplo 2: Modernização de Sistema Legado](#exemplo-2-modernização-de-sistema-legado)
- [Exemplo 3: Produto Interno com Múltiplos Stakeholders](#exemplo-3-produto-interno-com-múltiplos-stakeholders)
- [Exemplo 4: Startup com Recursos Limitados](#exemplo-4-startup-com-recursos-limitados)
- [Exemplo 5: Projeto com Dependências Externas](#exemplo-5-projeto-com-dependências-externas)

## Exemplo 1: Projeto de E-commerce com Prazo Regulatório

### Contexto
Uma empresa de varejo precisava adaptar seu e-commerce para novas regulamentações de proteção de dados, com prazo fixo definido por lei. O escopo incluía mudanças em todo o processo de coleta, armazenamento e processamento de dados de clientes.

### Desafio
- Prazo não-negociável (requisito legal)
- Escopo extenso e complexo
- Impacto em múltiplos sistemas legados

### Aplicação do FDCV

#### Fase de Discovery
- **Matriz de Valor Regulatório**: Classificação de requisitos em "obrigatórios para conformidade legal" vs. "melhorias desejáveis"
- **Event Storming para Mapeamento de Dados**: Sessões com especialistas jurídicos e técnicos para mapear o fluxo completo de dados dos clientes
- **Análise de Risco Técnico-Legal**: Avaliação conjunta de riscos técnicos e consequências legais

#### Fase de Planejamento
- **Escopo em Camadas**: Definição de camadas de implementação (essencial, importante, desejável)
- **Roadmap com Marcos Regulatórios**: Alinhamento de marcos técnicos com prazos regulatórios
- **Contrato de Flexibilidade**: Acordo formal sobre quais funcionalidades poderiam ser simplificadas em caso de desafios técnicos

#### Fase de Execução
- **Squads por Domínio de Dados**: Equipes dedicadas a áreas específicas do fluxo de dados
- **Checkpoints Semanais de Conformidade**: Validação regular com equipe jurídica
- **Dashboard de Valor Regulatório**: Visualização clara do progresso em termos de conformidade legal

### Resultados
- Conformidade legal alcançada dentro do prazo
- Redução de 30% no escopo de "melhorias desejáveis" após avaliação técnica
- Maior clareza para stakeholders sobre tradeoffs realizados
- Documentação abrangente de conformidade como subproduto do processo

### Lições Aprendidas
- A separação clara entre requisitos legais e melhorias desejáveis permitiu foco no que realmente importava
- A inclusão da equipe jurídica nos checkpoints de valor criou confiança e permitiu ajustes de interpretação regulatória
- O mapeamento detalhado inicial economizou tempo significativo durante a implementação

---

## Exemplo 2: Modernização de Sistema Legado

### Contexto
Uma instituição financeira precisava modernizar um sistema core com 15+ anos, escrito em tecnologias obsoletas e sem documentação adequada. O sistema processava mais de 70% das operações financeiras da empresa.

### Desafio
- Código legado altamente acoplado
- Conhecimento de domínio concentrado em poucos especialistas próximos da aposentadoria
- Necessidade de manter operação enquanto realizava a modernização
- Orçamento anual fixo para o projeto multiano

### Aplicação do FDCV

#### Fase de Discovery
- **Domain Storytelling Extensivo**: Múltiplas sessões com especialistas de domínio para documentar conhecimento tácito
- **Mapeamento de Dependências Ocultas**: Análise estática e dinâmica para identificar acoplamentos não documentados
- **Matriz de Valor por Módulo**: Identificação do valor de negócio real de cada componente do sistema

#### Fase de Planejamento
- **Estratégia de Strangler Pattern**: Planejamento de substituição gradual mantendo o sistema em funcionamento
- **Roadmap em Fases por Domínio**: Divisão do trabalho em domínios de negócio coesos
- **Parcerias Especialista-Desenvolvedor**: Vinculação formal de especialistas de domínio a equipes de desenvolvimento

#### Fase de Execução
- **Análise de Valor antes de cada Módulo**: Reavaliação do valor de negócio antes de iniciar cada componente
- **Dupla Implementação Temporária**: Execução paralela de sistemas antigo e novo com comparação automática de resultados
- **Documentação como Produto**: Elevação da documentação a um "produto" com usuários e feedback

### Resultados
- Modernização de 60% do sistema no primeiro ano (superando expectativa de 40%)
- Captura de conhecimento crítico de domínio antes da aposentadoria dos especialistas
- Redução de 25% no escopo após análise de valor (módulos raramente utilizados foram simplificados)
- Zero interrupções significativas durante a transição

### Lições Aprendidas
- A quantificação do valor real de cada módulo permitiu decisões objetivas de simplificação ou remoção
- A parceria formal entre especialistas e desenvolvedores criou transferência de conhecimento efetiva
- A abordagem de execução paralela reduziu significativamente o risco de transição

---

## Exemplo 3: Produto Interno com Múltiplos Stakeholders

### Contexto
Uma empresa multinacional precisava desenvolver um novo sistema de gestão de desempenho para uso global, atendendo requisitos de múltiplos departamentos (RH, Finanças, Operações) em diferentes regiões.

### Desafio
- Stakeholders com necessidades conflitantes
- Expectativas iniciais irrealistas (escopo amplo, prazo curto)
- Complexidade de requisitos regionais (legais e culturais)
- Necessidade de consenso entre diversos diretores

### Aplicação do FDCV

#### Fase de Discovery
- **Workshop de Alinhamento de Valor**: Sessão com todos stakeholders para definir critérios compartilhados de sucesso
- **Matriz de Requisitos por Região/Departamento**: Mapeamento visual de sobreposições e conflitos
- **Avaliação Técnica de Compatibilidade**: Análise da viabilidade técnica de unificar requisitos divergentes

#### Fase de Planejamento
- **Escopo Multi-fase com MVPs Regionais**: Definição de entregas incrementais por região/departamento
- **Comitê de Priorização Interdepartamental**: Criação de fórum formal para resolução de conflitos
- **Contrato de Flexibilidade com Gatilhos**: Mecanismos predefinidos para escalar decisões ao C-level quando necessário

#### Fase de Execução
- **Showcases por Grupo de Stakeholders**: Demonstrações personalizadas para diferentes áreas
- **Medição de Valor Percebido**: Pesquisas regulares com stakeholders sobre valor das entregas
- **Ajustes de Roadmap Trimestrais**: Revisões formais do plano com base em feedback e aprendizados

### Resultados
- Redução de 40% nas solicitações de mudança após implementação do comitê de priorização
- Maior satisfação de stakeholders comparado a projetos similares anteriores
- MVP global lançado 2 meses antes do planejado devido ao foco em valor essencial
- Adoção mais rápida por usuários finais devido ao envolvimento constante

### Lições Aprendidas
- A criação de um fórum formal para resolução de conflitos evitou impasses e mudanças constantes de direção
- A visualização conjunta de requisitos conflitantes facilitou negociações e compromissos
- A transparência sobre tradeoffs desde o início evitou frustrações posteriores

---

## Exemplo 4: Startup com Recursos Limitados

### Contexto
Uma startup de tecnologia precisava lançar um produto inovador com equipe reduzida (5 desenvolvedores) e investimento limitado, enfrentando pressão de investidores para mostrar resultados rapidamente.

### Desafio
- Recursos extremamente limitados (pessoas e orçamento)
- Alta incerteza sobre requisitos e mercado
- Necessidade de mostrar progresso rápido para próxima rodada de investimento
- Equipe com gaps de conhecimento em algumas tecnologias necessárias

### Aplicação do FDCV

#### Fase de Discovery
- **Matriz de Hipóteses de Valor**: Priorização de funcionalidades com base em impacto potencial de mercado
- **Workshop de Avaliação de Competências**: Mapeamento honesto de habilidades da equipe vs. necessidades técnicas
- **Exploração Técnica Timeboxed**: 2 semanas para validar viabilidade das abordagens técnicas mais arriscadas

#### Fase de Planejamento
- **MVP Realmente Mínimo**: Definição rigorosa do escopo mínimo para validar hipóteses principais
- **Roadmap Adaptativo**: Planejamento detalhado apenas até o próximo milestone de investimento
- **Matriz de Acordos Técnicos**: Definição explícita de onde investir em qualidade vs. onde aceitar dívida técnica

#### Fase de Execução
- **Ciclos Semanais de Revisão de Valor**: Análises frequentes para garantir foco constante no valor essencial
- **Pair Programming Estratégico**: Pairing focado em áreas de gap de conhecimento
- **Feedback de Early Adopters**: Ciclos rápidos de feedback com usuários selecionados após cada feature importante

### Resultados
- Lançamento de MVP funcional 3 semanas antes do previsto
- Feedback de mercado positivo permitindo captação de nova rodada de investimento
- Eliminação de 35% das features inicialmente planejadas por validação de baixo valor
- Redução significativa de retrabalho devido a validação constante

### Lições Aprendidas
- A documentação explícita de onde assumir dívida técnica permitiu decisões conscientes sem comprometer a manutenibilidade futura
- Os ciclos curtos de validação evitaram investimento em features que não se provaram valiosas
- A transparência sobre limitações técnicas da equipe permitiu decisões melhores de arquitetura e tecnologia

---

## Exemplo 5: Projeto com Dependências Externas

### Contexto
Uma empresa precisava integrar seu sistema core com múltiplos parceiros externos (20+ integrações) como parte de uma estratégia de plataforma aberta, com prazo comercial agressivo.

### Desafio
- Dependências de equipes e sistemas externos fora do controle direto
- Falta de padrão entre as diferentes integrações
- Necessidade de manter segurança e performance com aumento de tráfego
- Incerteza sobre as implementações dos parceiros

### Aplicação do FDCV

#### Fase de Discovery
- **Mapeamento de Dependências Críticas**: Identificação de quais integrações eram essenciais vs. opcionais
- **Avaliação de Riscos por Parceiro**: Classificação dos parceiros por maturidade técnica e importância estratégica
- **Prototipação de APIs Principais**: Validação técnica antecipada dos endpoints mais críticos

#### Fase de Planejamento
- **Plano de Parceiros em Ondas**: Agrupamento de parceiros por similaridade técnica e prioridade de negócio
- **Contratos de Serviço Claros**: Documentação detalhada e exemplos para facilitar integração dos parceiros
- **Roadmap com Buffers Estratégicos**: Inclusão deliberada de folgas em pontos de maior incerteza externa

#### Fase de Execução
- **Gateway de API com Sandbox**: Criação de ambiente de testes realista para parceiros
- **Checkpoints Técnicos com Parceiros-Chave**: Reuniões regulares com parceiros estratégicos
- **Dashboard de Progresso de Integrações**: Visibilidade sobre o status de cada integração para stakeholders

### Resultados
- 15 das 22 integrações concluídas no prazo inicial
- Parceiros adicionais completaram integrações nas 4 semanas seguintes
- Isolamento efetivo de problemas de parceiros individuais sem afetar o sistema core
- Menor tempo médio de integração por parceiro do que em projetos anteriores

### Lições Aprendidas
- O agrupamento de parceiros similares permitiu reutilização de conhecimento e acelerou as integrações
- A criação de sandbox e documentação detalhada reduziu significativamente o suporte necessário
- A classificação inicial de riscos permitiu alocação mais eficiente de recursos de suporte

---

## Aplicando Estes Exemplos

Estes casos demonstram como o FDCV pode ser adaptado para diferentes contextos e desafios. Ao estudá-los, considere:

1. **Quais práticas podem ser mais relevantes para seu contexto específico?**
2. **Como os princípios foram adaptados para atender às necessidades específicas de cada caso?**
3. **Quais lições aprendidas podem ser aplicadas antecipadamente em seu projeto?**

O poder do FDCV está em sua adaptabilidade. Use estes exemplos como inspiração, não como prescrições rígidas para sua implementação.

Para compartilhar sua própria experiência de aplicação do FDCV ou obter suporte, contribua para nossa [comunidade de prática](/deliver-value-methodology/community).
