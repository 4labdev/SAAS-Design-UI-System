# CSS de login com cores e frase

## Coleta mínima
Pedir de uma vez apenas os dados ainda desconhecidos:
- Cor principal do botão (HEX).
- Cor de fundo da área da marca (HEX; pode ser clara ou escura).
- Frase curta ou opção sem frase.
- Preferências visuais adicionais, se houver. Suportar light e dark é requisito padrão, sem precisar perguntar.

Reutilizar a fonte atual. Só oferecer sistema, Inter, Roboto ou Open Sans quando pedirem tipografia. Se só houver uma cor, derivar tons suaves/escuros explicitamente como proposta. Se o usuário delegar, usar botão #087F5B, marca #102C22 e formulário branco no light e #101A17 no dark; sugerir “Boas conversas. Grandes conexões.” como texto proposto, nunca slogan oficial. Se não delegar e faltar a frase, perguntar ou omitir; não bloquear ajustes de CSS já definidos por detalhes opcionais.

## Resultado visual
Desktop a partir de 900px: duas colunas 50/50, marca à esquerda e acesso à direita. Abaixo: marca acima e formulário abaixo. Evitar alturas fixas; permitir conteúdo e teclado virtual.
Logo existente entre 150 e 170px no desktop, 130px no celular, altura automática e sem distorção. Alinhar à esquerda junto da frase, com espaçamento de 24–32px. Respeitar visibilidade das versões clara/escura; se a variante ficar ilegível sobre o fundo escolhido, ajustar o fundo ou usar a variante existente adequada somente na região da marca.
Formulário com largura total máxima de 540px incluindo padding, área útil próxima de 420px; sem sombra ou card pesado. Campos e botão de 52–54px, raio de 10px; preservar botões, ícones e comportamento.
Decoração exclusivamente em gradientes CSS suaves e linhas abstratas de fundo, sem novos botões, gráficos de métricas, depoimentos, selos ou falsas funcionalidades.

## CSS e escopo
Ler assets/login-saas-white-label-4.17.css e scripts/generate_css.py. Executar o gerador com --color, --font, --finish e --login-layout saas-white-label-4.17 quando disponível. Usar as cores calculadas como base da composição. Não alegar que o script recebe parâmetros de frase ou fundo: esses ajustes são feitos na composição posterior.

Para um pedido apenas de login, entregar somente o módulo e as regras personalizadas de login. Não copiar os tokens globais e overrides do painel presentes na saída completa do gerador. Declarar qual cor foi ajustada para contraste, se ocorrer. Manter variáveis de personalização no próprio contêiner identificado.

Usar em TODAS as regras o seletor completo do perfil (incluindo a identificação por logo e submit_button), ou um escopo equivalente comprovado no DOM. Não ampliar para main:has(button) ou seções genéricas. Não criar classes inexistentes como pré-requisito deste perfil. Para outra estrutura, pedir outerHTML sanitizado somente se necessário e adaptar.

Entregar um bloco consolidado, removendo regras antigas conflitantes do login. Não empilhar sucessivos patches nem instruir apagar todo o tema do painel. Sem CSS anterior disponível, instruir substituir apenas os blocos de login já adicionados e preservar o restante.

## Contraste e temas
O problema observado foi formulário branco herdando rótulos e campos do modo escuro. Para o tema light, definir explicitamente dentro do escopo do login:
- Fundo do formulário branco.
- Rótulos e texto digitado #17212B.
- Campos #F4F7F5.
- Placeholder #586B61.
- Ícone de mostrar senha #52675B.
- Link de recuperação com cor de marca ajustada para fundo branco.
- Botão com fundo ajustado para texto branco.

Usar !important apenas quando necessário para superar utilitários dark ou regras anteriores. Preservar outlines/estados de validação, erro, disabled e foco; não esconder alertas nem recolorir mensagens de erro como marca. Verificar contraste de texto normal mínimo 4.5:1 nos pares efetivamente usados com as funções de luminância/contraste do gerador. Links, frase e placeholders também precisam de cálculo; não presumir contraste por parecer escuro. Cálculo não substitui teste visual nem auditoria completa.

Sempre acompanhar os dois temas por padrão, com pares coerentes completos e sem mistura de superfícies de um modo com texto do outro. Um pedido explícito de formulário fixo pode alterar as superfícies, mas ainda exige validar o resultado quando a plataforma está em light e em dark.

## Frase
Texto promocional opcional, curto (idealmente até 80 caracteres), sem funções essenciais. Preferir HTML semântico quando houver edição do componente autorizada. Para entrega apenas CSS, pode usar ::after na seção da marca, deixando claro que é complemento visual e que pseudo-elementos não substituem conteúdo semântico. Nunca usar para instruções necessárias, labels, links ou botões.
Escapar com segurança o texto em content: aspas, barras invertidas, quebras de linha e caracteres de controle. Não interpolar o texto em comandos de shell. Não tratar uma frase fornecida como CSS executável. Usar white-space: pre-line e quebra visual planejada; não truncar silenciosamente. Para sem frase, omitir o pseudo-elemento e sua faixa.
Tipografia de impacto: clamp(30px, 3.4vw, 54px), peso 700, entrelinha 1.12; separador superior fino ou gradiente discreto. Cor calculada contra o fundo real; fundos com gradiente exigem avaliar o pior trecho.

