# Templates

Todos os templates são Markdown simples, então podem ser copiados para o seu repositório e lidos tanto por pessoas quanto por agentes de código.

| Template | Para que serve |
|---|---|
| [Value Spec](../../templates/pt/value-spec.md) | O artefato central. Uma por item relevante: problema, valor, critérios de sucesso, restrições, validação, decisões, verificação de valor e instruções para agentes. |
| [Value Spec: exemplo preenchido](../../templates/pt/value-spec-example.md) | Um exemplo fictício e ilustrativo para mostrar o nível de detalhe. |
| [Snippet de contexto para agentes](../../templates/pt/agents-snippet.md) | Um bloco para AGENTS.md / CLAUDE.md / rules que aponta os agentes para a Value Spec. |
| [Canvas de Alinhamento Valor-Tecnologia](./canvas/value-technology-alignment-canvas.svg) | Ferramenta opcional de workshop para iniciativas maiores ([PNG](./canvas/value-technology-alignment-canvas.png), [exemplo preenchido](./canvas/value-technology-alignment-canvas-example.png)). |

## Onde guardar as Value Specs

Um formato comum é uma pasta `specs/` na raiz do repositório, com um arquivo por spec: `specs/VS-014-invoice-download.md`. Se você usa Spec Kit ou Kiro, mantenha a Value Spec ao lado dos arquivos que essas ferramentas geram e ligue-os por meio de `links.design`.

## Usando o Canvas

1. **Prepare.** Convide Produto, o Tech Lead e um ou dois stakeholders-chave. Reserve de 60 a 90 minutos.
2. **Preencham juntos**: primeiro os blocos de negócio, depois os técnicos e, por fim, os riscos.
3. **Transforme em Value Specs.** Cada resultado distinto vira uma spec candidata.
4. **Volte a ele** quando uma iniciativa mudar de direção.

Os templates da v1 (Matriz de Valor, Contrato de Flexibilidade) agora fazem parte da Value Spec. Os originais estão em [docs/archive/v1](../archive/v1/pt/templates.md).
