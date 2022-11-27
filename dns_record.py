# Simple program to fetch dns record of a given website 

#Import dns resolver class from dnspython library 
import dns.resolver 

def get_dns_record():
    # Dictionary to store the dns record of a website
    dns_record = {} 
    # User defined website
    website = input("Enter the name of the website: ")
    # Fetching the 'A' record of the website and storing it in the directory
    a_record = dns.resolver.resolve(website, 'A')
    for ipaddr in a_record:
        dns_record['A_Record_IP'] = ipaddr
    # Fetch MX record(DNS Email Client Service) of a website
    mx_record = dns.resolver.resolve(website, 'MX')
    for service in mx_record:
        dns_record['MX_Record'] = service 
    # Displaying the A record and MX record
    for key,value in dns_record.items():
        print(f"{key}: {value}")

get_dns_record()