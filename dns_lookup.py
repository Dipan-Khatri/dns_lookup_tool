import socket
import dns.resolver

def perform_dns_lookup(domain):
    try:
        print(f"\nPerforming DNS Lookup for: {domain}")
        
        # Get the IP address
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")

        # Get the A record
        print("\nA Records:")
        for answer in dns.resolver.resolve(domain, 'A'):
            print(f"- {answer}")

        # Get the MX record
        print("\nMX Records:")
        for answer in dns.resolver.resolve(domain, 'MX'):
            print(f"- {answer.exchange} with priority {answer.preference}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain = input("Enter a domain to lookup (e.g., google.com): ")
    perform_dns_lookup(domain)
