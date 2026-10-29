# Value-First brand guide

This guide covers the visual identity of **Value-First Development** (short form **Value-First**): the mark, color, type, diagrams and tone. All assets live in this folder. Tokens for the web are in [`tokens.css`](tokens.css).

The overall feel is calm, trustworthy and editorial. Think of a well-set technical book: no hype, no "AI sparkle", no robots, no decorative gradients.

## 1. The mark

![Value-First icon](logo-icon.svg)

The icon is a **V** with a **dot above it**, set on a rounded teal tile.

- **The dot is the value.** It sits first, at the top, before the work. Everything below it follows from it.
- **The V is the work converging.** The two arms are product and engineering. They start apart and meet at one point of delivery, under the value they serve.
- **The amber dot on the teal tile** pairs the warm accent (value, outcome) with the steady primary (discipline, engineering).

It also reads as a person with open arms. That reading is welcome, since the method is about people working together and not about ritual. It is the reason the dot must never be enlarged into a "head" or given a face.

Geometry (32 × 32 grid): tile `rx 7`; V path `M8 10 L16 24 L24 10`, stroke 3.5 with round caps and joins; dot `cx 16, cy 9, r 3`. The gap between the dot and the arms is about 2.7 units, which stays open at 16 px.

### Files

| File | Use |
|---|---|
| `logo-icon.svg` | Primary icon (tile). Works on light and dark backgrounds. Avatars, docs, app icons. |
| `favicon.svg` | Browser favicon. Same as the icon, with a slightly lifted tile in dark mode (`prefers-color-scheme`). |
| `logo-horizontal.svg` | Icon + wordmark, for light backgrounds. |
| `logo-horizontal-dark.svg` | Icon + wordmark, for dark backgrounds. |
| `logo-mono.svg` | Glyph only (no tile), single color, `currentColor`. For inline SVG that inherits text color. |
| `logo-mono-white.svg` | Glyph only, white. For photos or solid dark fills. |
| `social-card.svg` | 1200 × 630 Open Graph / social preview. |

> `currentColor` only inherits when the SVG is **inlined** in HTML. Loaded through `<img>` (including in GitHub READMEs), `logo-mono.svg` renders black. In that case, use `logo-mono-white.svg` or the tiled icon.

### README usage (light and dark)

GitHub supports `<picture>` with `prefers-color-scheme`:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/logo-horizontal-dark.svg">
  <img alt="Value-First Development" src="assets/brand/logo-horizontal.svg" width="360">
