---
name: cw-design-ui-system
description: "Gerar ou ajustar CSS para DASHBOARD_STYLE_CSS de SaaS White Label, escolhendo cor principal, tipografia e acabamento. Usar quando o cliente pedir tema, personalização visual, cores, fontes ou correção do CSS do painel, ou personalização da tela de login em duas colunas com SAAS Design UI System, ou extrair cores de uma logo anexada para criar CSS."
---

# SAAS Design UI System

Atender em português brasileiro, com linguagem simples. Entregar CSS utilizável, não só dicas. Este plugin é um gerador conversacional com skill e script Python; não é uma extensão instalada dentro do Chatwoot, não tem servidor e não modifica a plataforma do cliente.

## Entrada

Se houver pedido de cores a partir de uma logo, seguir primeiro o fluxo abaixo; não pedir HEX que possam ser obtidos do anexo.

1. Reaproveitar cor e fonte já fornecidas. Quando faltarem, perguntar numa única mensagem: “Qual a cor principal da sua marca (HEX, como #087F5B) e qual fonte você prefere: sistema, Inter, Roboto ou Open Sans?” Explicar que sistema dispensa carregamento externo; as demais usam Google Fonts.
2. Se houver apenas um nome de cor, propor um HEX explicitamente como aproximação. Se o usuário pedir para decidir, usar #087F5B e sistema. Nunca atribuir este verde a uma identidade oficial de marca sem evidência.
3. Usar acabamento padrão `essential`: cores e tipografia. Oferecer `polished` quando solicitado (fundos levemente tingidos, cantos de 10px em botões de marca e foco). Não pedir novamente dados conhecidos. Quando a fonte não for suportada, oferecer as disponíveis; não inserir URLs arbitrárias nem prometer disponibilidade de fonte proprietária.
4. Não exigir acesso, credenciais, domínio, chave API ou HTML para gerar o tema padrão. Se versão/estrutura não forem conhecidas, declarar que se usa a base SaaS White Label baseado em Chatwoot 4.14.5.2, sem garantia para outros forks.

## Geração

Ler [compatibilidade](references/compatibility.md). Executar o script incluído a partir do caminho real desta skill:

```bash
python3 scripts/generate_css.py --color '#087F5B' --font Inter --finish essential --output /caminho/absoluto/cw-dashboard-theme.css
```

Resolver `scripts/generate_css.py` relativamente à pasta desta skill, não ao diretório atual. O script usa apenas biblioteca padrão Python, não precisa de rede, normaliza HEX, rejeita entradas inválidas e calcula contraste. `--font` aceita `system`, `Inter`, `Roboto`, `Open Sans`. `--finish` aceita `essential` ou `polished`. Escrever em uma pasta de trabalho, nunca sobre o código do plugin. Salvar o CSS gerado pelos mecanismos de arquivos disponíveis no ambiente. Ler o resumo JSON do script e informar quando a cor de botão tiver sido escurecida para contraste com texto branco. Não alegar que o contraste de toda a aplicação foi auditado: o cálculo cobre pares específicos do tema.

Usar o resultado literal do gerador como base. Se houver CSS anterior do cliente, inspecionar antes de integrar: preservar regras independentes, remover blocos de tema duplicados, mover @import para o início e explicar conflitos materiais. Não substituir silenciosamente personalizações alheias. Sem Python disponível, ler o script e a referência, gerar CSS manual equivalente e declarar que o gerador não foi executado; nunca inventar resultados de testes ou ratios.

## Entrega

Entregar um CSS completo, sem tags <style>, por bloco de código e/ou arquivo .css acessível. Usar arquivo quando o tamanho prejudicar a conversa. Incluir resumo curto de cor original, cor aplicada, fonte e acabamento, e estes passos:
- Guardar cópia do CSS atual.
- Substituir o conteúdo de DASHBOARD_STYLE_CSS pelo CSS completo gerado (ou informar que preservou regras anteriores se houve integração).
- Salvar e atualizar com Ctrl + Shift + R.
- Conferir conversas, configurações, formulários, menus e modais nos temas claro e escuro; para desfazer, restaurar o CSS anterior.

Fontes Google exigem acesso a fonts.googleapis.com e fonts.gstatic.com e podem ser bloqueadas por CSP/rede. O fallback permanece disponível. Não alegar que já instalou, aplicou, testou no painel ou tornou público algo que apenas gerou.

## Correções e limites

O HTML inicial contendo apenas <div id="app"></div> não é o DOM renderizado. Se um elemento não mudar, solicitar o outerHTML apenas desse elemento via Inspecionar, ou CSS relevante, e analisar seletores existentes. Screenshots mostram aparência, não classes. Remover segredos de qualquer material que vá entrar na entrega.

A alteração estrutural permitida é somente o layout opcional de login descrito abaixo, com escopo confirmado. Fora desse módulo, nunca usar seletor universal para fonte, alterar ícones/monospace, esconder ações, alterar pointer-events, position, z-index, overflow ou dimensões estruturais, nem transformar todas as mensagens/status em cor de marca. Preservar ruby/amber e cores de etiquetas, erros e avisos. Não usar CSS para controle de acesso. Evitar seletores por substring genérica. Não importar scripts ou acessar sistemas do cliente para aplicar o tema sem pedido expresso.


## Login em duas colunas

Quando pedirem login dividido, tela de acesso em duas colunas ou split login, ler [login em duas colunas](references/login-layout.md). Usar apresentação visual da marca à esquerda e formulário real à direita no desktop, proporção 50/50, e uma coluna abaixo de 900px. Reaproveitar cor e fonte conhecidas; sem definição, usar os padrões existentes sem bloquear a alteração do plugin ou o planejamento.

O gerador aceita `--login-layout two-column` (padrão `unchanged`). Esse módulo usa um contrato explícito de classes, não seletores confirmados do Chatwoot. Não afirmar que basta colar CSS para criar markup inexistente. Se só houver DASHBOARD_STYLE_CSS, obter o outerHTML sanitizado do contêiner do login e adaptar os seletores aos elementos existentes antes de declarar o CSS pronto para aquela instalação. Verificar também se esse campo carrega na rota pública; se não carregar, indicar o ponto de estilo do layout de autenticação no código da plataforma. Não exigir credenciais.

O arquivo de referência explica o contrato e a integração no componente. O CSS sozinho não cria uma coluna com conteúdo acessível. Não inventar textos oficiais, depoimentos, estatísticas ou URLs de imagens. Se faltar coluna visual no DOM, oferecer alteração do componente com autorização de edição, ou uma decoração CSS sem conteúdo essencial, claramente diferenciada do layout completo.

Preservar o formulário, submissão, CSRF, mensagens de erro, recuperação de senha, cadastro quando habilitado, SSO, MFA e ordem de tabulação. Não esconder controles nem substituir o formulário por HTML estático. Alterações de grid e dimensões ficam restritas às classes do módulo; não usar regras globais em body, #app, form ou inputs para dividir a tela. Entregar CSS integrado e instruções de aplicação e reversão. Informar separadamente teste do gerador e validação visual/funcional na plataforma.


### Perfil confirmado no HTML fornecido: SaaS White Label 4.17.1
Para a estrutura já fornecida nesta instalação, usar `--login-layout saas-white-label-4.17`. Ler a seção correspondente da referência. Esse perfil funciona sobre as duas sections existentes, sem adicionar classes ou editar o componente. Não pedir novamente o HTML já disponível. O modo two-column continua sendo um contrato alternativo para integração no componente. A exceção estrutural inclui os seletores específicos documentados do perfil saas-white-label-4.17. Informar que o CSS foi preparado a partir do DOM fornecido, sem alegar aplicação ou teste visual no painel.

## Fluxo conversacional: CSS personalizado de login

Ao pedir “CSS para login”, “personalizar acesso” ou equivalente, priorizar este fluxo em vez de perguntar apenas cor e fonte do painel. Ler [personalização do login](references/login-customization.md) e a referência de layout.

1. Reaproveitar dados já informados. Perguntar numa única mensagem somente o que faltar: “Quais cores você quer no botão e no fundo da área da marca (HEX)? Qual frase deseja ao lado da logo? Há alguma preferência visual adicional?” Fonte é opcional; manter a existente por padrão. Aceitar “sem frase” e “escolha por mim”.
2. Gerar CSS de login em duas colunas com logo menor, frase opcional e elementos decorativos discretos, sem criar controles. Não editar o plugin a cada tema solicitado: entregar o CSS ao usuário.
3. Usar o gerador para calcular as cores e o perfil saas-white-label-4.17 como base quando a estrutura corresponder. A personalização de cores de fundo, frase e contraste é uma etapa de composição documentada na referência; não inventar flags do script.
4. Pedidos somente de login devem entregar apenas regras com escopo do login, sem tokens :root/.dark globais ou alterações no painel. Manter o tema atual; substituir os blocos anteriores de login por um bloco consolidado.
5. O padrão obrigatório é acompanhar os modos light e dark da plataforma. Entregar paletas coerentes e validar contraste separadamente nos dois temas, incluindo formulário, marca, logo e controles. Não fixar o formulário em branco por padrão. Nunca misturar superfícies de um tema com textos herdados do outro.
6. Entregar CSS pronto sem tags style, resumo das cores e frase, instruções de backup, aplicação e reversão. Não alegar teste visual sem fazê-lo.


## Posicionamento White Label
Tratar o produto do cliente como SaaS White Label e usar sua própria marca, cores e frase. Não atribuir identidade de fornecedor à entrega. Manter SAAS Design UI System como nome deste plugin. Os perfis e tokens existentes são compatibilidade técnica com uma estrutura específica baseada em Chatwoot, não suporte universal a qualquer SaaS. Para outra estrutura, adaptar ao DOM fornecido sem inventar seletores. O perfil de login passa a se chamar saas-white-label-4.17; usar esse identificador nos comandos.


## Posição do link de recuperação
No CSS personalizado de login, posicionar o link real de recuperação abaixo do campo de senha, alinhado à direita, antes do botão Entrar. Aplicar em light e dark e em desktop/celular. Seguir a seção de recuperação em references/login-customization.md; não criar links nem alterar o destino ou a ordem de foco.

## Fluxo: criar CSS a partir da logo anexada

1. Pedir para anexar a logo na conversa somente se ela ainda não estiver disponível. Preferir PNG com transparência ou SVG; aceitar JPG e WebP legíveis. O atalho inicial usa os anexos da conversa, não um formulário de upload próprio. Se não conseguir abrir o arquivo, informar e pedir novo anexo; nunca inventar suas cores.
2. Inspecionar a logo antes de escolher a paleta. Quando houver ferramentas de leitura de imagem, amostrar cores dos pixels ou ler as cores declaradas de um SVG como dados, sem executar conteúdo ou buscar recursos externos. Ignorar pixels transparentes, fundo externo à marca, artefatos de compressão e suavização. Não confundir uma grande área branca com a cor principal. Se a análise for apenas visual, apresentar os HEX como aproximações, sem alegar extração exata.
3. Selecionar uma cor principal e, quando existir na logo, uma secundária. Mostrar os HEX e distinguir cores extraídas de tons derivados para fundos, hover e contraste. Respeitar cores explícitas fornecidas pelo usuário. Em logos monocromáticas, manter a proposta neutra; não inventar uma cor oficial de destaque.
4. Reaproveitar o destino já informado: painel, login ou ambos. Se faltar, perguntar somente “Quer aplicar as cores no painel, na tela de login ou nos dois?”. Não pedir confirmação da paleta se o usuário já solicitou gerar CSS. Manter fonte existente no login e usar sistema no painel quando não houver preferência; não tentar identificar uma fonte com certeza apenas pela logo.
5. Gerar o CSS pelo fluxo existente do destino escolhido, usando a principal no gerador e compondo os fundos conforme as referências. Para login, manter duas colunas no desktop, uma no celular, logo menor, frase opcional, decoração discreta, recuperação abaixo da senha à direita e suporte light/dark. Sem frase fornecida, omitir a frase sem impedir a entrega. Para login apenas, manter todo CSS restrito ao login.
6. Calcular contraste dos pares aplicados com as ferramentas disponíveis e ajustar os tons de interface quando necessário, explicando a diferença entre a cor da logo e a cor aplicada. Não recolorir nem distorcer o arquivo da logo. Não alegar validação de contraste ou teste visual que não foi executado.
7. Entregar o CSS completo e um resumo da paleta, fonte e destino, com as instruções existentes de aplicação e reversão. Anexar a logo para analisar cores não a instala na plataforma: preservar a logo já configurada; só orientar sua substituição se solicitado, sem inventar URL pública para o anexo.
