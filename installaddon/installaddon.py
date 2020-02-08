import sys, re, httplib2
from bs4 import BeautifulSoup

# if they don't have beautiful soup, get beautiful soup


http = httplib2.Http()
headers, body = http.request('https://github.com/todotxt/todo.txt-cli/wiki/Todo.sh-Add-on-Directory#paper-print-your-todo-list.html')
tags = BeautifulSoup(body, 'html.parser')
# so we need to isolate the div whos class is markdown body
# then we need to take the unordered lists that are children
# then we need to take first child list of those lists
# and the we need to get the ist who's inner html is "New/Enhanced Actions"
# then get the child lists of that list
innerhtml = [tag.contents[-1] for tag in tags]
print(innerhtml)


# def htmlToUrl(url):
# def findHeaders(html):
#     htmlcontent = open(html, 'r').read()
#     re.findall(r'< h\d>(.*)< /h\d>', html_content)