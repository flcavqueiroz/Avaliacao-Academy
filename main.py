import os
import sys
import csv
import requests
import json



        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
       
        r = requests.get('https://jsonplaceholder.typicode.com/users').json()
        username = str(input('Insert a username: '))
        for username in r:
            if 'username' in username:
                lat = float(username['address']['geo']['lat'])
                if lat > 0:
                    hemisphere = "North"
                elif lat < 0:
                    hemisphere = "South"                   
                print(username['email'],
                username['website'], f"hemisphere:{hemisphere}")
            else: 
                print('Invalid username')
'''
    with open('users.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in csvreader:
            print(', '.join(row))
'''
        # Seu código entra aqui
#else:
#    print("passe um username")
