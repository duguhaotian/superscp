import netifaces

def get_ips():
    ips={}
    for itf in netifaces.interfaces():
        if itf == "lo" or itf == "docker0" or itf == "virbr0":
            continue
        ip = get_ip(itf) 
        if ip != None:
            ips[itf] = ip 
    return ips
def get_ip(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['addr']
    except (ValueError, KeyError):
        print("get_ip: %s is invalid" % interface)
def get_mask(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['netmask']
    except (ValueError, KeyError):
        print("get_mask: %s is invalid" % interface)
def get_mac(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_LINK][0]['addr']
    except (ValueError, KeyError):
        print("get_mac: %s is invalid" % interface)

