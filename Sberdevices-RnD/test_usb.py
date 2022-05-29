import usb.core

dev = usb.core.find(find_all=True)
if dev is None:
    raise ValueError("No devices founds")
print(dev)