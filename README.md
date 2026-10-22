# SAAS Design UI System

Crie CSS para o painel e a tela de login do seu SaaS White Label usando as cores, a tipografia e a logo da sua marca.

**Versão estável: 1.4.8** · Autor: Tayrone Dsan

## Página para clientes

A página de apresentação, download e primeiros passos está em [`docs/index.html`](docs/index.html), pronta para publicação no GitHub Pages a partir de **main → /docs**. Consulte [ativação e manutenção](docs/GITHUB-PAGES.md).

## Baixar o pacote

➡️ **[Baixar SAAS Design UI System 1.4.8 — ZIP completo](https://github.com/4labdev/SAAS-Design-UI-System/raw/refs/heads/main/dist/saas-design-ui-system-1.4.8.zip)**

[Ver releases](https://github.com/4labdev/SAAS-Design-UI-System/releases) · [Guia do cliente](docs/GUIA-DO-CLIENTE.md) · [Histórico de versões](CHANGELOG.md)

O ZIP contém o plugin completo, seus modelos CSS, gerador Python e documentação. Não é apenas uma atualização parcial. O arquivo `dist/SHA256SUMS.txt` permite conferir sua integridade. Se este repositório estiver privado, o download exige uma conta autorizada; o responsável também pode baixar o ZIP e enviá-lo ao cliente.

## O que você pode criar

| Opção | Resultado |
| --- | --- |
| Tema do painel | Cores da marca, tipografia e acabamento essencial ou refinado |
| Tela de login | Duas colunas no desktop, uma no celular, logo menor, frase opcional e decoração discreta |
| Tema a partir da logo | Análise das cores do anexo e CSS para painel, login ou ambos |
| Ajuste de CSS existente | Integração das personalizações com preservação das regras independentes |

O login acompanha os modos claro e escuro e posiciona o link real de recuperação abaixo da senha, à direita. O plugin mantém o formulário e seus controles. A compatibilidade depende do HTML da instalação; veja [compatibilidade](skills/cw-design-ui-system/references/compatibility.md).

## Começar pela conversa

Use o plugin em um ambiente compatível e envie um destes pedidos:

> Crie meu tema com a cor #087F5B e a fonte Inter.

> Crie o CSS para minha tela de login, com duas colunas e a frase “Conecte sua equipe”.

> Use a logo que anexei para extrair as cores e criar o CSS do login.

O anexo serve para analisar a paleta. Ele não substitui automaticamente a logo cadastrada na plataforma. Quando a leitura for apenas visual, os códigos HEX serão apresentados como aproximações.

## Usar o gerador local

Requisito: Python 3. O gerador não precisa de bibliotecas externas.

```bash
python3 skills/cw-design-ui-system/scripts/generate_css.py --color '#087F5B' --font Inter --finish essential --output tema-painel.css
```

No Windows, você pode substituir `python3` por `py`. Fontes disponíveis: `system`, `Inter`, `Roboto` e `Open Sans`. Acabamentos: `essential` e `polished`.

O script gera o tema a partir de uma cor; a análise da logo e a composição do CSS exclusivo de login são etapas do fluxo conversacional. Não existe uma opção de linha de comando para enviar a logo ao gerador.

## Aplicar com segurança

1. Guarde uma cópia do CSS atual.
2. Gere o CSS para a estrutura da sua plataforma.
3. Aplique em `DASHBOARD_STYLE_CSS`, quando esse campo estiver disponível e carregar na tela desejada.
4. Atualize com `Ctrl + Shift + R` e confira desktop, celular, modos claro e escuro e controles de acesso.
5. Para desfazer, restaure o CSS anterior.

CSS de login exige que os seletores correspondam ao HTML real. O perfil `saas-white-label-4.17` foi preparado para uma estrutura específica da versão 4.17.1; o perfil `two-column` exige as classes documentadas. Não há garantia universal para qualquer SaaS. Fontes Google dependem de acesso externo e das regras de CSP da plataforma.

## Documentação

- [Guia do cliente e instalação](docs/GUIA-DO-CLIENTE.md)
- [Manutenção e publicação de versões](docs/MANUTENCAO.md)
- [Compatibilidade do painel](skills/cw-design-ui-system/references/compatibility.md)
- [Layout do login](skills/cw-design-ui-system/references/login-layout.md)
- [Personalização do login](skills/cw-design-ui-system/references/login-customization.md)
- [Instruções do fluxo conversacional](skills/cw-design-ui-system/SKILL.md)

Este projeto gera CSS e orientações. Não acessa nem modifica a plataforma do cliente automaticamente. Baixar o pacote não publica o plugin no diretório público do ChatGPT. Não foi adicionada uma licença de código aberto; consulte o responsável para condições de uso e redistribuição.
