"""Deterministic, dependency-free CSS generator for the documented SaaS White Label base."""
import argparse
import json
import re
from pathlib import Path

FONTS = {'system': None, 'Inter': 'Inter', 'Roboto': 'Roboto', 'Open Sans': 'Open+Sans'}

def parse_color(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?', value):
        raise ValueError('Use uma cor HEX, como #087F5B ou #0A7.')
    h = value[1:]
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def mix(a, b, t):
    return tuple(round(x * (1-t) + y * t) for x, y in zip(a, b))

def lum(rgb):
    v = [x/255 for x in rgb]
    v = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in v]
    return sum(x*y for x,y in zip(v, (.2126, .7152, .0722)))

def contrast(a,b):
    x,y=sorted((lum(a),lum(b)))
    return (y+.05)/(x+.05)

def ensure_contrast(fg,bg,target):
    if contrast(fg,bg)>=4.5:return fg
    for i in range(1,1001):
        candidate=mix(fg,target,i/1000)
        if contrast(candidate,bg)>=4.5:return candidate
    raise ValueError('Não foi possível obter contraste suficiente.')

def channels(c): return ' '.join(map(str,c))
def hexcolor(c): return '#'+''.join(f'{n:02X}' for n in c)

def block(selector, values):
    return selector+' {\n'+''.join(f'  {k}: {v};\n' for k,v in values.items())+'}\n'

