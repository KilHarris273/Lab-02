import re
pattern = r"\d+\.\d+\.\d+\.\d+"
ips = []
with open ("auth.log","r") as f:
    for line in f:
        ips.extend(re.findall(pattern,line))
print(ips)
unique_ips = set(ips)
print("Unique IPs:")
with open("unique_ips.txt","w") as g:
    for ip in unique_ips:
        print(ip)
        g.write(ip+"\n")