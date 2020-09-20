#!/usr/bin/env python
import subprocess
import time
import re
import optparse


def get_arguments():
    """
    Function to fetch command line arguments
    """
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Inerface to change macc adress")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(
            "[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info")
    return options


def change_mac(interface, new_mac):
    """
    Function that changes mac address to new one
    :param interface: Interface of your device # Unix Based: ifconfig / iwconfig | Windows: getmac -v 
    :param new_mac: New Mac Address as a String 
    """
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    time.sleep(2)
    print("[+] Your new mac with " + interface + " is " + new_mac)

def g_curr_mac(interface): 
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    mac_result_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_result_search:
        return mac_result_search.group(0)
    else:
        print("[-] Could not read MAC address. ")
       

options = get_arguments() # for getting inline arguments
curr_mac = g_curr_mac(options.interface) #func to get find and get current mac
print("Current MAC = " + str(curr_mac))
change_mac(options.interface, options.new_mac) # func to change the mac


curr_mac = g_curr_mac(options.interface)
if curr_mac == options.new_mac:
    print("[+] MAC address is successfully chabged to " + curr_mac)
    print("[+]Your Operation of Changing MAC is Successfully completed !")

else:
    print("[-] Operation Failed !")
    print("[-] MAC address is not changed try again. ")




