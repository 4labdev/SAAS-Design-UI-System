# Página do cliente — GitHub Pages

A página estática está em `docs/index.html`, com ícone em `docs/assets/icon.svg`. Não exige instalação de dependências nem build.

## Ativar a publicação

No repositório, abra **Settings → Pages**. Em **Build and deployment**, escolha **Deploy from a branch**. Selecione a branch **main**, a pasta **/docs** e clique em **Save**. Acompanhe a publicação na aba Actions. O endereço efetivo será exibido em Settings → Pages após a publicação.

## Atualizações

Edite `docs/index.html`. Depois do commit e envio para main, o GitHub Pages publicará as alterações automaticamente, desde que a configuração acima esteja ativa.

A versão do site é independente da versão do plugin. Os links atuais apontam para o pacote fixo 1.4.8. Para uma nova versão, publique e verifique o ZIP na release antes de atualizar número e links na página. Preserve a release anterior.

## Verificação

Confira navegação por âncoras, botão de download, exemplos para copiar, perguntas expansíveis e visual em desktop e celular. A ilustração do login é apenas uma demonstração visual, não uma captura da plataforma de um cliente. A página não recebe logos e não executa o gerador Python; orienta o uso do pacote em ambiente compatível.

Não anunciar compatibilidade validada com Claude enquanto o pacote adaptado não tiver sido testado.
