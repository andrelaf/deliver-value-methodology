"""Build the Value-First landing page (static, EN + PT).

Run:     python site/build.py
Preview: python -m http.server 8000 -d site   →  http://localhost:8000/

Writes site/index.html (EN), site/pt/index.html (PT) and copies brand assets,
diagrams and the canvas into site/assets/. Small inline JS only as progressive enhancement (Value Map demo and fillable map); no build tools.
"""
import json
import shutil
from html import escape
from pathlib import Path

SITE = Path(__file__).parent
ROOT = SITE.parent
REPO = "https://github.com/andrelaf/value-first"
BLOB = f"{REPO}/blob/main"


def copy_assets():
    out = SITE / "assets"
    out.mkdir(exist_ok=True)
    for name in ["tokens.css", "favicon.svg", "logo-horizontal.svg", "logo-horizontal-dark.svg", "logo-icon.svg"]:
        shutil.copy(ROOT / "assets/brand" / name, out / name)
    shutil.copy(ROOT / "assets/brand/social-card.svg", out / "social-card.svg")
    for f in (ROOT / "assets/diagrams").glob("*.svg"):
        shutil.copy(f, out / f.name)


T = {
    "en": {
        "lang": "en", "other": "pt", "other_label": "Português", "other_href": "pt/", "base": "",
        "title": "Value-First Development",
        "meta": "Make the value of each piece of work explicit, shared and measurable before anyone builds it, so people and coding agents build the right thing.",
        "skip": "Skip to content",
        "nav": [("#problem", "Problem"), ("#idea", "The idea"), ("#principles", "Principles"), ("#ai", "Specs and AI"), ("#check", "Checklist"), ("#map", "Value Map")],
        "tagline": "From ritual to value, from spec to software.",
        "thesis": "Value-First Development makes the value of each piece of work explicit, shared and measurable before anyone builds it, so that people and coding agents build the right thing, not only build it fast.",
        "cta1": "Get the Value Spec template", "cta1_href": f"{BLOB}/templates/en/value-spec.md",
        "cta2": "Read the docs on GitHub", "cta2_href": f"{BLOB}/README.md",
        "hero_note": "A light layer on top of Scrum, Kanban or your own process. Open source, MIT.",
        "problem_h": "The gap between spec and development",
        "problem_p": [
            "Every way of working we use today answered a real problem. Writing things down gave us clarity, Agile gave us short feedback loops and Scrum gave us a steady cadence. Value-First keeps all of that.",
            "In many teams, though, the ceremonies stay while the purpose fades. Stories describe <em>what</em>, rarely <em>why</em>, and almost never the constraints or how success will be measured.",
            "Someone fills that gap, and it's usually the Tech Lead: translating, completing and deciding, mostly unseen. It works, but the work stays invisible, depends on one person and happens late.",
        ],
        "gap_alt": "The gap: a story says only what to build, while building also needs the why, the value and metric, constraints, edge cases and what is fixed or flexible.",
        "idea_h": "The idea",
        "idea_lead": "One short, living document per item of value, written by Product and the Tech Lead together.",
        "idea": [
            ("Value Spec", "One page: problem, expected value, measurable success criteria, constraints, what's fixed and what's flexible. Versioned next to the code and readable by people and agents."),
            ("Value Pair", "Product owns the problem and the value. The Tech Lead owns feasibility and makes the spec buildable. The translation work gets a name and a partner."),
            ("The cycle", "Specify, validate, build, check value, then back to the spec. It runs inside the cadence you already have."),
        ],
        "cycle_alt": "The Value-First cycle: Specify, Validate, Build, Check value, around a living Value Spec.",
        "principles_h": "Six principles",
        "principles": [
            ("Value is explicit before the work starts", "Problem, value and how we'll know, stated up front. Deadlines and scope serve the value."),
            ("The spec is a value contract, and it lives", "Short, versioned with the code, changed with a reason. For agents, it's executable input."),
            ("Validate before you build", "Reduce the biggest uncertainty the cheapest way. Prototypes are evidence, not deliverables."),
            ("Product and Tech specify together", "Two owners per spec. The Tech Lead's translation work becomes explicit and shared."),
            ("A changed plan is information, not failure", "Fixed and flexible are agreed up front. Changes go into the spec, visibly."),
            ("People own the outcome; AI speeds it up", "Decisions, review, security and technical debt stay with people. Measure outcomes, not output."),
        ],
        "principles_more": "Read the principles",
        "ai_h": "Specs in the AI era",
        "ai_lead": "Coding agents read specs and act on them. That turns the gap from a nuisance into a bottleneck.",
        "ai_points": [
            ("The spec became executable input", "A person interprets a vague story. An agent executes it and guesses the rest. Models are “exceptional at pattern completion, but not at mind reading” (<a href=\"https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/\">GitHub, 2025</a>)."),
            ("AI amplifies the system it lands in", "DORA's 2025 research calls AI an amplifier and finds that, without a user-centric focus, adopting it can hurt team performance (<a href=\"https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report\">DORA 2025</a>)."),
            ("The Tech Lead as specification engineer", "The translation work becomes central. Value-First shares it with Product instead of leaving it to one person."),
            ("A layer above the tools", "Spec Kit, Kiro and AGENTS.md handle spec to code. Value-First decides what is worth building and how we'll know it worked."),
        ],
        "ai_limits": "<strong>Limits, stated plainly.</strong> Productivity gains aren't guaranteed, AI code needs human review, and heavy upfront specs can bring back waterfall. Value-First answers with small, value-scoped, living specs.",
        "ai_more": "Read the full argument and sources",
        "ba_alt": "Before and now. Before: the Tech Lead informally fills a gap between story and developers. Now: the Value Pair writes a Value Spec, validates it with a prototype, and it becomes executable input for tools and agents, with a value check that updates the spec.",
        "layers_alt": "Value-First sits above how the team works (Scrum, Kanban, Shape Up) and how the spec becomes code (Spec Kit, Kiro, agents).",
        "check_h": "You're Value-First if…",
        "check_lead": "Signals you can see in the work, not statements of intent.",
        "check": [
            "Every relevant item in progress has a Value Spec with at least one measurable success criterion.",
            "Every spec has two named owners: Product and Tech Lead.",
            "Specs live in the repo, and your agent instructions point to them.",
            "Risky items get a prototype or spike before the commitment.",
            "Scope and date changes show up as spec changes, with a reason.",
            "You check value after delivery and can name what didn't work.",
            "People review all AI-generated code, and stability is tracked alongside speed.",
        ],
        "check_more": "Checklist and maturity model",
        "map_h": "Value Map",
        "map_lead": "For initiatives bigger than one spec. Like C4 does for architecture: levels of zoom, four rules, and you can draw it on a whiteboard.",
        "map_layers": "The map says what we bet on. The spec says what we agree to build. The tools say how to build it.",
        "map_levels": [("1", "Outcome", "Why, and how will we know?"), ("2", "Slices", "What first, and what are we betting on?"), ("3", "Value Spec", "What do we agree to build in this slice?")],
        "map_example": "Fictional example, based on the VS-014 template example.",
        "map_up": "contribute to",
        "map_zoom": "zoom into VS-014 = open its Value Spec",
        "map_spec": ("VS-014 · Download invoices in the portal", "Problem, success criteria SC-1 to SC-4, constraints, decisions and agent instructions. It lives in the repository, not on the map.", "See the example spec"),
        "map_outcome": ("Outcome", "Customers get their invoices on their own", "Billing contacts ask support for invoices.", "Invoice tickets: ~120 → ≤ 40 / week, 6 weeks after launch", "Out: payments, invoice editing"),
        "map_slices": [
            ("VS-014", "Download invoices in the portal", "Bet: customers use the portal instead of emailing support (validated 5/6)", "In build"),
            ("VS-015", "Filter invoices by date", "Bet: audits need date ranges (2 of 6 asked)", "Next"),
            ("VS-016", "Monthly invoice by email", "Bet: receiving beats searching (not validated)", "Maybe"),
        ],
        "map_rules_h": "Four rules",
        "map_rules": ["Every box has a type, a name and one sentence.", "Every outcome and slice has a metric or a signal.", "Every arrow has a verb.", "One drawing per level. Zoom in only where you need to."],
        "map_code": "The map draws levels 1 and 2. Level 3 is the Value Spec, and level 4, code, isn't drawn: tests and PRs cite the spec's SC IDs.",
        "map_blank": "Fill in your own map",
        "map_more": "How to run a Value Map session",
        "demo_label": "How to fill it in",
        "demo_ui": {"step": "Step {n} of {t}", "play": "Play", "pause_l": "Pause", "restart": "Watch again", "prev": "Previous step", "next": "Next step"},
        "demo_hints": [
            "Start at the top. Write the change you want to see, from the user's point of view. Not the name of a feature.",
            "One sentence: who has the problem today, and what it is. Data helps.",
            "One metric, with a baseline, a target and a date. If you can't agree on it, you probably have two initiatives.",
            "Say what's out. It stops the initiative from growing without anyone noticing.",
            "Now the slices. Each one should move the metric on its own. Start with the one that teaches you fastest, and write its riskiest bet.",
            "The next slice can be a smaller bet with partial evidence. Say how many people asked for it.",
            "“Not validated” is an honest answer. It shows the team where the risk is before anyone builds.",
            "To zoom into a slice, open its Value Spec. Criteria, constraints and decisions live there, not on the map. That keeps the map a list of bets, not a requirements document.",
            "Done. Each slice becomes a Value Spec. After each value check, update the status and the order of the slices.",
        ],
        "blank_hints_outcome": ["The change you want, not a feature. E.g. Customers get their invoices on their own", "Who has the problem today, and what it is", "E.g. invoice tickets ~120 → ≤ 40 / week, 6 weeks after launch", "What this initiative won't do"],
        "blank_hints_slice": ["VS-___ · what this slice delivers", "Why this slice, on its own, moves the metric", "What must be true? How do we check it cheaply?", "idea · next · in build · delivered · not delivered"],
        "blank_ui": {"print": "Print", "md": "Download Markdown", "clear": "Clear", "clear2": "Click again to clear", "title_ph": "initiative", "md_title": "Value Map", "md_l1": "Level 1 · Outcome", "md_l2": "Level 2 · Slices", "md_order": "Order", "file": "value-map.md"},
        "blank_title": "Value Map (blank)",
        "blank_slice": "Slice",
        "blank_fields_outcome": ["Name", "Problem and for whom", "Metric: baseline → target, by when", "Out of scope"],
        "blank_fields_slice": ["Value Spec · Delivers", "How it moves the metric", "Riskiest bet (value or tech)", "Status"],
        "blank_print": "Fill it in here or print it blank (landscape). Drafts are saved in this browser only. Level 3 lives in each Value Spec.",
        "blank_back": "Back to Value-First",
        "cta_h": "Try it on one item this week",
        "cta_steps": ["Pick one upcoming item with real value and some uncertainty.", "Write a Value Spec as a pair. Keep it to a page.", "Validate the riskiest assumption with the cheapest prototype.", "Build, then check the value on the date you set."],
        "cta_contrib": "Share what happened, critique it or contribute",
        "footer": "Value-First Development, formerly Deliver-Value Framework. Created by André Lara Amorim. MIT License.",
        "sources": "Sources",
        "docs_base": f"{BLOB}/docs/en",
    },
    "pt": {
        "lang": "pt-BR", "other": "en", "other_label": "English", "other_href": "../", "base": "../",
        "title": "Value-First Development",
        "meta": "Torne explícito, compartilhado e mensurável o valor de cada trabalho antes de construí-lo, para que pessoas e agentes de código construam a coisa certa.",
        "skip": "Pular para o conteúdo",
        "nav": [("#problem", "Problema"), ("#idea", "A ideia"), ("#principles", "Princípios"), ("#ai", "Specs e IA"), ("#check", "Checklist"), ("#map", "Mapa de Valor")],
        "tagline": "Do ritual ao valor, da spec ao software.",
        "thesis": "O Value-First Development torna explícito, compartilhado e mensurável o valor de cada trabalho antes que alguém o construa, para que pessoas e agentes de código construam a coisa certa, e não só construam rápido.",
        "cta1": "Pegar o template de Value Spec", "cta1_href": f"{BLOB}/templates/pt/value-spec.md",
        "cta2": "Ler a documentação no GitHub", "cta2_href": f"{BLOB}/README.pt-BR.md",
        "hero_note": "Uma camada leve sobre Scrum, Kanban ou o seu próprio processo. Código aberto, MIT.",
        "problem_h": "O abismo entre a spec e o desenvolvimento",
        "problem_p": [
            "Cada forma de trabalhar que usamos hoje respondeu a um problema real. Escrever antes nos deu clareza, o Agile nos deu ciclos curtos de feedback e o Scrum, uma cadência estável. O Value-First mantém tudo isso.",
            "Em muitos times, porém, as cerimônias continuam e o propósito se perde. As histórias descrevem <em>o quê</em>, raramente o <em>porquê</em>, e quase nunca as restrições ou como o sucesso será medido.",
            "Alguém preenche esse abismo, e geralmente é o Tech Lead: traduzindo, completando e decidindo, quase sempre sem que ninguém veja. Funciona, mas o trabalho fica invisível, depende de uma pessoa e acontece tarde.",
        ],
        "gap_alt": "O abismo: a história diz só o que construir, mas construir exige também o porquê, o valor e a métrica, restrições, casos de borda e o que é fixo ou flexível.",
        "idea_h": "A ideia",
        "idea_lead": "Um documento curto e vivo por item de valor, escrito por Produto e Tech Lead juntos.",
        "idea": [
            ("Value Spec", "Uma página: problema, valor esperado, critérios de sucesso mensuráveis, restrições, o que é fixo e o que é flexível. Versionada junto com o código e legível por pessoas e agentes."),
            ("Par de Valor", "Produto responde pelo problema e pelo valor. O Tech Lead responde pela viabilidade e por tornar a spec construível. O trabalho de tradução ganha nome e parceiro."),
            ("O ciclo", "Especificar, validar, construir, verificar o valor e voltar à spec. Roda dentro da cadência que você já tem."),
        ],
        "cycle_alt": "O ciclo do Value-First: Especificar, Validar, Construir, Verificar valor, em torno de uma Value Spec viva.",
        "principles_h": "Seis princípios",
        "principles": [
            ("O valor fica explícito antes do trabalho", "Problema, valor e como saberemos, ditos desde o início. Prazo e escopo servem ao valor."),
            ("A spec é um contrato de valor, e ela vive", "Curta, versionada com o código, alterada com motivo. Para agentes, é insumo executável."),
            ("Validar antes de construir", "Reduzir a maior incerteza pelo meio mais barato. Protótipos são evidência, não entrega."),
            ("Produto e Tecnologia especificam juntos", "Dois donos por spec. O trabalho de tradução do Tech Lead fica explícito e compartilhado."),
            ("Mudar o plano é informação, não falha", "Fixo e flexível são combinados no início. Mudanças entram na spec, à vista de todos."),
            ("Pessoas respondem pelo resultado; a IA acelera", "Decisões, revisão, segurança e dívida técnica continuam com pessoas. Mede-se resultado, não volume."),
        ],
        "principles_more": "Ler os princípios",
        "ai_h": "Specs na era da IA",
        "ai_lead": "Agentes de código leem specs e agem a partir delas. Isso transforma o abismo de incômodo em gargalo.",
        "ai_points": [
            ("A spec virou insumo executável", "Uma pessoa interpreta uma história vaga. Um agente a executa e supõe o resto. Os modelos são “excepcionais em completar padrões, mas não em ler mentes” (<a href=\"https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/\">GitHub, 2025</a>)."),
            ("A IA amplifica o sistema em que entra", "A pesquisa DORA de 2025 descreve a IA como amplificador e conclui que, sem foco no usuário, adotá-la pode prejudicar o desempenho do time (<a href=\"https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report\">DORA 2025</a>)."),
            ("O Tech Lead como engenheiro de especificação", "O trabalho de tradução passa a ser central. O Value-First o divide com Produto em vez de deixá-lo com uma pessoa só."),
            ("Uma camada acima das ferramentas", "Spec Kit, Kiro e AGENTS.md cuidam do caminho da spec ao código. O Value-First decide o que vale construir e como saberemos que funcionou."),
        ],
        "ai_limits": "<strong>Limites, sem rodeios.</strong> Ganho de produtividade não é garantido, código gerado por IA precisa de revisão humana, e specs pesadas feitas antes de tudo podem trazer o waterfall de volta. O Value-First responde com specs pequenas, focadas em valor e vivas.",
        "ai_more": "Ler o argumento completo e as fontes",
        "ba_alt": "Antes e agora. Antes: o Tech Lead preenche informalmente o abismo entre a história e os desenvolvedores. Agora: o Par de Valor escreve uma Value Spec, valida com um protótipo, e ela vira insumo executável para ferramentas e agentes, com uma verificação de valor que atualiza a spec.",
        "layers_alt": "O Value-First fica acima de como o time trabalha (Scrum, Kanban, Shape Up) e de como a spec vira código (Spec Kit, Kiro, agentes).",
        "check_h": "Você é Value-First se…",
        "check_lead": "Sinais que dá para ver no trabalho, não declarações de intenção.",
        "check": [
            "Todo item relevante em andamento tem uma Value Spec com pelo menos um critério de sucesso mensurável.",
            "Toda spec tem dois donos nomeados: Produto e Tech Lead.",
            "As specs ficam no repositório, e as instruções dos seus agentes apontam para elas.",
            "Itens arriscados ganham um protótipo ou spike antes do compromisso.",
            "Mudanças de escopo e de prazo aparecem como mudanças na spec, com motivo.",
            "Vocês verificam o valor depois da entrega e sabem dizer o que não funcionou.",
            "Pessoas revisam todo código gerado por IA, e a estabilidade é acompanhada junto com a velocidade.",
        ],
        "check_more": "Checklist e modelo de maturidade",
        "map_h": "Mapa de Valor",
        "map_lead": "Para iniciativas maiores que uma spec. Como o C4 faz com a arquitetura: níveis de zoom, quatro regras, e dá para desenhar no quadro branco.",
        "map_layers": "O mapa diz em que apostamos. A spec diz o que combinamos construir. As ferramentas dizem como construir.",
        "map_levels": [("1", "Resultado", "Por quê, e como saberemos?"), ("2", "Fatias", "O que primeiro, e em que apostamos?"), ("3", "Value Spec", "O que combinamos construir nesta fatia?")],
        "map_example": "Exemplo fictício, baseado no exemplo de template da VS-014.",
        "map_up": "contribuem para",
        "map_zoom": "zoom na VS-014 = abrir a Value Spec dela",
        "map_spec": ("VS-014 · Baixar faturas no portal", "Problema, critérios de sucesso SC-1 a SC-4, restrições, decisões e instruções para agentes. Fica no repositório, não no mapa.", "Ver a spec de exemplo"),
        "map_outcome": ("Resultado", "Clientes obtêm as próprias faturas", "Contatos financeiros pedem faturas ao suporte.", "Tickets de fatura: ~120 → ≤ 40 / semana, 6 semanas após o lançamento", "Fora: pagamento, edição de faturas"),
        "map_slices": [
            ("VS-014", "Baixar faturas no portal", "Aposta: clientes usam o portal em vez de mandar e-mail ao suporte (validada 5/6)", "Em construção"),
            ("VS-015", "Filtrar faturas por data", "Aposta: auditorias precisam de intervalos de datas (2 de 6 pediram)", "Próxima"),
            ("VS-016", "Fatura mensal por e-mail", "Aposta: receber é melhor que procurar (não validada)", "Talvez"),
        ],
        "map_rules_h": "Quatro regras",
        "map_rules": ["Toda caixa tem tipo, nome e uma frase.", "Todo resultado e toda fatia têm uma métrica ou um sinal.", "Toda seta tem um verbo.", "Um desenho por nível. Aproxime só onde precisar."],
        "map_code": "O mapa desenha os níveis 1 e 2. O nível 3 é a Value Spec, e o nível 4, código, não se desenha: testes e PRs citam os IDs dos SC da spec.",
        "map_blank": "Preencher o seu mapa",
        "map_more": "Como conduzir uma sessão de Mapa de Valor",
        "demo_label": "Como preencher",
        "demo_ui": {"step": "Passo {n} de {t}", "play": "Continuar", "pause_l": "Pausar", "restart": "Ver de novo", "prev": "Passo anterior", "next": "Próximo passo"},
        "demo_hints": [
            "Comece pelo topo. Escreva a mudança que vocês querem ver, do ponto de vista de quem usa. Não é o nome de uma feature.",
            "Uma frase: quem tem o problema hoje, e qual é. Se houver dado, melhor.",
            "Uma métrica só, com linha de base, meta e prazo. Se não houver acordo sobre ela, provavelmente são duas iniciativas.",
            "Diga o que fica de fora. É o que impede a iniciativa de crescer sem ninguém perceber.",
            "Agora as fatias. Cada uma deve conseguir mover a métrica sozinha. Comece pela que ensina mais rápido e escreva a aposta mais arriscada dela.",
            "A próxima fatia pode ser uma aposta menor, com evidência parcial. Diga quantas pessoas pediram.",
            "“Não validada” é uma resposta honesta. Mostra ao time onde está o risco antes de alguém construir.",
            "Para dar zoom numa fatia, abra a Value Spec dela. Critérios, restrições e decisões ficam lá, não no mapa. Assim o mapa continua sendo uma lista de apostas, não um documento de requisitos.",
            "Pronto. Cada fatia vira uma Value Spec. Depois de cada verificação de valor, atualize o status e a ordem das fatias.",
        ],
        "blank_hints_outcome": ["A mudança que vocês querem, não uma feature. Ex.: Clientes obtêm as próprias faturas", "Quem tem o problema hoje, e qual é", "Ex.: tickets de fatura ~120 → ≤ 40 / semana, 6 semanas após o lançamento", "O que esta iniciativa não vai fazer"],
        "blank_hints_slice": ["VS-___ · o que esta fatia entrega", "Por que esta fatia, sozinha, move a métrica", "O que precisa ser verdade? Como checar barato?", "ideia · próxima · em construção · entregue · não entregue"],
        "blank_ui": {"print": "Imprimir", "md": "Baixar Markdown", "clear": "Limpar", "clear2": "Clique de novo para limpar", "title_ph": "iniciativa", "md_title": "Mapa de Valor", "md_l1": "Nível 1 · Resultado", "md_l2": "Nível 2 · Fatias", "md_order": "Ordem", "file": "mapa-de-valor.md"},
        "blank_title": "Mapa de Valor (em branco)",
        "blank_slice": "Fatia",
        "blank_fields_outcome": ["Nome", "Problema e para quem", "Métrica: linha de base → meta, até quando", "Fora do escopo"],
        "blank_fields_slice": ["Value Spec · Entrega", "Como move a métrica", "Aposta mais arriscada (valor ou técnica)", "Status"],
        "blank_print": "Preencha aqui ou imprima em branco (paisagem). O rascunho fica salvo só neste navegador. O nível 3 fica em cada Value Spec.",
        "blank_back": "Voltar ao Value-First",
        "cta_h": "Experimente em um item nesta semana",
        "cta_steps": ["Escolha um item próximo com valor real e alguma incerteza.", "Escreva uma Value Spec em par. Uma página basta.", "Valide a premissa mais arriscada com o protótipo mais barato.", "Construa e verifique o valor na data combinada."],
        "cta_contrib": "Conte o que aconteceu, critique ou contribua",
        "footer": "Value-First Development, antes Deliver-Value Framework. Criado por André Lara Amorim. Licença MIT.",
        "sources": "Fontes",
        "docs_base": f"{BLOB}/docs/pt",
    },
}

