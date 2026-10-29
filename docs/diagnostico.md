# Diagnóstico: de "Deliver-Value Framework" para Value-First Development

> Documento interno de trabalho (rascunho para `docs/diagnostico.md`). Autor: estrategista de produto/metodologia. Data: 2026-10-28.
> Convenção: **[fonte?]** marca uma afirmação factual que precisa de URL verificável antes de ir para o texto público. Quando não houver fonte, a afirmação vira opinião/hipótese ou sai.
> Nada aqui apaga conteúdo do repositório. Toda remoção sugerida está marcada como **[remoção: requer aprovação do autor]**.

---

> **Nota (v2):** este diagnóstico foi escrito antes da pesquisa de fontes. Afirmações marcadas com [fonte?] foram verificadas (ou descartadas) em [research/sources.md](research/sources.md); os textos públicos do v2 só usam as versões com fonte. As decisões tomadas a partir deste documento estão em [DECISIONS.md](../DECISIONS.md).

## 1. Resumo executivo

1. O diagnóstico central do repositório continua válido: entre a especificação de produto e o desenvolvimento existe uma lacuna, e o Tech Lead costuma preenchê-la por conta própria, sem que ninguém tenha combinado isso.
2. Com agentes de IA escrevendo código, essa lacuna ficou mais cara. Uma pessoa compensa uma especificação incompleta conversando; um agente executa o que está escrito. Esse é o argumento novo e mais forte.
3. O conteúdo atual dilui a ideia: catálogo de 22 práticas de terceiros, papel novo (Analista de Valor) que cria repasse, artefatos com ar contratual, estudos de caso "reais" com números sem fonte.
4. A forma tem problemas que minam a credibilidade: três nomes diferentes, links quebrados e placeholders, um arquivo que aparece como bloco de código no GitHub, números que divergem entre PT e EN.
5. **Recomendação: REPOSICIONAR.** Manter a tese e as melhores ideias, mudar o eixo (a especificação como contrato de valor, na era da IA), o nome e o posicionamento (uma camada de valor e alinhamento *acima* de Scrum/Kanban e das ferramentas de spec-driven development, não concorrente delas).

**Por que reposicionar, e não evoluir nem reescrever:**
- *Evoluir* (ajustes incrementais) não resolve o problema principal: o texto atual se apresenta como "mais um framework" com papéis, fases e comitês, e quase não fala de IA. Retocar mantém essa identidade.
- *Reescrever do zero* jogaria fora ativos reais: a tese do Tech Lead como tradutor informal, o Canvas de Alinhamento, a ideia de "fixo vs. flexível", a avaliação técnica antes do compromisso. Esses ativos são o núcleo do v2.
- *Reposicionar* significa reaproveitar as ideias e reescrever boa parte do texto em volta de um eixo novo. Na prática, uns 70% do texto muda; quase todas as ideias boas ficam.

---

## 2. O manifesto ainda faz sentido?

**Sim, e hoje o problema é mais agudo do que quando o texto foi escrito.** Mas ele precisa ser descrito de outra forma.

### O problema real hoje (formulado como hipótese, não como acusação)

- **A especificação virou entrada executável.** Com agentes de código (Copilot, Claude Code, Cursor, Kiro etc.), a qualidade da entrega depende muito da qualidade do que está escrito. Spec vaga gera código errado, só que mais rápido. *(Hipótese do autor. Dá para sustentar com materiais de ferramentas de spec-driven development que dizem a mesma coisa: GitHub Spec Kit, Kiro [fonte?: github.com/github/spec-kit, kiro.dev].)*
- **A lacuna ficou mais cara.** Antes, pessoas compensavam especificações incompletas com conversa, contexto e intuição. Um agente não pergunta "mas o que vocês querem dizer com isso?" com a frequência de uma pessoa. Ele preenche o vazio com suposições plausíveis. O que antes era um incômodo agora vira gargalo.
- **O Tech Lead já faz esse trabalho, só que sem nome e sozinho.** Ele traduz, completa e decide. O v1 já via isso; o v2 deve tornar o papel explícito ("engenharia de especificação") e **dividi-lo com Produto**, em vez de criar uma terceira pessoa no meio.
- **Velocidade sem validação de valor amplifica desperdício.** Se construir ficou mais barato, o risco passa a ser construir com eficiência a coisa errada. Há indícios de que a adoção de IA pode vir junto com perda de estabilidade de entrega quando faltam práticas de base [fonte?: DORA, *Accelerate State of DevOps Report 2024*, dora.dev; confirmar os números exatos antes de citar].
- **Protótipo barato muda a ordem do processo.** Hoje dá para gerar com IA um protótipo navegável em horas. O protótipo pode *ser* parte da especificação: validar valor antes de investir em construção. *(Opinião; não precisa de fonte se escrito como recomendação.)*

### O que o v2 **não** deve dizer