</picture>
```

### Wordmark

"Value-First" is set in IBM Plex Sans SemiBold (600), with tracking of -0.5 at 36 px. The hyphen is in the amber accent: it is the link between value and everything that comes first. "DEVELOPMENT" is set in IBM Plex Sans Medium (500) at 13 px, in uppercase with +3.2 tracking, in the muted color.

**Production note:** the wordmark SVGs use live `<text>` with a fallback stack (`'IBM Plex Sans', 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif`). An `<img>` SVG cannot load web fonts, so most viewers will see the fallback. That is acceptable for the repository, but before the brand is used on a website, print or anywhere else that needs pixel stability, **outline the text to paths** (for example Inkscape: *Path → Object to Path*, with IBM Plex Sans installed) and commit `logo-horizontal-outlined.svg` variants.

### Clear space and minimum size

- **Clear space:** keep a margin of at least **half the icon's height** on all sides (about 0.5 × the tile). Nothing else should enter it: no text, no edges, no other logos.
- **Minimum sizes:** icon at **16 px** (favicon) and 24 px elsewhere; horizontal logo at **160 px wide** (below that, "DEVELOPMENT" stops being legible; use the icon alone instead).

### Don'ts

- Don't recolor the tile, swap the dot color, or add gradients, glows, shadows or outlines.
- Don't rotate, skew or stretch the mark, or change the V angle or stroke weight.
- Don't enlarge the dot or turn it into a face, sparkle or star.
- Don't use the light horizontal logo on dark backgrounds (the ink text drops to unreadable contrast). Use the `-dark` variant.
- Don't place the mark on busy photos without a solid backing.
- Don't set "Value-First" in a different typeface, or without its hyphen.
- Don't pair the mark with robots, circuit motifs or "AI magic" imagery.

## 2. Color

Teal is the primary color (steady, trustworthy, engineering). Amber is the accent, used sparingly (value, the outcome, "this matters"). Everything else is warm-neutral ink and paper.

Contrast ratios are WCAG 2.x relative-luminance ratios, computed with a script (sRGB linearization, `(L1 + 0.05) / (L2 + 0.05)`). **AA** means at least 4.5:1 for normal text, 3:1 for large text (24 px, or 18.66 px bold) and for non-text UI or graphics.

### Light theme

| Token | Hex | On bg `#FFFFFF` | On surface `#F5F6F3` | Use |
|---|---|---|---|---|
| `--vf-bg` | `#FFFFFF` | n/a | n/a | Page background |
| `--vf-surface` | `#F5F6F3` | n/a | n/a | Cards, "paper", social card |
| `--vf-ink` | `#16212B` | 16.32 | 15.05 | Body text, diagram strokes |
| `--vf-muted` | `#4F5D6A` | 6.76 | 6.23 | Secondary text, connectors |
| `--vf-border` | `#D5DAD9` | 1.41 | 1.30 | Decorative dividers only (never the only cue) |
| `--vf-primary` | `#0B6E63` | 6.13 | 5.65 | Links, primary fills, highlights |
| `--vf-primary-strong` | `#08564D` | 8.58 | 7.91 | Hover, emphasis |
| `--vf-on-primary` | `#FFFFFF` | 6.13 on primary | n/a | Text on primary fills |
| `--vf-accent` | `#A15708` | 5.41 | 4.99 | Amber **text** (AA) |
| `--vf-accent-mark` | `#C97A16` | 3.34 | 3.08 | Amber **graphics only** (3:1 non-text); not for body text |
| `--vf-accent-soft` | `#F5C26B` | 3.74 on primary | n/a | The value dot on teal |
| `--vf-success` | `#1D7A46` | 5.35 | 4.93 | Validated, done |
| `--vf-warning` | `#8F5B00` | 5.73 | 5.28 | Risk, needs attention |
| `--vf-danger` | `#B42318` | 6.57 | 6.06 | Blocking, failure |
| `--vf-info` | `#2F5F98` | 6.54 | 6.03 | Notes, neutral callouts |

### Dark theme

| Token | Hex | On bg `#0E151B` | On surface `#16212B` |
|---|---|---|---|
| `--vf-bg` | `#0E151B` | n/a | n/a |
| `--vf-surface` | `#16212B` | n/a | n/a |
| `--vf-ink` | `#E7ECEE` | 15.44 | 13.70 |
| `--vf-muted` | `#A3B0BA` | 8.30 | 7.37 |
| `--vf-border` | `#2C3A45` | 1.57 | 1.40 |
| `--vf-primary` | `#4CC2B0` | 8.45 | 7.50 |
| `--vf-primary-strong` | `#7DD8CA` | 10.99 | 9.75 |
| `--vf-on-primary` | `#0E151B` | 8.45 on primary | n/a |
| `--vf-accent` / `--vf-accent-mark` | `#F0AC4C` | 9.38 | 8.32 |
| `--vf-success` | `#5CCB8D` | 9.09 | 8.07 |
| `--vf-warning` | `#EBC05A` | 10.70 | 9.50 |
| `--vf-danger` | `#F4847A` | 7.38 | 6.55 |
| `--vf-info` | `#86B2E8` | 8.36 | 7.42 |

### Notes on contrast

- The logo tile `#0B6E63` reaches 6.13 against white and 3.09 against GitHub's dark background `#0D1117`. Both clear the 3:1 threshold for graphics, which is why one icon works on both. White on the tile is 6.13 and the amber dot on the tile is 3.74.
- Light-theme amber comes in two strengths. Use `--vf-accent` (`#A15708`, 5.41) for any text. Use `--vf-accent-mark` (`#C97A16`, 3.34) only for marks, rules, the wordmark hyphen and diagram highlights.
- Never rely on color alone for meaning (semantic states also need an icon or a word).

## 3. Typography