CSS = """
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--vf-bg);color:var(--vf-ink);font-family:var(--vf-font-sans);font-size:var(--vf-text-base);line-height:var(--vf-leading-body)}
a{color:var(--vf-primary)}a:hover{color:var(--vf-primary-strong)}
:focus-visible{outline:3px solid var(--vf-accent-mark);outline-offset:2px;border-radius:4px}
.skip{position:absolute;left:-999px;top:8px;background:var(--vf-primary);color:var(--vf-on-primary);padding:8px 12px;border-radius:var(--vf-radius);z-index:10}
.skip:focus{left:16px}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px}
header.top{border-bottom:1px solid var(--vf-border);background:var(--vf-bg);position:sticky;top:0;z-index:5}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:60px}
.brand img{display:block;height:34px;width:auto}
.brand .dark{display:none}
@media (prefers-color-scheme:dark){.brand .light{display:none}.brand .dark{display:block}}
nav ul{display:flex;gap:20px;list-style:none;margin:0;padding:0}
nav a{color:var(--vf-muted);text-decoration:none;font-size:var(--vf-text-sm);font-weight:500}
nav a:hover{color:var(--vf-ink)}
.lang{font-size:var(--vf-text-sm);font-weight:600;text-decoration:none;border:1px solid var(--vf-border);padding:4px 10px;border-radius:999px;white-space:nowrap}
@media (max-width:820px){nav{display:none}}
section{padding:var(--vf-space-16) 0;border-bottom:1px solid var(--vf-border)}
section:nth-of-type(even){background:var(--vf-surface)}
h1,h2,h3{line-height:var(--vf-leading-tight);font-weight:600;margin:0 0 var(--vf-space-4)}
h1{font-size:clamp(1.9rem,4.5vw,var(--vf-text-3xl));letter-spacing:-.01em;max-width:22ch}
h2{font-size:clamp(1.5rem,3vw,var(--vf-text-xl))}
h3{font-size:var(--vf-text-md)}
p{margin:0 0 var(--vf-space-4);max-width:var(--vf-measure)}
.lead{font-size:var(--vf-text-md);color:var(--vf-muted)}
.hero{padding:var(--vf-space-16) 0 var(--vf-space-12)}
.tag{color:var(--vf-accent);font-weight:600;letter-spacing:.02em;margin-bottom:var(--vf-space-4)}
.thesis{font-size:clamp(1.1rem,2.2vw,var(--vf-text-md));max-width:60ch}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin:var(--vf-space-8) 0 var(--vf-space-4)}
.btn{display:inline-block;padding:12px 20px;border-radius:var(--vf-radius);font-weight:600;text-decoration:none;border:2px solid var(--vf-primary)}
.btn.primary{background:var(--vf-primary);color:var(--vf-on-primary)}
.btn.primary:hover{background:var(--vf-primary-strong);border-color:var(--vf-primary-strong);color:var(--vf-on-primary)}
.btn.ghost{color:var(--vf-primary)}
.note{color:var(--vf-muted);font-size:var(--vf-text-sm)}
figure{margin:var(--vf-space-8) 0 0}
figure img{display:block;width:100%;height:auto;border-radius:var(--vf-radius-lg)}
.grid{display:grid;gap:var(--vf-space-6);grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));margin-top:var(--vf-space-8)}
.card{background:var(--vf-bg);border:1px solid var(--vf-border);border-radius:var(--vf-radius-lg);padding:var(--vf-space-6)}
section:nth-of-type(odd) .card{background:var(--vf-surface)}
.card p{margin:0;color:var(--vf-muted)}
.num{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--vf-primary);color:var(--vf-on-primary);font-weight:600;font-size:var(--vf-text-sm);margin-bottom:var(--vf-space-3)}
.two{display:grid;gap:var(--vf-space-8);grid-template-columns:1fr}
@media (min-width:900px){.two{grid-template-columns:1fr 1fr;align-items:center}}
.callout{border-left:4px solid var(--vf-accent-mark);background:var(--vf-bg);padding:var(--vf-space-4) var(--vf-space-6);border-radius:0 var(--vf-radius) var(--vf-radius) 0;margin-top:var(--vf-space-8);max-width:none}
.more{font-weight:600;display:inline-block;margin-top:var(--vf-space-6)}
ul.checks{list-style:none;padding:0;margin:var(--vf-space-6) 0 0;display:grid;gap:12px;max-width:var(--vf-measure)}
ul.checks li{display:grid;grid-template-columns:28px 1fr;gap:12px;align-items:start}
ul.checks li::before{content:"";width:22px;height:22px;margin-top:2px;border-radius:6px;background:var(--vf-primary) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='white' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat}
ol.steps{padding-left:1.4em;max-width:var(--vf-measure)}
ol.steps li{margin-bottom:8px}
.levels{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));margin:var(--vf-space-6) 0 0;padding:0;list-style:none}
.levels li{display:grid;grid-template-columns:30px 1fr;gap:4px 12px}
.levels .num{grid-row:span 2;margin:0}
.levels span:not(.num){color:var(--vf-muted);font-size:var(--vf-text-sm)}
.map{margin-top:var(--vf-space-8);border:1px solid var(--vf-border);border-radius:var(--vf-radius-lg);padding:var(--vf-space-6);background:var(--vf-bg)}
.map .ex{color:var(--vf-muted);font-size:var(--vf-text-sm);font-style:italic;margin-bottom:var(--vf-space-4)}
.lvl{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr))}
.lvl-1{max-width:560px;margin:0 auto}
.lvl-1 .box{grid-column:1/-1}
.box{border:2px solid var(--box,var(--vf-primary));border-radius:var(--vf-radius);padding:12px 14px;background:var(--vf-bg);display:flex;flex-direction:column;gap:4px}
.box .ty{font-size:.72rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--box,var(--vf-primary))}
.box b{font-weight:600;line-height:1.3}
.box p,.box small{margin:0;color:var(--vf-muted);font-size:var(--vf-text-sm);line-height:1.4}
.box .m{color:var(--vf-ink);font-weight:500}
.box .st{align-self:flex-start;margin-top:4px;font-size:.75rem;font-weight:600;border:1px solid var(--vf-border);border-radius:999px;padding:1px 8px;color:var(--vf-muted)}
.box.out{--box:var(--vf-accent)}
.box.slice.on{box-shadow:0 0 0 4px color-mix(in srgb,var(--vf-primary) 18%,transparent)}
.box.spec{--box:var(--vf-muted);border-style:dashed;max-width:560px;margin:0 auto;width:100%}
.box.spec a{font-size:var(--vf-text-sm);font-weight:600}
.verb{display:flex;align-items:center;justify-content:center;gap:8px;margin:10px 0;color:var(--vf-muted);font-size:var(--vf-text-sm);font-style:italic}
.verb::before,.verb::after{content:"";height:1px;width:40px;background:var(--vf-border)}
.zoom{border-top:1px dashed var(--vf-border);margin-top:16px;padding-top:4px}
.guide{position:sticky;top:70px;z-index:2;background:var(--vf-primary);color:var(--vf-on-primary);border-radius:var(--vf-radius);padding:12px 16px;margin-bottom:var(--vf-space-4);box-shadow:0 6px 18px rgba(0,0,0,.12)}
.guide[hidden]{display:none}
.gtop{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.glabel{font-size:.78rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;opacity:.9}
.gbtn{display:flex;gap:6px}
.gbtn button{font:inherit;font-size:var(--vf-text-sm);font-weight:600;color:inherit;background:transparent;border:1px solid currentColor;border-radius:999px;padding:3px 12px;cursor:pointer;min-width:36px}
.gbtn button:hover{background:rgba(255,255,255,.15)}
.ghint{margin:8px 0 0;max-width:none;font-size:var(--vf-text-base);line-height:1.45;min-height:2.9em}
.map.js .fld{display:grid}
.map.js .fld::after{content:attr(data-full);visibility:hidden;grid-area:1/1;white-space:pre-wrap}
.map.js .fld>.t{grid-area:1/1}
.map.js [data-s]:not(.fld){transition:opacity .35s,box-shadow .35s}
.map.js .dim{opacity:.28}
.map.js .box.cur{box-shadow:0 0 0 4px color-mix(in srgb,var(--vf-accent-mark) 55%,transparent)}
.map.js .box.slice.on:not(.cur){box-shadow:none}
.typing>.t::after{content:"";display:inline-block;width:2px;height:1em;margin-left:1px;vertical-align:-.12em;background:var(--vf-ink);animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
@media (prefers-reduced-motion:reduce){.map.js [data-s]{transition:none}.typing>.t::after{animation:none}}
.mapfoot{display:grid;gap:var(--vf-space-8);grid-template-columns:1fr;margin-top:var(--vf-space-8)}
@media (min-width:900px){.mapfoot{grid-template-columns:1fr 1fr}}
.mapfoot ol{padding-left:1.3em;margin:0}.mapfoot li{margin-bottom:6px}
footer{padding:var(--vf-space-8) 0;color:var(--vf-muted);font-size:var(--vf-text-sm)}
footer p{max-width:none}
"""