- Que "o Scrum falhou". A formulação correta: "o Scrum, *como muitas empresas o praticam*, às vezes vira cerimônia e deixa a especificação fora do ciclo de inspeção". E reconhecer o mérito: cadência, inspeção e adaptação, times multifuncionais.
- Que a IA resolve o problema. A IA aumenta o custo de especificar mal e o ganho de especificar bem. Riscos que o texto precisa nomear: qualidade, revisão humana obrigatória, dívida técnica, segurança, dependência de fornecedor.

### Risco honesto para a própria proposta

- **Parecer "Waterfall com nome novo".** Dar ênfase à spec pode ser lido como volta do grande design antecipado. A defesa: a spec é *curta, viva e versionada junto com o código*, e o protótipo faz parte dela.
- **Parecer "Shape Up + Specification by Example com outro nome".** As ideias vizinhas existem e precisam receber crédito (seção 5). O diferencial está na *combinação*: valor mensurável + spec como entrada para IA + responsabilidade compartilhada Produto/Tech + sinais observáveis.

---

## 3. Manter, cortar, acrescentar

### 3.1 Manter (ideias fortes)

| Ideia atual | Por que é forte | Como entra no v2 |
|---|---|---|
| Tech Lead como "tradutor informal" que ocupa o espaço do antigo analista de sistemas | Observação reconhecível por quem vive o dia a dia; é a tese de origem | Vira o argumento central, ligado à spec e à IA |
| Valor acima de prazo | Mensagem simples | Reescrito como "valor explícito antes do trabalho" (não é contra prazos) |
| Avaliação técnica preliminar antes do compromisso | Prática concreta, com retorno evidente | Vira "validar antes de construir" (spike, protótipo, protótipo com IA) |
| Separar o fixo do flexível (núcleo do "Contrato de Flexibilidade") | Resolve de verdade o dilema prazo regulatório vs. escopo | Vira uma *seção* da Value Spec, não um contrato à parte |
| Canvas de Alinhamento Valor-Tecnologia | Ativo visual pronto, fácil de usar em workshop | Mantido como artefato de iniciativa (kickoff) |
| Métricas de resultado (outcome) vs. entrega (output) | Correto e alinhado ao estado da arte | Vira "sinais observáveis" |
| "Documentar o porquê, não só o quê"; registros de decisão | Base de uma spec viva | Entra na Value Spec (decisões ligadas a ADRs) |
| Compatível com Scrum/Kanban, adoção gradual por piloto | Posicionamento certo | Mantido e reforçado como "camada acima" |
| Prazos regulatórios são reais | Mostra maturidade, não é ingênuo | Mantido como exemplo de "fixo" |

### 3.2 Cortar ou fundir (inchaço, risco, contradição)

| Item | Problema | Proposta |
|---|---|---|
| **Analista de Valor** como papel novo | Cria uma camada de repasse (Produto → Analista → Tech), justamente o "telefone sem fio" que o framework quer eliminar. O próprio FAQ precisa se defender ("não aumenta burocracia?", "como evitar que vire gargalo?"). Também esbarra no Product Owner do Scrum | Deixa de ser cargo. Vira responsabilidade compartilhada do par Produto + Tech Lead (seção 7.3). "Analista de valor" pode existir como *chapéu*, nunca como etapa obrigatória **[remoção: requer aprovação do autor]** |
| **"Renegociação Formal"** (princípio 4) | "Formal" soa como processo, escalonamento e auditoria. Passa a ideia de que mudar é exceção | Reescrever: "mudança de plano é informação" (leve, visível, registrada na spec) |
| **Contrato de Flexibilidade**, **Acordos de Compromisso**, **Comitê de Priorização**, **Escalonamento Baseado em Dados** | Quatro mecanismos parecidos e com tom jurídico. "Contrato" entre áreas da mesma empresa sugere desconfiança | Fundir na seção "Fixo vs. flexível + gatilhos de revisão" da Value Spec. Comitê e escalonamento saem do núcleo (no máximo, nota de adoção em empresas grandes) **[remoção: requer aprovação do autor]** |
| **Estudos de caso "reais"** (banco, saúde) | Números precisos sem fonte nem organização identificável (40%, 65%, 28%, $300.000). **A versão PT diz "R$ 1,2 milhão" onde a EN diz "$300,000"**, o que tira a credibilidade das duas | Sair do texto público, a menos que o autor tenha evidência publicável. Se houver, reescrever com fonte e permissão **[remoção: requer aprovação do autor]** |
| **Exemplos ilustrativos** com percentuais (30%, 60% vs. 40%, 25%, "2 meses antes", "3 semanas antes", 35%, 15 de 22) | Mesmo rotulados como "compostos", números exatos parecem dados | Manter 2–3 exemplos curtos, sem percentuais, focados em *como a Value Spec ficou* |
| Catálogo de 22 práticas (C4, BPMN, UML, ERD, Event Storming, Domain Storytelling, RICE, Impact Mapping…) | Técnicas de terceiros sem crédito nem link. Dilui a identidade: o leitor não sabe o que é *do* Value-First | Trocar por 3–5 práticas próprias. As de terceiros vão para "Técnicas compatíveis", com autor e link |
| Quatro fases (Descoberta, Planejamento, Execução, Entrega & Aprendizado) | Fases sequenciais lembram Waterfall e conflitam com a cadência do Scrum/Kanban. Além disso, `practices.md` usa outras fases (Validação, Resolução de Conflitos) | Trocar por um *ciclo* curto por item de trabalho: Especificar → Validar → Construir → Verificar valor |
| Matriz de Valor, Mapa de Complexidade Técnica, Dashboard Valor vs. Progresso | Três artefatos parcialmente sobrepostos, e dois deles marcados "Em breve" | Matriz → visão opcional de priorização entre specs. Mapa de complexidade → seção da spec. Dashboard → sinais observáveis |
| "Funciona para hardware, design de serviços, transformação organizacional" (FAQ) | Expansão de escopo sem base; enfraquece o foco | Cortar. O foco é desenvolvimento de software com IA |
| Linha do tempo de resultados ("1–3 meses", "3–6 meses") no FAQ | Promessa sem dados | Cortar ou reescrever como expectativa sem prazo |
| Citações entre aspas sem autor nos princípios ("Um dia investido em avaliação técnica pode economizar semanas de retrabalho") | Parecem citação de terceiros | Tirar as aspas e assumir como frase do próprio texto, ou cortar |

