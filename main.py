import requests

server = "http://psll.club"

opt = input("<-> Select Option:\n1. Create Link\n2. Track Link\n3. Delete Link\n4. Exit\n\n")

try:
    int(opt)

except:
    print("[*] Something Went Wrong!")
    exit()

if int(opt) == 1:
    url = input("Enter URL to being short: Ex: https://google.com/\n")
    print(f'[#] Shorted Link is: {requests.get(f"{server}/create-short-link?link={url}").text}')
    with open("links.txt", "a+") as f:
        f.write(f'{url} {requests.get(f"{server}/create-short-link?link={url}").text}\n')
    print('\n[!] Exiting...')

elif int(opt) == 2:
    print("[@] Choose Link from Below:\n")
    with open("links.txt", "r") as f:
        links = f.readlines()
    i = 1
    for line in links:
        print(str(i) + ". " + line.split()[1].replace("\n", ""))
        i = i + 1
    print("")
    choice = int(input("[@] Enter your choice:\n"))
    temp = links[choice-1]
    link = temp.split()[1]
    print("Sending Request to get tracking info to server and printing it in a good way is remained here.")

elif int(opt) == 3:
    print("[@] Choose Link from Below:\n")
    with open("links.txt", "r") as f:
        links = f.readlines()
    i = 1
    for line in links:
        print(str(i) + ". " + line.split()[1].replace("\n", ""))
        i = i + 1
    print("")
    choice = int(input("[@] Enter your choice:\n"))
    temp = links[choice-1]
    link = temp.split()[1]
    r = requests.get(f"{server}/delete-short-link?endpoint={link.split('/')[3]}").json()
    print(f"\n[*] {r['Message']}")
    print("[!] Exiting...")

elif int(opt) == 4:
    print("[!] Exiting...")

else:
    print("[!] Something Went Wrong...") 
    print("[!] Exiting...") 
