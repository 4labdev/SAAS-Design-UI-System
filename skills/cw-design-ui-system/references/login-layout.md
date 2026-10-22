# Login em duas colunas

Este módulo é uma base de integração responsiva. Há um contrato genérico e um perfil baseado no DOM fornecido pelo cliente, descrito abaixo. Não alegar compatibilidade nativa comprovada.

## Contrato do componente
Aplicar as classes aos elementos existentes, sem duplicar formulários:
- `.cw-login-layout`: contêiner exclusivo da página de login.
- Filho direto `.cw-login-brand`: painel com logo e apresentação real da marca.
- Filho direto `.cw-login-main`: região de acesso.
- Filho direto desta região `.cw-login-form`: invólucro de todo o conteúdo de acesso, incluindo título, formulário, alertas e métodos alternativos. Não limitar a classe apenas aos inputs.

Estrutura conceitual (integrar no componente existente; não substituir seu conteúdo):
```html
<div class="cw-login-layout">
  <aside class="cw-login-brand"><!-- Logo e apresentação da marca --></aside>
  <main class="cw-login-main">
    <div class="cw-login-form"><!-- Conteúdo e formulário reais preservados --></div>
  </main>
</div>
```

Desktop a partir de 900px: duas colunas iguais, marca à esquerda. Abaixo: marca acima e acesso abaixo, sem esconder conteúdo. Altura mínima da viewport, sem altura fixa, recorte ou posicionamento absoluto. Permitir rolagem normal com teclado virtual e mensagens longas.

## Geração
```bash
python3 scripts/generate_css.py --color '#087F5B' --font system --login-layout two-column --output /caminho/absoluto/cw-theme.css
```
O padrão `--login-layout unchanged` mantém o tema sem alterações estruturais. O resumo JSON identifica o módulo e a exigência de integração. Usa a cor sólida calculada pelo tema com contraste mínimo de 4.5:1 contra branco; imagens ou novos fundos exigem nova verificação.

## Integração só por CSS
Primeiro confirmar se DASHBOARD_STYLE_CSS carrega no login e analisar outerHTML sanitizado do contêiner renderizado. Se as duas regiões já existirem, mapear as classes do contrato para seletores específicos observados, mantendo o escopo exclusivo do login. Não adivinhar seletores, usar :has(input[type=password]) como detector universal, ou alterar #app globalmente. Se não houver região de marca, CSS não cria conteúdo semântico: integrar no componente ou esclarecer a limitação e propor decoração sem texto essencial. Nunca colocar formulário, botão, título necessário ou links em pseudo-elementos.

## Validação e reversão
Conferir desktop, 899px, 390px e 320px, zoom 200%, temas claro/escuro e teclado virtual. Verificar ausência de rolagem horizontal, conteúdo longo, logo sem distorção, foco visível e ordem de tabulação. Exercitar envio, erro de credenciais, recuperação, SSO e MFA quando existentes. Sem acesso ao painel, informar que esses testes permanecem pendentes. Guardar CSS e componente anteriores; para reverter, restaurá-los ou gerar com unchanged e remover apenas as classes/markup adicionados.

## Evidência da instalação fornecida pelo usuário
O HTML inicial fornecido em 21/10/2026 informa APP_VERSION 4.17.1 e inclui /dashboard_style.css no head. O corpo contém apenas o ponto de montagem #app; portanto não confirma classes, hierarquia nem presença da coluna visual. A inclusão do arquivo confirma a referência ao stylesheet, mas não comprova o conteúdo servido ou sua aplicação. Não reutilizar configurações, tokens ou dados do HTML no pacote.

Para coletar a estrutura: abrir a tela de login, pressionar F12, usar a aba Elementos/Inspetor, selecionar o contêiner externo que envolve logo e formulário e escolher Copiar > Copiar outerHTML. Não usar Exibir código-fonte. Remover valores de campos, tokens e informações pessoais. Solicitar apenas esse trecho, não o documento inteiro.


## Perfil CSS direto: saas-white-label-4.17
O outerHTML renderizado fornecido confirma um main.flex.flex-col com duas sections filhas: a primeira contém as variantes clara/escura do logo; a segunda contém o formulário com button[data-testid="submit_button"]. O asset assets/login-saas-white-label-4.17.css usa essas duas regiões existentes. Não é necessário editar HTML para este perfil. Não armazenar o documento completo nem configurações da instalação.

Gerar com `--login-layout saas-white-label-4.17`. O seletor combina #app, main, logo com caminho observado e botão com data-testid, usando :has(). Sem suporte a :has(), as regras do perfil não se aplicam e permanece o layout anterior. O formulário e seu comportamento continuam os originais. O painel esquerdo usa fundo suave para preservar a legibilidade do logo existente, mantendo as classes de visibilidade claro/escuro. Sem textos inventados ou conteúdo em pseudo-elementos.

Desktop: duas colunas 50/50. Abaixo de 900px: logo acima e formulário abaixo. O CSS remove apenas margens, padding e sombra dos contêineres identificados, define grid e aplica cor da marca ao botão observado; não muda inputs, ordem de foco ou o botão de mostrar senha. Nenhuma validação visual ou autenticação real foi feita. MFA/SSO podem trocar o DOM: o seletor deixa de corresponder e preserva o layout original dessas etapas; não garantir duas colunas nelas sem HTML correspondente.

Para aplicar, guardar o CSS atual e acrescentar o asset ao final de DASHBOARD_STYLE_CSS para manter cores/fontes existentes, ou usar o tema completo gerado quando solicitado. Recarregar com Ctrl+Shift+R e conferir claro/escuro, 320/390/899/1440px, zoom e erros. Remover o bloco do perfil para reverter apenas o layout. Só solicitar novo HTML se a estrutura mudar ou o seletor não corresponder.


## Personalização com cores e frase
O perfil acima é a base estrutural. Para pedidos de cores, logo menor e frase, seguir [personalização do login](login-customization.md). Nesse fluxo, é permitido ajustar campos e usar frase promocional complementar em pseudo-elemento, conforme os limites da referência. Consolidar o CSS e manter todos os seletores restritos ao contêiner confirmado.


## Temas obrigatórios
Toda composição personalizada de login deve suportar e verificar light e dark conforme login-customization.md. O asset estrutural é apenas uma base; suas cores isoladas não constituem validação completa de ambos os modos. Substituir regras conflitantes por um único bloco consolidado com paletas e contraste por tema.
