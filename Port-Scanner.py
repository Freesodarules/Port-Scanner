import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[- 0 Scanning Target]' + str(target))
    for port in range(1, 100):  # Range can be changed (loops the scan on the range)
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(sock):
    return sock.recv(1024)

def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) #timeout can be changed also, however the faster the scan the less accurate it will be
        sock.connect((ip_address, port))
        try:
            banner = get_banner(sock)
            print ('[+] Open Port' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass

targets = input('[+] Enter Target to scan(split multiple targets with ,): ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan_port(ip_add.strip(' '))
else:
    scan(targets)
