import utils
import sys




# Main
def main():
  command = None

  if len(sys.argv) > 2:
    command = sys.argv[1]

  while True:
    if command == "build":
      fullpage_template = utils.set_template('templates/whole_page_template.html')
      event_template = utils.set_template('templates/event_template.html')
      space_template = utils.set_template('templates/space_template.html')
      pages = []

      utils.build_pages_list(pages)
      utils.build_site(pages, fullpage_template, event_template, space_template)
      break
    elif command == "new":
      utils.create_new_content()
      break
    elif command == "quit":
      print("quitting without doing anything")
      break
    else:
      print("invalid or missing command")
      print("please enter either build, new or quit")
      command = input(">> ")
      
  
if __name__ == "__main__":
  main()