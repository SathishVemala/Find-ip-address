from requests import get
ip=get('http://api.ipify.org').text
print("=========Ip address =========")
print(f'my public Ip address is:{ip}')
print("========*========*========")