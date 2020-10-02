import subprocess

subprocess.call("sudo ifconfig ", shell=True)

interface = input("interface > ")
new_mac = input("new mac > ")

print("[+] Changing MAC address for ", interface, " to ", new_mac)


subprocess.call("sudo ifconfig " + interface + " down ", shell=True)
subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac , shell=True)
subprocess.call("sudo ifconfig " + interface + " up ", shell=True)
subprocess.call("sudo ifconfig " + interface , shell=True)