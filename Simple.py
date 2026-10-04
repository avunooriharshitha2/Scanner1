import socket

target = "127.0.0.1"

print("Simple Vulnerability Scanner")
print("----------------------------")
print("Target:", target)

# Common ports
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print(f"Port {port} is OPEN - {service}")

    sock.close()

print("----------------------------")
print("Scan completed.")
