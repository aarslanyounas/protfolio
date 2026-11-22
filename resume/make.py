import re, html, pathlib
SI=pathlib.Path('/tmp/claude-0/-home-user-protfolio/b391e7b5-1752-5da5-8646-050b5cc2145b/scratchpad/si/node_modules/simple-icons/icons')
LOGOS=pathlib.Path('logos'); LOGOS.mkdir(exist_ok=True)
# keep a copy of the brand icons inside the repo so the resume can be rebuilt later
def si(slug):
    f=SI/f'{slug}.svg'
    if f.exists():
        (LOGOS/f'{slug}.svg').write_text(f.read_text())
    f=LOGOS/f'{slug}.svg'
    if not f.exists(): return None
    p=re.search(r'<path d="([^"]+)"',f.read_text()).group(1)
    return f'<svg viewBox="0 0 24 24" class="bi"><path d="{p}"/></svg>'
def mono(t): return f'<span class="mono">{t}</span>'
def item(name, slug=None, m=None):
    ic=si(slug) if slug else None
    return f'<li>{ic or mono(m or name[:2])}<span>{html.escape(name)}</span></li>'

cyber=pathlib.Path('logos/cybernest-icon.svg').read_text() if pathlib.Path('logos/cybernest-icon.svg').exists() else ''
click=pathlib.Path('logos/clicktap-icon.svg').read_text() if pathlib.Path('logos/clicktap-icon.svg').exists() else ''
def comp(svg, letters): return f'<span class="clogo">{svg}</span>' if svg else f'<span class="clogo m">{letters}</span>'

tools_research=[('Ahrefs',None,'Ah'),('Semrush','semrush'),('Moz',None,'Mz'),('Screaming Frog',None,'SF'),('PageSpeed Insights','pagespeedinsights')]
tools_analytics=[('Google Analytics 4','googleanalytics'),('Google Search Console','googlesearchconsole'),('Google Tag Manager','googletagmanager'),('Looker Studio','looker'),('Microsoft Clarity',None,'Cl'),('Bing Webmaster Tools',None,'Bi')]
tools_plugins=[('Rank Math',None,'RM'),('Yoast SEO','yoast')]
platforms=[('WordPress','wordpress'),('Shopify','shopify'),('Webflow','webflow'),('Wix','wix'),('Framer','framer'),('Google Business Profile','google')]
ai=[('ChatGPT','openai'),('Claude','claude'),('Gemini','googlegemini'),('Perplexity','perplexity')]
workflow=[('Jira','jira'),('ClickUp','clickup'),('Trello','trello'),('Notion','notion'),('Asana','asana'),('HubSpot','hubspot')]
def ul(items,cls='tools'): return f'<ul class="{cls}">'+''.join(item(*t) for t in items)+'</ul>'

T=pathlib.Path('template.html').read_text()
out=(T.replace('{{CYBER}}',comp(cyber,'CN')).replace('{{CLICK}}',comp(click,'CT')).replace('{{TN}}',comp('','TN')).replace('{{ID}}',comp('','ID'))
 .replace('{{RESEARCH}}',ul(tools_research)).replace('{{ANALYTICS}}',ul(tools_analytics)).replace('{{PLUGINS}}',ul(tools_plugins))
 .replace('{{PLATFORMS}}',ul(platforms)).replace('{{AI}}',ul(ai)).replace('{{WORKFLOW}}',ul(workflow))
 .replace('{{LINKEDIN}}',si('linkedin')).replace('{{G}}',si('google')).replace('{{GA}}',si('googleanalytics')).replace('{{GADS}}',si('googleads') or si('google')).replace('{{HUB}}',si('hubspot')).replace('{{LI}}',si('linkedin')))
pathlib.Path('resume.html').write_text(out)
print('ok')
