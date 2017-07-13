#!/usr/bin/env python
"""Exercises using Netmiko"""
from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler


pynet_rtr1 = {
        'device_type': 'cisco_ios',
        'ip':   '184.105.247.70',
        'username': 'pyclass',
        'password': getpass,
}


pynet_srx = {
        'device_type': 'juniper_junos',
        'ip':   '184.105.247.76',
        'username': 'pyclass',
        'password': getpass,
}

for a_device in (pynet_rtr1, pynet_srx):
        net_connect = ConnectHandler(**a_device)
        print("Current Prompt: " + net_connect.find_prompt())

        show_ver = net_connect.send_command("show version")
        print()
        print('#' * 80)
        print(show_ver)
        print('#' * 80)
        print()

        if 'cisco' in a_device['device_type']:
            cmd = "show run"
        elif 'juniper' in a_device['device_type']:
            cmd = "show configuration"

        show_run = net_connect.send_command(cmd)
        filename = net_connect.base_prompt + ".txt"
        print("Save show run output: {}\n".format(filename))
        save_file(filename, show_run)

if __name__ == "__main__":
main()

