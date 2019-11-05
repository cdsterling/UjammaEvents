top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

index_content = open('content/index.html').read()
about_content = open('content/about.html').read()
events_content = open('content/events.html').read()
spaces_content = open('content/spaces.html').read()

open('docs/index.html', 'w+').write(top + index_content + bottom)
open('docs/about.html', 'w+').write(top + about_content + bottom)
open('docs/events.html', 'w+').write(top + events_content + bottom)
open('docs/spaces.html', 'w+').write(top + spaces_content + bottom)

