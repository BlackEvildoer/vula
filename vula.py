import os, sys, time
os.system('clear')
try:
    a = raw_input('\x1b[30;1m\xe2\x94\x8c\xe2\x94\x80[\x1b[30;1m Input File\x1b[30;1m\n\x1b[30;1m\xe2\x94\x94\xe2\x94\x80[\x1b[31;1mB L A C K\x1b[0;37m]> \x1b[33;1m')
    b = open(a).read().replace('exec', 'x=')
    c = open('xyz.py', 'w')
    if 'marshal' in b:
        c.write('from sys import stdout\nfrom uncompyle6.main import decompile\n' + b + '\ndecompile(2.7, x, stdout)')
        c.close()
    elif 'marshal' not in b:
        c.write(b + '\nprint (x)')
        c.close()
    d = a.replace('.py', '-decompiled.py')
    os.system('python2 xyz.py > ' + d)
    e = open(d).read()
    f = open(d, 'w')
    f.write('# Decompiled By BLACK\n' + e)
    f.close()
    os.system('rm -rf xyz.py')
    print '\x1b[31;1m[\x1b[0;37m+\x1b[31;1m]\x1b[0;37m File saved as\x1b[32;1m %s' % d
except IndexError:
    print '\n\x1b[31;1m[\x1b[0;37m!\x1b[31;1m] \x1b[0;37mthere is an error'
    sys.exit()
except KeyboardInterrupt:
    print '\n\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m ctrl+c detected'
    print '\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m trying to exit'
    time.sleep(3)
    sys.exit()
except EOFError:
    print '\n\n\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m ctrl+d detected'
    print '\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m trying to exit'
    time.sleep(3)
    sys.exit()
except:
    print '\n\x1b[31;1m[\x1b[0;37m!\x1b[31;1m] \x1b[0;37m Exit'
    sys.exit()
