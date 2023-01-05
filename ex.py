import nmap

def scan_ports(hosts, port_range):
  """Scans a range of ports on a given list of hosts using nmap."""
  nm = nmap.PortScanner()
  for host in hosts:  # loop through the list of hosts
    nm.scan(hosts=host, arguments="-p" + port_range)  # scan each host
    print(f"Host: {host}")
    for protocol in nm[host].all_protocols():
      print(f"Protocol: {protocol}")
      ports = nm[host][protocol].keys()
      for port in ports:
        print(f"Port: {port}  State: {nm[host][protocol][port]['state']}")

# Example usage
with open("hosts.txt") as f:
  hosts = [line.strip() for line in f]
port_range = "1-10"
scan_ports(hosts, port_range)
