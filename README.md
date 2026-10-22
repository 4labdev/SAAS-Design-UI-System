# SAAS Design UI System

Plugin baseado em **skill conversacional** para gerar e adaptar CSS de interfaces SaaS White Label. A partir de uma cor, tipografia ou logo, produz temas para a interface e a tela de login, preservando o escopo solicitado.

**Versão estável do pacote:** 1.4.8 · **Autor:** Tayrone Dsan

[Baixar o plugin (ZIP 1.4.8)](https://github.com/4labdev/SAAS-Design-UI-System/raw/refs/heads/main/dist/saas-design-ui-system-1.4.8.zip) · [Releases](https://github.com/4labdev/SAAS-Design-UI-System/releases) · [Guia de uso](docs/USO-DO-PLUGIN.md) · [Histórico](CHANGELOG.md)

## Apresentação em vídeo

[![Assistir ao vídeo de apresentação do SAAS Design UI System](https://img.youtube.com/vi/gvIcpga4sM4/hqdefault.jpg)](https://youtu.be/gvIcpga4sM4)

[▶ Assistir ao vídeo no YouTube](https://youtu.be/gvIcpga4sM4)

## Recursos do plugin

- **Temas CSS:** cores, tipografia e acabamento `essential` ou `polished`.
- **Login:** layout responsivo em duas colunas, personalização da área de marca e suporte aos temas claro e escuro.
- **Identidade visual:** leitura de uma logo anexada para propor uma paleta; cores aproximadas são identificadas como tal.
- **Adaptação:** integração com CSS existente e orientação sobre compatibilidade com estruturas HTML documentadas.
- **Gerador local:** script Python 3 sem dependências externas para temas baseados em uma cor HEX.

O plugin **gera arquivos e instruções**, mas não se instala na aplicação SaaS nem executa alterações remotas.

## Utilização

Carregue a skill da pasta `skills/cw-design-ui-system` em um ambiente que ofereça esse mecanismo. A disponibilidade de importação de plugins e skills depende de cada ambiente; **anexar o ZIP a uma conversa não equivale a instalar o plugin**.

Exemplos de solicitação:

> Crie um tema CSS com a cor #087F5B, fonte Inter e acabamento refinado.

> Gere somente o CSS do login, em duas colunas, com minha paleta e suporte aos modos claro e escuro.

> Analise a logo que anexei e proponha as cores para o tema, mostrando os códigos HEX.

Para executar apenas o gerador local:

```bash
python3 skills/cw-design-ui-system/scripts/generate_css.py --color '#087F5B' --font Inter --finish essential --output tema.css
```

No Windows, `py` pode substituir `python3`. Fontes disponíveis: `system`, `Inter`, `Roboto` e `Open Sans`. Acabamentos: `essential` e `polished`. A análise de logo e a composição conversacional de login não são opções de upload do gerador CLI.

## Organização do repositório

| Caminho | Conteúdo |
| --- | --- |
| `plugin.json` e `.codex-plugin/plugin.json` | Manifestos do plugin |
| `skills/cw-design-ui-system/SKILL.md` | Fluxo e instruções da skill |
| `skills/cw-design-ui-system/scripts/` | Gerador CSS |
| `skills/cw-design-ui-system/assets/` | Modelos CSS |
| `skills/cw-design-ui-system/references/` | Compatibilidade e composição de login |
| `docs/USO-DO-PLUGIN.md` | Instalação, execução e exemplos |
| `docs/MANUTENCAO.md` | Desenvolvimento e empacotamento |
| `dist/` | Artefato estável e checksum |

## Documentação técnica

- [Guia de uso do plugin](docs/USO-DO-PLUGIN.md)
- [Referência de compatibilidade](skills/cw-design-ui-system/references/compatibility.md)
- [Layout de login](skills/cw-design-ui-system/references/login-layout.md)
- [Personalização de login](skills/cw-design-ui-system/references/login-customization.md)
- [Manutenção e empacotamento](docs/MANUTENCAO.md)

**Limites:** a compatibilidade depende do DOM da plataforma e não é universal. A geração do CSS não comprova sua aplicação ou validação visual em uma instalação real. Fontes externas podem ser bloqueadas por política CSP. O pacote 1.4.8 é um artefato de versão fixa; ajustes na documentação do repositório não alteram retroativamente esse ZIP.

Este repositório não declara licença de código aberto. Consulte o responsável sobre uso e redistribuição.
