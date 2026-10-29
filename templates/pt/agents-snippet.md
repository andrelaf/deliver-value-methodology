# Snippet de contexto para agentes

Cole o bloco abaixo no seu `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*.mdc` ou arquivo de steering do Kiro. Ajuste o caminho para onde ficam as suas Value Specs.

Arquivos de contexto são orientação, não imposição. Os agentes ainda podem ignorá-los, por isso a revisão humana continua valendo ([documentação do Claude Code](https://code.claude.com/docs/en/memory); [Böckeler, 2026](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)).

```markdown
## Value Specs (Value-First Development)

Este projeto usa Value Specs como fonte da intenção: `specs/VS-*.md`.

Antes de planejar ou alterar código de uma funcionalidade:
1. Encontre a Value Spec dela (pergunte se não houver uma). Leia as seções 1 a 9.
2. Implemente apenas o que os critérios de sucesso (SC-n) exigem, dentro do escopo.
   O que está fora do escopo é um limite rígido.
3. Se algo for ambíguo, contradisser o código ou tocar em uma Pergunta em
   aberto, pare e pergunte. Não escolha uma interpretação em silêncio.
4. Relacione cada tarefa e cada teste a um ou mais IDs de SC. Trabalho sem SC
   está fora do escopo.
5. Nas descrições de PR, inclua `Spec: <id>@<version>`, os IDs de SC cobertos,
   os IDs de SC ainda não cobertos e as premissas que você assumiu.
6. Não edite você mesmo o problema, o valor, os critérios, o escopo ou as
   restrições da spec. Proponha a mudança aos donos (Produto + Tech Lead).
7. Nunca enfraqueça autenticação, autorização, validação de entrada ou
   tratamento de segredos para fazer um critério passar. Sinalize o problema.
```