DEMO_JS = r"""
(function(){
var root=document.querySelector('[data-demo]');if(!root)return;
var cfg=JSON.parse(root.querySelector('script[type="application/json"]').textContent);
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var flds=[].slice.call(root.querySelectorAll('.fld'));
flds.forEach(function(f){f.setAttribute('data-full',f.textContent);f.innerHTML='<span class="t"></span>';});
var parts=[].slice.call(root.querySelectorAll('[data-s]:not(.fld)'));
var guide=root.querySelector('.guide');guide.hidden=false;root.classList.add('js');
var stepEl=guide.querySelector('.gstep'),hint=guide.querySelector('.ghint'),playB=guide.querySelector('.gplay');
var N=cfg.hints.length,cur=1,playing=!reduce,timer=null,token=0;
function txt(f,v){f.firstChild.textContent=v;}
function setBtn(){playB.textContent=(cur===N&&!playing)?cfg.restart:(playing?cfg.pause_l:cfg.play);}
function render(n,mode){
  token++;var my=token;clearTimeout(timer);cur=n;
  stepEl.textContent=cfg.step.replace('{n}',n).replace('{t}',N);hint.textContent=cfg.hints[n-1];
  parts.forEach(function(p){var s=+p.getAttribute('data-s');p.classList.toggle('dim',s>n);p.classList.toggle('cur',s===n&&p.classList.contains('box'));});
  var q=[];
  flds.forEach(function(f){var s=+f.getAttribute('data-s');f.classList.remove('typing');
    if(s<n||(s===n&&mode==='show'))txt(f,f.getAttribute('data-full'));
    else{txt(f,'');if(s===n&&mode==='type')q.push(f);}});
  setBtn();
  if(mode!=='wait')typeAll(q,my);
}
function typeAll(q,my){
  if(my!==token)return;
  if(!q.length){if(playing&&cur<N)timer=setTimeout(function(){render(cur+1,'type');},1800);else if(cur===N){playing=false;setBtn();}return;}
  var f=q[0],full=f.getAttribute('data-full'),i=0;f.classList.add('typing');
  (function tick(){if(my!==token)return;i++;txt(f,full.slice(0,i));
    if(i<full.length)timer=setTimeout(tick,22+Math.random()*45);
    else timer=setTimeout(function(){f.classList.remove('typing');typeAll(q.slice(1),my);},300);})();
}
guide.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var act=b.getAttribute('data-a');
  if(act==='play'){
    if(cur===N&&!playing){playing=true;render(1,reduce?'show':'type');}
    else if(playing){playing=false;render(cur,'show');}
    else{playing=true;render(cur<N?cur+1:cur,reduce?'show':'type');}
  }else if(act==='prev'){playing=false;render(Math.max(1,cur-1),'show');}
  else if(act==='next'){playing=false;render(Math.min(N,cur+1),reduce?'show':'type');}
  setBtn();});
render(1,reduce?'show':'wait');
if(reduce)return;
var go=function(){render(1,'type');};
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){io.disconnect();go();}},{threshold:.35});io.observe(root);}else go();
})();
"""


