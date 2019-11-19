import utils


# Main
def main():
  fullpage_template = utils.set_template('templates/whole_page_template.html')
  event_template = utils.set_template('templates/event_template.html')
  space_template = utils.set_template('templates/space_template.html')
  pages = []

  utils.build_pages_list(pages)

  for page in pages:
    item_content = ""
    full_page = None
    page_title = page["PAGE_TITLE"]
    #special caveat for spaces and events
    if page_title == "spaces" or page_title == "events" :
      if page_title == "events":
        for event in utils.events:
          #for events we use the apply_event_template function to build up the content
          item_content += ' '+ utils.apply_event_template(event_template, event)
      elif page_title == "spaces":
        for space in utils.spaces:
          #for spaces we use the apply_space_template to build up the content
          #note this function also builds out the individual space pages
          item_content += utils.apply_space_template(space_template, space, fullpage_template, page, pages)
      
      full_item_template = utils.set_template(page["content"])
      item_content =  utils.apply_all_template(full_item_template, item_content)
      full_page = utils.apply_fullpage_template(fullpage_template, page, item_content, pages, False)
      utils.write_file(full_page, page["output"])
    else:
      full_page = utils.apply_fullpage_template(fullpage_template, page, page["content"], pages)
      utils.write_file(full_page, page["output"])    
  
if __name__ == "__main__":
  main()