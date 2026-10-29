# Specs na era da IA

> Fontes verificadas em 28/10/2026. Os números são citados com o seu escopo; onde a evidência é mista, dizemos isso.

Durante anos, a maioria dos times tratou o abismo entre "o que produto pediu" e "o que o código precisa saber" como parte normal do trabalho. Uma história chegava um pouco vaga, alguém (muitas vezes o Tech Lead) fazia três perguntas no corredor, completava as lacunas com a própria experiência, e o trabalho seguia. Essa tradução informal é uma das forças silenciosas dos bons times.

Os agentes de código mudam a economia desse abismo. Esta página explica como, o que a indústria está construindo em resposta e onde o Value-First se encaixa. É um convite para atualizar a forma como pensamos sobre specs. Não é um veredito sobre nenhuma forma anterior de trabalhar: o Waterfall nos deu a disciplina de escrever as coisas, o Agile nos deu ciclos curtos de feedback e o Scrum nos deu uma cadência estável. Queremos manter os três.

---

![Antes e agora: do produto à spec e ao código](../../assets/diagrams/before-after-pt.svg)

## 1. A spec virou insumo executável

Quando uma pessoa lê uma spec, ela interpreta. Quando um agente lê uma spec, ele age, muitas vezes produzindo centenas de linhas de código plausível em minutos.

A introdução do GitHub ao seu Spec Kit de código aberto diz isso diretamente. Modelos de linguagem são "excepcionais em completar padrões, mas não em ler mentes". Um pedido como "adicione compartilhamento de fotos ao meu app" deixa o modelo adivinhando "potencialmente milhares de requisitos não declarados" ([GitHub Blog, set. 2025](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)). O mesmo post descreve as specs como "artefatos vivos e executáveis" e "a fonte compartilhada da verdade".

A consequência prática: **com um agente no ciclo, a qualidade do que é entregue fica limitada pela qualidade do que foi especificado.** Uma spec vaga não deixa o trabalho mais lento. Ela produz a coisa errada mais rápido.

## 2. O abismo ficou mais caro

Pessoas compensam specs incompletas com conversa, contexto e intuição. Um agente só faz perguntas se for instruído a fazer, e executa o que está escrito. O que antes era um incômodo vira um gargalo.

As evidências sobre IA e entrega apontam na mesma direção. A IA amplifica qualquer sistema em que é inserida:

- O [relatório DORA de 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) constatou que mais adoção de IA vinha acompanhada de melhor qualidade de documentação, melhor qualidade de código e revisões mais rápidas. Também constatou que cada aumento de 25% na adoção de IA estava associado a uma **queda estimada de 1,5% na vazão de entrega e de 7,2% na estabilidade de entrega** (correlações de pesquisa, não efeitos causais). A leitura do DORA foi que a IA não substitui "o básico de uma entrega de software bem-sucedida, como lotes pequenos e testes robustos".
- O [relatório DORA de 2025](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/) encontrou adoção de 90% e, desta vez, uma relação com vazão *maior*. Seu enquadramento central é que a IA é "um espelho e um multiplicador": ajuda organizações coesas e expõe as fragmentadas.
- O [AI Capabilities Model](https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model) do DORA aponta o **foco no usuário** como uma de sete capacidades amplificadoras: "quando os usuários não são o foco, times de desenvolvimento assistido por IA podem estar apenas se movendo rapidamente na direção errada". Trabalhar em lotes pequenos é outra.

Velocidade no teclado já não é o recurso escasso. Clareza sobre *o que* construir, e *por quê*, é.

## 3. O Tech Lead como "engenheiro de especificação", junto com produto

Em muitos times, o Tech Lead já faz esse trabalho de maneira informal: traduzindo, completando, decidindo. O Value-First propõe tornar esse papel **explícito e central**, sem deixar o Tech Lead carregá-lo sozinho.

- **Produto** é dono do problema, do valor esperado e de como o sucesso será medido.
- **O Tech Lead** é dono da tradução em restrições, riscos, critérios testáveis e do contexto de que os agentes precisam (regras de arquitetura, convenções, requisitos não funcionais).
- **Os dois** assinam a spec, e os dois respondem quando ela muda.