def page(t):
    b = t["base"]
    a = lambda s: escape(s, quote=True)
    nav = "".join(f'<li><a href="{h}">{escape(l)}</a></li>' for h, l in t["nav"])
    problem = "".join(f"<p>{p}</p>" for p in t["problem_p"])
    idea = "".join(f'<div class="card"><h3>{escape(h)}</h3><p>{escape(p)}</p></div>' for h, p in t["idea"])
    princ = "".join(f'<div class="card"><span class="num" aria-hidden="true">{i}</span><h3>{escape(h)}</h3><p>{escape(p)}</p></div>'
                    for i, (h, p) in enumerate(t["principles"], 1))
    ai = "".join(f'<div class="card"><h3>{escape(h)}</h3><p>{p}</p></div>' for h, p in t["ai_points"])
    checks = "".join(f"<li>{escape(c)}</li>" for c in t["check"])
    steps = "".join(f"<li>{escape(s)}</li>" for s in t["cta_steps"])
    L = "en" if t["lang"] == "en" else "pt"
    d = t["docs_base"]
    o = t["map_outcome"]
    levels = "".join(f'<li><span class="num" aria-hidden="true">{n}</span><b>{escape(h)}</b><span>{escape(q)}</span></li>' for n, h, q in t["map_levels"])
    slices = "".join(
        f'<div class="box slice{" on" if i == 0 else ""}" data-s="{5 + i}"><span class="ty">2 · {vs}</span><b class="fld" data-s="{5 + i}">{escape(n)}</b><p class="fld" data-s="{5 + i}">{escape(bet)}</p><span class="st fld" data-s="{5 + i}">{escape(st)}</span></div>'
        for i, (vs, n, bet, st) in enumerate(t["map_slices"]))
    ms = t["map_spec"]
    crit = (f'<div class="box spec" data-s="8"><span class="ty">3 · Value Spec</span><b class="fld" data-s="8">{escape(ms[0])}</b>'
            f'<p class="fld" data-s="8">{escape(ms[1])}</p><a href="{BLOB}/templates/{L}/value-spec-example.md">{escape(ms[2])} →</a></div>')
    ui = t["demo_ui"]
    demo_cfg = json.dumps({"hints": t["demo_hints"], **ui}, ensure_ascii=False).replace("</", "<\\/")
    rules = "".join(f"<li>{escape(r)}</li>" for r in t["map_rules"])
    url ="https://andrelaf.github.io/value-first/" + ("" if L == "en" else "pt/")
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(t['title'])}</title>
<meta name="description" content="{a(t['meta'])}">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="https://andrelaf.github.io/value-first/">
<link rel="alternate" hreflang="pt-BR" href="https://andrelaf.github.io/value-first/pt/">
<meta property="og:title" content="{a(t['title'])}">
<meta property="og:description" content="{a(t['meta'])}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<link rel="icon" href="{b}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{b}assets/tokens.css">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">{escape(t['skip'])}</a>
<header class="top"><div class="wrap">
<a class="brand" href="#top" aria-label="Value-First Development"><img class="light" src="{b}assets/logo-horizontal.svg" alt="" width="200" height="34"><img class="dark" src="{b}assets/logo-horizontal-dark.svg" alt="" width="200" height="34"></a>
<nav aria-label="{'Sections' if L == 'en' else 'Seções'}"><ul>{nav}</ul></nav>
<a class="lang" href="{t['other_href']}" hreflang="{'pt-BR' if L == 'en' else 'en'}" lang="{'pt-BR' if L == 'en' else 'en'}">{escape(t['other_label'])}</a>
</div></header>
<main id="main">
<section class="hero" id="top"><div class="wrap">
<p class="tag">{escape(t['tagline'])}</p>
<h1>Value-First Development</h1>
<p class="thesis">{escape(t['thesis'])}</p>
<div class="ctas"><a class="btn primary" href="{t['cta1_href']}">{escape(t['cta1'])}</a><a class="btn ghost" href="{t['cta2_href']}">{escape(t['cta2'])}</a></div>
<p class="note">{escape(t['hero_note'])}</p>
</div></section>

