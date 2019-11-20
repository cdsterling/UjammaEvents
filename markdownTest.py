import markdown
md = markdown.Markdown(extensions=["markdown.extensions.meta"])
data = """title: My New Blog
author: Jane Q Hacker
Welcome to my ~~site~~ *blog*
"""
html = md.convert(data)
print(html)
