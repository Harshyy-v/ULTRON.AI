import socket

def ipAddress():
    # Get hostname
    hostname = socket.gethostname()

    # Get IP address
    local_ip = socket.gethostbyname(hostname)

    # Print the IP address
    print(f"Local IP address: {local_ip}")

ipAddress()