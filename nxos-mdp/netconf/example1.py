#! /usr/bin/env python
from device_info import nxos1
from ncclient import manager

if __name__ == '__main__':
    with manager.connect(host=nxos1["address"],
                         port=nxos1["port"],
                         username=nxos1["username"],
                         password=nxos1["password"],
                         hostkey_verify=False) as m:

        print("Here are the NETCONF Capabilities")
        for capability in m.server_capabilities:
            print(capability)
