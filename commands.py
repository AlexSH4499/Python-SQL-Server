import sqlite3 as sql

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

def cmd_help(cmds):

    str_cmds = str(cmds)

    li = str_cmds.strip('{}').split(',')

    for i in li:
        print(i.strip('[]')+'\n')

    print('\n')
    return
