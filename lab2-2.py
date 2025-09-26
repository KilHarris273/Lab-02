LOGFILE = "sample_auth_small.log"

def ip_parse(line):
    if " from " in line:        #Checks if a line has an ip
        parts = line.split()
        try:
            anchor = parts.index("from")
            ip = parts[anchor+1]    #Adds word(IP address) that appears after the word "from"
            return ip.strip()       #Returns IP
        
        
        except (ValueError,IndexError):
            return None        
    return None
def top_n(counts, n=5):
    return sorted(counts.items(),key=lambda kv:kv[1], reverse=True)[:n] #function to sort list

if __name__ == "__main__":
    from collections import defaultdict
    import time
    iplist = []
    sorted_list = []
    test={}
    start = time.time() #Starting time for program

    with open(LOGFILE, "r") as f:
        for linecount, line in enumerate(f):
            ip = ip_parse(line.strip()) #Checks for IP address in each line
            if ip:
                iplist.append(ip)       #Adds IP if there is one

    print("Total lines read: " + str(linecount))
    sorted_list=sorted(set(iplist))     #Duplicate IPs removed, and are sorted
    print("Number of unique ips: " +str(len(sorted_list)))
    print("First 10 IPs: " + str(sorted_list[0:10]))
    counts = defaultdict(int)
    with open(LOGFILE) as f:    #Checks for users who gave an invalid username or password, and adds them to a dictonary with the number of failed attempts for each IP
        for line in f:
            if "Failed password" in line or "Invalid user" in line:
                ip = ip_parse(line)
                if ip:
                    counts[ip] += 1
    end = time.time()   #Timestamp for end of main data processing
    print("Number of failed attempts: " + str(counts))
    ranked = top_n(counts)  #Sorts which IPs had the most failed logins because of invalid passwords/usernames
    print(ranked)
    print("Elapsed:", end-start, "seconds")
    with open('failed_counts.txt', 'w') as f:   #Creates and adds ranked list to text file
        f.write("\t\tIP\t\t\tFailed Count \n")
        for val, ind in enumerate(ranked):
            f.write(str(val+1) + ". " + str(ind[0])+" \t\t"+str(ind[1])+"\n")