<section id="problem" aria-labelledby="problem-h"><div class="wrap">
<h2 id="problem-h">{escape(t['problem_h'])}</h2>
{problem}
<figure><img src="{b}assets/gap-{L}.svg" alt="{a(t['gap_alt'])}" width="940" height="500" loading="lazy"></figure>
</div></section>

<section id="idea" aria-labelledby="idea-h"><div class="wrap">
<div class="two"><div>
<h2 id="idea-h">{escape(t['idea_h'])}</h2>
<p class="lead">{escape(t['idea_lead'])}</p>
</div>
<figure style="margin:0"><img src="{b}assets/cycle-{L}.svg" alt="{a(t['cycle_alt'])}" width="760" height="580" loading="lazy"></figure></div>
<div class="grid">{idea}</div>
</div></section>

<section id="principles" aria-labelledby="principles-h"><div class="wrap">
<h2 id="principles-h">{escape(t['principles_h'])}</h2>
<div class="grid">{princ}</div>
<a class="more" href="{d}/principles.md">{escape(t['principles_more'])} →</a>
</div></section>

<section id="ai" aria-labelledby="ai-h"><div class="wrap">
<h2 id="ai-h">{escape(t['ai_h'])}</h2>
<p class="lead">{escape(t['ai_lead'])}</p>
<figure><img src="{b}assets/before-after-{L}.svg" alt="{a(t['ba_alt'])}" width="1200" height="860" loading="lazy"></figure>
<div class="grid">{ai}</div>
<figure><img src="{b}assets/comparison-{L}.svg" alt="{a(t['layers_alt'])}" width="940" height="520" loading="lazy"></figure>
<p class="callout">{t['ai_limits']}</p>
<a class="more" href="{d}/ai-and-specs.md">{escape(t['ai_more'])} →</a>
</div></section>

