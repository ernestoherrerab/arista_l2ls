#! /usr/bin/env python

from scrapli.driver.core import EOSDriver
from scrapli.exceptions import ScrapliConnectionError
from scrapli.exceptions import ScrapliAuthenticationFailed
import yaml
from pathlib import Path
import re
import sys
import time
from rich import print as pprint
from py_load_yaml import load_yaml


class Device:
    ### CLASS ATTRIBUTES ###
    transport_options = {
        "open_cmd": [
            "-o",
            "KexAlgorithms=+diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1",
            "-o",
            "Ciphers=+aes256-cbc",
        ]
    }

    ### OBJECT INITIALIZATION ###
    def __init__(self, host):
        self.host = host
        self.connection = None

    ### OBJECT TRANSPORT OPTIONS ###
    def set_transport(self):
        DEVICE = {
            "host": self.host,
            "auth_username": "cvpadmin",
            "auth_password": "arista1234",
            "auth_strict_key": False,
            "transport_options": self.transport_options,
        }
        return DEVICE
    
    def connect(self):
        if not self.connection:
            device = self.set_transport()
            self.connection = EOSDriver(**device)
            self.connection.open()

    def disconnect(self):
        if self.connection:
            self.connection.close()

class DeviceEOS(Device):
    def ping(self, remote_server):
        """Send commands and structure them in a dictionary"""
        self.remote_server = remote_server 
        command = f"ping vrf ACME {self.remote_server} repeat 3"

        try:
            response = self.connection.send_command(command)
            return response.result
        except ScrapliConnectionError as e:
            print(f"Failed to Login: {e}")
        except ScrapliAuthenticationFailed as e:
            print(f"Authentication Failed: {e}")
  
def main():     
    start_time = time.time()
    inventory_yml_file = Path("hosts.yml")
    inventory_dict = load_yaml(inventory_yml_file)
    ping_source = sys.argv[1]
    server = DeviceEOS(ping_source)
    server.connect()
    result = {}

    for hostname in inventory_dict["all"]["children"]["acme_fabric"]["children"]["servers"]["hosts"]:
        server_ip = inventory_dict["all"]["children"]["acme_fabric"]["children"]["servers"]["hosts"][hostname]["vars"]["srv_ip"]
        server_ip = server_ip.split('/')[0]
        server_ping = server.ping(server_ip)
        ping_result = re.search(r'(\d+)% packet loss', server_ping)
        packet_loss = ping_result.group(1)
        if packet_loss == "0":
            result[hostname] = "Success!"
        elif packet_loss == "100":
            result[hostname] = "Unreachable!"
        else:
            result[hostname] = "Partial packet loss"

    server.disconnect()
    end_time = time.time()
    elapsed_time = end_time - start_time
    pprint(result)
    print(f"Execution time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()