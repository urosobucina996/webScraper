from modules import request
from modules import database

tag = request.parseHtml('http://web.mta.info/developers/turnstile.html')
rows = []
for href in tag:
     rows.append((href.get("href"),href.text))

database.executeQuery(rows)

