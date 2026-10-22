# Guia de uso do SAAS Design UI System

Este documento trata **exclusivamente da utilização do plugin** para gerar CSS. O pacote reúne manifestos, uma skill conversacional, referências, modelos CSS e um gerador Python.

## Formas de executar

### Skill conversacional

1. Obtenha o [pacote estável](https://github.com/4labdev/SAAS-Design-UI-System/releases) e extraia-o.
2. Em um ambiente compatível com skills locais, configure a pasta `skills/cw-design-ui-system` conforme o mecanismo oferecido pelo próprio ambiente.
3. Envie um pedido informando o escopo desejado: tema, login ou ambos.

O ZIP **não é um instalador universal**, e anexá-lo a uma conversa não instala automaticamente o plugin. A disponibilidade de importação varia conforme o ambiente.

### Gerador Python

Requisito: Python 3, sem bibliotecas externas.

```bash
python3 skills/cw-design-ui-system/scripts/generate_css.py --color '#087F5B' --font Inter --finish essential --output tema.css
```

No Windows, é possível usar `py` no lugar de `python3`.

Parâmetros principais:
- `--color`: cor principal em hexadecimal.
- `--font`: `system`, `Inter`, `Roboto` ou `Open Sans`.
- `--finish`: `essential` (cores e tipografia) ou `polished` (acabamento visual adicional).
- `--output`: caminho do arquivo CSS gerado.

A análise de logo anexada e a composição personalizada do login pertencem ao fluxo conversacional. O script de linha de comando não recebe upload de logo nem uma frase promocional por parâmetro.

## Exemplos de solicitações

> Crie CSS com a cor #087F5B, fonte Inter e acabamento essencial.

> Personalize somente o login em duas colunas, com modo claro e escuro. Mantenha o formulário original.

> Extraia as cores da minha logo e crie um tema CSS. Identifique cores observadas e tons derivados.

> Integre o tema com meu CSS atual, preservando as regras que não conflitam.

## Resultado e cuidados

A saída é CSS, acompanhado quando necessário de paleta, opções selecionadas e informações de compatibilidade. O plugin não modifica aplicações, contas ou servidores automaticamente.

Guarde sempre uma cópia do CSS original antes de utilizar um tema gerado. Valide responsividade, acessibilidade, contraste e comportamento da interface no ambiente de destino. Para uma estrutura HTML diferente das referências, os seletores podem precisar de adaptação.

O perfil `saas-white-label-4.17` refere-se a um DOM específico; o perfil `two-column` exige um contrato de classes. Nenhum dos dois implica compatibilidade universal. Consulte [compatibilidade](../skills/cw-design-ui-system/references/compatibility.md), [layout de login](../skills/cw-design-ui-system/references/login-layout.md) e [personalização do login](../skills/cw-design-ui-system/references/login-customization.md).

Fontes Google dependem de conectividade e CSP. A leitura apenas visual de logos produz valores HEX aproximados, que devem ser identificados como estimativas.

## Versões

Consulte o [histórico](../CHANGELOG.md) e os [releases](https://github.com/4labdev/SAAS-Design-UI-System/releases). Cada ZIP publicado corresponde a uma versão fixa.