<section id="check" aria-labelledby="check-h"><div class="wrap">
<h2 id="check-h">{escape(t['check_h'])}</h2>
<p class="lead">{escape(t['check_lead'])}</p>
<ul class="checks">{checks}</ul>
<a class="more" href="{d}/adoption.md">{escape(t['check_more'])} →</a>
</div></section>

<section id="map" aria-labelledby="map-h"><div class="wrap">
<h2 id="map-h">{escape(t['map_h'])}</h2>
<p class="lead">{escape(t['map_lead'])}</p>
<p class="callout" style="margin-top:0">{escape(t['map_layers'])}</p>
<ol class="levels">{levels}</ol>
<div class="map" data-demo>
<script type="application/json">{demo_cfg}</script>
<div class="guide" hidden><div class="gtop"><span class="glabel">{escape(t['demo_label'])} · <span class="gstep"></span></span><span class="gbtn"><button type="button" data-a="prev" aria-label="{a(ui['prev'])}">←</button><button type="button" data-a="play" class="gplay">{escape(ui['pause_l'])}</button><button type="button" data-a="next" aria-label="{a(ui['next'])}">→</button></span></div><p class="ghint" aria-live="polite"></p></div>
<p class="ex">{escape(t['map_example'])}</p>
<div class="lvl lvl-1"><div class="box out" data-s="1"><span class="ty">1 · {escape(o[0])}</span><b class="fld" data-s="1">{escape(o[1])}</b><p class="fld" data-s="2">{escape(o[2])}</p><p class="m fld" data-s="3">{escape(o[3])}</p><small class="fld" data-s="4">{escape(o[4])}</small></div></div>
<p class="verb" data-s="5">↑ {escape(t['map_up'])}</p>
<div class="lvl">{slices}</div>
<div class="zoom" data-s="8"><p class="verb">↓ {escape(t['map_zoom'])}</p>
<div class="lvl">{crit}</div></div>
</div>
<div class="mapfoot"><div>
<h3>{escape(t['map_rules_h'])}</h3>
<ol>{rules}</ol>
<p class="note" style="margin-top:12px">{escape(t['map_code'])}</p>
</div><div>
<div class="ctas" style="margin-top:0"><a class="btn primary" href="map.html">{escape(t['map_blank'])}</a></div>
<a class="more" style="margin-top:0" href="{d}/value-map.md">{escape(t['map_more'])} →</a>
</div></div>
</div></section>