### 3.3 O que falta

1. **Eixo IA/especificações.** Não existe hoje. Precisa ser o centro: spec como entrada executável, protótipo como spec, revisão humana, a ligação entre spec e arquivos de instrução de agentes (AGENTS.md / CLAUDE.md) [fonte?: agents.md].
2. **Identidade observável.** Como saber se um time "pratica Value-First"? Hoje não há resposta. O v2 precisa de sinais concretos e verificáveis (seção 7.5).
3. **Comparação honesta** com Scrum, Kanban, Shape Up, SAFe e as ferramentas de spec-driven development, com crédito a cada um (seção 5).
4. **Modelo de maturidade.** `practices.md` promete um ("Desenvolver um modelo de maturidade"), mas ele não existe. Proposta mínima, em três níveis:
   - *Nível 1, Explícito:* todo item relevante tem uma Value Spec com critério de sucesso mensurável.
   - *Nível 2, Compartilhado:* specs coassinadas por Produto e Tech, versionadas no repositório e usadas como entrada pelos agentes.
   - *Nível 3, Fechando o ciclo:* a verificação de valor depois da entrega acontece e realimenta a spec e o backlog.
5. **Fontes.** Lista de referências com URL (Scrum Guide, Kanban Guide, Shape Up, Spec Kit, Kiro, DORA, Specification by Example, Impact Mapping, Royce 1970, Boehm).
6. **Templates de verdade.** "Matriz de Valor" e "Contrato de Flexibilidade" estão como "Em breve". O v2 precisa de pelo menos `value-spec.md` pronto para copiar.
7. **Quando *não* usar / antipadrões.** Exemplos: time muito pequeno com produto estável; spec virando documento de 30 páginas; "valor" virando métrica de vaidade.
8. **Limites e riscos da IA**, de forma explícita: segurança, qualidade, revisão, dívida técnica, privacidade de dados enviados ao modelo.
9. **Glossário** curto (spec, valor, critério de sucesso, agente, protótipo, outcome/output).

---

## 4. Problemas de forma

### 4.1 Nomes inconsistentes

- O framework aparece como **"Framework de Desenvolvimento Centrado em Valor (FDCV)"** (README PT), **"Deliver-Value Framework (DV)"** (docs), **"(DV)"** com parênteses como se fosse o nome ("Princípios e Estrutura do (DV)", "Why (DV)?"), **"Deliver-Value (DV) Framework"** e **"framework Deliver-Value"** (templates). O repositório se chama **"methodology"** e o texto diz **"framework"**.
- Papéis: "Especialista Técnico" / "Team Leader" / "Tech Lead"; "Especialista de Negócio/Produto" em vez do termo de mercado (Product Owner/Product Manager); "Analista Médico de Valor" surge em um caso.
- Fases: `principles.md` tem 4 fases (… Entrega & Aprendizado); `practices.md` organiza por Descoberta/Planejamento/Execução/**Validação**/**Resolução de Conflitos**/Escala.
- Artefatos: "Mapa de Complexidade Técnica" vs. "matriz de complexidade técnica" (caso 1); "Dashboard Valor vs. Progresso" vs. "dashboards de valor vs. complexidade" (caso 1).
- **Decisão para o v2:** "Value-First Development" no título; "Value-First" no texto. Sem sigla, sem parênteses. Usar "abordagem" ou "modelo" no lugar de "framework/metodologia" (é mais leve e combina com "camada acima"), ou decidir um só termo e usar em todo lugar.

