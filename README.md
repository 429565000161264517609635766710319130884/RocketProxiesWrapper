# RocketProxiesWrapper
shitty wrapper i even don't know why i made this i'll probably delete

# Install
```
pip install -U git+https://github.com/Mewzax/RocketProxiesWrapper
```

# Usage
```py
import requests, httpx

from RocketProxies import RocketProxies

rp = RocketProxies(requests.get('https://api.ipify.org').content.decode('utf8'), 'YOUR_API_KEY')
proxy = rp.getProxy()

# activate key to use proxy
resp = rp.activateKey('username')
resp = httpx.get('https://www.google.com', proxies='http://' + proxy, timeout=4)
```
