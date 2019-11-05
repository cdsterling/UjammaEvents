Ujamma Events
Chad Sterling


4 pages for Ujamma events - a community based website that puts people who have spaces in touch with people who want to host events.

Relevant Files:
  ./README.md
  ./build.py              -   Python script to create my static html files in the docs directory from files in the content directory and top.html and bottom.html from the templates directoriy
      ./build_advanced.py     -   python script to create my static html files in the docs directory from files in the content directory and top_advanced.html and bottom.html from the templates directory
      ./build_advanced2.py    -   python script to create my static html files in the docs directory from files in the content directory and the whole_page_template file in the templates directory
  ./build.sh              -   Shell script to create my static html files in the docs directory from files in the content and and top.html and bottom.html from the templates directorie
  ./docs/index.html       -   static html file built by build.sh
  ./docs/events.html      -   static html file built by build.sh
  ./docs/spaces.html      -   static html file built by build.sh
  ./docs/about.html       -   static html file built by build.sh
  ./docs/css/uje.css      -   css file used by static html files
  ./docs/images/*         -   images used by static html files
  ./templates/top.html    -   template for the top of all of my static html files
      ./templates/top_advanced.html           -   template for the top of all static files, uses templating for page title and active link (used by build_advanced.py)
      ./templates/whole_page_template.html    -   full page template for all static files, uses templating for page title, active link and page content (used by build_advanced2.py)
  ./templates/bottom.html -   template for the bottom of all of my static html files
  ./content/index.html    -   content of the static docs/index.html file, used to create docs/index.html by build.sh and build.py
  ./content/events.html   -   content of the static docs/events.html file, used to create docs/index.html by build.sh and build.py
  ./content/spaces.html   -   content of the static docs/spaces.html file, used to create docs/index.html by build.sh and build.py
  ./content/about.html    -   content of the static docs/about.html file, used to create docs/index.html by build.sh and build.py
  ./originalSite/*        -   sub directory containing the original static html files and cooresponding supporting files
  

