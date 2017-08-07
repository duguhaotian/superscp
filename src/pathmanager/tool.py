import netifaces

def get_ip(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['addr']
    except ValueError:
        print("interface is invalid")

