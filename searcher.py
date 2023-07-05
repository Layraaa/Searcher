# searcher.py
# Tool made for search on Google, export results and download files from Google results

import datetime
import requests
import os
import shutil
from urllib.parse import urlparse
from bs4 import BeautifulSoup
try:
    from googlesearch import search # https://python-googlesearch.readthedocs.io/en/latest/
except ImportError:
    print("No module named 'google' found")

# Function that get the number of results of the given query
def number_results(query):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    URL = "https://www.google.com/search?q=" + query
    result = requests.get(URL, headers=headers)

    soup = BeautifulSoup(result.content, 'html.parser')

    total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False) # This will give back 'About 1,410,000,000 results'
    global results_num
    results_num = ''.join([num for num in total_results_text if num.isdigit()]) # It clean it up and remove all the characters that are not a number
    print("")
    print("There are about " + results_num + " results")
    print("")


print(" ____                      _               ")
print("/ ___|  ___  __ _ _ __ ___| |__   ___ _ __ ")
print("\___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__|")
print(" ___) |  __/ (_| | | | (__| | | |  __/ |   ")
print("|____/ \___|\__,_|_|  \___|_| |_|\___|_|   ")
print("")
print("Made by @Layraaa | v1.0")
print("https://github.com/Layraaa/Searcher")

# Create directory with the name of the case
case = input("Name of the case -> ")
directory = os.getcwd()

# Delete directory and   content if it exists
if os.path.exists(directory + "/" + case) == True :
    shutil.rmtree(directory + "/" + case)
    

# Create new directory
os.mkdir(os.path.join(directory, case))

# Ask for query and get back number of results
query = input("What do you want search? -> ")
number_results(query)

# search(stop)
total = int(input("How many results do you want get? -> "))

# search(num)
split = int(input("How many results do you want get in each request? (Default: 10) -> ") or 10)

# search(pause)
delay = int(input("How many delay (in senconds) do you want set up for each request? (Default: 2) -> ") or 2)

# search(safe)
while True:
    safe = str(input("Want activate the safe mode? [on/off] (Default: off) -> ") or "off")

    if safe == "on" or safe == "off":
        break
    else:
        print("Enter on or off")
        continue

# search(verify_ssl)
while True:
    ssl = input("Do you want verify the SSL certificate? (Default: Yes) -> ") or "Yes"

    if ssl.capitalize() == "Yes":
        ssl = bool(True)
        break
    elif ssl.capitalize() == "No":
        ssl = bool(False)
        break
    else:
        print("Enter Yes or No")
        continue

# search(user_aggent)
user_aggent = str(input("Which User Agent do you want use? (Default: None) -> ") or "None")

# serach(tld)
tld = str(input("Which Google TLD do you want use? (Default: com) -> ") or "com")

# Ask if the user want download the files
while True:
    download = input("Do you want download the content? It is recommended if you want search files (Default: No) -> ") or "No"

    if download.capitalize() == "Yes":
        download = bool(True)
        break
    elif download.capitalize() == "No":
        download = bool(False)
        break
    else:
        print("Enter Yes or No")
        continue

print("")
print("Starting...")
print("")

# Try create the output file
try:
    with open(directory + "/" + case + "/output.txt", 'w') as f:
        now = datetime.datetime.now()
        f.write("Output file from Searcher on " + now.strftime("%Y-%m-%d %H:%M:%S \n \n") + " - " + query)
except FileNotFoundError:
    print("output.txt couldn't be created, check permissions")
    exit()

f = open(directory + "/" + case + "/output.txt", 'a')   
x = 1

if download == True:
    # Try create the error file
    try:
        with open(directory + "/" + case + "/error.txt", 'w') as e:
            now = datetime.datetime.now()
            e.write("Files that couldn't be downloaded will be here \n \n")
    except FileNotFoundError:
        print("error.txt couldn't be created, check permissions")
        exit()

    e = open(directory + "/" + case + "/error.txt", 'a')

    # Get the results back and download them
    for j in search(query, tld=tld, safe=safe, num=split, stop=total, pause=delay, user_agent=user_aggent, verify_ssl=ssl):
        try:
            print("Downloading " + str(x) + "/" + str(total) + ": " + j)
            f.write(j + "\n")
            response = requests.get(j, allow_redirects=True)
            directory = os.getcwd()
            j = urlparse(j)
            open(directory + "/" + case + "/" + os.path.basename(j.path), "wb").write(response.content)
        except:
            print(j + " couldn't be downloaded")
            e.write(j + "\n")
        x = x + 1
    
    f.close()
    e.close()

else:

    # Get the results back
    for j in search(query, tld=tld, safe=safe, num=split, stop=total, pause=delay, user_agent=user_aggent, verify_ssl=ssl):
        print("Getting " + str(x) + "/" + str(total) + ": " + j)
        f.write(j + "\n")
        x = x + 1
    
    f.close()

print("Thanks for use Searcher!")
print("https://github.com/Layraaa/Searcher")
print("Made by @Layraaa")
print("")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⢉⣉⣉⣉⡉⠛⠷⣦⣄⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⣠⣴⣿⣿⣿⣿⣿⡿⣿⣶⣌⠹⣷⡀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⠉⠻⣧⠘⣷⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⠀⢹⡇⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣿⠛⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⢸⡇⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⢿⡆⠈⠛⠻⠟⠛⠉⠀⠀⠀⠀⠀⠀⣾⠃⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣦⠀⠀⠈⠉⠛⠓⠲⠶⠖⠚⠋⠉⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⢀⣄⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
