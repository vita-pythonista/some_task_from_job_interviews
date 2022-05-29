import netifaces

def test_1():
    interfaces = netifaces.interfaces()
    print(interfaces)