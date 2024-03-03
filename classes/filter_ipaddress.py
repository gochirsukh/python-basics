import re

class IPFilter:
    def __init__(self, log_file):
        self.log_file = log_file

    def filter_ips(self):
        try:
            with open(self.log_file, "r") as file:
                log_content = file.read()
                ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"  # Regular expression pattern for matching IP addresses
                ips = re.findall(ip_pattern, log_content)
                unique_ips = set(ips)  # Removing duplicates
                return unique_ips
        except Exception as e:
            print(f"Error filtering IPs: {e}")

# Example usage:
if __name__ == "__main__":
    ip_filter = IPFilter("logfile.txt")
    ip_addresses = ip_filter.filter_ips()
    print("IP Addresses found in the log file:")
    for ip in ip_addresses:
        print(ip)
