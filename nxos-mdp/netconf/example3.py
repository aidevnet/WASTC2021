from ncclient import manager


def main():
    """
    Main method that prints netconf capabilities of device.
    """

    device = {"ip": "10.10.20.177", "port": "830", "platform": "nexus",}

    with manager.connect(host=device['ip'], port=device['port'], username='admin',
                         password='admin', hostkey_verify=False,
                         device_params={'name': device['platform']},
                         look_for_keys=False, allow_agent=False) as m:

        rpc = '''
                <config>
                    <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
                        <ospf-items>
                            <inst-items>
                                <Inst-list>
                                    <name>100</name>
                                    <dom-items>
                                        <Dom-list>
                                            <name>default</name>
                                            <rtrId>3.3.3.3</rtrId>
                                            <if-items>
                                                <If-list>
                                                    <id>lo1</id>
                                                    <advertiseSecondaries>true</advertiseSecondaries>
                                                    <area>0.0.0.0</area>
                                                </If-list>
                                            </if-items>
                                        </Dom-list>
                                    </dom-items>
                                </Inst-list>
                            </inst-items>
                        </ospf-items>
                        <fm-items>
                            <ospf-items>
                                <adminSt>enabled</adminSt>
                            </ospf-items>
                        </fm-items>
                    </System>
                </config>
            '''

        reply = m.edit_config(rpc, target='running')
        print(reply)


if __name__ == '__main__':
    main()