Isso bate com o que praticantes relatam sobre trabalhar com agentes. O [post do GitHub sobre o Spec Kit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) diz isso claramente: "o seu papel não é só conduzir. É verificar." Birgitta Böckeler (Thoughtworks) destaca a mesma frase em sua [análise de ferramentas de SDD](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html). Seu [artigo sobre engenharia de contexto](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) mostra quanto julgamento existe em decidir que contexto um agente deve receber. Alguém precisa ser dono desse julgamento. Achamos que deve ser uma dupla, não um herói.

## 4. A spec como contrato de valor, não como documento

Uma spec Value-First não é um despejo de requisitos. É um acordo curto sobre quatro coisas:

1. **O problema**, e para quem.
2. **O valor esperado**: um resultado (outcome), uma métrica, uma linha de base e uma meta.
3. **Critérios de sucesso mensuráveis**: afirmações testáveis com as quais um agente consegue relacionar tarefas e que um revisor consegue verificar. Critérios de comportamento podem usar [EARS](https://alistairmavin.com/ears/) ("Quando <gatilho>, o <sistema> deve <resposta>"), uma notação da Rolls-Royce que o [Kiro](https://kiro.dev/docs/specs/feature-specs/) também usa, ou Given/When/Then.
4. **Restrições técnicas**: requisitos não funcionais, segurança, compliance, limites de arquitetura.

E ela é **viva**. Böckeler separa três níveis de SDD: *spec-first* (a spec é escrita para uma tarefa), *spec-anchored* (a spec é mantida e evolui com a funcionalidade) e *spec-as-source* (pessoas editam apenas a spec) ([martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)). O Value-First mira no **spec-anchored**. A spec fica ao lado do código, é versionada com ele e muda quando o código ou o feedback dos usuários nos ensinam algo. Um registro de decisões e um registro de mudanças tornam isso visível. Veja o [template de Value Spec](../../templates/pt/value-spec.md).

## 5. Um ciclo mais curto da ideia à validação

Agentes tornam protótipos baratos. Isso abre espaço para uma prática que queremos tornar padrão: **usar um protótipo como forma de spec.** Um fluxo clicável ou uma implementação descartável, gerados em horas, podem mostrar a produto, usuários e engenharia o que as palavras não conseguiram. Eles testam a premissa mais arriscada *antes* de investirmos em uma construção de nível de produção.

Isso também responde a uma crítica justa ao SDD (veja "Limites e riscos" abaixo). O objetivo não é escrever mais antes de construir. É **aprender mais cedo o que vale a pena construir e, então, escrever exatamente isso.** Protótipos são evidência, não entregáveis. Eles são descartados, e a spec guarda o que eles nos ensinaram.

---

## Estado da arte: quem faz o quê

| Camada | O que responde | Exemplos |
|---|---|---|
| **Valor e alinhamento** | *Vale a pena construir isso? Como vamos saber? O que é inegociável?* | **Value-First** (Value Spec, validação, verificação de valor) |
| **Fluxo de spec para código** | *Dada a intenção, qual é o plano, quais tarefas, que código?* | [GitHub Spec Kit](https://github.com/github/spec-kit): constitution → specify → plan → tasks → implement. [AWS Kiro](https://kiro.dev/docs/specs/): `requirements.md` (EARS) → `design.md` → `tasks.md`, com uma variante requirements-first ou design-first. [Tessl](https://tessl.io/): explorou o *spec-as-source* enquanto estava em beta em 2025 ([Böckeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)) e hoje se apresenta como uma "plataforma de habilitação de agentes" para skills e contexto. |
| **Contexto do agente** | *O que toda sessão de agente deveria saber sobre este código e este time?* | [AGENTS.md](https://agents.md/) (formato aberto mantido pela Agentic AI Foundation, sob a Linux Foundation; o site informa uso em mais de 60 mil projetos de código aberto). [CLAUDE.md](https://code.claude.com/docs/en/memory) (Claude Code, que também consegue ler o AGENTS.md). [Cursor rules](https://cursor.com/docs/context/rules) (`.cursor/rules/*.mdc`, além do AGENTS.md). [Kiro steering](https://kiro.dev/docs/steering/) (`product.md`, `tech.md`, `structure.md`). |
| **Avaliação da indústria** | *Quão maduro isso está?* | Thoughtworks Technology Radar (nov. 2025): [spec-driven development em **Assess**](https://www.thoughtworks.com/radar/techniques/spec-driven-development) e [AGENTS.md em **Trial**](https://www.thoughtworks.com/radar/techniques/agents-md). |

**Onde o Value-First fica.** O Value-First é a **camada de valor e alinhamento acima** dessas ferramentas, não um concorrente delas:

- **Value-First** decide *o que vale a pena construir e como vamos saber que funcionou*: problema, valor esperado, critérios de sucesso, restrições, plano de validação.
- **Ferramentas de SDD** (Spec Kit, Kiro e outras) transformam isso em plano, tarefas e código.
- **Arquivos de contexto do agente** (AGENTS.md, CLAUDE.md, rules, steering) levam as restrições e convenções duradouras para cada sessão.

Na prática, uma Value Spec pode servir de entrada para a etapa `specify` do Spec Kit ou para a fase de requisitos do Kiro. Suas restrições e seus inegociáveis podem alimentar uma *constitution* do Spec Kit ou um arquivo de steering ou AGENTS.md. O Value-First não substitui nenhum deles. Ele garante que o que entra neles vale a pena ser construído.

---

## Limites e riscos

Aqui preferimos ser honestos a ser persuasivos.

- **Ganhos de produtividade não são garantidos.** No [ensaio controlado randomizado (RCT) de 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) do METR, 16 desenvolvedores experientes de código aberto levaram **19% mais tempo** com ferramentas de IA, embora acreditassem que a IA os tinha deixado cerca de 20% mais rápidos. A [atualização de fevereiro de 2026](https://metr.org/blog/2026-02-24-uplift-update/) do METR, com ferramentas do fim de 2025, aponta para ganhos de velocidade, mas todos os intervalos de confiança incluem zero, e o próprio METR considera os novos dados pouco confiáveis por causa de efeitos de seleção. O resumo honesto: percepção não é medição, e o resultado depende do contexto.
- **Qualidade e segurança.** O [2025 GenAI Code Security Report](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/) da Veracode constatou que o código gerado introduziu vulnerabilidades em 45% dos casos, testando 80 tarefas selecionadas em mais de 100 modelos. É um benchmark de fornecedor, não uma taxa universal, mas é um motivo para manter as restrições de segurança explícitas na spec e continuar fazendo varreduras.
- **Riscos de segurança próprios de agentes.** Modelos podem recomendar pacotes que não existem. Num estudo com 16 modelos de código, os pacotes alucinados ficaram em média em pelo menos 5,2% nos modelos comerciais e 21,7% nos de código aberto, e atacantes podem explorar isso publicando esses nomes ([Spracklen et al., USENIX Security 2025](https://arxiv.org/abs/2406.10279)). Agentes que leem conteúdo não confiável (issues, páginas web, arquivos) também ficam expostos a prompt injection, o primeiro risco do [OWASP Top 10 para aplicações com LLM](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). As instruções para agentes da Value Spec pedem que eles confiram dependências novas e tratem conteúdo como dado, não como instrução. Essas instruções são orientação, então permissões mínimas e revisão humana continuam necessárias.
- **Confiança e carga de revisão.** Na [pesquisa de 2025 do Stack Overflow](https://survey.stackoverflow.co/2025/ai), 46% dos desenvolvedores disseram não confiar na precisão do que a IA produz, e 45% apontaram a depuração demorada de código de IA como uma frustração importante. Ferramentas de SDD trazem sua própria carga de revisão: Böckeler viu o Spec Kit gerar muitos arquivos markdown verbosos que ela preferiria não revisar, e o Kiro transformar um bug pequeno em quatro histórias de usuário com 16 critérios de aceite ("matar uma mosca com uma bala de canhão").
- **"Vibe coding".** Andrej Karpathy [cunhou o termo](https://x.com/karpathy/status/1886192184808149383) para um estilo em que você "esquece que o código sequer existe". Serve bem para protótipos descartáveis e é arriscado em produção. A [regra](https://simonwillison.net/2025/Mar/19/vibe-coding/) de Simon Willison é um bom padrão: não faça commit de código que você não conseguiria explicar para outra pessoa.
- **Specs que se desatualizam e specs ignoradas.** A maioria das ferramentas é *spec-first* na prática, e a manutenção da spec no longo prazo costuma ficar vaga ([Böckeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)). Agentes também ignoram instruções ou as aplicam em excesso, e arquivos de contexto são orientação, não imposição. A documentação do Claude Code diz que eles são tratados "como contexto, não como configuração imposta" ([docs](https://code.claude.com/docs/en/memory)). Böckeler alerta para uma "ilusão de controle" ([engenharia de contexto](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)). A Thoughtworks acrescenta que "escrever à mão regras detalhadas para a IA, no fim das contas, não escala" e que "talvez estejamos reaprendendo uma lição amarga" ([Radar](https://www.thoughtworks.com/radar/techniques/spec-driven-development)).
- **A crítica do retorno ao waterfall.** François Zaninotto argumenta que o SDD ressuscita a documentação pesada antecipada e que "agentes de código turbinam o Agile" quando usados em pequenos incrementos ([Marmelab, nov. 2025](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html)). Marc Brooker (AWS) responde que o SDD "não é sobre trazer o design *para antes*, é sobre trazer o design *para cima*" ([abr. 2026](https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec)). Levamos a crítica a sério.

**Como o Value-First evita reconstruir o waterfall:**

1. **Specs pequenas, recortadas por valor.** Uma spec por resultado ou fatia de valor, não por projeto. Mire em uma página. Passou de duas, divida. (São os "lotes pequenos" do DORA aplicados às specs.)
2. **Protótipo primeiro quando o valor é incerto.** Valide a premissa mais arriscada de forma barata e depois especifique o que você aprendeu.
3. **Viva, não congelada.** As specs são versionadas ao lado do código, com um registro de decisões e um registro de mudanças. O princípio 5 ("um plano que muda é informação, não fracasso") é como uma spec muda: com um motivo, de forma visível, e com a concordância dos dois donos.
4. **Valor antes de volume.** A spec declara o problema, o valor e a evidência. Planos e tarefas são gerados depois, então não os escrevemos à mão de antemão.
5. **Pessoas verificam.** Toda mudança produzida por um agente é rastreada até o ID de um critério de sucesso e revisada por uma pessoa.

---

## Como começar (uma funcionalidade, uma semana)

1. **Escolha uma funcionalidade próxima** com valor de negócio real e alguma incerteza.
2. **Escrevam juntos uma Value Spec**: produto e Tech Lead, em uma sessão, usando o [template](../../templates/pt/value-spec.md). Mantenha-a curta.
3. **Nomeie a premissa mais arriscada** e valide-a com o protótipo ou spike mais barato (muitas vezes gerado por IA) antes de se comprometer a construir.
4. **Crie ou organize um `AGENTS.md`** (ou CLAUDE.md, rules ou steering) com as restrições duradouras: comandos de build e teste, regras de arquitetura, requisitos obrigatórios de segurança.
5. **Passe a spec para sua ferramenta de SDD ou seu agente** e exija que tarefas e PRs citem os IDs dos critérios de sucesso.
6. **Revise contra a spec, não só contra o diff.** Atendemos aos critérios? A spec precisou mudar? Registre.
7. **Meça o valor** que vocês disseram que iriam medir e façam uma retro curta sobre o que faltou na spec.

---

### Fontes

- GitHub Blog — [Spec-driven development with AI](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) (Den Delimarsky, 2 set. 2025)
- [Repositório do GitHub Spec Kit](https://github.com/github/spec-kit)
- Kiro — [Specs](https://kiro.dev/docs/specs/), [Feature specs / EARS](https://kiro.dev/docs/specs/feature-specs/), [Steering](https://kiro.dev/docs/steering/)
- [Tessl](https://tessl.io/)
- Birgitta Böckeler — [Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) (15 out. 2025); [Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) (5 fev. 2026)
- Thoughtworks Technology Radar — [Spec-driven development (Assess)](https://www.thoughtworks.com/radar/techniques/spec-driven-development); [AGENTS.md (Trial)](https://www.thoughtworks.com/radar/techniques/agents-md) (nov. 2025)
- [AGENTS.md](https://agents.md/) · [Claude Code memory / CLAUDE.md](https://code.claude.com/docs/en/memory) · [Cursor rules](https://cursor.com/docs/context/rules)
- DORA — [anúncio do relatório de 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report); [resumo do relatório de 2025](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/); [AI Capabilities Model](https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model)
- METR — [RCT do início de 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [atualização de desenho de fev. 2026](https://metr.org/blog/2026-02-24-uplift-update/)
- [Veracode 2025 GenAI Code Security Report (press release)](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/)
- [Stack Overflow 2025 Developer Survey (press release)](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/)
- [EARS — Alistair Mavin](https://alistairmavin.com/ears/)
- Simon Willison — [Not all AI-assisted programming is vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/)
- François Zaninotto — [Spec-Driven Development: The Waterfall Strikes Back](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html); Marc Brooker — [Spec Driven Development isn't Waterfall](https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec)
