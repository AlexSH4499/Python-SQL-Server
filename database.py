import os

import sqlite3

import json

import csv


#Data Base part
conn = sqlite3.connect('name.db')
curs = conn.cursor()

'''curs.execute('''CREATE TABLE zoo
(critter VARCHAR(20) PRIMARY KEY,
count INT,
damages FLOAT)''')
'''

#Safe way to insert data into table
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?,?,?)'
curs.execute(ins, ('weasel',1, 2000.0))

#Fetch all
curs.execute('SELECT * FROM zoo')

rows = curs.fetchall()
print(rows)

#Always close at the end of program
curs.close()
conn.close()

#JSON PART
menu = \
{
    "breakfast": {
            "hours": "7-11",
            "items":{
                    "breakfast burritos":"$6.00",
                    "pancakes": "$4.00"
                }
        },
    "lunch" : {
            "hours": "11-3",
            "items":{
                    "hamburger": "$5.00"
                }
        },
    "dinner":{
            "hours":"3-10",
            "items": {
                    "spaghetti": "$8.00"
                }
        }
}

#Will create it into JSON structure
menu_json = json.dumps(menu)

print(menu_json)

#Will turn back into a python data
menu2 = json.loads(menu_json)
print(menu2)

#CSV PART

villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
    ]
#writes the key-value pairs into a csv style file
with open('villains','wt')as fout:
    cout = csv.DictWriter(fout, ['first','last'])
    cout.writeheader()
    cout.writerows(villains)

#reads the key-value pairs and loads them into 'villains'
with open('villains','rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

#To store data structures 'as-is' use pickle module


def prepare_file(name):
    if(os.path.exists(name)):
        pass
    
    elif(not os.path.exists(name)):
        os.mkdir(name)
        print('Directory with name'+'%s'+ 'has been created!', name)

#DECORATORS uses '@'+ name_of_dec_func

def doc_func(func):
    def new_function(*arg, **kwargs):
        print('Running function:', func.__name__)
        print('Positional args:', args)
        print('Keyword args:', kwargs)
        result = func(*args,**kwargs)
        print('Result:', result)
        return result
    return new_function

if __name__ == "__main__":
    database_shell()
