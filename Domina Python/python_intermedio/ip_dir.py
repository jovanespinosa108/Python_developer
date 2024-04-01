import requests
#import public_ip as ip
#se instala pip install requests

#se usa una api
request = requests.get("https://ident.me")
ip_publica = request.text
print(ip_publica)

#se usa la libreria ip_public
#se instala: pip install public-ip
#ip_publica2 = ip.get()
#print(ip_publica2)