| Role | Font | Fallback stack |
|---|---|---|
| UI, headings, body | **IBM Plex Sans** (400, 500, 600) | `"IBM Plex Sans", "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif` |
| Code, specs, file names, diagram tags | **IBM Plex Mono** (400, 500) | `"IBM Plex Mono", "Cascadia Mono", "SFMono-Regular", Consolas, "Liberation Mono", monospace` |

Why this pairing:

- **Free and open.** Both are SIL Open Font License and available on Google Fonts, so contributors, forks and translations can use them without licensing questions.
- **Product meets engineering.** Plex was designed as a single superfamily: the grotesk sans and the mono share proportions, so prose and specs (the core artifacts of the method) sit together naturally. That is the brand's "bridge" expressed in type.
- **Calm and legible.** Plex Sans has a sober, slightly technical, editorial voice: it reads well in long documents and does not shout. It also covers Latin Extended, which PT and ES need.

Type scale: 1.25 ratio on a 16 px base (see `tokens.css`: 12.8, 14, 16, 20, 25, 31, 39, 49 px). Body line height 1.6 and headings 1.2. Keep line length at about 68 characters. Use sentence case for headings. Use uppercase only for small, tracked labels such as "DEVELOPMENT".

Loading on the web:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
```

## 4. Diagram style

Diagrams explain mechanisms (the loop, the value contract, who fills which gap). They are not decoration. One idea per diagram.

| Element | Rule |
|---|---|
| Canvas | Transparent background, so diagrams sit on any page. Align to an 8 px grid. |
| Stroke | **2 px** for shapes and primary connectors, 1.5 px for secondary and grouping lines. Stroke weight is not scaled per diagram; the canvas is resized instead. |
| Corners | **8 px** radius on boxes; pills only for loop stages. No drop shadows. |
| Arrows | Straight or orthogonal lines with an **open chevron head** (two strokes, about 8 px, round caps), not filled triangles. Use **dashed** (`6 6`) for feedback / "returns to" paths, such as learn → intent. |
| Labels | IBM Plex Sans **14 px** (minimum 12 px) for prose labels; IBM Plex Mono 14 to 18 px for artifact or stage names (`value spec`, `AGENTS.md`). Sentence case. Labels must stay horizontal. |
| Color | Ink for strokes and text, muted for connectors, white or transparent fills. Use **primary** for the single most important element (usually the value spec). Use **amber** at most once, to mark where value is created or measured. Semantic colors only for real states (validated, risk, blocked). |
| Density | At most about 7 nodes. If it needs more, split it. |

### Light and dark compatibility

For SVG embedded inline (docs site), use CSS variables with `currentColor` as the base:

```svg
<svg viewBox="0 0 400 120" style="color: var(--vf-ink)">
  <rect x="8" y="40" width="140" height="40" rx="8"
        fill="var(--vf-diagram-fill, transparent)" stroke="currentColor" stroke-width="2"/>
  <rect x="252" y="40" width="140" height="40" rx="8"
        fill="var(--vf-primary, #0B6E63)" stroke="var(--vf-primary, #0B6E63)" stroke-width="2"/>
  <path d="M156 60 H244" stroke="var(--vf-muted, #4F5D6A)" stroke-width="2" fill="none"/>
</svg>
```

For SVG files loaded with `<img>` (GitHub), variables do not inherit. Do one of the following:

1. Put a `<style>` inside the SVG with `@media (prefers-color-scheme: dark)` overrides (as `favicon.svg` does), or
2. Export a `-dark.svg` twin and switch with `<picture>`.

Check every diagram on `#FFFFFF` and on `#0D1117` before committing.

## 5. Voice in visuals

- **Invitation, not critique.** Visuals never show Scrum, ceremonies or past methods as broken, crossed out or on fire. Show the path forward: a loop that closes, a gap that gets bridged.
- **Honest about AI.** Show AI as one tool in the loop (for example a "prototype" step), with human review visible. No sparkles, glowing brains, robots or magic wands.
- **Evidence over drama.** No fake metrics, unlabeled charts or "10x" call-outs. If a number appears, it has a source.
- **Quiet confidence.** Generous whitespace, one highlight per composition, plain words on labels (`validate`, not `supercharge`).
- **Bilingual parity.** Every diagram with text has PT and EN versions with the same structure. Leave room: Portuguese labels run about 20–30% longer.
