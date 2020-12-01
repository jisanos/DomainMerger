# DomainMerger
Hosts file and domain merging utility

# Usage

In the DomainLinks.txt paste links that lead to a set of hosts file or domains (examples are provided: eg. https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts)

In the Whitelist.txt enter the domains you wish to whitelist (examples are provided: eg. login.live.com)

Run the script (double click it or `run python .\Script.py`) and select 1 if you wish to generate a domain list or 2 if you wish to generate a Hosts file.

The script will now obtain the data from the provided links and generate a merged.txt with all the domains

# Description
Merge a set of domains from the links you provide in the DomainLinks.txt
They can be in the form of 0.0.0.0 (hosts) or plain domains separated by enters of course

The script will ask the user if he wishes to generate a hosts file or a simple domain file.
This gives you the option to paste it to the windows or linux hosts file.
Alternatively you can generate a list with the domains only, good if you want to import it to something like Simple DNSCrypt.

You can also provide domains you wish to whitelist in the Whitelist.txt




# External Libraries
requests
