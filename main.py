#Author Richard Rosenthal
#Date 5-12-21

import random 
import time

#This will generate a random number between 0 and 1. If 0 the coin is tails, if 1 the coin is heads
coin_toss = random.randint(0, 1)

#Start of user interaction 
print("Hello, welcome to heads or tails!")

answer = input("Are you ready? Y or N")

if(answer == 'Y' or answer == 'y'):
  print(".")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print("Give me a second, let me look")
  time.sleep(1)
  print(".")
  time.sleep(1)
  if(coin_toss == 0):
    print("Well it looks like you tossed tails!")
  else:
    print("Well it looks like you tossed heads")

print("See you later!")
  
  