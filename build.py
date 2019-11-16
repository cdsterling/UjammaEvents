# Note this file originated from ./scriptArchive/build_advanced2.py


# This is a list of dictionaries that contain data about my pages
page_links = {
  "index_link" : "./index.html",
  "spaces_link" : "./spaces.html",
  "events_link" : "./events.html",
  "about_link" : "./about.html",  
}
events = [
  {
    "content" : "events/afro_comic_con.html",
    "output" : "docs/afro_comic_con.html",
    "EVENT_IMAGE" : "images/events/acc_logo.jpg",
    "EVENT_TITLE" : "Afro Comic Con",
    "EVENT_DATES" : "Nov 3-7 2019",
    "EVENT_SPACE_NAME" : "SAE Expression College",
    "EVENT_SPACE_ADDRESS" : "6601 Shellmound St, Emeryville, CA 94608",
    "EVENT_ORGANIZER" : "The Afro Comic Con Planning Committe",
    "EVENT_ORGANIZER_URL": "https://www.afrocomiccon.org/",
    "EVENT_EMAIL" : "acc-planning@gmail.com",
    "EVENT_MODAL_ID" :"afro_comic_con",
  },
  {
    "content" : "events/travel_more5.html",
    "output" : "docs/travel_more5.html",
    "EVENT_IMAGE" : "images/events/trvl_black_flyer.png",
    "EVENT_TITLE" : "Travel More Spend Less #5",
    "EVENT_DATES" : "August 25, 2019",
    "EVENT_SPACE_NAME" : "Kingston 11 Cuisine",
    "EVENT_SPACE_ADDRESS" : "2270 Telegraph Ave, Oakland, CA 94612",
    "EVENT_ORGANIZER" : "Traveling Black",
    "EVENT_ORGANIZER_URL": "https://traveling.black/",
    "EVENT_EMAIL" : "travelingblack@gmail.com",
    "EVENT_MODAL_ID" : "travel_more5",
  },
  {
    "content" : "events/black_to_yoga.html",
    "output" : "docs/black_to_yoga.html",
    "EVENT_IMAGE" : "images/events/black_to_yoga_flyer.jpg",
    "EVENT_TITLE" : "Yoga Informational Workshop and Practice for Men",
    "EVENT_DATES" : "November 10, 2019",
    "EVENT_SPACE_NAME" : "Queen Hippie Gypsie",
    "EVENT_SPACE_ADDRESS" : "337 14th St, Oakland, CA 94612",
    "EVENT_ORGANIZER" : "Men of Substance",
    "EVENT_ORGANIZER_URL": "https://www.facebook.com/MenOfSubstanceMag/",
    "EVENT_EMAIL" : "menofsubstancemag@gmail.com",
    "EVENT_MODAL_ID" : "black_to_yoga",
  },
   
]