### 4.2 Links quebrados e placeholders

| Arquivo | Link | Problema |
|---|---|---|
| README.md | `github.com/seu-usuario/fdcv` (badge + 3 links no rodapé: repo, wiki, discussions) | Placeholder |
| translations/README.en.md | `github.com/your-username/(DV)` (badge + 3 links no rodapé) | Placeholder |
| README.md | `/docs/docs/ROLES.md`, `/docs/pt/ROLES.md` | Arquivo não existe |
| translations/README.en.md | `/docs/en/ROLES.md`, `/docs/ROLES.md`, `/docs/ARTIFACTS.md`, `/examples/case-studies/` | Arquivos/pastas não existem |
| translations/README.en.md | Sumário com âncoras `#-our-proposal-the-(DV)`, `#-why-(DV)` | Âncoras não resolvem |
| docs/en/templates.md / docs/pt/templates.md | `/docs/en/practice.md`, `/docs/pt/pratica.md` | Arquivos não existem |
| docs/*/templates.md | "Guia de Templates" aponta para o próprio arquivo | Link circular |
| docs/*/case-studies.md, templates.md, faq.md, CONTRIBUTORS.md | `/deliver-value-methodology/CONTRIBUTING.md`, `/deliver-value-methodology/en/principles.md`, `/deliver-value-methodology/community` | No GitHub, o caminho absoluto começa na raiz do repo, então o prefixo com o nome do repo quebra. `community` não existe |
| README.md | Link "English Version" aponta para `/translations/README.en.md`, mas a EN não tem link de volta para PT | Navegação de mão única |

Outros defeitos de forma:
- **`docs/en/principles.md` tem todas as linhas indentadas com 4 espaços.** O GitHub renderiza o arquivo inteiro como bloco de código. É o defeito mais visível do repositório.
- `docs/pt/principles.md` não tem o bloco de navegação que a versão EN tem (PT e EN divergem).
- `docs/en/templates.md` tem o título **"## Other Templates" duplicado**.
- `translations/README.es.md` e `translations/README.pt.md` estão vazios. Ter um `README.pt.md` vazio ao lado de um README.md em PT confunde **[remoção: requer aprovação do autor]**.
- `CONTRIBUTORS.md` lista o criador como **"Your Username"**, quando deveria ser André Lara Amorim (que está no LICENSE).
- `CONTRIBUTING.md` existe só em PT, mas o título usa "(DV)". Não há versão EN.
- Badges "Em Desenvolvimento" / "Em Construção" passam a ideia de rascunho. Trocar por versão ("v2.0").
- Finais de linha CRLF misturados (vistos em `docs/en/principles.md`). Recomendação: `.gitattributes`.

### 4.3 Tamanho

- Hoje são cerca de 3.250 linhas de Markdown. O README PT tem 155 linhas, das quais umas 60 são história das metodologias antes de chegar à proposta.
- `practices.md` (~390 linhas), `faq.md` (~300) e `case-studies.md` (~370) são longos e repetem o mesmo conteúdo com outras palavras.
- **Meta v2:** README lido em 3 minutos (no máximo ~120 linhas, proposta nas primeiras 15). Documentação núcleo em PT ≤ ~1.000 linhas no total.

### 4.4 Tom: trechos que soam acusatórios ou exagerados

| Trecho atual (PT / EN) | Problema | Direção |
|---|---|---|
| "A área de Produto, frequentemente pressionada pelo negócio, estabelece prazos e escopo (…) sem compreensão profunda dos desafios técnicos" | Culpa Produto | "Produto e Tecnologia muitas vezes decidem com informações diferentes" |
| "o modelo ágil, ao distribuir responsabilidades, criou uma lacuna" / "Esta abordagem eliminou a figura centralizada do analista de sistemas" | Atribui ao Ágil a culpa por um problema de prática | "Em muitas adoções, a responsabilidade de traduzir ficou sem dono claro" |
| "O resultado é um ciclo de frustração, com tentativas desesperadas de cumprir prazos cada vez mais irrealistas" / "desperate attempts" | Dramático | Descrever o efeito (retrabalho, prazos renegociados tarde) sem adjetivos |
| "Combina o melhor dos dois mundos: A clareza do Waterfall com a flexibilidade do Ágil" | Clichê de marketing | Reconhecer o mérito de cada um sem prometer síntese |
| "Resolve a desconexão entre áreas de Produto e Engenharia" | Promessa absoluta | "Ajuda a reduzir…" |
| "O FDCV preenche uma lacuna crítica nas metodologias atuais" | Exagero, e critica outras abordagens | "Complementa…" |
| "Reduz frustração e burnout das equipes" | Afirmação de saúde sem fonte | Cortar ou transformar em hipótese |
| "When implemented correctly, this role increases efficiency, not bureaucracy" (FAQ) | Defensivo, não dá para falsificar | Cortar junto com o papel |
| "This situation is precisely where the DV can bring the most benefits" (FAQ) | Exagero | Cortar |
| "DV is particularly valuable in regulated environments" (FAQ) | Afirmação sem evidência | "Pode ajudar porque separa o obrigatório do desejável" |
| "Scrum (…) trouxe uma abordagem radicalmente diferente" | Leve exagero | "trouxe ciclos curtos e inspeção frequente" |
| "These practices have been compiled from real experiences" | Afirmação de evidência sem evidência | "Práticas sugeridas pelo autor" |
| "grau W" ("often called 'W-grade'") | Jargão não explicado e, ao que parece, sem uso no mercado [fonte?] | Cortar ou explicar |

