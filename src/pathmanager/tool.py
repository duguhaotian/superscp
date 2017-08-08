import netifaces

def get_ip(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['addr']
    except ValueError:
        print("get_ip: interface is invalid")
def get_mask(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['netmask']
    except ValueError:
        print("get_mask: interface is invalid")
def get_mac(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_LINK][0]['addr']
    except ValueError:
        print("get_mac: interface is invalid")