spaces = [
  {
    "content" : "spaces/kingston11.html",
    "output" : "docs/kingston11.html",
    "SPACE_LOGO" : "./images/spaces/k11_logo2.png",
    "SPACE_NAME" : "Kingston 11 Cuisine",
    "SPACE_IMAGE" : "./images/spaces/k11_event_space.jpg",
    "SPACE_PAGE_LINK" : "./kingston11.html",
  },
  {
    "content" : "spaces/queen_hippie_gypsy.html",
    "output" : "docs/queen_hippie_gypsy.html",
    "SPACE_LOGO" : "./images/spaces/qhg_storefront.jpg",
    "SPACE_NAME" : "Queen Hippie Gypsy",
    "SPACE_IMAGE" : "./images/spaces/qhg_kyrah_eventspace.jpg",
    "SPACE_PAGE_LINK" : "./queen_hippie_gypsy.html",
  },
  {
    "content" : "spaces/SAE_Expression_College.html",
    "output" : "docs/SAE_Expression_College.html",
    "SPACE_LOGO" : "./images/spaces/sae_logo.jpg",
    "SPACE_NAME" : "SAE Expression College",
    "SPACE_IMAGE" : "./images/spaces/sae_outdoor.jpg",
    "SPACE_PAGE_LINK" : "./SAE_Expression_College.html",
  }


]

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
    "content" : "content/spaces_using_template.html",
    "output" : "docs/spaces.html",
    "page_link" : "./spaces.html",
    "PAGE_TITLE" : "SPACES",
    "ACTIVE_INDEX" : "",
    "ACTIVE_SPACES" : "active",
    "ACTIVE_EVENTS" : "",
    "ACTIVE_ABOUT" : "",
  },
  {
    "content" : "content/events_using_template.html",
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

# apply_fullpage_template takes a Template object and all of the 
# template replacement strings for a page and returns 
# the new page with the templated values replaced with the replacement strings
def apply_fullpage_template(page_template, content, page):
  from datetime import datetime 
  print("applying template to:", page["PAGE_TITLE"])
  print("----> Taking this content:",content)
  if len(content) < 100:   #this is not the best way to determine if content was a filename or the actual content, but i can't think of a better way at the moment
    content = open(content).read()
  full_page = page_template.safe_substitute(
    PAGE_TITLE=page["PAGE_TITLE"],
    ACTIVE_INDEX=page["ACTIVE_INDEX"],
    ACTIVE_SPACES=page["ACTIVE_SPACES"],
    ACTIVE_EVENTS=page["ACTIVE_EVENTS"],
    ACTIVE_ABOUT=page["ACTIVE_ABOUT"],
    PAGE_CONTENT=content,
    COPYRIGHT_YEAR=datetime.now().year,
    INDEX_LINK=page_links["index_link"],
    SPACES_LINK=page_links["spaces_link"],
    EVENTS_LINK=page_links["events_link"],
    ABOUT_LINK=page_links["about_link"]

  )
  return full_page

# description_content_reader - pulls both the long and short versions of the content out of the content file
# stores the short content as the first list entry in short_descripton variable (this is available to the calling function)
# stores the detailed content as the 1st entry in the detailed description variable (this is available to the calling funciton)
def description_content_reader(content, short_description, detailed_description):
  description_type = None
  current_description = None

  description_text = open(content).read()
  description_lines = description_text.splitlines()

  for line in description_lines:
    if line == "----SHORT DESCRIPTION----":
      description_type="short"
      short_description.append("")
      current_description=""
      continue
    elif line == "----DETAILED DESCRIPTION----":
      description_type="detailed"
      detailed_description.append("")
      current_description=""
      continue

    line = line.strip()  
    if description_type == "short":
      short_description[0] += " " + line
    elif description_type == "detailed":
      detailed_description[0] += " " + line
    else:
      print("something wroing in the description file", content)
      chad= input("cancel now before it's too late!!")
    


# used to take a single event and apply the short description template to it
def apply_event_template(event_template, event_template_dict):
  print("applying event template to", event_template_dict["EVENT_TITLE"])
  event_short_content = []
  event_detailed_content = []
  description_content_reader(event_template_dict["content"], event_short_content, event_detailed_content)
  event_entry = event_template.safe_substitute(
    EVENT_IMAGE = event_template_dict["EVENT_IMAGE"],
    EVENT_TITLE = event_template_dict["EVENT_TITLE"],
    EVENT_DATES = event_template_dict["EVENT_DATES"],
    EVENT_SPACE_NAME = event_template_dict["EVENT_SPACE_NAME"],
    EVENT_SPACE_ADDRESS = event_template_dict["EVENT_SPACE_ADDRESS"],
    EVENT_ORGANIZER = event_template_dict["EVENT_ORGANIZER"],
    EVENT_EMAIL = event_template_dict["EVENT_EMAIL"],
    EVENT_MODAL_ID = event_template_dict["EVENT_MODAL_ID"],
    EVENT_DETAILS = event_short_content[0],
    EVENT_EXTENDED_DETAILS= event_detailed_content[0]
  )
  return event_entry

# used to build the full content from multiple different singular event/space contents
def apply_all_template(all_template, page_content):
  print("creating the content of the full page")
  full_page_content = all_template.safe_substitute(
    ALL_CONTENT = page_content
  )
  return full_page_content

# used to take a single space and apply the short description template to it
def apply_space_template(space_template, space_template_dict, fullpage_template, page):
  print("applying space template to", space_template_dict["SPACE_NAME"])
  space_short_content = []
  space_detailed_content = []
  description_content_reader(space_template_dict["content"],space_short_content, space_detailed_content)
  space_entry = space_template.safe_substitute(
    SPACE_LOGO = space_template_dict["SPACE_LOGO"],
    SPACE_NAME = space_template_dict["SPACE_NAME"],
    SPACE_IMAGE = space_template_dict["SPACE_IMAGE"],
    SPACE_PAGE_LINK = space_template_dict["SPACE_PAGE_LINK"],
    SPACE_DESCRIPTION = space_short_content[0]
  )
  
  # Create the new space pages here
  individual_space_page = apply_fullpage_template(fullpage_template, space_detailed_content[0], page)
  write_file(individual_space_page, space_template_dict["output"])



  return space_entry

# write_file takes html content (or really any content) and an output file to write to
def write_file(html_page, output):
  print("----> Writing the output to", output)
  open(output, 'w+').write(html_page)


# Main
def main():
  fullpage_template = set_template('templates/whole_page_template.html')
  event_template = set_template('templates/event_template.html')
  space_template = set_template('templates/space_template.html')
  for page in pages:
    event_content = ""
    space_content = ""
    full_page = None
    if page["PAGE_TITLE"] == "EVENTS":
      for event in events:
        event_content += ' '+ apply_event_template(event_template, event)
      full_event_template = set_template(page["content"])
      event_content = apply_all_template(full_event_template, event_content)
      full_page = apply_fullpage_template(fullpage_template, event_content, page)
      write_file(full_page, page["output"])
    elif page["PAGE_TITLE"] == "SPACES":
      for space in spaces:
        space_content += apply_space_template(space_template, space, fullpage_template, page)
      full_space_template = set_template(page["content"])
      space_content = apply_all_template(full_space_template, space_content)
      full_page = apply_fullpage_template(fullpage_template, space_content, page)
      write_file(full_page, page["output"])
    else:
      full_page = apply_fullpage_template(fullpage_template, page["content"], page)
      write_file(full_page, page["output"])
    
  
if __name__ == "__main__":
  main()