### 4.5 Afirmações sem fonte (lista para o pesquisador)

1. "modelo Cascata (Waterfall), formalizado por Winston Royce em 1970". Royce descreveu o modelo sequencial *como arriscado* e recomendou iterar; o nome "waterfall" veio depois [fonte?: Royce, *Managing the Development of Large Software Systems*, 1970]. **Reescrever com mais precisão, com crédito ao Waterfall pela clareza.**
2. "Como destacado por Boehm (1988), o custo de correção de um defeito aumenta exponencialmente". A curva de custo costuma ser atribuída a Boehm 1981 (*Software Engineering Economics*); Boehm 1988 é o artigo do modelo espiral. A "curva exponencial" é contestada (ex.: Bossavit, *The Leprechauns of Software Engineering*) [fonte?]. **Corrigir a citação ou suavizar.**
3. "Pressman (2014) também observou que projetos que seguem rigidamente o modelo Waterfall frequentemente falham" [fonte?: edição e página].
4. "o Scrum se destacou como uma das mais adotadas" [fonte?: ex. *State of Agile Report*, Digital.ai].
5. "Schwaber e Sutherland (2020)": correto quanto ao Scrum Guide 2020 [fonte: scrumguides.org], mas o Guide usa *Product Owner*, não "Especialista de Negócio/Produto". Ajustar o termo.
6. "Manifesto Ágil, 2001" [fonte: agilemanifesto.org]. Fácil de citar.
7. "muitas organizações adotaram estruturas com áreas separadas de Produto e Engenharia" [fonte? ou reformular como observação].
8. "O Tech Lead passou a assumir informalmente o papel do analista de sistemas". É a tese do autor; **manter como opinião/observação, não como fato**.
9. Todos os números dos estudos de caso e exemplos (seção 3.2).
10. Prazos de resultado no FAQ (1–3, 3–6, 6+ meses).
11. "Um dia investido em avaliação técnica pode economizar semanas de retrabalho" (citação sem autor).
12. Afirmações novas do eixo IA (DORA 2024, comportamento de agentes) [fonte?], a verificar antes de publicar.

---

## 5. Proposta de valor e diferenciação

### 5.1 Proposta de valor

**Uma frase:**
> Value-First é uma camada leve de valor e alinhamento que transforma a especificação em um contrato de valor, compartilhado entre Produto e Tecnologia, para que times com agentes de IA (ou sem eles) construam a coisa certa, e não só a coisa rápida.

- **Clareza antes de velocidade.** Cada item começa com problema, valor esperado e critério de sucesso mensurável. É a melhor entrada tanto para pessoas quanto para agentes de código.
- **Uma lacuna com dono.** O trabalho que o Tech Lead faz sozinho e sem nome vira responsabilidade explícita de um par Produto + Tecnologia, sem criar cargo novo.
- **Funciona com o que você já usa.** Não substitui Scrum, Kanban nem ferramentas de spec-driven development. Define o *porquê* e o *como saberemos* que esses processos e ferramentas executam.

### 5.2 Diferenciação (com crédito)

