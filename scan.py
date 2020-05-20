import os
import argparse

import paramiko
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException


def main(username, password):
    print('Finding subnetwork ...')
    # print('Scanning all available subnets in your network ...')
    os.system(r"ip a | grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}\b' | grep -v '^127' > subnets.txt")
    
    with open('subnets.txt', 'r') as subnets_file:
        subnets = list()
        # Show scanned subnetworks in your network.
        print('-------------- SCANNED SUBNETWORKS -------------\n')
        for subnet in subnets_file:
            print(f"\t\t{subnet}")
            subnets.append(subnet)

        print('BE SCANNING ...\n')
        for idx, raw_subnet in enumerate(subnets):
            # correct the current subnet string by remove '\n'
            subnet = raw_subnet[:-1]

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

            # Currently, we will bypass for faster scanning
            if subnet_list[-1] != '24':
                continue

            os.system("sudo netdiscover -r {} -P | grep Pi | awk '{}' > ip_tmp{}.txt".format(subnet, '{print $1}', idx+1))
            with open('ip_tmp{}.txt'.format(idx+1), 'r') as IPs_list:
                for ip in IPs_list:
                    ssh_client = paramiko.client.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                    # Loop over each of IP address in the IP addresses above
                    try:
                        ssh_client.connect(hostname=ip, username=username, password=password)
                        print(f"Your Raspberry Pi IP address is: {ip}")
                        return
                    except NoValidConnectionsError:
                        continue
                    except AuthenticationException:
                        continue

    print('Please re-check your Raspberry Pi connection (e.g: Power, Network cable, Wifi connection, ..)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scan headless Raspberry Pi IP in your massive network.')
    
    parser.add_argument('-u', '--username', type=str, required=True,  help='Unix account you want to log in')
    parser.add_argument('-p', '--password', type=str, required=True, help='Password for logging')
    
    args = parser.parse_args()
    main(args.username, args.password)
