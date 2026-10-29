# Templates

Todos os templates são Markdown simples, então podem ser copiados para o seu repositório e lidos tanto por pessoas quanto por agentes de código.

| Template | Para que serve |
|---|---|
| [Value Spec](../../templates/pt/value-spec.md) | O artefato central. Uma por item relevante: problema, valor, critérios de sucesso, restrições, validação, decisões, verificação de valor e instruções para agentes. |
| [Value Spec: exemplo preenchido](../../templates/pt/value-spec-example.md) | Um exemplo fictício e ilustrativo para mostrar o nível de detalhe. |
| [Snippet de contexto para agentes](../../templates/pt/agents-snippet.md) | Um bloco para AGENTS.md / CLAUDE.md / rules que aponta os agentes para a Value Spec. |
| [Mapa de Valor](../../templates/pt/value-map.md) | Opcional, para iniciativas maiores que uma spec: o resultado e as Value Specs ordenadas que o movem. Guarde em `specs/README.md`. |

## Onde guardar as Value Specs

Um formato comum é uma pasta `specs/` na raiz do repositório, com um arquivo por spec: `specs/VS-014-invoice-download.md`. Se você usa Spec Kit ou Kiro, mantenha a Value Spec ao lado dos arquivos que essas ferramentas geram e ligue-os por meio de `links.design`.

## Usando o Mapa de Valor

Veja [Mapa de Valor](./value-map.md) para os três níveis, as quatro regras e uma sessão de 60 minutos. Também há um [mapa em branco para imprimir](https://andrelaf.github.io/value-first/pt/map.html). O canvas da v1 está em [docs/archive/v1](../archive/v1/pt/canvas/value-technology-alignment-canvas.svg).

Os templates da v1 (Matriz de Valor, Contrato de Flexibilidade) agora fazem parte da Value Spec. Os originais estão em [docs/archive/v1](../archive/v1/pt/templates.md).
