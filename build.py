# Note this file originated from ./scriptArchive/build_advanced2.py


pages = [
  {
    "content" : "content/index.html",
    "output" : "docs/index.html",
    "PAGE_TITLE" : "WELCOME",
    "ACTIVE_INDEX" : "active",
    "ACTIVE_SPACES" : "",
    "ACTIVE_EVENTS" : "",
    "ACTIVE_ABOUT" : "",
  },
  {
    "content" : "content/spaces.html",
    "output" : "docs/spaces.html",
    "PAGE_TITLE" : "SPACES",
    "ACTIVE_INDEX" : "",
    "ACTIVE_SPACES" : "active",
    "ACTIVE_EVENTS" : "",
    "ACTIVE_ABOUT" : "",
  },
  {
    "content" : "content/events.html",
    "output" : "docs/events.html",
    "PAGE_TITLE" : "EVENTS",
    "ACTIVE_INDEX" : "",
    "ACTIVE_SPACES" : "",
    "ACTIVE_EVENTS" : "active",
    "ACTIVE_ABOUT" : "",
  },
  {
    "content" : "content/about.html",
    "output" : "docs/about.html",
    "PAGE_TITLE" : "ABOUT",
    "ACTIVE_INDEX" : "",
    "ACTIVE_SPACES" : "",
    "ACTIVE_EVENTS" : "",
    "ACTIVE_ABOUT" : "active",
  },
]

def main():
  whole_page_template = open('templates/whole_page_template.html').read()
  from string import Template
  template = Template(whole_page_template)

  for page in pages:
    print("creating:", page["PAGE_TITLE"])
    print("----> Taking this content:",page["content"])
    page_content = open(page["content"]).read()
    full_page = template.safe_substitute(
      PAGE_TITLE=page["PAGE_TITLE"],
      ACTIVE_INDEX=page["ACTIVE_INDEX"],
      ACTIVE_SPACES=page["ACTIVE_INDEX"],
      ACTIVE_EVENTS=page["ACTIVE_INDEX"],
      ACTIVE_ABOUT=page["ACTIVE_INDEX"],
      PAGE_CONTENT=page_content 
    )
    print("----> Writing the output to", page["output"])
    open(page["output"], 'w+').write(full_page)
    print("------------------------")

  
if __name__ == "__main__":
  main()