import httpx, json, socket
config = json.load(open('config.json'))

def activateKey(ip, username, key):
    resp = httpx.post(f'http://www.proxies.gay/activate?ip={ip}&username={username}&api_key={key}')
    print(resp)

def changeIP(ip, key):
    resp = httpx.post(f'http://www.proxies.gay/change_ip?ip={ip}&api_key={key}')
    print(resp)

def scrapeProxies():
    ip_address = httpx.get('https://api.ipify.org/', proxies='http://proxies.gay:6968').text + ':6968'
    print(ip_address)
    return ip_address

def saveProxy(ip):
    with open('proxies.txt', 'w') as f:
        # write ip then newline
        f.write(ip + '\n')
        f.close()


def getMyIpv4():
    my_ip = socket.gethostbyname(socket.gethostname())
    return my_ip

def main():
    try:
        my_ip = getMyIpv4()
        activateKey(my_ip, config['username'], config['key'])
    except:
        my_ip = changeIP(getMyIpv4, config['key'])

    while True:
        new_ip = getMyIpv4()
        if new_ip != my_ip:
            changeIP(new_ip, config['key'])
            my_ip = new_ip
            print(f'Changed IP to {my_ip}')
        proxy = scrapeProxies()
        saveProxy(proxy)

main()
