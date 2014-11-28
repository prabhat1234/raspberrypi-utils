#!/usr/bin/python

import commands

# finding all the running instance of the voicecommand processes
cmd = "ps -elf | grep 'voicecommand'"
cmd_output = commands.getoutput(cmd)

# spliting on the basis of newline
com = cmd_output.split('\n')

if len(com) > 1:
    for c in com:
        # splitting the grep output on the basis of space
        pid = c.split(' ')[6] # pid of the process

        out = commands.getoutput('kill -9 %s' % pid)
        print "Killed %s voicecommand process" % pid


#startng the new voicecommand process
#commands.getoutput("voicecommand -c")
