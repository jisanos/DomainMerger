#import pandas as pd
import requests


domain_links = [] #List containing the domain links extracted from DomainLinks.exe
whitelists = [] #List containing domains from the Whitelist.txt
input_ = 0



while input_ <= 0 or input_ > 2:
    input_ = int(input("1. Domains Only\n2. Hosts File\n"))
    

with open("DomainLinks.txt", "r") as f:
    #Stripping the \n characters and appending to list
    domain_links = [line.strip() for line in f.readlines()]
    
with open("Whitelist.txt", "r") as f:
    whitelists = [line.strip() for line in f.readlines()]
    
domains = [] #List containing the domains from each of the links provided

for line in domain_links:
    #Appending all the domains from the links provided
    [domains.append(sub_line) for sub_line in requests.get(line).text.strip().split("\n")]
        

print("Domains default "+ str(len(domains)))


#Will contain the domains stripped from 0.0.0.0 and other unncecesary values
domains_clean = []

for line in domains:
    
    string = ""
    
    string = line.replace("0.0.0.0 ", "")
    
    string = string.replace("0.0.0.0", "")
    
    #Removing unnecesary strings.
    #                                                                                if there is a comment | if the line contains only whitespace
    if("127.0.0.1" in line or "localhost" in line or "::" in line or "broadcasthost" in line or "#" in line or not line.strip()):
        continue
        
    
    else:
        domains_clean.append(string)
    


#Taking out any duplicates
domains_no_dups = list(dict.fromkeys(domains_clean)) 


print("Domains after comments, whitespace and others removal "+ str(len(domains_clean)))
print("Domains after dups removal "+str(len(domains_no_dups)))

#Removing whitelisted domains
for line in whitelists:
    #If the string is in the list then remove, else dont
    if line in domains_no_dups:
        domains_no_dups.remove(line)


print("Domains after whitelist removal "+str(len(domains_no_dups)))

 
def write_file(doms):
    with open("merged.txt", "w") as f:
        for line in doms:
            f.write(line)
            f.write("\n")


if input_ == 1:
    write_file(domains_no_dups)

elif input_ == 2:
    hosts = [("0.0.0.0 "+line) for line in domains_no_dups]
    
    write_file(hosts)


input("Press return or enter to exit")
