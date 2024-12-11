# Importing libraries 
from tkinter import *

# Creating display window
root = Tk()
root.geometry('300x300')
root.title("Mad Libs Generator")
Label(root, text= 'Mad Libs Generator\nHave fun!', font='arial 20 bold').pack()
Label(root, text= 'Click Any One:', font='arial 15 bold').place(x = 40, y = 80)

def mad_libs_1():
    animals = input("Enter a animal name")
    profession = input("Enter a profession name")
    cloth = input("Enter a cloth name")
    things = input("Enter a things name")
    name = input("Enter a name name")
    place = input("Enter a place name")
    verb = input("Enter a verb name")
    food = input("Enter a food name")
    print('say ' + food + ', the photographer said as the camera flashed! \n'
          + name + ' and I had gone to ' + place +' to get our photos taken on my birthday.\n'
          'The first photo we really wanted was a picture of us dressed as \n'
          + animals + ' pretending to be a ' + profession + '. when we saw the second photo,\n'
          'it was exactly what I wanted. We both looked like ' + things + ' wearing \n'
          + cloth + ' and ' + verb + ' --exactly what I had in mind')

def mad_libs_2():
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print('Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that\n'
          'looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a\n'
          +adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ 
          '\nand the dream ended when I said-- lets ' +verb+ '.')

def mad_libs_3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties\n"
          "of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a\n'
          +adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to\n'
          +place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to\n'
          'get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  

Button(root, text="The Photographer", font='arial 15', command= mad_libs_1, bg='ghost white').place(x = 60, y = 120)
Button(root, text="The Butterfly", font='arial 15', command= mad_libs_2, bg='ghost white').place(x = 70, y = 180)
Button(root, text="Apple And Apple", font='arial 15', command= mad_libs_3, bg='ghost white').place(x = 80, y = 240)

root.mainloop()