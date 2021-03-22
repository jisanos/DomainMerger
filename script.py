import requests
import re
from gui import Ui_MainWindow

# List containing the domain links extracted from blacklist_packs.txt
blacklist_packs = []
# List containing domains from the whitelist.txt
whitelist = []
# List containing domains from the blacklist.txt
blacklist = []
input_ = 0

while input_ <= 0 or input_ > 2:
    input_ = int(input("1. Domains Only\n2. Hosts File\n"))


with open("blacklist_packs.txt", "r") as f:
    # Stripping the \n characters and appending to list
    blacklist_packs = [line.strip() for line in f.readlines()]


with open("whitelist.txt", "r") as f:
    whitelist = [line.strip() for line in f.readlines()]


with open("blacklist.txt", "r") as f:
    blacklist = [line.strip() for line in f.readlines()]


# Appending all the domains from the links provided
domains = [sub_line for line in blacklist_packs
           for sub_line in
           requests.get(line).text.strip().split("\n")]


print("Domains default " + str(len(domains)))


# Will contain the domains stripped from 0.0.0.0
# and other unncecesary values
domains_clean = []

# using https://gist.github.com/chew-z/3a43967812fdac788d56
# as reference
localhost_pat = re.compile(
    '^0.0.0.0.*localhost\.localdomain.*$|^(?!\#).*broadcasthost.*$|^0.0.0.0.*local.*$')


comment_pat = re.compile('#(.*)\n')

other_pat = re.compile('(::)')

bad_pats = re.compile(
    '^0.0.0.0(\s*|\t*)|^127.0.0.1(\s*|\t*)|#(.*)')

for line in domains:

    line = bad_pats.sub("", line)

    if localhost_pat.search(line):
        print("localhost_pat: ", line)
        continue

    if comment_pat.search(line):
        print("comment_pat: ", line)
        continue

    if other_pat.search(line):
        print("other_pat: ", line)
        continue

    if re.fullmatch("0.0.0.0", line):
        print("fullmatch 0.0.0.0: ", line)
        continue

    if re.fullmatch("local", line):
        print("fullmatch local: ", line)
        continue

    if re.fullmatch("localhost", line):
        print("fullmatch localhost: ", line)
        continue

    if not line.strip():  # If whitespace
        # print("whitespace: ",line)
        continue

    domains_clean.append(line.strip())



print("Domains after comments, whitespace and others patterns removed " + str(len(domains_clean)))


# Adding lines from the blacklist.txt

for line in blacklist:
    domains_clean.append(line)

# Taking out any duplicates
domains_no_dups = list(set(domains_clean))

print("Domains after dups removal "+str(len(domains_no_dups)))

# Removing whitelisted domains
for line in whitelist:
    # If the string is in the list then remove, else dont
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

del blacklist_packs
del whitelist
del domains
del domains_clean
del domains_no_dups

input("Press return or enter to exit")