<section id="start" aria-labelledby="start-h"><div class="wrap">
<h2 id="start-h">{escape(t['cta_h'])}</h2>
<ol class="steps">{steps}</ol>
<div class="ctas"><a class="btn primary" href="{t['cta1_href']}">{escape(t['cta1'])}</a><a class="btn ghost" href="{BLOB}/CONTRIBUTING.md">{escape(t['cta_contrib'])}</a></div>
</div></section>
</main>
<footer><div class="wrap">
<p>{escape(t['footer'])} · <a href="{d}/sources.md">{escape(t['sources'])}</a> · <a href="{REPO}">GitHub</a></p>
</div></footer>
<script>{DEMO_JS}</script>
</body>
</html>
"""


BLANK_CSS = """
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--vf-bg);color:var(--vf-ink);font-family:var(--vf-font-sans);font-size:14px;line-height:1.35}
.sheet{max-width:1100px;margin:0 auto;padding:16px;display:flex;flex-direction:column;gap:10px}
.head{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
h1{font-size:1.4rem;font-weight:600;margin:0;display:flex;align-items:baseline;gap:6px;flex:1;min-width:260px}
h1 input{flex:1;min-width:0;font:inherit;color:inherit;background:transparent;border:0;border-bottom:2px dashed var(--vf-border);padding:0 4px}
.tools{display:flex;gap:8px;flex-wrap:wrap}
button{font:inherit;font-size:13px;font-weight:600;border-radius:999px;padding:5px 14px;cursor:pointer;border:1.5px solid var(--vf-primary);background:transparent;color:var(--vf-primary)}
button.primary{background:var(--vf-primary);color:var(--vf-on-primary)}
.help{color:var(--vf-muted);font-size:12.5px;margin:0}
.help a{color:var(--vf-primary)}
.row{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr))}
.out{max-width:760px;width:100%;margin:0 auto}
.box{border:2px solid var(--box,var(--vf-primary));border-radius:8px;padding:8px 10px;display:flex;flex-direction:column;gap:6px;background:var(--vf-bg)}
.box.big{--box:var(--vf-accent)}
.box.big .fs{display:grid;gap:6px 14px;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr))}
.ty{font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--box,var(--vf-primary))}
label{display:flex;flex-direction:column;gap:2px;font-size:11.5px;font-weight:600;color:var(--vf-muted)}
textarea{font:inherit;font-size:13.5px;font-weight:400;color:var(--vf-ink);background:var(--vf-surface);border:1px solid var(--vf-border);border-radius:6px;padding:6px 8px;resize:vertical;min-height:58px;overflow:hidden}
textarea::placeholder{color:var(--vf-muted);opacity:.75}
textarea:focus{outline:2px solid var(--vf-accent-mark);outline-offset:1px;background:var(--vf-bg)}
.verb{text-align:center;color:var(--vf-muted);font-style:italic;font-size:12px;margin:0}
.rules{color:var(--vf-muted);font-size:12px;margin:0}
@page{size:A4 landscape;margin:10mm}
@media print{body{background:#fff;color:#000}.sheet{max-width:none;padding:0}.noprint{display:none}.box{break-inside:avoid}textarea{background:#fff;border:0;border-bottom:1px dashed #bbb;border-radius:0;resize:none;min-height:42px}textarea::placeholder{color:transparent}h1 input{border-bottom:1px solid #999}}
"""

BLANK_JS = r"""
(function(){
var cfg=JSON.parse(document.getElementById('cfg').textContent),KEY='vf-map-'+cfg.lang;
var els=[].slice.call(document.querySelectorAll('[data-k]'));
function grow(el){if(el.tagName==='TEXTAREA'){el.style.height='auto';el.style.height=el.scrollHeight+2+'px';}}
try{var saved=JSON.parse(localStorage.getItem(KEY)||'{}');els.forEach(function(el){if(saved[el.dataset.k])el.value=saved[el.dataset.k];});}catch(e){}
function save(){var o={};els.forEach(function(el){if(el.value)o[el.dataset.k]=el.value;});try{localStorage.setItem(KEY,JSON.stringify(o));}catch(e){}}
els.forEach(function(el){grow(el);el.addEventListener('input',function(){grow(el);save();});});
var v=function(k){var el=document.querySelector('[data-k="'+k+'"]');return el?el.value.trim():'';};
var cell=function(x){return x.replace(/\|/g,'\\|').replace(/\s*\n\s*/g,' ');};
document.getElementById('print').onclick=function(){window.print();};
document.getElementById('md').onclick=function(){
  var L=[ '# '+cfg.md_title+': '+(v('title')||'<'+cfg.title_ph+'>'),'','## '+cfg.md_l1,''];
  cfg.fo.forEach(function(f,i){L.push('- **'+f+':** '+cell(v('o'+i)));});
  L.push('','## '+cfg.md_l2,'','| '+cfg.md_order+' | '+cfg.fs.join(' | ')+' |','|---|'+cfg.fs.map(function(){return '---';}).join('|')+'|');
  for(var n=1;n<=4;n++){var r=cfg.fs.map(function(_,i){return cell(v('s'+n+'_'+i));});if(r.join(''))L.push('| '+n+' | '+r.join(' | ')+' |');}
  var blob=new Blob([L.join('\n')+'\n'],{type:'text/markdown'}),a=document.createElement('a');
  a.href=URL.createObjectURL(blob);a.download=cfg.file;document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(a.href);},1000);
};
var clr=document.getElementById('clear'),armed=false;
clr.onclick=function(){if(!armed){armed=true;clr.textContent=cfg.clear2;setTimeout(function(){armed=false;clr.textContent=cfg.clear;},3000);return;}
  els.forEach(function(el){el.value='';grow(el);});try{localStorage.removeItem(KEY);}catch(e){}armed=false;clr.textContent=cfg.clear;};
document.querySelectorAll('.noprint').forEach(function(n){n.hidden=false;});
})();
"""


def blank(t):
    b = t["base"]
    a = lambda x: escape(x, quote=True)
    ui = t["blank_ui"]
    fo, fs = t["blank_fields_outcome"], t["blank_fields_slice"]

    def field(key, label, hint):
        return f'<label>{escape(label)}<textarea data-k="{key}" rows="2" placeholder="{a(hint)}"></textarea></label>'

    outcome = "".join(field(f"o{i}", l, h) for i, (l, h) in enumerate(zip(fo, t["blank_hints_outcome"])))
    slices = "".join(
        f'<div class="box"><span class="ty">2 · {escape(t["blank_slice"])} {n}</span>'
        + "".join(field(f"s{n}_{i}", l, h) for i, (l, h) in enumerate(zip(fs, t["blank_hints_slice"])))
        + "</div>" for n in range(1, 5))
    rules = " · ".join(escape(r) for r in t["map_rules"])
    cfg = json.dumps({"lang": t["lang"], "fo": fo, "fs": fs, **ui}, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(t['blank_title'])}</title>
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{b}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{b}assets/tokens.css">
<style>{BLANK_CSS}</style>
</head>
<body>
<main class="sheet">
<div class="head"><h1>{escape(t['map_h'])}: <input data-k="title" aria-label="{a(ui['title_ph'])}" placeholder="{a(ui['title_ph'])}"></h1>
<div class="tools noprint" hidden><button type="button" class="primary" id="print">{escape(ui['print'])}</button><button type="button" id="md">{escape(ui['md'])}</button><button type="button" id="clear">{escape(ui['clear'])}</button></div></div>
<p class="help noprint">{escape(t['blank_print'])} <a href="./#map">{escape(t['blank_back'])}</a></p>
<div class="out"><div class="box big"><span class="ty">1 · {escape(t['map_levels'][0][1])}</span><div class="fs">{outcome}</div></div></div>
<p class="verb">↑ {escape(t['map_up'])}</p>
<div class="row">{slices}</div>
<p class="rules">{rules} {escape(t['map_code'])}</p>
</main>
<script type="application/json" id="cfg">{cfg}</script>
<script>{BLANK_JS}</script>
</body>
</html>
"""


if __name__ == "__main__":
    copy_assets()
    (SITE / "index.html").write_text(page(T["en"]), encoding="utf-8")
    (SITE / "map.html").write_text(blank(T["en"]), encoding="utf-8")
    (SITE / "pt").mkdir(exist_ok=True)
    (SITE / "pt/index.html").write_text(page(T["pt"]), encoding="utf-8")
    (SITE / "pt/map.html").write_text(blank(T["pt"]), encoding="utf-8")
    print("ok")
