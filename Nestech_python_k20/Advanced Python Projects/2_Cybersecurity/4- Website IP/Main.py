import socket

# Get the website URL from user input
website_url = input("Enter a website URL: ")

try:
    # Get the IP address of the website
    website_ip = socket.gethostbyname(website_url)
    print("The IP address of", website_url, "is:", website_ip)
except socket.gaierror:
    # If the website URL is invalid, print an error message
    print("Invalid website URL!")
