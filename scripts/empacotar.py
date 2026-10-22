"""Gerar um pacote completo e reproduzível para distribuição aos clientes."""
import hashlib
import json
from pathlib import Path
import zipfile

raiz = Path(__file__).resolve().parents[1]
manifesto = json.loads((raiz / 'plugin.json').read_text(encoding='utf-8'))
legado = json.loads((raiz / '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
versao = manifesto['version']
assert versao == legado['version'], 'Versões dos manifestos divergentes.'
arquivos = [raiz / p for p in ('plugin.json', '.codex-plugin/plugin.json', 'README.md', 'CHANGELOG.md', 'docs/GUIA-DO-CLIENTE.md', 'docs/MANUTENCAO.md', 'scripts/empacotar.py')]
for pasta in ('assets', 'skills'):
    arquivos.extend(p for p in (raiz / pasta).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc')
destino = raiz / 'dist'
destino.mkdir(exist_ok=True)
pacote = destino / f'saas-design-ui-system-{versao}.zip'
with zipfile.ZipFile(pacote, 'w', zipfile.ZIP_DEFLATED) as zipado:
    for arquivo in sorted(arquivos):
        info = zipfile.ZipInfo(arquivo.relative_to(raiz).as_posix(), (2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        zipado.writestr(info, arquivo.read_bytes())
resumo = hashlib.sha256(pacote.read_bytes()).hexdigest()
(destino / 'SHA256SUMS.txt').write_text(f'{resumo}  {pacote.name}\n', encoding='utf-8')
print(f'Pacote gerado: {pacote.name} ({pacote.stat().st_size} bytes)')
