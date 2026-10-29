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
    for lang in ("en", "pt"):
        shutil.copy(ROOT / f"docs/{lang}/canvas/value-technology-alignment-canvas.png", out / f"canvas-{lang}.png")


T = {
    "en": {
        "lang": "en", "other": "pt", "other_label": "Português", "other_href": "pt/", "base": "",
        "title": "Value-First Development",
        "meta": "Make the value of each piece of work explicit, shared and measurable before anyone builds it, so people and coding agents build the right thing.",
        "skip": "Skip to content",
        "nav": [("#problem", "Problem"), ("#idea", "The idea"), ("#principles", "Principles"), ("#ai", "Specs and AI"), ("#check", "Checklist")],
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
            "Every item in progress has a Value Spec with at least one measurable success criterion.",
            "Every spec has two named owners: Product and Tech Lead.",
            "Specs live in the repo, and your agent instructions point to them.",
            "Risky items get a prototype or spike before the commitment.",
            "Scope and date changes show up as spec changes, with a reason.",
            "You check value after delivery and can name what didn't work.",
            "People review all AI-generated code, and stability is tracked alongside speed.",
        ],
        "check_more": "Checklist and maturity model",
        "canvas_h": "Value-Technology Alignment Canvas",
        "canvas_p": "For larger initiatives: an optional one-page workshop that puts business and technical perspectives side by side before you write Value Specs.",
        "canvas_alt": "The Value-Technology Alignment Canvas, a one-page grid with business and technical blocks.",
        "canvas_link": "Download the canvas (SVG)",
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
        "nav": [("#problem", "Problema"), ("#idea", "A ideia"), ("#principles", "Princípios"), ("#ai", "Specs e IA"), ("#check", "Checklist")],
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
            "Todo item em andamento tem uma Value Spec com pelo menos um critério de sucesso mensurável.",
            "Toda spec tem dois donos nomeados: Produto e Tech Lead.",
            "As specs ficam no repositório, e as instruções dos seus agentes apontam para elas.",
            "Itens arriscados ganham um protótipo ou spike antes do compromisso.",
            "Mudanças de escopo e de prazo aparecem como mudanças na spec, com motivo.",
            "Vocês verificam o valor depois da entrega e sabem dizer o que não funcionou.",
            "Pessoas revisam todo código gerado por IA, e a estabilidade é acompanhada junto com a velocidade.",
        ],
        "check_more": "Checklist e modelo de maturidade",
        "canvas_h": "Canvas de Alinhamento Valor-Tecnologia",
        "canvas_p": "Para iniciativas maiores: um workshop opcional, em uma página, que coloca as visões de negócio e de tecnologia lado a lado antes de escrever as Value Specs.",
        "canvas_alt": "O Canvas de Alinhamento Valor-Tecnologia, uma grade de uma página com blocos de negócio e de tecnologia.",
        "canvas_link": "Baixar o canvas (SVG)",
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
.canvas img{background:#fff;border:1px solid var(--vf-border)}
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
    canvas_svg = f"{BLOB}/docs/{L}/canvas/value-technology-alignment-canvas.svg"
    url = "https://andrelaf.github.io/deliver-value-methodology/" + ("" if L == "en" else "pt/")
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

<section id="canvas" aria-labelledby="canvas-h"><div class="wrap">
<div class="two"><div>
<h2 id="canvas-h">{escape(t['canvas_h'])}</h2>
<p>{escape(t['canvas_p'])}</p>
<a class="more" href="{canvas_svg}">{escape(t['canvas_link'])} →</a>
</div>
<figure class="canvas" style="margin:0"><img src="{b}assets/canvas-{L}.png" alt="{a(t['canvas_alt'])}" loading="lazy"></figure></div>
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


if __name__ == "__main__":
    copy_assets()
    (SITE / "index.html").write_text(page(T["en"]), encoding="utf-8")
    (SITE / "pt").mkdir(exist_ok=True)
    (SITE / "pt/index.html").write_text(page(T["pt"]), encoding="utf-8")
    print("ok")
