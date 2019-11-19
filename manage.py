import utils




# Main
def main():
  fullpage_template = utils.set_template('templates/whole_page_template.html')
  event_template = utils.set_template('templates/event_template.html')
  space_template = utils.set_template('templates/space_template.html')
  pages = []

  utils.build_pages_list(pages)
  utils.build_site(pages, fullpage_template, event_template, space_template)
      
  
if __name__ == "__main__":
  main()