# Guia do cliente

## Conteúdo do pacote

O arquivo `saas-design-ui-system-1.4.8.zip` contém os manifestos do plugin, ícones, uma skill conversacional, modelos CSS, referências de compatibilidade, gerador Python e esta documentação em português brasileiro.

## Como começar

1. Baixe e extraia o ZIP em uma pasta.
2. Se seu ambiente oferecer importação de plugins compatíveis, use o ZIP completo conforme as instruções desse ambiente. A disponibilidade dessa função varia; este pacote não garante instalação por upload em qualquer conta do ChatGPT.
3. Em ambientes que carregam skills locais, o componente está em `skills/cw-design-ui-system`. Instale-o pelo mecanismo de skills do seu ambiente, incluindo todos os arquivos de suporte.
4. Como alternativa independente da instalação do plugin, execute o gerador Python descrito no README.

Anexar o ZIP em uma conversa não equivale, por si só, a instalar o plugin permanentemente. O plugin original da conta do autor e este pacote distribuível são formas separadas de acesso.

## Escolher cores e fonte

Informe a cor principal em HEX, por exemplo `#087F5B`, e escolha `system`, `Inter`, `Roboto` ou `Open Sans`. A fonte do sistema dispensa download externo; as demais usam Google Fonts com fallback.

O acabamento `essential` aplica cores e tipografia. O `polished` também acrescenta fundos levemente tingidos, cantos e foco nos elementos previstos pelo tema.

## Criar pela logo

Anexe sua logo na conversa, preferencialmente PNG transparente ou SVG. JPG e WebP legíveis também podem servir. Diga se deseja personalizar o painel, o login ou os dois.

O fluxo identifica uma cor principal e, quando presente, uma secundária; apresenta os HEX e diferencia as cores observadas dos tons derivados para fundos e contraste. Se a análise for apenas visual, os HEX são aproximados. Logos monocromáticas mantêm uma proposta neutra, sem inventar uma cor oficial.

Exemplo:

> Extraia as cores desta logo e crie o CSS do login. Mantenha duas colunas, use a frase “Sua operação em um só lugar” e preserve a fonte atual.

A logo não será recolorida nem instalada automaticamente na plataforma.

## Personalizar o login

O fluxo de login mantém duas colunas no desktop e uma abaixo de 900 px, logo menor, frase opcional, decoração discreta, suporte claro/escuro e recuperação de senha abaixo do campo, à direita.

Antes de aplicar, é necessário que o HTML corresponda a um dos perfis documentados. Caso contrário, envie o `outerHTML` sanitizado do contêiner de login, obtido pelo Inspecionar do navegador. Uma captura de tela não revela os seletores. Não envie senhas, tokens ou dados pessoais.

Peça explicitamente “somente login” para receber CSS com esse escopo. O gerador de linha de comando produz tokens globais do painel mesmo quando inclui um módulo de login; seu resultado integral não deve ser tratado como CSS exclusivo de login. A composição restrita é feita pelo fluxo conversacional documentado.

## Aplicação e reversão

Salve o CSS anterior antes de substituir qualquer conteúdo. Se já houver personalizações, envie-as para integração em vez de acumular blocos duplicados. Aplique apenas CSS, sem tags `<style>`.

Confirme que `DASHBOARD_STYLE_CSS` é carregado na rota pública de login. Se não for, a plataforma precisará de um ponto de estilo no layout de autenticação, conforme sua implementação.

Após salvar, confira:

- Desktop e celular, nos modos claro e escuro.
- Campos, foco por teclado, mensagens de erro e botão Entrar.
- Recuperação de senha, cadastro, SSO e MFA, quando habilitados.
- Menus, modais e conversas se o painel também foi alterado.

Para desfazer, restaure o CSS salvo e atualize a página.

## Dúvidas comuns

**A cor ficou mais escura?** O gerador pode ajustar a cor dos botões para obter contraste com o texto branco. A entrega deve mostrar a cor solicitada e a aplicada.

**A fonte não carregou?** Verifique a política CSP e o acesso a `fonts.googleapis.com` e `fonts.gstatic.com`. O fallback continua disponível.

**O CSS não alterou um elemento?** Confira o carregamento do CSS e o HTML renderizado; envie o trecho relevante para ajuste dos seletores.

**Funciona em qualquer SaaS?** Não. Os perfis atendem às estruturas documentadas. Outras plataformas precisam de adaptação.

**Atualiza sozinho?** O ZIP é uma versão fixa. Para atualizar uma instalação feita pelo pacote, obtenha a nova versão e siga o procedimento do ambiente utilizado, preservando suas personalizações.
