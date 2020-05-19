import os

import paramiko


if __name__ == '__main__':
    print('Scanning all available IP addresses in your network ...')
    os.system(r"ip a | grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}\b' | grep -v '^127' > subnets.txt")
    
    # Scan IPs over all possible subnetwork
    with open('subnets.txt', 'r') as subnets:
        for idx, raw_subnet in enumerate(subnets):
            # correct the current subnet string by remove '\n'
            subnet = raw_subnet[:-1]
            
            """ scan all ip in the current subnet
            and just get IPs whose values have 'Pi' inside.
            """

            # convert /24 /16 /8
            subnet_list = subnet.split('.')
            subnet_list.extend(subnet_list.pop().split('/'))
            if subnet_list[-1] == '24':
                subnet_list[3] = '0'
            elif subnet_list[-1] == '16':
                subnet_list[3] = subnet_list[2] = '0'
            elif subnet_list[-1] == '8':
                subnet_list[1] = subnet_list[2] = subnet_list[3] = '0'
            subnet = '.'.join(subnet_list[:-1]) + '/{}'.format(subnet_list[-1])

            os.system("sudo netdiscover -r {} -P | grep Pi | awk '{}' > ip_tmp{}.txt".format(subnet, '{print $1}', idx+1))
            with open('ip_tmp{}.txt'.format(idx+1), 'r') as IPs_list:
                for ip in IPs_list:
                    ssh_client = paramiko.client.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    # Loop over each of IP address in the IP addresses above
                    for raw_ip in ALL_IPs:
                        print(f"current IP: {raw_ip}")
                        try:
                            ssh_client.connect(hostname=raw_ip, username='pi', password='Badien123')
                            print(f"Your Raspberry Pi IP address is: {raw_ip}")
                            break
                        except paramiko.ssh_exception.NoValidConnectionsError:
                            continue
                        except paramiko.ssh_exception.AuthenticationException:
                            continue
                    print("----\nDONE.")
