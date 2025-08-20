# importing socket library
import socket
import subprocess
import time
import sys

def progress_bar(duration=4, bar_length=100):
    
    for i in range(bar_length + 1):
        percent = (i / bar_length) * 100
        bar = "█" * i + " " * (bar_length - i)
        
        sys.stdout.write(f"\r[{bar}] {percent:.1f}%")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    
    sys.stdout.write("\nLoaded!\n")
    sys.stdout.flush()

# Start de animatie
progress_bar(duration=5)

def get_hostname_IP():
    	print("Sheriff v20")
    	print("Made by CLOUD_STUDIOS")
    	hostname = input("Please enter website address (URL): ")
    	try:
    	   print("--------------------------------------")
    	   print (f'Hostname: {hostname}')
    	   print (f'IP: {socket.gethostbyname(hostname)}')
    	except socket.gaierror as error:
    		print (f'Invalid Hostname, error raised is {error}')

get_hostname_IP()

print()
print("------------Your Device Info--------------")
import socket
import platform
import os

def get_server_info():
    # Get hostname
    hostname = socket.gethostname()
    
    # Get IP address
    ip_address = socket.gethostbyname(hostname)
    
    # Get OS details
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()
    
    # Get CPU details
    cpu_count = os.cpu_count()
    processor = platform.processor()
    
    # Display server information
    server_info = {
        "Hostname": hostname,
        "IP Address": ip_address,
        "Operating System": f"{os_name} {os_release} (Version: {os_version})",
        "CPU": f"{processor} ({cpu_count} cores)"
    }
    
    return server_info

if __name__ == "__main__":
    info = get_server_info()
    for key, value in info.items():
        print(f"{key}: {value}")

import requests

def get_location(ip_address=""):
    try:
        # Use ipinfo.io API to get location data
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            data = response.json()
            location = {
                "IP": data.get("ip"),
                "City": data.get("city"),
                "Region": data.get("region"),
                "Country": data.get("country"),
                "Coordinates": data.get("loc"),
                "ISP": data.get("org")
            }
            return location
        else:
            return {"Error": f"Failed to fetch data. Status code: {response.status_code}"}
    except Exception as e:
        return {"Error": str(e)}

# Example usage
if __name__ == "__main__":
    print()
    print("-------------Server Location--------------")
    ip = input("IP Adress: ")
    location_info = get_location(ip)
    for key, value in location_info.items():
        print(f"{key}: {value}")

