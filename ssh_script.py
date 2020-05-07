import paramiko


if __name__ == '__main__':
    print('Scanning all available IP addresses in your network ...')
    import os
    os.system('arp -a > net_info.txt')
    
    """ Read net_info.txt file 
    and get list of valid IP addresses.
    """
    ALL_IPs = list()
    with open('net_info.txt', 'r') as f:
        for line_idx, line in enumerate(f):
            for c_idx, c in enumerate(line):
                if c == '(':
                    ip_address = ''
                    start_idx = c_idx + 1
                    while line[start_idx] != ')':
                        ip_address += line[start_idx]
                        start_idx += 1
                    ALL_IPs.append(ip_address)

    """ Connect to Pi over SSH using Paramiko Package
    """
    ssh_client = paramiko.client.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Loop over each of IP address in the IP addresses above
    for raw_ip in ALL_IPs:
        try:
            o = ssh_client.connect(hostname=raw_ip, username='pi', password='Badien123')
            print(f"Your Raspberry Pi IP address is: {raw_ip}")
            break
        except paramiko.ssh_exception.NoValidConnectionsError:
            continue
        except paramiko.ssh_exception.AuthenticationException:
            continue
    print("----\nDONE.")

    """
    import subprocess
    for raw_ip in ALL_IPs:
        subprocess.Popen(f"ssh pi@{raw_ip}").communicate()
    """

