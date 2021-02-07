import math
import requests

url = "http://challenges.ctfd.io:30107/calc/calc.php"

res = requests.Session()
content = res.get(url).text
cal = content[content.find("<expression>")+12:content.find("</expression>")].split("<br/>")
print(cal)
pos = 1
total = int(cal[0])
while True:
    if pos >= len(cal) - 1:
        break
    if cal[pos] == "+":
        total = total + int(cal[pos+1])
    elif cal[pos] == "-":
        total = total - int(cal[pos+1])
    elif cal[pos] == "*":
        total = total * int(cal[pos+1])
    elif cal[pos] == "/":
        total = total / int(cal[pos+1])
    pos = pos + 2
print(math.floor(total))
payload = {'answer': total}
post = res.post(url, data=payload)
print(post.text)
