from ncclient import manager


def main():
    """
    Main method that prints netconf capabilities of device.
    """

    # Device dictionary to use
    device = {"ip": "10.10.20.177", "port": "830", "platform": "nexus",}

    # ncclient manager instantiation for nexus
    with manager.connect(host=device['ip'], port=device['port'], username='admin',
                         password='admin', hostkey_verify=False,
                         device_params={'name': device['platform']},
                         look_for_keys=False, allow_agent=False) as m:

        # Filter using top-level container namespace and node matching for physical interface
        int_filter1 = '''
                    <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
                        <intf-items>
                            <phys-items>
                                <PhysIf-list>
                                    <id>eth1/3</id>
                                </PhysIf-list>
                            </phys-items>
                        </intf-items>
                    </System>
                    '''

        # Filter using top-level container namespace and node matching for ipv4 interface
        int_filter2 = '''
                    <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
                        <ipv4-items>
                            <inst-items>
                                <dom-items>
                                    <Dom-list>
                                        <if-items>
                                            <If-list>
                                                <id>eth1/3</id>
                                            </If-list>
                                        </if-items>
                                    </Dom-list>
                                </dom-items>
                            </inst-items>
                        </ipv4-items>
                    </System>
                    '''

        # get-config RPC against the running datastore using first subtree filter
        r = m.get_config('running', filter=('subtree', int_filter1))

        # Print RPC reply against running datastore
        print(r)

        # get-config RPC against the running datastore using second subtree filter
        r = m.get_config('running', filter=('subtree', int_filter2))

        # Print RPC reply against running datastore
        print(r)


if __name__ == '__main__':
    main()