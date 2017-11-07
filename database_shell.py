#The import statements comply with PEP 8
#Must be in order of First-Party then Third Party
#Followed by Alphabetical order in each case
import csv
from datetime import date
import os
import sqlite3

from debug import timer

#TODO: Add appropriate commands to the dict or the option to run them directly
#If either is done, remember to update the cmd_manager
def commands():
    dic = {\
            1:'''SELECT * FROM images''',\
            2:'''CUSTOM''',\
            3:'''ROW''',\
            4:'''VALUE(INT, INT, INT)''',\
            5:'''WHERE'''\
        }
    return dic

def sql_command(curr,s):
    if sqlite3.complete_statement(s):
        try:
            s = s.strip()
            curr.execute(s)

        except sqlite3.Error, e:
            print("Error while executing SQL command in {}".format(__name__))

    s = ''
    
    return 

def cmd_help(cmds):

    str_cmds = str(cmds)

    li = str_cmds.strip('{}').split(',')

    for i in li:
        print(i.strip('[]')+'\n')

    print('\n')
    return
    
def command_handler(curr, cmd):
    cmds = commands()
    if cmd in cmds.keys():
        try:
            
            if cmd == 1:
                curr.execute(cmds[cmd])
                print(curr.fetchall())
            if cmd == 2:#This blows up, giving invalid syntax error
                line = str(input('Provide the custom command:'))
                curr.execute(line)
                
        except sqlite3.Error, e:
            print "[!]Error occured while processing SQL Command:", e.args[0]

        return 0
    
    elif cmd == 0:
        cmd_help(cmds)
        return 0
    
    elif cmd == -1:
        print("[!]Terminating Database Session!")
        return -1

    else:
        print("Sorry, command not in list!")
        return 0

@timer
def database_shell():
    ''' Provides a simplistic commandline interface '''
    print('Welcome to the simple SQLite 3 database interactive shell!\n\
            To exit type -1!')
    print('(For help utilize the number 0)\n')
    
    try:
        conn, curr = setup_database('my.db')
    except IOError as e:
        print(e)

    line = 0
    while(line != -1):
        line = int(input("Input your commands here:"))
        line = command_handler(curr,line)
       
    conn.commit()
    close_db(conn, curr)

#Completely Unused
def load_database(name):
    '''Returns a list of dicts representing the csv filename provided'''
    #Assumes csv extension is already provided
    if(os.path.exists(name)):
        try:
            with open(name,'rt') as fin:
                cin = csv.DictReader(fin)
                data = [row for row in cin]
        except IOError as detail:
            print 'Run-time error while reading data:', detail
            
    else:
        raise IOError('Database with name {} does not exist!'.format(name))
    
    return data

def is_image(f):
    '''Compares the file '/f' to a list of Image extensions'''
    #TODO Apply ignore case-sensitivity
    IMG_FILE_EXTENSIONS = ['jpg', 'png', 'bmp','gif']
    isImg = False
    
    str_f = '{}'.format(f)
    li = str_f.split('.')
    mx = len(li)-1
    
    if li[mx].lower() in IMG_FILE_EXTENSIONS:#I think this sort of helps(?)
        isImg = True
    
    return isImg
    
@timer
def setup_database(name):
    '''Returns a tuple containing conn and cursor objects'''
    name += '.db'
    if(os.path.exists(name)):
        try:
            conn = sqlite3.connect(name)
            curr = conn.cursor()
            
            return (conn, curr)
        except sqlite3.Error, e:
            print("[@] Error while setting up existing DB:",e.args[0])
            
    else:
        print('[!]Creating database locally!')

        try:        
            conn = sqlite3.connect(name)
            curr = conn.cursor()

            #TODO: Find a better way to convert this into a list of tuples
            #       Using only one date instance
            #print(os.listdir('../Python-SQL-Server'))
            data = [f for f in os.listdir('../Python-SQL-Server') if is_image(f)]# this is list comprehension with a condition added
            today = str(date.today())
            date_li = []
            i = 0
            
            while(i <( len(data) -1)):
                date_li.append(today)
                i+= 1
                
            lib = zip(data,date_li)
            date_li = []
            today = ''
            data = []
            i=0

            name = name[0:len(name)-3]
            name += '.csv'
            
            #TODO: Something here is not working appropriately
            try:
                with open(name,'wt') as fout:
                    cout = csv.writer(fout,quoting=csv.QUOTE_NONE)#Likely candidate since it usually processes a list of lists
                    #Confirmed must take a list of list, Tups or Dicts
                    #Works fine now
                    cout.writerows(lib)
            except IOError, e:
                print("[#]Error while writing CSV data:", e)

            #Should check if table has previously been created
            try:
                curr.execute('''CREATE TABLE images(name VARCHAR(100)PRIMARY KEY, date VARCHAR(10))''')

                #ins = 'INSERT INTO images (name) VALUES(?)' for some reason this one won't work
               # print(lib)
                #curr.execute('INSERT INTO images (name) VALUES("{} , {}")'.format(lib[0],None) )#This was a test command 
                conn.commit()
                
            except sqlite3.Error , e:
                print('[@]Error while creating table in DB file:', e.args[0])
                
        except IOError, e:
            print('Some error?', e.args[0])
        
    return(conn, curr)

def update_database(name):
    #TODO LATER
    try:
        copy = load_database(name)
        today = str(date.today)
        local_dir = os.listdir('../')

        changes = [f for f in local_dir if f not in copy['name']]

        if len(changes) > 0:
            #should add the (new file and today's date) as a dict
            for f in changes:
                copy.append(zip(f,today))
                
            
            
    except Error as e:
        print('[@]Error updating database!',e)
    return

def close_db(conn, curs):
    curs.close()
    conn.close()

def main():
    database_shell()
    return

if __name__ == "__main__":
    main()
