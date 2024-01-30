import ipaddress
import tkinter as tk
from tkinter import simpledialog, messagebox

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

def get_user_input():
    ip_address = simpledialog.askstring("Input", "Enter an IP address:")
    subnet_mask = simpledialog.askstring("Input", "Enter a Subnet Mask:")
    return ip_address, subnet_mask

def show_menu():
    messagebox.showinfo("Menu", "1. Output the class of the IP address\n2. Output the available subnets\n3. Output all valid IP addresses\n4. Quit")
    choice = simpledialog.askinteger("Input", "Enter your choice:")
    return choice

if __name__ == "__main__":
    ip_address, subnet_mask = get_user_input()
    total_subnets, total_addresses = calculate_total_subnets_and_addresses(ip_address, subnet_mask)

    while True:
        choice = show_menu()

        if choice == 1:
            result = calculate_class(ip_address)
            messagebox.showinfo("Result", result)
            print(f"Total subnets: {total_subnets}")
            print(f"Total IP addresses: {total_addresses}")
        elif choice == 2:
            result = calculate_subnets(ip_address, subnet_mask)
            messagebox.showinfo("Result", result)
        elif choice == 3:
            result = calculate_all_ip_addresses(ip_address, subnet_mask)
            messagebox.showinfo("Result", result)
        elif choice == 4:
            break
        else:
            messagebox.showerror("Error", "Invalid choice")