| Abordagem | O que faz bem (crédito) | Onde Value-First se encaixa | Relação |
|---|---|---|---|
| **Scrum** [fonte: scrumguides.org] | Cadência, inspeção e adaptação, transparência, time multifuncional, Product Goal | Melhora a *entrada* do Sprint: itens com Value Spec. A verificação de valor complementa a Sprint Review. Não mexe em eventos nem papéis do Scrum | **Complementar** |
| **Kanban** [fonte?: Kanban Guide, prokanban.org / kanban.university] | Fluxo, limite de WIP, políticas explícitas, métricas de fluxo | "Spec pronta" vira política explícita de entrada de uma coluna. A verificação de valor vira uma etapa do fluxo | **Complementar** |
| **Shape Up** (Basecamp) [fonte: basecamp.com/shapeup] | *Shaping* antes de construir, *appetite* (tempo fixo, escopo variável), apostas | É o parente mais próximo; merece crédito explícito. Value-First acrescenta critério de sucesso *mensurável*, spec como entrada para IA, spec viva versionada no repo e verificação depois da entrega. Não prescreve ciclos de 6 semanas | **Alternativa** na parte de *shaping*; **complementar** no resto |
| **SAFe** [fonte?: scaledagileframework.com] | Coordenação em escala, portfólio, alinhamento estratégico | Value-First atua no nível do item e do time. Não trata de escala. Pode alimentar *features/enablers* com Value Specs | **Complementar** (escopo diferente) |
| **Spec-driven development**: GitHub Spec Kit, Kiro, AGENTS.md/CLAUDE.md [fonte?: github.com/github/spec-kit, kiro.dev, agents.md] | Transformar spec em plano, tarefas e código com agentes; padronizar contexto para IA | Value-First fica *acima*: diz o que a spec precisa conter sobre valor e sucesso, quem é dono dela e como verificar depois. As ferramentas cuidam do caminho spec → código | **Complementar** (camada acima) |
| **Specification by Example / BDD** (Gojko Adzic; Dan North) [fonte?] | Exemplos concretos como especificação executável e testável | Os critérios de aceite da Value Spec podem (e devem) ser escritos como exemplos. Crédito explícito | **Complementar**; ideia-mãe a reconhecer |
| **Impact Mapping, JTBD, Lean Startup** [fonte?] | Ligar entregas a objetivos e hipóteses de valor | Técnicas recomendadas para preencher "valor esperado" | **Complementar** (técnicas compatíveis) |

**Frase honesta para o texto público:** "Value-First não inventa a ideia de especificar bem nem de medir valor. Ele junta essas ideias em um conjunto mínimo e as aplica a um problema novo: especificações que agora são executadas por máquinas."

---

## 6. Nova arquitetura de informação (enxuta)

```
README.md                    # EN, ≤120 linhas, leitura em 3 min (decisão do autor: EN ou PT como principal)
README.pt-BR.md              # espelho em PT, mesmo conteúdo
CONTRIBUTING.md              # EN + PT (ou dois arquivos), sem "(DV)"
CONTRIBUTORS.md              # corrigir criador
CHANGELOG.md                 # v1 (Deliver-Value) → v2 (Value-First), o que mudou e por quê
LICENSE                      # MIT; avaliar CC BY 4.0 para o texto (decisão do autor)
.gitattributes               # normalizar finais de linha

docs/
  diagnostico.md             # este documento (interno, só PT)
  en/ | pt/                  # mesmos arquivos, mesmos nomes (nomes em EN nos dois)
    why.md                   # o problema, história com crédito, eixo IA/spec, riscos e limites
    principles.md            # 6 princípios
    practices.md             # 3–5 práticas próprias + "técnicas compatíveis" com crédito
    roles-and-artifacts.md   # par Produto+Tech, time; Value Spec, Canvas
    adoption.md              # começar em 1 semana, sinais observáveis, maturidade (3 níveis), antipadrões, quando não usar
    comparison.md            # tabela da seção 5.2, expandida
    faq.md                   # ≤15 perguntas
    examples.md              # 2–3 exemplos ilustrativos, sem números inventados
    glossary.md
    sources.md               # todas as referências com URL

templates/
  en/ | pt/
    value-spec.md            # artefato central, pronto para copiar
    value-check.md           # registro curto da verificação de valor (ou seção da spec)
    agents-snippet.md        # trecho para AGENTS.md/CLAUDE.md apontando para a Value Spec
  canvas/                    # alignment-canvas.{svg,png} en/pt

assets/
  canvas/                    # imagens do Canvas (vindas de docs/*/canvas) + exemplo preenchido
  diagrams/                  # ciclo Especificar → Validar → Construir → Verificar
  logo/

site/                        # opcional: uma página única (GitHub Pages) que espelha o README
```

**Mapeamento do conteúdo atual:**
- `README.md` / `translations/README.en.md` → `README*.md` + `docs/*/why.md`
- `principles.md` → `principles.md` + `roles-and-artifacts.md`
- `practices.md` → `practices.md` (3–5 práticas) + seção "técnicas compatíveis"; o resto sai **[remoção: requer aprovação do autor]**
- `case-studies.md` → `examples.md` (sem os casos "reais") **[remoção: requer aprovação do autor]**
- `templates.md` → `templates/`
- `faq.md` → `faq.md` enxuto
- `translations/` → deixa de existir **[remoção: requer aprovação do autor]**

---

## 7. Modelo núcleo v2 (rascunho)

### 7.1 Princípios inegociáveis (6)

1. **Valor explícito antes do trabalho.** *(substitui "Valor sobre Prazo")*
   Todo item relevante começa dizendo qual problema resolve, que valor espera gerar e como vamos saber se gerou. Prazo e escopo continuam importando; eles servem ao valor, não o contrário.

