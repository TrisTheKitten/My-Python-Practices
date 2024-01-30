import ipaddress

def calculate_class(ip_address):
    first_octet = int(ip_address.split('.')[0])

    if first_octet <= 126:
        return 'Class A'
    elif first_octet <= 191:
        return 'Class B'
    elif first_octet <= 223:
        return 'Class C'
    else:
        return 'Not a class A, B, or C IP address'

def calculate_subnets(ip_address, subnet_mask):
    network = ipaddress.ip_network(f'{ip_address}/{subnet_mask}', strict=False)
    return {i: str(subnet) for i, subnet in enumerate(network.subnets(), 1)}
def calculate_all_ip_addresses(ip_address, subnet_mask):
    network = ipaddress.ip_network(f'{ip_address}/{subnet_mask}', strict=False)
    return [str(ip) for ip in network.hosts()]

def calculate_total_subnets_and_addresses(ip_address, subnet_mask):
    network = ipaddress.ip_network(f'{ip_address}/{subnet_mask}', strict=False)
    total_subnets = network.subnets()
    total_addresses = network.hosts()
    return len(list(total_subnets)), len(list(total_addresses))

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    subnet_mask = input("Enter a Subnet Mask: ")
    
    total_subnets, total_addresses = calculate_total_subnets_and_addresses(ip_address, subnet_mask)
    
    while True:
        print("Menu:")
        print("1. Output the class of the IP address")
        print("2. Output the available subnets")
        print("3. Output all valid IP addresses")
        print("4. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(calculate_class(ip_address))
            print(f"Total subnets: {total_subnets}")
            print(f"Total IP addresses: {total_addresses}")
        elif choice == 2:
            print("Available Subnets: ")
            for number, address in calculate_subnets(ip_address, subnet_mask).items():
                print(f"{number}: {address}")
        elif choice == 3:
            print("All Valid IP Addresses: ")
            for address in calculate_all_ip_addresses(ip_address, subnet_mask):
                print(address)
        elif choice == 4:
            break
        else:
            print("Invalid choice")

