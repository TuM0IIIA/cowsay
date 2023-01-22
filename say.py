import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("Please, enter the phrase: ")
print(cowsay.get_output_string('trex', this)) #can be  eliminated
#cowsay.cow(this)
engine.say(this)
engine.runAndWait()

#  Number of creatures: 16
#  ['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'pig',
#  'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']