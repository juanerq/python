from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://www.amazon.com/MAXSUN-AMD-Radeon-RX-550/dp/B08VHWFWSD')
top = r.html.find('#buy-now-button')
print(top)