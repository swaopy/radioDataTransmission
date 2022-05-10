# countdown_sender.py

from microbit import *
import radio

radio.on()
radio.config(channel=7,length=50)

sleep(1000)

print("Countdown App")
print("micro:bit sender")

while True:
    text = input("Enter countdown start: ")
    value = int(text)
    text = input("Enter ms time between counts: ")         # add
    ms = int(text)                                         # add
    message = input("Enter message after countdown: ")
    
    dictionary = {  }
    dictionary['start'] = value
    dictionary['time'] = ms                                # add
    dictionary['after'] = message

    packet = str(dictionary)
    
    print("Send: ", packet)
    radio.send(packet)
    
    print()
    
    
    
    
    