import socket
import subprocess


def portscanner(ip):
    print(f'\nStarting a scan on {ip}')
    open_ports = 0  # Count of open ports

    for port in range(1, 1025):  # Adjusted range to include port 1024
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)  

        try:
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f'Port {port} is open')
                open_ports += 1

        except socket.error:
            pass
        finally:
            s.close()

    print(f'\nScan on {ip} is complete. Found {open_ports} open port(s)')

   

# Get user input for IP address
ip_address = input("Please enter the IP address to scan: ")

# Call the portscanner function with the provided IP address
portscanner(ip_address)
