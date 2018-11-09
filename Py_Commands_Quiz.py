#!/usr/bin/env python

content = {
'mkdir' : {
'prompt' : 'Does mkdir a) create a new directory, b) make a delivery, or c) marks the directory with a tag?',
'answer' : 'a',
'wrong_answer' : 'Oops. That\'s wrong. mkdir creates a new directory'
},

'echo' : {
'prompt' : 'Does echo a) increase your computer volume, b) print some arguments, or c) opens former versions of scripts?',
'answer' : 'b',
'wrong_answer' : 'Oops. That\'s wrong. echo prints some arguments'
},

'xargs' : {
'prompt' : 'Does xargs mean a) delete the arguments, b) execute the arguments, or c) eliminate the args file?',
'answer' : 'b',
'wrong_answer' : 'Oops. That\'s wrong. xargs means execute the arguments'
},

'cat' : {
'prompt' : 'Does cat a) call a category, b) prints the whole file, or c) is a question you have to answer?',
'answer' : 'b',
'wrong_answer' : 'Oops. That\'s wrong. cat prints the whole file'
},

'pwd' : {
'prompt' : 'Does pwd mean a) password, b) plain window display, or c) print working directory?',
'answer' : 'c',
'wrong_answer' : 'Oops. That\'s wrong. pwd means print working directory'
},

'ls' : {
'prompt' : 'Does ls mean a) lost system, b) level secure, or c) list directory?',
'answer' : 'c',
'wrong_answer' : 'Oops. That\'s wrong. ls means list directory',
},

'cd' : {
'prompt' : 'Does cd mean a) change directory, b) compact disc, or c) change developer?',
'answer' : 'a',
'wrong_answer' : 'Oops. That\'s wrong. cd means change directory',
},

'hostname' : {
'prompt' : 'Does hostname mean a) the computer\'s network name, b) the encrypted wifi name, or c) the server name?',
'answer' : 'a',
'wrong_answer' : 'Oops. That\'s wrong. hostname is the computer\'s network name',
},

'rmdir' : {
'prompt' : 'Does rmdir mean a) repair directory, b) run directory maintenance, or c) remove directory?',
'answer' : 'c',
'wrong_answer' : 'Oops. That\'s wrong. rmdir mean remove directory',
},

'man' : {
'prompt' : 'Does man mean a) manipulate the variable, b) modem and network, or c) read manual page?',
'answer' : 'c',
'wrong_answer' : 'Oops. That\'s wrong. man means read manual page'
},
}

#-------------------------------------------------------------------------

def shuffle(a):
return random.sample(a, len(a))
def ask(command):
data = content[command]
question = raw_input(content[command]['prompt'] + ' (type q to quit the game) ')
if question == content[command]['answer']:
print "Correct! Good job!"
return True
elif question == 'q':
print "Goodbye"
return None
else:
print content[command]['wrong_answer']
return False

#------------------------------------------------------------------

print "Welcome to the Newbie Commands flash card game!"
answer = raw_input("What is your name?")
if len(answer) > 0:
print "Good luck, " + answer + ", let's play!"

total = 0
correct = 0
for item in content.keys():
total += 1
result = ask(item)
if result == True:
correct += 1
elif result == False:
pass
else:
break

print "Thank you for playing " + answer + "!"
print "You have " + str(correct) + "/" + str(total)
