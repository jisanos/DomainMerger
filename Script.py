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
        
#Will contain the domains stripped from 0.0.0.0
domains_clean = []

for line in domains:
    
    string = ""
    
    string = line.replace("0.0.0.0 ", "")
    
    string = string.replace("0.0.0.0", "")
    
    domains_clean.append(string)
    
    

tmp = []

#Taking out any duplicates
domains_no_dups = [line for line in domains_clean if line not in tmp]


print("Domains "+ str(len(domains_clean)))
print("Domains after dups removal "+str(len(domains_no_dups)))

#Removing whitelisted domains
for line in whitelists:
    domains_no_dups.remove(line)


print("Domains after whitelist removal "+str(len(domains_no_dups)))

domains_no_comments =[]

#Removing comments and enter spaces
for line in domains_no_dups:
    if line.find("#") == -1 and line.strip() !="": #If not found then append
        domains_no_comments.append(line)
    
    

print("Domains after comments and enter removal "+str(len(domains_no_comments)))

def write_file(doms):
    with open("merged.txt", "w") as f:
        for line in doms:
            f.write(line)
            f.write("\n")


if input_ == 1:
    write_file(domains_no_comments)

elif input_ == 2:
    hosts = [("0.0.0.0 "+line) for line in domains_no_comments]
    
    write_file(hosts)

    
