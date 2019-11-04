top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()


#from string import Template
#template = Template(top)
#index_top=template.safe_substitute(PAGE_TITLE="About Me - Bob Ross", INDEX_ACTIVE="class=\"active\"", ART_ACTIVE="", BLOG_ACTIVE="")
#art_top=template.safe_substitute(PAGE_TITLE="Art - Bob Ross", ART_ACTIVE="class=\"active\"", BLOG_ACTIVE="", INDEX_ACTIVE="")
#blog_top=template.safe_substitute(PAGE_TITLE="Blog - Bob Ross", BLOG_ACTIVE="class=\"active\"", ART_ACTIVE="", INDEX_ACTIVE="")

index_content = open('content/index.html').read()
about_content = open('content/about.html').read()
events_content = open('content/events.html').read()
spaces_content = open('content/spaces.html').read()

open('docs/index.html', 'w+').write(top + index_content + bottom)
open('docs/about.html', 'w+').write(top + about_content + bottom)
open('docs/events.html', 'w+').write(top + events_content + bottom)
open('docs/spaces.html', 'w+').write(top + spaces_content + bottom)

