# Manutenção do plugin e publicação de versões

## Estrutura

- `plugin.json`: manifesto principal e versão.
- `.codex-plugin/plugin.json`: manifesto de compatibilidade.
- `skills/`: instruções, gerador, modelos e referências.
- `assets/`: ícones do plugin.
- `docs/`: documentação de uso do plugin e manutenção.
- `scripts/empacotar.py`: gera ZIP completo e soma SHA-256.
- `dist/`: pacotes prontos para baixar.

## Gerar o pacote

Na raiz do repositório, execute:

```bash
python3 scripts/empacotar.py
```

O script confere a versão dos dois manifestos e inclui somente os componentes do plugin, README, histórico e guia de uso do plugin. Não inclui Git, credenciais, arquivos temporários, releases anteriores nem o próprio diretório `dist` dentro do ZIP. O conteúdo original da versão 1.4.8 é preservado; comentários internos do gerador podem citar uma versão anterior do módulo.

## Publicar uma versão

1. Atualize os dois manifestos com a mesma versão e registre as mudanças no histórico.
2. Atualize o link e a versão destacada no README e os exemplos do guia.
3. Valide o gerador e gere novamente o pacote.
4. Faça commit das alterações e publique na branch `main` quando autorizado.
5. O workflow de release detecta a versão do manifesto, confere o pacote e cria a release `v<VERSÃO>` com ZIP e checksum. A release criada é marcada como mais recente.

O workflow usa o token temporário do GitHub Actions com permissão de escrita em conteúdo. Uma release já existente não é sobrescrita: correções devem usar uma nova versão. Também é possível iniciar o workflow manualmente pela aba Actions.

## Verificar integridade

Em Linux:

```bash
cd dist
sha256sum -c SHA256SUMS.txt
```

Em PowerShell:

```powershell
Get-FileHash .\dist\saas-design-ui-system-1.4.8.zip -Algorithm SHA256
Get-Content .\dist\SHA256SUMS.txt
```

Compare os valores. A validação local não substitui o teste visual e funcional na plataforma do cliente.

## Disponibilização do plugin

O pacote pode ser distribuído pelo ZIP publicado na release. O repositório público não equivale à publicação automática do plugin em um diretório de terceiros. A versão 1.4.8 permanece um artefato histórico fixo; mudanças na documentação só integrarão um novo ZIP quando uma nova versão for empacotada.
