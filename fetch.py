import requests
baseUrl = 'https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt'
r = requests.get(baseUrl)
try:
    f = open('rules.txt',mode='x')
except:
    f = open('rules.txt', mode='w')
rules = r.content.decode()
f.write(rules)
f.close()

srules = rules.replace('||','DOMAIN-SUFFIX,')
srules = srules.replace('^','')
srules = srules.replace('!','#')

qrules = rules.replace('||','HOST-SUFFIX,')
qrules = qrules.replace('^',',Advertising')
qrules = qrules.replace('!',';')
try:
    f = open('srocket.txt',mode='x')
except:
    f = open('srocket.txt', mode='w')
f.write(srules)
f.close()
try:
    f = open('qx.txt', mode='x')
except:
    f = open('qx.txt', mode='w')
f.write(qrules)
f.close()
