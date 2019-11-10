# Note this file originated from ./scriptArchive/build_advanced2.py


# This is a list of dictionaries that contain data about my pages
page_links = {
  "index_link" : "./index.html",
  "spaces_link" : "./spaces.html",
  "events_link" : "./events.html",
  "about_link" : "./about.html",  
}

pages = [
  {
    "content" : "content/index.html",
    "output" : "docs/index.html",
    "PAGE_TITLE" : "WELCOME",
    "page_link" : "./index.html",
    "ACTIVE_INDEX" : "active",
    "ACTIVE_SPACES" : "",
    "ACTIVE_EVENTS" : "",
    "ACTIVE_ABOUT" : "",
  },
  {
    "content" : "content/spaces.html",
    "output" : "docs/spaces.html",
    "page_link" : "./spaces.html",
    "PAGE_TITLE" : "SPACES",
    "ACTIVE_INDEX" : "",
    "ACTIVE_SPACES" : "active",
    "ACTIVE_EVENTS" : "",
    "ACTIVE_ABOUT" : "",
  },
  {
    "content" : "content/events.html",
    "output" : "docs/events.html",
    "page_link" : "./events.html",
    "PAGE_TITLE" : "EVENTS",
    "ACTIVE_INDEX" : "",
    "ACTIVE_SPACES" : "",
    "ACTIVE_EVENTS" : "active",
    "ACTIVE_ABOUT" : "",
  },
  {
    "content" : "content/about.html",
    "output" : "docs/about.html",
    "page_link" : "./about.html",
    "PAGE_TITLE" : "ABOUT",
    "ACTIVE_INDEX" : "",
    "ACTIVE_SPACES" : "",
    "ACTIVE_EVENTS" : "",
    "ACTIVE_ABOUT" : "active",
  },
]


# set template takes the file name of a template file, 
# reads it and uses that to creates a object of Type Template
def set_template(template_file):
  page_template = open(template_file).read()
  from string import Template
  my_template = Template(page_template)
  return my_template

# apply_template takes a Template object and all of the 
# template replacement strings for a page and returns 
# the new page with the templated values replaced with the replacement strings
def apply_template(page_template, content, title, aIndex, aSpaces, aEvents, aAbout):
  from datetime import datetime 
  print("applying template to:", title)
  print("----> Taking this content:",content)
  page_content = open(content).read()
  full_page = page_template.safe_substitute(
    PAGE_TITLE=title,
    ACTIVE_INDEX=aIndex,
    ACTIVE_SPACES=aSpaces,
    ACTIVE_EVENTS=aEvents,
    ACTIVE_ABOUT=aAbout,
    PAGE_CONTENT=page_content,
    COPYRIGHT_YEAR=datetime.now().year,
    INDEX_LINK=page_links["index_link"],
    SPACES_LINK=page_links["spaces_link"],
    EVENTS_LINK=page_links["events_link"],
    ABOUT_LINK=page_links["about_link"],

  )
  return full_page

# write_file takes html content (or really any content) and an output file to write to
def write_file(html_page, output):
  print("----> Writing the output to", output)
  open(output, 'w+').write(html_page)


# Main
def main():
  template = set_template('templates/whole_page_template.html')
  for page in pages:
    full_page = apply_template(template, page["content"], page["PAGE_TITLE"], page["ACTIVE_INDEX"], page["ACTIVE_SPACES"], page["ACTIVE_EVENTS"], page["ACTIVE_ABOUT"])
    write_file(full_page, page["output"])
    
  
if __name__ == "__main__":
  main()