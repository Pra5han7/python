#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:21:32 2018

@author: prashant
"""
# show board to user
def show_board():
    print'board looks as below. use numbers to put your response'
    print'in the designated position\n'
    print'|7|8|9|'
    print'|4|5|6|'
    print'|1|2|3|'
    print'\n'

#live board with user responses
def live_board(num,key):
    global position
    #check user dont select already filled position.
    if position[num-1] != ' ':
        num=input('position already marked. choose any vacant position: ')
        
    position[num-1]=player[key]
    print position
    i=8
    while i>=0:
        print'|{}|{}|{}|'.format(position[i-2],position[i-1],position[i])
        i-=3
        
# flip users to give alternative chance
def flip(key):
    if key=='player1':
        return 'player2'
    else:
        return 'player1'

# check for win
def win():
    # case1=> horizontal alignment
    #===> a bug was here I used for i in range(3) and incremented i by three. 
        # it doesnt work i will always iterate range. used while after that
    i=0
    while (i<=6):
        if position[i]==position[i+1] and position[i]==position[i+2] and position[i] != ' ':
          # uncomment below line for debugging win cases 
            # print'inside 1st for loop'
            print '{} won'.format(key)
            print'*****Horizontal alignment*****'
            return True
        i+=3
     # case 2=> vertical alignment
    for i in range(3):
        if position[i]==position[i+3] and position[i]==position[i+6] and position[i] != ' ':
            # uncomment below line for debugging win cases 
            #print'inside 2nd for loop'
            print '{} won'.format(key)
            print'*****Vertical alignment*****'
            return True
    # case 3=> diagonal alignment
    #position[::4] checks for 0,4,8 and position[2:7:2] for2,4,6 positions not to be blank
    #refer slicing for more info
    if position[0]==position[4] and position[0]==position[8] and position[::4] !=[' ',' ',' ']:
       # uncomment below line for debugging win cases 
        #print'inside 1st diagonal case'
        print '{} won'.format(key)
        print'*****Diagonal alignment*****'
        return True
            
    if position[2]==position[4] and position[2]==position[6] and position[2:7:2] !=[' ',' ',' ']:
        # uncomment below line for debugging win cases 
        #print'inside 2nd diagonal case'
        print '{} won'.format(key)
        print'*****Diagonal alignment*****'
        return True
    if ' ' not in position:
        print'\n*****Its a draw*****'
        
# Main program starts here
    #list of positions in the board. initially all blanks
#position=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
#list can also be defined as below
position=[' ']*9
print'*****welcome to TIC TAC TOE*****'
# player is a dictionary that have choices of the players either x or o
while True:
	
	player={'player1':None,'player2':None}
#get input from user for his choice x or o
	player['player1']=raw_input('player1 enter your choice X or O: ')

#if x chosen by player1 make player2 o or vice versa
	if player['player1']=='x':
    		player['player2']='o'
	else:
    		player['player2']='x'

#greet user with board help
    #===> a bug was here instead of chk_key key was used which was getting changed.
        # by the loop and greet was not able to address the correct player. 
        # used chk_key there and assigned the player value match to key.
	print'game is on {}'.format(player)
	for chk_key,value in player.items():
    		if value=='x':
        		key=chk_key
        		print'{} will go first'.format(key)
	show_board()


	for chance in range(9):
	    #pos is the response in number given by user
	    print'{}: enter your response where you want to mark'.format(key)
	    pos=input()
	    live_board(pos,key)      
	    res=win()
	    if (res):
		break
	    key=flip(key)
	if ' ' not in position or res==True:
		play_again=raw_input('want to play again. y/n: ')
		if play_again=='y':
			position=[' ']*9
		elif play_again=='n':
			print'*****THANKS FOR PLAYING*****'
			break
		else:
			print'not a valid choice. exiting*****'
