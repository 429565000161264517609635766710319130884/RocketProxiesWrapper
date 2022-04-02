import httpx

class RocketProxies:
    def __init__(self, ip, key):
        self.ip = ip
        self.key = key
    
    def activateKey(self, username):
        resp = httpx.post(f'http://www.proxies.gay/activate?ip={self.ip}&username={username}&api_key={self.key}')
        return resp

    def changeIP(self):
        resp = httpx.post(f'http://www.proxies.gay/change_ip?ip={self.ip}&api_key={self.key}')
        return resp

    def getProxy(self):
        resp = httpx.post('http://api.ipify.org/', proxies='http://proxies.gay:6968').text
        return resp
