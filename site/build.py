"""Build the Value-First landing page (static, EN + PT).

Run:     python site/build.py
Preview: python -m http.server 8000 -d site   →  http://localhost:8000/

Writes site/index.html (EN), site/pt/index.html (PT) and copies brand assets,
diagrams and the canvas into site/assets/. No external JS, no build tools.
"""
import shutil
from html import escape
from pathlib import Path

SITE = Path(__file__).parent
ROOT = SITE.parent
REPO = "https://github.com/andrelaf/deliver-value-methodology"
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
        "map_lead": "For initiatives bigger than one spec. Like C4 does for architecture: three levels of zoom, four rules, and you can draw it on a whiteboard.",
        "map_levels": [("1", "Outcome", "Why, and how will we know?"), ("2", "Slices", "What first, and what are we betting on?"), ("3", "Criteria", "How do we know this slice works?")],
        "map_example": "Fictional example, based on the VS-014 template example.",
        "map_up": "contribute to",
        "map_zoom": "zoom into VS-014",
        "map_outcome": ("Outcome", "Customers get their invoices on their own", "Billing contacts ask support for invoices.", "Invoice tickets: ~120 → ≤ 40 / week, 6 weeks after launch", "Out: payments, invoice editing"),
        "map_slices": [
            ("VS-014", "Download invoices in the portal", "Bet: customers use the portal instead of emailing support (validated 5/6)", "In build"),
            ("VS-015", "Filter invoices by date", "Bet: audits need date ranges (2 of 6 asked)", "Next"),
            ("VS-016", "Monthly invoice by email", "Bet: receiving beats searching (not validated)", "Maybe"),
        ],
        "map_criteria": [
            ("SC-1", "Lists the account's last 24 months", "end-to-end test"),
            ("SC-2", "Delivers the stored PDF unchanged", "integration test"),
            ("SC-3", "403 without billing_admin, attempt logged", "security test"),
            ("SC-4", "p95 < 1 s up to 500 invoices", "load test"),
        ],
        "map_verified": "verified by",
        "map_rules_h": "Four rules",
        "map_rules": ["Every box has a type, a name and one sentence.", "Every outcome and slice has a metric or a signal.", "Every arrow has a verb.", "One drawing per level. Zoom in only where you need to."],
        "map_code": "Level 4, code, isn't drawn: tests and PRs cite the SC IDs.",
        "map_blank": "Blank map to print",
        "map_more": "How to run a Value Map session",
        "blank_title": "Value Map (blank)",
        "blank_slice": "Slice",
        "blank_fields_outcome": ["Name", "Problem and for whom", "Metric: baseline → target, by when", "Out of scope"],
        "blank_fields_slice": ["VS-___  ·  Delivers", "How it moves the metric", "Riskiest bet (value or tech)", "Status"],
        "blank_print": "Print this page (landscape). Level 3 lives in each Value Spec.",
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
        "map_lead": "Para iniciativas maiores que uma spec. Como o C4 faz com a arquitetura: três níveis de zoom, quatro regras, e dá para desenhar no quadro branco.",
        "map_levels": [("1", "Resultado", "Por quê, e como saberemos?"), ("2", "Fatias", "O que primeiro, e em que apostamos?"), ("3", "Critérios", "Como sabemos que esta fatia funciona?")],
        "map_example": "Exemplo fictício, baseado no exemplo de template da VS-014.",
        "map_up": "contribuem para",
        "map_zoom": "zoom na VS-014",
        "map_outcome": ("Resultado", "Clientes obtêm as próprias faturas", "Contatos financeiros pedem faturas ao suporte.", "Tickets de fatura: ~120 → ≤ 40 / semana, 6 semanas após o lançamento", "Fora: pagamento, edição de faturas"),
        "map_slices": [
            ("VS-014", "Baixar faturas no portal", "Aposta: clientes usam o portal em vez de mandar e-mail ao suporte (validada 5/6)", "Em construção"),
            ("VS-015", "Filtrar faturas por data", "Aposta: auditorias precisam de intervalos de datas (2 de 6 pediram)", "Próxima"),
            ("VS-016", "Fatura mensal por e-mail", "Aposta: receber é melhor que procurar (não validada)", "Talvez"),
        ],
        "map_criteria": [
            ("SC-1", "Lista os últimos 24 meses da conta", "teste ponta a ponta"),
            ("SC-2", "Entrega o PDF armazenado sem alterações", "teste de integração"),
            ("SC-3", "403 sem billing_admin, tentativa registrada", "teste de segurança"),
            ("SC-4", "p95 < 1 s com até 500 faturas", "teste de carga"),
        ],
        "map_verified": "verificado por",
        "map_rules_h": "Quatro regras",
        "map_rules": ["Toda caixa tem tipo, nome e uma frase.", "Todo resultado e toda fatia têm uma métrica ou um sinal.", "Toda seta tem um verbo.", "Um desenho por nível. Aproxime só onde precisar."],
        "map_code": "O nível 4, código, não se desenha: testes e PRs citam os IDs dos SC.",
        "map_blank": "Mapa em branco para imprimir",
        "map_more": "Como conduzir uma sessão de Mapa de Valor",
        "blank_title": "Mapa de Valor (em branco)",
        "blank_slice": "Fatia",
        "blank_fields_outcome": ["Nome", "Problema e para quem", "Métrica: linha de base → meta, até quando", "Fora do escopo"],
        "blank_fields_slice": ["VS-___  ·  Entrega", "Como move a métrica", "Aposta mais arriscada (valor ou técnica)", "Status"],
        "blank_print": "Imprima esta página (paisagem). O nível 3 fica em cada Value Spec.",
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
.box.sc{--box:var(--vf-muted);border-width:1px}
.verb{display:flex;align-items:center;justify-content:center;gap:8px;margin:10px 0;color:var(--vf-muted);font-size:var(--vf-text-sm);font-style:italic}
.verb::before,.verb::after{content:"";height:1px;width:40px;background:var(--vf-border)}
.zoom{border-top:1px dashed var(--vf-border);margin-top:16px;padding-top:4px}
.mapfoot{display:grid;gap:var(--vf-space-8);grid-template-columns:1fr;margin-top:var(--vf-space-8)}
@media (min-width:900px){.mapfoot{grid-template-columns:1fr 1fr}}
.mapfoot ol{padding-left:1.3em;margin:0}.mapfoot li{margin-bottom:6px}
footer{padding:var(--vf-space-8) 0;color:var(--vf-muted);font-size:var(--vf-text-sm)}
footer p{max-width:none}
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
        f'<div class="box slice{" on" if i == 0 else ""}"><span class="ty">2 · {vs}</span><b>{escape(n)}</b><p>{escape(bet)}</p><span class="st">{escape(st)}</span></div>'
        for i, (vs, n, bet, st) in enumerate(t["map_slices"]))
    crit = "".join(
        f'<div class="box sc"><span class="ty">3 · {sc}</span><b>{escape(s)}</b><small>{escape(t["map_verified"])}: {escape(v)}</small></div>'
        for sc, s, v in t["map_criteria"])
    rules = "".join(f"<li>{escape(r)}</li>" for r in t["map_rules"])
    url ="https://andrelaf.github.io/deliver-value-methodology/" + ("" if L == "en" else "pt/")
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(t['title'])}</title>
<meta name="description" content="{a(t['meta'])}">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="https://andrelaf.github.io/deliver-value-methodology/">
<link rel="alternate" hreflang="pt-BR" href="https://andrelaf.github.io/deliver-value-methodology/pt/">
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
<ol class="levels">{levels}</ol>
<div class="map">
<p class="ex">{escape(t['map_example'])}</p>
<div class="lvl lvl-1"><div class="box out"><span class="ty">1 · {escape(o[0])}</span><b>{escape(o[1])}</b><p>{escape(o[2])}</p><p class="m">{escape(o[3])}</p><small>{escape(o[4])}</small></div></div>
<p class="verb">↑ {escape(t['map_up'])}</p>
<div class="lvl">{slices}</div>
<div class="zoom"><p class="verb">↓ {escape(t['map_zoom'])}</p>
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
</body>
</html>
"""


BLANK_CSS = """
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--vf-bg);color:var(--vf-ink);font-family:var(--vf-font-sans);font-size:14px;line-height:1.35}
.sheet{max-width:1100px;margin:0 auto;padding:16px;display:flex;flex-direction:column;gap:10px;min-height:100vh}
.head{display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap}
h1{font-size:1.4rem;font-weight:600;margin:0}
.head span{color:var(--vf-muted);font-size:12px}
.row{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr))}
.out{max-width:620px;width:100%;margin:0 auto}
.box{border:2px solid var(--box,var(--vf-primary));border-radius:8px;padding:8px 10px;min-height:150px;display:flex;flex-direction:column}
.box.big{--box:var(--vf-accent);min-height:30vh}
.row .box{min-height:42vh}
.ty{font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--box,var(--vf-primary))}
.f{flex:1;border-bottom:1px dashed var(--vf-border);color:var(--vf-muted);font-size:11px;padding-top:2px}
.f:last-child{border-bottom:0}
.verb{text-align:center;color:var(--vf-muted);font-style:italic;font-size:12px;margin:0}
.rules{color:var(--vf-muted);font-size:12px;margin:0}
.rules a{color:var(--vf-primary)}
@page{size:A4 landscape;margin:10mm}
@media print{body{background:#fff;color:#000}.sheet{max-width:none;padding:0;min-height:0}.box.big{min-height:55mm}.row .box{min-height:85mm}.noprint{display:none}.box{break-inside:avoid}}
"""


def blank(t):
    L = "en" if t["lang"] == "en" else "pt"
    b = t["base"]
    outcome = "".join(f'<div class="f">{escape(f)}</div>' for f in t["blank_fields_outcome"])
    slice_fields = "".join(f'<div class="f">{escape(f)}</div>' for f in t["blank_fields_slice"])
    slices = "".join(f'<div class="box"><span class="ty">2 · {escape(t["blank_slice"])} {i}</span>{slice_fields}</div>' for i in range(1, 5))
    rules = " · ".join(escape(r) for r in t["map_rules"])
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
<div class="head"><h1>{escape(t['map_h'])}: ____________________</h1><span>Value-First Development · ____ / ____ / ______</span></div>
<p class="rules noprint">{escape(t['blank_print'])} <a href="./">{escape(t['blank_back'])}</a></p>
<div class="out"><div class="box big"><span class="ty">1 · {escape(t['map_levels'][0][1])}</span>{outcome}</div></div>
<p class="verb">↑ {escape(t['map_up'])}</p>
<div class="row">{slices}</div>
<p class="rules">{rules} {escape(t['map_code'])}</p>
</main>
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
