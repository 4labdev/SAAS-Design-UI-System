# Base e limites

Base: CSS de uma instalação SaaS White Label com APP_VERSION 4.14.5.2, inspecionado em 21/10/2026. O cliente confirmou a aplicação das cores no painel. Não se testaram todas as telas, variantes e forks. Não declarar compatibilidade universal com Chatwoot.

Tokens confirmados: --blue-1 a --blue-12, --solid-blue, --solid-blue-2, --border-blue, --border-blue-strong. Tokens blue/solid usam canais RGB separados por espaços; --border-blue usa vírgulas e alfa. Tema escuro usa .dark. --text-blue é texto comum, não cor de marca: não substituir. --n-brand não é o token central de cor nesta base.

Classes n-brand incluem cores fixas #2781f6 e rgb(39 129 246 / alpha), além de variantes hover, focus, checked, dark e pseudo-elementos. O arquivo assets/brand-overrides.css contém overrides derivados dessas classes, preservando estados e opacidades. Usar tokens de texto específicos com contraste adequado; não forçar texto de todo fundo de marca para branco indiscriminadamente.

Fonte: system usa system-ui e fallbacks locais. Inter, Roboto e Open Sans usam Google Fonts (pesos 400/500/600/700), sem baixar ou redistribuir arquivos de fontes. @import deve vir antes das regras CSS. O script não verifica a disponibilidade de rede do cliente. Fonte do sistema é a alternativa quando importações são bloqueadas.

O modo essential mantém superfícies originais; polished altera tokens de fundo/divisórias, cantos dos botões de marca e foco. Não modificar dimensões do layout. O foco existente permanece no modo essential. Não aplicar bordas globais a inputs: estados de erro podem existir via classes sem aria-invalid.

Cores: manter seed original para os tons suaves. Escurecer cor sólida quando necessário para contraste mínimo 4.5:1 com branco. Ajustar textos claros/escuros independentemente. O relatório de contraste refere-se aos pares definidos pelo gerador, não a um certificado de acessibilidade do painel.

Nunca incluir HTML bruto do cliente, tokens CSRF, configurações de conta, emails, endpoints privados ou dados de conversas no pacote ou CSS. Sem DOM renderizado não inventar seletor específico para sidebar, avatar, editor ou modal.


## Exceção opcional: layout do login
O módulo two-column permite grid e dimensões apenas no contrato .cw-login-layout e seus elementos. Essas classes são um contrato de integração novo, não classes verificadas da base 4.14.5.2. Ler references/login-layout.md. DASHBOARD_STYLE_CSS pode não ser carregado nas rotas públicas: verificar antes de orientar a instalação. O padrão unchanged não inclui esse módulo e mantém o comportamento anterior.