def generate(color, font='system', finish='essential', login_layout='unchanged'):
    if font not in FONTS: raise ValueError('Fonte não suportada.')
    if finish not in ('essential','polished'):raise ValueError('Acabamento não suportado.')
    if login_layout not in ('unchanged', 'two-column', 'saas-white-label-4.17'): raise ValueError('Layout de login não suportado.')
    seed=parse_color(color); white=(255,255,255); black=(0,0,0)
    darkbase=(17,25,22)
    solid=ensure_contrast(seed,white,black)
    hover=mix(solid,black,.14)
    lightbg=mix(seed,white,.90)
    textlight=ensure_contrast(solid,lightbg,black)
    darkbg=mix(seed,darkbase,.90)
    textdark=ensure_contrast(mix(seed,white,.55),darkbg,white)
    parts=[]
    if FONTS[font]:
        parts.append("@import url('https://fonts.googleapis.com/css2?family="+FONTS[font]+":wght@400;500;600;700&display=swap');\n")
    parts.append('/* SAAS Design UI System 1.4.0 | Base SaaS White Label 4.14.5.2\n'
                 f'   Cor solicitada: {hexcolor(seed)} | Botões: {hexcolor(solid)}\n'
                 f'   Fonte: {font} | Acabamento: {finish}\n'
                 '   Substituir o tema anterior em DASHBOARD_STYLE_CSS.\n'
                 '   Guardar uma cópia para restaurar. Validar na instalação. */\n')
    light={f'--blue-{i}':channels(mix(seed,white,t)) for i,t in enumerate((.985,.965,.90,.82,.72,.60,.43,.22),1)}
    light.update({'--blue-9':channels(solid),'--blue-10':channels(hover),'--blue-11':channels(textlight),'--blue-12':channels(mix(textlight,black,.30)),'--cw-brand-rgb':channels(solid),'--cw-brand-text-rgb':channels(textlight),'--cw-brand-hover-rgb':channels(hover),'--solid-blue':channels(mix(seed,white,.82)),'--solid-blue-2':channels(mix(seed,white,.965)),'--border-blue':', '.join(map(str,solid))+', .5','--border-blue-strong':channels(textlight),'--color-woot':hexcolor(solid),'--color-primary':hexcolor(solid),'--color-primary-dark':hexcolor(hover),'--color-primary-light':hexcolor(lightbg)})
    dark={f'--blue-{i}':channels(mix(seed,darkbase,t)) for i,t in enumerate((.985,.96,.90,.84,.76,.65,.52,.36),1)}
    dark.update({'--blue-9':channels(solid),'--blue-10':channels(hover),'--blue-11':channels(textdark),'--blue-12':channels(mix(textdark,white,.70)),'--cw-brand-text-rgb':channels(textdark),'--solid-blue':channels(darkbg),'--solid-blue-2':channels(mix(seed,darkbase,.96)),'--border-blue':', '.join(map(str,textdark))+', .5','--border-blue-strong':channels(textdark),'--color-primary-light':hexcolor(darkbg)})
    if finish=='polished':
        light.update({'--background-color':channels(mix(seed,white,.97)),'--surface-1':channels(mix(seed,white,.987)),'--surface-2':'255 255 255','--border-container':channels(mix(seed,white,.88)),'--border-weak':channels(mix(seed,white,.93)),'--border-strong':channels(mix(seed,white,.77))})
        dark.update({'--background-color':channels(mix(seed,darkbase,.97)),'--surface-1':channels(darkbase),'--surface-2':channels(mix(darkbase,white,.025)),'--border-container':channels(mix(darkbase,white,.12)),'--border-weak':channels(mix(darkbase,white,.08)),'--border-strong':channels(mix(darkbase,white,.20))})
    parts += [block(':root',light),block('.dark',dark)]
    parts.append((Path(__file__).resolve().parents[1]/'assets/brand-overrides.css').read_text())
    parts.append('''/* Hover de botões sólidos: manter contraste com rótulo branco. */
#app button.bg-n-brand:not(:disabled):not([aria-disabled="true"]):hover,
#app a.bg-n-brand:not([aria-disabled="true"]):hover {
  background-color: rgb(var(--cw-brand-hover-rgb)) !important;
}
''')
    stack='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    if font!='system':stack='"'+font+'", '+stack
    parts.append('/* Não alterar ícones, fontes monospace ou blocos de código. */\n'+block('body, #app, #app button, #app input, #app textarea, #app select, #app .font-sans',{'font-family':stack+' !important'}))
    if finish=='polished':
        parts.append('''/* Acabamento opcional, sem alterar dimensões ou posicionamento. */
#app button.bg-n-brand, #app a.bg-n-brand { border-radius: 10px; }
#app :where(button, a[href], input, textarea, select):focus-visible {
  outline: 2px solid rgb(var(--blue-11));
  outline-offset: 2px;
}
@media (prefers-reduced-motion: no-preference) {
  #app button.bg-n-brand, #app a.bg-n-brand {
    transition: background-color 150ms ease, border-color 150ms ease;
  }
}
''')
    if login_layout == 'two-column':
        parts.append((Path(__file__).resolve().parents[1]/'assets/login-two-column.css').read_text())
    if login_layout == 'saas-white-label-4.17':
        parts.append((Path(__file__).resolve().parents[1]/'assets/login-saas-white-label-4.17.css').read_text())
    css='\n'.join(parts)
    report={'requested_color':hexcolor(seed),'button_color':hexcolor(solid),'button_color_adjusted':solid!=seed,'font':font,'external_font':font!='system','finish':finish,'contrast_pairs':{'button_white':round(contrast(solid,white),3),'hover_white':round(contrast(hover,white),3),'text_light_on_soft':round(contrast(textlight,lightbg),3),'text_dark_on_soft':round(contrast(textdark,darkbg),3)},'compatibility':'Base SaaS White Label baseado em Chatwoot 4.14.5.2; validar na instalação do cliente.'}
    report['login_layout'] = login_layout
    report['login_integration_required'] = login_layout == 'two-column'
    report['login_dom_profile'] = 'SaaS White Label 4.17.1 fornecido pelo usuário' if login_layout == 'saas-white-label-4.17' else None
    return css,report

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--color',required=True)
    p.add_argument('--font',choices=list(FONTS),default='system')
    p.add_argument('--finish',choices=['essential','polished'],default='essential')
    p.add_argument('--login-layout',choices=['unchanged','two-column','saas-white-label-4.17'],default='unchanged')
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    try: css,report=generate(a.color,a.font,a.finish,a.login_layout)
    except ValueError as e:p.error(str(e))
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(css,encoding='utf-8')
    report['output']=str(a.output.resolve())
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
