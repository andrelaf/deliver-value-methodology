"""Generate the Value-First diagrams (SVG, EN + PT, light/dark).

Run: python assets/diagrams/build.py
Colors follow assets/brand/tokens.css. Each SVG carries its own background and
switches palette with prefers-color-scheme, so it stays legible on any page.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent

STYLE = """<style>
text{font-family:'IBM Plex Sans','Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif}
.bg{fill:#FFFFFF}.panel{fill:#F5F6F3}.node{fill:#FFFFFF;stroke:#16212B;stroke-width:2}
.node-soft{fill:#FFFFFF;stroke:#D5DAD9;stroke-width:1.5}.pri{fill:#0B6E63}.acc-node{fill:#FFFFFF;stroke:#C97A16;stroke-width:2}
.t-ink{fill:#16212B}.t-muted{fill:#4F5D6A}.t-on{fill:#FFFFFF}.t-pri{fill:#0B6E63}.t-acc{fill:#A15708}.dot{fill:#F5C26B}
.l-conn{stroke:#4F5D6A;stroke-width:2;fill:none}.l-pri{stroke:#0B6E63;stroke-width:2.5;fill:none}
.l-acc{stroke:#C97A16;stroke-width:2;fill:none}.dash{stroke-dasharray:6 5}
.m-conn{fill:#4F5D6A}.m-pri{fill:#0B6E63}.m-acc{fill:#C97A16}.hatch{stroke:#C97A16;stroke-width:1.5;opacity:.55}
.gap-edge{fill:none;stroke:#C97A16;stroke-width:1.5;stroke-dasharray:4 4}
@media (prefers-color-scheme: dark){
.bg{fill:#0E151B}.panel{fill:#16212B}.node{fill:#0E151B;stroke:#E7ECEE}.node-soft{fill:#0E151B;stroke:#2C3A45}
.pri{fill:#4CC2B0}.acc-node{fill:#0E151B;stroke:#F0AC4C}.t-ink{fill:#E7ECEE}.t-muted{fill:#A3B0BA}.t-on{fill:#0E151B}
.t-pri{fill:#4CC2B0}.t-acc{fill:#F0AC4C}.l-conn{stroke:#A3B0BA}.l-pri{stroke:#4CC2B0}.l-acc{stroke:#F0AC4C}
.m-conn{fill:#A3B0BA}.m-pri{fill:#4CC2B0}.m-acc{fill:#F0AC4C}.hatch{stroke:#F0AC4C}.gap-edge{stroke:#F0AC4C}}
</style>"""

DEFS = """<defs>
<marker id="a-conn" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="m-conn"/></marker>
<marker id="a-pri" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="m-pri"/></marker>
<marker id="a-acc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="m-acc"/></marker>
<pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="10" class="hatch"/></pattern>
</defs>"""


def svg(w, h, title, desc, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-labelledby="title desc">\n<title id="title">{escape(title)}</title>\n'
            f'<desc id="desc">{escape(desc)}</desc>\n{STYLE}\n{DEFS}\n'
            f'<rect width="{w}" height="{h}" rx="14" class="bg"/>\n{body}\n</svg>\n')


def rect(x, y, w, h, cls="node", rx=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>'


def text(x, y, lines, cls="t-ink", size=15, anchor="middle", weight=400, gap=None):
    if isinstance(lines, str):
        lines = [lines]
    gap = gap or round(size * 1.35)
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else gap}">{escape(t)}</tspan>' for i, t in enumerate(lines))
    return (f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{spans}</text>')


def line(d, cls="l-conn", marker="conn", dashed=False, start=False):
    c = cls + (" dash" if dashed else "")
    m = f' marker-end="url(#a-{marker})"' if marker else ""
    if start:
        m += f' marker-start="url(#a-{marker})"'
    return f'<path d="{d}" class="{c}"{m}/>'


def node(cx, cy, w, h, title, sub=None, cls="node", tcls="t-ink", scls="t-muted", tsize=16, ssize=13):
    out = [rect(cx - w / 2, cy - h / 2, w, h, cls)]
    if sub:
        sub = [sub] if isinstance(sub, str) else sub
        top = cy - (len(sub) * ssize * 1.3) / 2 - 2
        out.append(text(cx, top, title, tcls, tsize, weight=600))
        out.append(text(cx, top + tsize + 4, sub, scls, ssize))
    else:
        out.append(text(cx, cy + tsize / 3, title, tcls, tsize, weight=600))
    return "\n".join(out)


# ---------------------------------------------------------------- strings
S = {
    "en": {
        "cycle_title": "The Value-First cycle",
        "cycle_desc": "Four steps in a loop around a living Value Spec: Specify, Validate, Build, Check value, then back to the spec. It runs inside your existing cadence.",
        "steps": [("1 · Specify", ["Value Pair writes", "the Value Spec"]),
                  ("2 · Validate", ["Cheapest test of the", "riskiest assumption"]),
                  ("3 · Build", ["People and agents,", "traced to criteria"]),
                  ("4 · Check value", ["Result vs. target,", "on the agreed date"])],
        "center": ("Value Spec", ["living,", "in the repo"]),
        "cycle_caption": "Runs inside the cadence you already use: Scrum, Kanban or your own.",

        "gap_title": "The gap between spec and development",
        "gap_desc": "A typical story states only what to build. Building also needs the why, the expected value and metric, constraints, edge cases and non-goals, and what is fixed or flexible. Before, the Tech Lead filled that gap with conversation. With agents, the agent guesses. Value-First closes the gap upstream, in the Value Spec.",
        "gap_left": "What the story usually says",
        "gap_right": "What building needs",
        "gap_rows": ["What to build", "Why: problem, and for whom", "Expected value and metric",
                     "Constraints, non-functional reqs", "Edge cases and non-goals", "What's fixed vs. flexible"],
        "gap_label": "The gap",
        "gap_before": ["Before: the Tech Lead fills it,", "with conversation and intuition"],
        "gap_now": ["With agents: the agent guesses.", "Wrong code, faster."],
        "gap_bar": "Value-First: the Value Pair closes the gap upstream, in the Value Spec",

        "ba_title": "Before and now: from product to spec to code",
        "ba_desc": "Before: product writes a story, a gap of missing context sits between story and developers, and the Tech Lead fills it informally; feedback arrives late. Now: Product and Tech Lead write a Value Spec together, validate it with a prototype, and the spec becomes executable input for spec-driven tools and coding agents, with agent context files. People review against the spec, value is checked after release, and the spec is updated.",
        "before": "BEFORE · human-paced delivery",
        "now": "NOW · with coding agents and Value-First",
        "b_nodes": [("Product", "intent, priorities"), ("Story", "the what, little why"),
                    ("Developers", "interpret and code"), ("Release", "software shipped")],
        "b_tl": ("Tech Lead", "translates · completes · decides"),
        "b_gap": "Missing: why, constraints, edge cases",
        "b_writes": "writes", "b_handoff": "handoff", "b_fill": "fills blanks from experience",
        "b_feedback": "Feedback: late, often about output rather than value",
        "b_strength": "Works thanks to conversation, but depends on one person",
        "n_pair": ("Value Pair", ["Product + Tech Lead"]),
        "n_spec": ("Value Spec", ["problem · value · criteria", "constraints · non-goals"]),
        "n_proto": "AI prototype",
        "n_validate": "validate",
        "n_agents": ("SDD tools + agents", ["plan → tasks → code"]),
        "n_ctx": "AGENTS.md · CLAUDE.md · rules",
        "n_review": ("People review", ["against the spec"]),
        "n_check": ("Value check", ["metric vs. target"]),
        "a_write": "write together", "a_exec": "executable input", "a_prs": "PRs cite SC IDs",
        "a_release": "release", "a_ask": "unclear? ask, don't guess", "a_ctx": "context",
        "warn": ["Vague spec:", "wrong code, faster"],
        "loop": "Living spec: decisions and change log",

        "roles_title": "Roles in Value-First",
        "roles_desc": "The Value Pair, Product and Tech Lead, co-own the Value Spec. Product owns problem, value and metrics. The Tech Lead owns feasibility, constraints, testable criteria and agent context. The team questions the spec, builds and reviews all AI code. Coding agents read the spec, ask instead of guessing and cite criterion IDs. Stakeholders validate prototypes and know what is fixed.",
        "pair": "Value Pair",
        "product": ("Product", ["Problem, and for whom", "Expected value and metric", "Leads the value check"]),
        "tl": ("Tech Lead", ["Feasibility and constraints", "Testable criteria", "Agent context"]),
        "spec": ("Value Spec", ["two named owners"]),
        "team": ("Team", ["Questions the spec", "Builds", "Reviews all AI code"]),
        "agents": ("Coding agents", ["Read the spec", "Ask, don't guess", "Cite SC IDs"]),
        "stake": ("Stakeholders", ["Validate prototypes", "Know what's fixed", "and what's flexible"]),

        "cmp_title": "Where Value-First sits",
        "cmp_desc": "Value-First is a value and alignment layer above two kinds of tools: how the team works (Scrum, Kanban, Shape Up, SAFe) and how a spec becomes code (Spec Kit, Kiro, coding agents), which draws on agent context files (AGENTS.md, CLAUDE.md, rules, steering).",
        "top": ("Value and alignment: Value-First", "Is this worth building? How will we know it worked?"),
        "left": ("How the team works", ["Scrum · Kanban · Shape Up · SAFe", "cadence, flow, bets"]),
        "right": ("How the spec becomes code", ["Spec Kit · Kiro · coding agents", "plan, tasks, code"]),
        "bottom": "Agent context: AGENTS.md · CLAUDE.md · rules · steering",
        "feed_l": "Value Specs feed the backlog", "feed_r": "Value Specs feed the workflow",
        "cmp_caption": "Value-First doesn't replace these layers. It decides what goes into them and checks what comes out.",
    },
    "pt": {
        "cycle_title": "O ciclo do Value-First",
        "cycle_desc": "Quatro passos em ciclo em torno de uma Value Spec viva: Especificar, Validar, Construir, Verificar valor e voltar à spec. Roda dentro da cadência que o time já usa.",
        "steps": [("1 · Especificar", ["O Par de Valor", "escreve a Value Spec"]),
                  ("2 · Validar", ["Teste mais barato da", "premissa mais arriscada"]),
                  ("3 · Construir", ["Pessoas e agentes,", "ligados aos critérios"]),
                  ("4 · Verificar valor", ["Resultado vs. meta,", "na data combinada"])],
        "center": ("Value Spec", ["viva,", "no repositório"]),
        "cycle_caption": "Roda dentro da cadência que você já usa: Scrum, Kanban ou a sua própria.",

        "gap_title": "O abismo entre a spec e o desenvolvimento",
        "gap_desc": "Uma história típica diz só o que construir. Construir exige também o porquê, o valor esperado e a métrica, restrições, casos de borda e o que fica fora do escopo, e o que é fixo ou flexível. Antes, o Tech Lead preenchia esse abismo conversando. Com agentes, o agente supõe. O Value-First fecha o abismo antes, na Value Spec.",
        "gap_left": "O que a história costuma dizer",
        "gap_right": "O que construir exige",
        "gap_rows": ["O que construir", "Por quê: problema e para quem", "Valor esperado e métrica",
                     "Restrições, requisitos não funcionais", "Casos de borda e fora do escopo", "O que é fixo e o que é flexível"],
        "gap_label": "O abismo",
        "gap_before": ["Antes: o Tech Lead preenche,", "com conversa e intuição"],
        "gap_now": ["Com agentes: o agente supõe.", "Código errado, mais rápido."],
        "gap_bar": "Value-First: o Par de Valor fecha o abismo antes, na Value Spec",

        "ba_title": "Antes e agora: do produto à spec e ao código",
        "ba_desc": "Antes: produto escreve uma história, um abismo de contexto faltante fica entre a história e os desenvolvedores, e o Tech Lead o preenche informalmente; o feedback chega tarde. Agora: Produto e Tech Lead escrevem juntos uma Value Spec, validam com um protótipo, e a spec vira insumo executável para ferramentas de spec-driven development e agentes de código, com arquivos de contexto. Pessoas revisam contra a spec, o valor é verificado depois da entrega e a spec é atualizada.",
        "before": "ANTES · entrega no ritmo humano",
        "now": "AGORA · com agentes de código e Value-First",
        "b_nodes": [("Produto", "intenção, prioridades"), ("História", "o quê, pouco porquê"),
                    ("Desenvolvedores", "interpretam e codam"), ("Entrega", "software no ar")],
        "b_tl": ("Tech Lead", "traduz · completa · decide"),
        "b_gap": "Falta: porquê, restrições, casos de borda",
        "b_writes": "escreve", "b_handoff": "repasse", "b_fill": "completa com a experiência",
        "b_feedback": "Feedback: tarde, muitas vezes sobre a entrega e não sobre o valor",
        "b_strength": "Funciona graças à conversa, mas depende de uma pessoa",
        "n_pair": ("Par de Valor", ["Produto + Tech Lead"]),
        "n_spec": ("Value Spec", ["problema · valor · critérios", "restrições · fora do escopo"]),
        "n_proto": "Protótipo com IA",
        "n_validate": "validar",
        "n_agents": ("Ferramentas SDD + agentes", ["plano → tarefas → código"]),
        "n_ctx": "AGENTS.md · CLAUDE.md · regras",
        "n_review": ("Pessoas revisam", ["contra a spec"]),
        "n_check": ("Verificação de valor", ["métrica vs. meta"]),
        "a_write": "escrevem juntos", "a_exec": "insumo executável", "a_prs": "PRs citam os SC",
        "a_release": "entrega", "a_ask": "ficou ambíguo? pergunta, não supõe", "a_ctx": "contexto",
        "warn": ["Spec vaga:", "código errado, mais rápido"],
        "loop": "Spec viva: decisões e histórico de mudanças",

        "roles_title": "Papéis no Value-First",
        "roles_desc": "O Par de Valor, Produto e Tech Lead, é dono da Value Spec. Produto responde por problema, valor e métricas. O Tech Lead responde por viabilidade, restrições, critérios testáveis e contexto dos agentes. O time questiona a spec, constrói e revisa todo código gerado por IA. Agentes de código leem a spec, perguntam em vez de supor e citam os IDs dos critérios. Stakeholders validam protótipos e sabem o que é fixo.",
        "pair": "Par de Valor",
        "product": ("Produto", ["Problema e para quem", "Valor esperado e métrica", "Conduz a verificação"]),
        "tl": ("Tech Lead", ["Viabilidade e restrições", "Critérios testáveis", "Contexto dos agentes"]),
        "spec": ("Value Spec", ["dois donos nomeados"]),
        "team": ("Time", ["Questiona a spec", "Constrói", "Revisa todo código de IA"]),
        "agents": ("Agentes de código", ["Leem a spec", "Perguntam, não supõem", "Citam os IDs (SC)"]),
        "stake": ("Stakeholders", ["Validam protótipos", "Sabem o que é fixo", "e o que é flexível"]),

        "cmp_title": "Onde o Value-First se encaixa",
        "cmp_desc": "O Value-First é uma camada de valor e alinhamento acima de dois tipos de ferramenta: como o time trabalha (Scrum, Kanban, Shape Up, SAFe) e como a spec vira código (Spec Kit, Kiro, agentes de código), que usa arquivos de contexto (AGENTS.md, CLAUDE.md, regras, steering).",
        "top": ("Valor e alinhamento: Value-First", "Vale a pena construir? Como saberemos que funcionou?"),
        "left": ("Como o time trabalha", ["Scrum · Kanban · Shape Up · SAFe", "cadência, fluxo, apostas"]),
        "right": ("Como a spec vira código", ["Spec Kit · Kiro · agentes de código", "plano, tarefas, código"]),
        "bottom": "Contexto dos agentes: AGENTS.md · CLAUDE.md · regras · steering",
        "feed_l": "Value Specs alimentam o backlog", "feed_r": "Value Specs alimentam o fluxo",
        "cmp_caption": "O Value-First não substitui essas camadas. Ele decide o que entra nelas e verifica o que sai.",
    },
}


# ---------------------------------------------------------------- diagrams
def cycle(s):
    import math
    W, H, cx, cy, R = 760, 580, 380, 280, 195
    pos = [(cx, cy - R), (cx + R, cy), (cx, cy + R), (cx - R, cy)]
    b = []
    for a0, a1 in [(-52, -22), (22, 52), (128, 158), (202, 232)]:
        p0 = (cx + R * math.cos(math.radians(a0)), cy + R * math.sin(math.radians(a0)))
        p1 = (cx + R * math.cos(math.radians(a1)), cy + R * math.sin(math.radians(a1)))
        b.append(line(f"M{p0[0]:.1f} {p0[1]:.1f} A{R} {R} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}", "l-pri", "pri"))
    for (x, y), (t, sub) in zip(pos, s["steps"]):
        b.append(node(x, y, 220, 78, t, sub))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="78" class="pri"/>')
    b.append(f'<circle cx="{cx}" cy="{cy - 44}" r="6" class="dot"/>')
    b.append(text(cx, cy - 8, s["center"][0], "t-on", 18, weight=600))
    b.append(text(cx, cy + 16, s["center"][1], "t-on", 13))
    b.append(text(cx, H - 18, s["cycle_caption"], "t-muted", 14))
    return svg(W, H, s["cycle_title"], s["cycle_desc"], "\n".join(b))


def gap(s):
    W, H = 940, 500
    b = [rect(30, 30, 270, 360, "panel", 12), rect(640, 30, 270, 360, "panel", 12)]
    b.append(text(165, 62, s["gap_left"], "t-ink", 15, weight=600))
    b.append(text(775, 62, s["gap_right"], "t-ink", 15, weight=600))
    y0 = 92
    for i, r in enumerate(s["gap_rows"]):
        y = y0 + i * 48
        b.append(rect(655, y, 240, 36, "node-soft", 6))
        b.append(text(775, y + 23, r, "t-ink", 13))
        if i == 0:
            b.append(rect(45, y, 240, 36, "node-soft", 6))
            b.append(text(165, y + 23, r, "t-ink", 13))
            b.append(line(f"M290 {y + 18} H650", "l-conn", "conn"))
        else:
            b.append(f'<rect x="45" y="{y}" width="240" height="36" rx="6" class="gap-edge"/>')
            b.append(text(165, y + 23, "?", "t-acc", 15, weight=600))
    b.append(f'<rect x="320" y="140" width="300" height="230" rx="10" fill="url(#hatch)"/>')
    b.append(f'<rect x="320" y="140" width="300" height="230" rx="10" class="gap-edge"/>')
    b.append(rect(340, 158, 260, 194, "bg", 8))
    b.append(text(470, 186, s["gap_label"], "t-acc", 17, weight=600))
    b.append(text(470, 222, s["gap_before"], "t-ink", 13))
    b.append(text(470, 290, s["gap_now"], "t-acc", 13, weight=600))
    b.append(rect(30, 420, 880, 52, "pri", 10))
    b.append(f'<circle cx="58" cy="446" r="6" class="dot"/>')
    b.append(text(480, 451, s["gap_bar"], "t-on", 15, weight=600))
    return svg(W, H, s["gap_title"], s["gap_desc"], "\n".join(b))


def before_after(s):
    W, H = 1200, 860
    b = [rect(20, 20, 1160, 360, "panel", 12), rect(20, 400, 1160, 440, "panel", 12)]
    # BEFORE
    b.append(text(44, 54, s["before"], "t-muted", 14, "start", 600))
    xs, y = [115, 350, 790, 1040], 210
    for x, (t, sub) in zip(xs, s["b_nodes"]):
        b.append(node(x, y, 180, 64, t, sub))
    b.append(f'<rect x="455" y="160" width="230" height="100" rx="8" fill="url(#hatch)"/>')
    b.append(f'<rect x="455" y="160" width="230" height="100" rx="8" class="gap-edge"/>')
    b.append(text(560, 288, s["b_gap"], "t-acc", 13, weight=600))
    b.append(node(560, 100, 240, 60, s["b_tl"][0], s["b_tl"][1], "acc-node"))
    b.append(line("M205 210 H254", "l-conn", "conn"))
    b.append(text(230, 200, s["b_writes"], "t-muted", 12))
    b.append(line("M440 210 H692", "l-conn", "conn"))
    b.append(rect(515, 198, 90, 24, "bg", 4))
    b.append(text(560, 215, s["b_handoff"], "t-muted", 12))
    b.append(line("M520 130 Q470 150 400 178", "l-acc", "acc", dashed=True))
    b.append(line("M600 130 Q660 150 715 178", "l-acc", "acc", dashed=True))
    b.append(text(800, 112, s["b_fill"], "t-acc", 12, "start"))
    b.append(line("M880 210 H942", "l-conn", "conn"))
    b.append(line("M1040 244 C1040 340 115 340 115 248", "l-conn", "conn", dashed=True))
    b.append(text(580, 335, s["b_feedback"], "t-muted", 13))
    b.append(text(1156, 54, s["b_strength"], "t-muted", 12, "end"))
    # NOW
    b.append(text(44, 434, s["now"], "t-pri", 14, "start", 600))
    y = 600
    b.append(node(120, y, 180, 64, *s["n_pair"]))
    b.append(rect(240, y - 42, 190, 84, "pri", 8))
    b.append(f'<circle cx="256" cy="{y - 28}" r="5" class="dot"/>')
    b.append(text(335, y - 14, s["n_spec"][0], "t-on", 16, weight=600))
    b.append(text(335, y + 8, s["n_spec"][1], "t-on", 12))
    b.append(node(335, 490, 170, 40, s["n_proto"]))
    b.append(line(f"M315 {y - 44} V514", "l-pri", "pri"))
    b.append(line(f"M355 512 V{y - 46}", "l-pri", "pri"))
    b.append(text(366, 538, s["n_validate"], "t-pri", 12, "start"))
    b.append(node(680, y, 230, 64, *s["n_agents"]))
    b.append(node(680, 712, 260, 40, s["n_ctx"], cls="node-soft", tsize=13))
    b.append(line("M680 690 V636", "l-conn", "conn"))
    b.append(text(690, 668, s["a_ctx"], "t-muted", 12, "start"))
    b.append(node(900, y, 150, 64, *s["n_review"]))
    b.append(node(1080, y, 176, 64, *s["n_check"]))
    b.append(line(f"M210 {y} H234", "l-conn", "conn"))
    b.append(text(150, y + 52, s["a_write"], "t-muted", 12))
    b.append(line(f"M430 {y} H559", "l-pri", "pri"))
    b.append(text(495, y - 10, s["a_exec"], "t-pri", 12, weight=600))
    b.append(text(495, y - 66, s["warn"], "t-acc", 12, weight=600))
    b.append(line(f"M567 {y + 32} Q495 {y + 70} 430 {y + 36}", "l-conn", "conn", dashed=True))
    b.append(text(495, y + 84, s["a_ask"], "t-muted", 12))
    b.append(line(f"M795 {y} H819", "l-conn", "conn"))
    b.append(text(810, y - 44, s["a_prs"], "t-muted", 12))
    b.append(line(f"M975 {y} H986", "l-conn", "conn"))
    b.append(line(f"M1080 {y + 32} C1080 815 335 815 335 {y + 46}", "l-pri", "pri"))
    b.append(rect(560, 784, 400, 26, "panel", 4))
    b.append(text(760, 802, "↻ " + s["loop"], "t-pri", 13, weight=600))
    return svg(W, H, s["ba_title"], s["ba_desc"], "\n".join(b))


def roles(s):
    W, H = 940, 620
    b = []
    b.append(text(470, 46, s["pair"], "t-pri", 18, weight=600))
    b.append(line("M170 120 V70 H770 V120", "l-pri", None))
    b.append(f'<circle cx="470" cy="70" r="6" class="dot"/>')

    def card(x, y, w, h, title, items, cls="node"):
        out = [rect(x, y, w, h, cls, 10), text(x + w / 2, y + 30, title, "t-ink", 16, weight=600)]
        out.append(text(x + w / 2, y + 58, items, "t-muted", 13, gap=22))
        return "\n".join(out)

    b.append(card(40, 120, 260, 140, *s["product"]))
    b.append(card(640, 120, 260, 140, *s["tl"]))
    b.append(rect(370, 140, 200, 100, "pri", 10))
    b.append(f'<circle cx="388" cy="158" r="5" class="dot"/>')
    b.append(text(470, 186, s["spec"][0], "t-on", 18, weight=600))
    b.append(text(470, 210, s["spec"][1], "t-on", 13))
    b.append(line("M300 190 H364", "l-pri", "pri"))
    b.append(line("M640 190 H576", "l-pri", "pri"))
    b.append(card(40, 400, 260, 140, *s["team"], cls="node-soft"))
    b.append(card(340, 400, 260, 140, *s["agents"], cls="node-soft"))
    b.append(card(640, 400, 260, 140, *s["stake"], cls="node-soft"))
    b.append(line("M430 240 Q300 320 170 394", "l-conn", "conn"))
    b.append(line("M470 240 V394", "l-conn", "conn"))
    b.append(line("M510 240 Q640 320 770 394", "l-conn", "conn"))
    return svg(W, H, s["roles_title"], s["roles_desc"], "\n".join(b))


def comparison(s):
    W, H = 940, 520
    b = [rect(40, 30, 860, 96, "pri", 12), f'<circle cx="70" cy="58" r="6" class="dot"/>']
    b.append(text(470, 70, s["top"][0], "t-on", 19, weight=600))
    b.append(text(470, 98, s["top"][1], "t-on", 14))
    b.append(node(250, 250, 400, 100, s["left"][0], s["left"][1]))
    b.append(node(690, 250, 400, 100, s["right"][0], s["right"][1]))
    b.append(line("M250 128 V194", "l-pri", "pri"))
    b.append(line("M690 128 V194", "l-pri", "pri"))
    b.append(text(262, 165, s["feed_l"], "t-pri", 12, "start"))
    b.append(text(702, 165, s["feed_r"], "t-pri", 12, "start"))
    b.append(node(690, 384, 400, 52, s["bottom"], cls="node-soft", tsize=13))
    b.append(line("M690 356 V306", "l-conn", "conn"))
    b.append(text(470, 470, s["cmp_caption"], "t-muted", 14))
    return svg(W, H, s["cmp_title"], s["cmp_desc"], "\n".join(b))


if __name__ == "__main__":
    for lang, s in S.items():
        for name, fn in [("cycle", cycle), ("gap", gap), ("before-after", before_after),
                         ("roles", roles), ("comparison", comparison)]:
            (OUT / f"{name}-{lang}.svg").write_text(fn(s), encoding="utf-8")
    print("ok")
