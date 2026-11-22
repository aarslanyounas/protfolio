"""Builds resume.html from template.html, inlining brand-coloured icons and company logos."""
import re, html, json, base64, pathlib

ROOT = pathlib.Path(__file__).parent
LOGOS = ROOT / 'logos'
COLORS = json.loads((LOGOS / 'colors.json').read_text())


def icon(slug):
    f = LOGOS / f'{slug}.svg'
    if not f.exists():
        return None
    path = re.search(r'<path d="([^"]+)"', f.read_text()).group(1)
    color = '#' + (COLORS.get(slug) or '3a3936')
    return f'<svg viewBox="0 0 24 24" class="bi"><path fill="{color}" d="{path}"/></svg>'


def badge(text, color):
    return f'<span class="mono" style="background:{color}">{text}</span>'


def item(name, slug=None, mono=None, color='#3a3936'):
    ic = icon(slug) if slug else None
    return f'<li>{ic or badge(mono or name[:2], color)}<span>{html.escape(name)}</span></li>'


def ul(items):
    return '<ul class="tools">' + ''.join(item(*t) for t in items) + '</ul>'


def img(file):
    data = base64.b64encode((LOGOS / file).read_bytes()).decode()
    return f'<img src="data:image/png;base64,{data}" alt="">'


def svgfile(file):
    return (LOGOS / file).read_text()


def logo(inner):
    return f'<span class="clogo">{inner}</span>'


research = [('Ahrefs', None, 'Ah', '#054ADA'), ('Semrush', 'semrush'), ('Moz', None, 'Mz', '#1B7FCC'),
            ('Screaming Frog', None, 'SF', '#7CB342'), ('PageSpeed Insights', 'pagespeedinsights')]
analytics = [('Google Analytics 4', 'googleanalytics'), ('Google Search Console', 'googlesearchconsole'),
             ('Google Tag Manager', 'googletagmanager'), ('Looker Studio', 'looker'),
             ('Microsoft Clarity', None, 'Cl', '#0078D4'), ('Bing Webmaster Tools', None, 'B', '#008373')]
plugins = [('Rank Math', None, 'RM', '#7B3FE4'), ('Yoast SEO', 'yoast')]
platforms = [('WordPress', 'wordpress'), ('Shopify', 'shopify'), ('WooCommerce', 'woocommerce'),
             ('Webflow', 'webflow'), ('Wix', 'wix'), ('Squarespace', 'squarespace'),
             ('Framer', 'framer'), ('Magento', 'magento')]
ai = [('ChatGPT', 'openai'), ('Claude', 'claude'), ('Gemini', 'googlegemini'), ('Perplexity', 'perplexity')]
workflow = [('Jira', 'jira'), ('ClickUp', 'clickup'), ('Trello', 'trello'), ('Notion', 'notion'),
            ('Asana', 'asana'), ('HubSpot', 'hubspot')]

T = (ROOT / 'template.html').read_text()
repl = {
    '{{CYBER}}': logo(svgfile('cybernest-icon.svg')),
    '{{CLICK}}': '<span class="clogos">' + logo(svgfile('clicktap-icon.svg')) + logo(img('intelliscence.png')) + '</span>',
    '{{TN}}': logo(img('technerds.png')),
    '{{ID}}': logo(img('ideoversity.png')),
    '{{RESEARCH}}': ul(research), '{{ANALYTICS}}': ul(analytics), '{{PLUGINS}}': ul(plugins),
    '{{PLATFORMS}}': ul(platforms), '{{AI}}': ul(ai), '{{WORKFLOW}}': ul(workflow),
    '{{LINKEDIN}}': icon('linkedin'), '{{G}}': icon('google'), '{{GA}}': icon('googleanalytics'),
    '{{GADS}}': icon('googleads'), '{{HUB}}': icon('hubspot'), '{{LI}}': icon('linkedin'),
}
for k, v in repl.items():
    T = T.replace(k, v)
assert '{{' not in T, re.findall(r'{{\w+}}', T)
(ROOT / 'resume.html').write_text(T)
print('ok')
