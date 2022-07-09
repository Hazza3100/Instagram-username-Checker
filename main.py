import requests
import threading
import random




def check():
    for i in range(10):
        while True:
        
            user = open('usernames.txt', 'r').read().splitlines()
            username = random.choice(user)

            r = requests.get(f'https://www.instagram.com/{username}/')
            if r.status_code == 200:
                print(f"Username is Taken | {username}\n")
            else:
                print(f"Username is available/not in use | {username}\n")
                open('available.txt', 'a').write(f'{username}\n')



def start():
    r = input("Amount of threads: ")
    for i in range(int(r)):
        threading.Thread(target=check).start()

start()
