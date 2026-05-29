import socket
import sys

# Target config (Use 'localhost' or '127.0.0.1' to test)
target = "127.0.0.1"

# Ports you want to scan (e.g., standard web and SSH ports)
ports_to_scan = [21, 22, 80, 443, 8080]

print(f"Scanning target: {target}")
print("-" * 30)

try:
    for port in ports_to_scan:
        # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: Closed")
            
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()