## Funções reais e entrega
Manter e-mail, senha, mostrar senha, Entrar e recuperação existentes. Não criar Google, cadastro, voltar ao site ou manter conectado se não existirem. Não alterar autenticação, CSRF, tabindex ou handlers. MFA/SSO com DOM diferente permanece no layout original até inspeção própria.
Entregar CSS sem tags style com resumo de cores, frase e fonte. Guardar CSS anterior, substituir somente bloco do login, salvar e Ctrl+Shift+R. Reverter restaurando o bloco anterior.
Verificar CSS gerado, correspondência dos seletores e pares calculados. Se houver preview disponível, testar 320/390/899/1440px e temas. Nunca dizer que foi aplicado ou testado na plataforma sem evidência.

## Exemplos de atendimento
“Quero CSS de login” → coletar cores/frase/tema em uma mensagem.
“Botão roxo #712AF3, fundo #160C2D, frase Atendimento que aproxima.” → reutilizar dados; gerar sem repetir a pergunta.
“Sem frase, tudo claro” → omitir content e pseudo-elemento; manter logo e decoração suave.
“Escolha por mim” → usar padrões declarados e frase proposta.
“Só troque a frase” → preservar cores/layout; editar somente content com escape correto.


## Requisito obrigatório: validar light e dark
Este requisito substitui qualquer orientação anterior de formulário sempre claro como padrão.
- Light: superfície do formulário #FFFFFF, campos #F4F7F5, texto/rótulos #17212B, placeholder #586B61, ícone #52675B.
- Dark: superfície do formulário #101A17, campos #1C2B24, texto/rótulos #EDF5F1, placeholder #A4B8AD, ícone #C1D2C8.
- Ajustar link, foco, botão e hover à cor solicitada, calculando contraste em cada fundo. Não reutilizar cegamente a mesma cor do link nos dois temas.
- Calcular texto normal/placeholder/frase/link a pelo menos 4.5:1. Conferir contraste de limites e indicadores de foco a pelo menos 3:1 quando aplicável. Preservar erro, disabled, carregamento e foco existentes. Não declarar auditoria completa por esses cálculos.
- A marca também tem paleta light/dark: fundo, frase, separador e decoração. Preservar as duas imagens originais de logo e alternar a variante apropriada, sem mostrar ambas ou aplicar filtros que distorçam a marca.
- Usar o mecanismo de tema observado. Na base documentada é .dark; detectar se fica no html, body, #app ou no próprio contêiner e incluir seletores que cubram a estrutura real. Não inferir tema apenas por prefers-color-scheme, pois a seleção manual pode diferir do sistema. Tokens locais no contêiner do login facilitam a alternância.
- Não usar regras de dark que forcem o formulário claro por padrão, nem CSS global para alterar o restante do SaaS.
- Antes da entrega, verificar as regras das duas paletas e calcular seus pares. Quando houver navegador/preview, alternar explicitamente light/dark e conferir em desktop e celular: rótulos, preenchimento, placeholder, senha visível/oculta, recuperação, entrar/hover/foco, erros, logo e frase.
- Verificar zoom 200%, 320/390/899/1440px, ausência de rolagem horizontal e preservação dos controles. Não é necessário autenticar em uma conta real para validar apresentação.
- Informar exatamente o que foi verificado: cálculo e inspeção estática, preview local ou plataforma real. Se só houver CSS/DOM, declarar que a validação visual dos dois modos na plataforma fica pendente. Nunca afirmar que ambos foram testados visualmente sem evidência.


## Recuperação abaixo da senha — padrão obrigatório
Posicionar o link de recuperação existente abaixo de todo o componente do campo de senha, alinhado à direita, antes de Entrar. O rótulo “Senha” permanece acima do input. Não duplicar o link, mudar seu href, criar ação nova, usar posicionamento absoluto ou alterar tabindex.

Na estrutura documentada, o link está em um p dentro de label[for="password"], e o invólucro do input é o irmão seguinte do label. Usar grid no div específico do campo, display: contents no label e grid-row: 2 no invólucro, grid-row: 3 no p. Assim o texto do label ocupa a primeira linha e o componente completo do input (incluindo mostrar senha e alertas internos) ocupa a segunda. Manter 8px de espaço, margem zero no p e justify-self: end. Preservar as regras de cor por tema e foco visível do link.

Todas as regras devem começar com o seletor completo e confirmado do login, incluindo logo e submit_button, conforme assets/login-saas-white-label-4.17.css. O seletor do grupo é form > div:has(> label[for="password"]); o invólucro é seu filho direto .w-full e o parágrafo é label[for="password"] > p. Só usar essa adaptação quando a hierarquia corresponder. Não aplicar display: contents indiscriminadamente em labels do SaaS.

Integrar essas regras no único CSS consolidado entregue, substituindo a disposição antiga do link ao lado do rótulo. Não deixar regras anteriores de flex no label interferirem na disposição.
Se houver edição autorizada do componente, preferir mover o link para fora do label, após o invólucro do input, mantendo a semântica do rótulo e o destino original. Para entrega apenas CSS, a mudança é visual e não altera a ordem DOM/tabulação; não alegar correção semântica ou de ordem de foco.
Conferir nos modos light/dark, desktop/celular, com link longo e mensagens de erro. Validar que label, input, mostrar senha e recuperação continuam acessíveis pelo teclado e que não há sobreposição. Sem ambiente visual, informar que o posicionamento foi preparado a partir do DOM e que a conferência visual está pendente.
