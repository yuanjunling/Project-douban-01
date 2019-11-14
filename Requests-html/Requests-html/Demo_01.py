from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://movie.douban.com/top250')
#查看页面内容
print(r.html.html)