2. **A especificação é um contrato de valor, e ela vive.** *(substitui "Tradução Eficiente")*
   A spec não é um documento que se entrega e esquece. É um acordo curto sobre problema, valor, critérios de sucesso e restrições. Ela fica versionada junto com o código e muda quando o código ou o feedback ensinam algo novo. Com agentes de IA, ela é também a entrada de execução: o que não está escrito, o agente supõe.

3. **Validar antes de construir.** *(substitui "Avaliação Técnica Preliminar")*
   Antes de assumir compromisso, reduzir a maior incerteza pelo meio mais barato: conversa, spike técnico, protótipo (inclusive gerado por IA, descartável por padrão). O protótipo pode fazer parte da spec.

4. **Produto e Tecnologia especificam juntos.** *(substitui o "Analista de Valor")*
   A spec tem dois donos: Produto responde pelo problema e pelo valor; o Tech Lead responde pela viabilidade, pelas restrições e por a spec ser executável. O trabalho que o Tech Lead já faz sem nome passa a ser explícito, e ele não o carrega sozinho.

5. **Mudar o plano é informação, não falha.** *(substitui "Renegociação Formal" e "Transparência Contínua")*
   O que é fixo e o que é flexível fica combinado desde o início. Quando a realidade muda, a mudança vai para a spec, com motivo, e todos ficam sabendo. Sem contrato e sem comitê: registro leve e visível.

6. **Pessoas respondem pelo resultado; a IA acelera.** *(novo)*
   Agentes ajudam a especificar, prototipar e construir. Decisões, revisão de código, segurança e dívida técnica continuam sendo responsabilidade de pessoas. Mede-se o resultado (outcome), não a quantidade de código ou tarefas (output).

### 7.2 Práticas próprias (4 núcleo + 1 opcional)

1. **Escrever a Value Spec em par.** Produto e Tech Lead escrevem juntos, em até 1 página, uma Value Spec por item relevante. Em 30–60 minutos [sugestão, não dado]. O time revisa.
2. **Checagem de prontidão da spec.** Antes de construir (por pessoas ou agentes), a spec responde cinco perguntas: *Qual problema? Para quem? Que valor esperamos? Como vamos medir? O que é fixo e o que é flexível?* Se alguma fica sem resposta, ainda não está pronta. *(Funciona como política de entrada no Kanban ou como critério de refinamento no Scrum.)*
3. **Protótipo como pergunta.** Para itens de alta incerteza, um protótipo barato (frequentemente gerado com IA) responde *uma* pergunta de valor ou de viabilidade antes do compromisso. O código do protótipo é descartável por padrão; a decisão tomada vai para a spec.
4. **Verificação de valor.** Depois da entrega, comparar o resultado com os critérios de sucesso da spec, na data combinada nela. Registrar o que se aprendeu, atualizar a spec e o backlog. Fecha o ciclo.
5. *(Opcional, para iniciativas maiores)* **Sessão do Canvas de Alinhamento.** Kickoff com o Canvas Valor-Tecnologia atual para alinhar perspectivas antes de quebrar em Value Specs.

**Ciclo por item:** Especificar → Validar → Construir → Verificar valor (e voltar à spec). Ele roda dentro da cadência que o time já usa.

### 7.3 Papéis — decisão: **o Analista de Valor deixa de ser cargo**

**Decisão:** eliminar o "Analista de Valor" como papel separado. "Valor + spec" vira **responsabilidade compartilhada do Par de Valor (Produto + Tech Lead)**. "Analista de valor" sobrevive só como *chapéu*: uma habilidade de facilitação que qualquer pessoa pode usar (por exemplo, um analista de negócio numa empresa grande), nunca uma etapa obrigatória no fluxo.

**Justificativa:**
- Um terceiro papel entre Produto e Tech cria um repasse a mais, que é exatamente a perda de contexto que o modelo quer evitar. Com IA isso piora: cada repasse é mais uma chance de a spec perder informação antes de virar código.
- O próprio FAQ v1 precisa defender o papel contra burocracia e gargalo, sinal de que ele é um ponto fraco.
- Adotar fica mais fácil: no Scrum, o par é Product Owner + um Developer com papel de Tech Lead. Não é preciso contratar ninguém nem mudar organograma.
- É mais fiel à tese original: quem já faz a tradução é o Tech Lead. A ideia é dar nome e parceria a esse trabalho, não transferi-lo.

| Papel | Responsabilidade no Value-First |
|---|---|
| **Produto** (PO/PM) | Dono do problema, do valor esperado e dos critérios de sucesso; conduz a verificação de valor |
| **Tech Lead** | Dono da viabilidade, das restrições, dos requisitos não funcionais e de a spec ser executável (por pessoas e agentes); "engenharia de especificação" |
| **Time de desenvolvimento** | Revisa e questiona a spec; constrói; faz **revisão humana de todo código gerado por IA**; avisa quando a realidade diverge da spec |
| **Stakeholders** | Validam valor (protótipo, verificação); sabem o que é fixo e o que é flexível |

### 7.4 Artefatos

1. **Value Spec (artefato central).** Markdown, ≤1 página, no repositório, ao lado do código. Seções:
   - Problema e para quem
   - Valor esperado (hipótese)
   - Critérios de sucesso mensuráveis: métrica, alvo, quando medir
   - Escopo / fora do escopo
   - Restrições técnicas e requisitos não funcionais (absorve o "Mapa de Complexidade Técnica")
   - Riscos e premissas; perguntas em aberto
   - **Fixo vs. flexível e gatilhos de revisão** (absorve o "Contrato de Flexibilidade")
   - Exemplos / critérios de aceite (estilo Specification by Example)
   - Decisões (links para ADRs) e histórico de mudanças
   - Donos: Produto + Tech Lead
   - Resultado da verificação de valor (preenchido depois)
2. **Canvas de Alinhamento Valor-Tecnologia** (mantido, para iniciativas). O ideal é revisar os rótulos para usar os termos v2 (decisão de design; os arquivos atuais ficam).
3. **Trecho para AGENTS.md / CLAUDE.md** (modelo): instrui agentes a ler a Value Spec antes de agir e a perguntar quando faltar critério.
4. *(Opcional)* **Visão de priorização** entre specs: o que sobra da Matriz de Valor, como tabela simples.

### 7.5 Sinais observáveis (como saber se um time pratica Value-First)

**Sinais positivos:**
- Todo item em andamento aponta para uma Value Spec com pelo menos **um critério de sucesso mensurável**.
- Toda Value Spec tem **dois donos nomeados** (Produto + Tech).
- As specs estão **versionadas no repositório** e são **referenciadas pelas instruções dos agentes**.
- Itens de alta incerteza têm um **protótipo ou spike registrado antes** do compromisso.
- Mudança de escopo ou prazo aparece como **mudança na spec, com motivo**, e não como "atraso" descoberto na reunião de status.
- **Verificações de valor acontecem** e ficam registradas. O time sabe dizer quais entregas *não* geraram o valor esperado.
- **Todo código gerado por IA passa por revisão humana.** Métricas de estabilidade (ex.: taxa de falha de mudanças, DORA [fonte?: dora.dev]) são acompanhadas para equilibrar a velocidade.

**Antissinais:**
- Spec com mais de uma página que ninguém atualiza.
- "Valor" escrito como "melhorar a experiência" sem métrica.
- Tech Lead escrevendo a spec sozinho, de novo.
- A Value Spec virou mais um formulário de aprovação.

**Métrica-hipótese** (para o autor validar com uso real, sem prometer): proporção de retrabalho atribuído a ambiguidade de spec.

---

## Colisão de nome

**Veredito: risco baixo-médio. Manter "Value-First Development", sempre com o nome completo na primeira menção; "Value-First" (com hífen) como forma curta.** Detalhes e fontes em [research/name-collision.md](research/name-collision.md).

- **Nome exato livre:** nenhuma metodologia, livro ou produto chamado "Value-First Development" foi encontrado; busca de repositórios no GitHub retorna 0 resultados.
- **Colisão principal é "ValueFirst" (uma palavra):** empresa de mensageria da Tanla (Índia), ativa em vfirst.com; `valuefirst.com` é de uma consultoria suíça; os handles `ValueFirst` e `Value-first` no GitHub estão ocupados (sem repositórios públicos). Evitar "ValueFirst" como marca.
- **Usos menores:** uma empresa sul-africana anuncia uma "Value-First Engineering Approach"; um white paper antigo "Putting Value First" (não confirmado).
- **Domínios:** `valuefirstdevelopment.com` e `value-first.dev` aparentam estar livres (RDAP "not found"); `valuefirst.dev` foi registrado em 2026-08-23 por titular desconhecido.
- **Não verificado:** marcas registradas (USPTO, EUIPO, INPI-BR) — fazer antes de qualquer uso comercial.
- **Nomes reserva:** Spec-to-Value (sem colisão encontrada), ValueSpec (risco baixo-médio), Value Loop (risco médio).

---

## Decisões pendentes para o autor

1. Autorizar as remoções marcadas (Analista de Valor como cargo, estudos de caso "reais", comitê/acordos, catálogo de práticas, pasta `translations/`).
2. README principal em EN ou PT (recomendação: EN no `README.md` + `README.pt-BR.md`, pelo alcance; PT e EN com o mesmo conteúdo).
3. Termo único: "abordagem", "modelo", "framework" ou "metodologia".
4. Licença do texto: manter MIT ou adotar CC BY 4.0 para a documentação.
5. Existe evidência publicável de algum dos casos? Se sim, reescrever com fonte. Se não, sai.
