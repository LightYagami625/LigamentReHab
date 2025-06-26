import time
import pyttsx3 as txt

en = txt.init()
en.setProperty('rate', 150)
en.say("Let's START")
en.runAndWait()

num = 4

def laps(num):
    count = 0
    lap = 0
    while lap < num:
        print("Second:", count)
        en.say(str(count))
        en.runAndWait()
        count += 1
        if count % 5 == 0: # reset section
            print("5 seconds have passed!")
            # en.say("Leg down")
            lap = lap + 1
            en.say(f"{lap} lap completed")
            en.runAndWait()
            time.sleep(3)
            count = 0
            # en.say("Leg Up")
            # en.runAndWait()    
        time.sleep(1)


def straight_count(num):
    count = 0
    while count <= num:
        print(str(count))
        en.say(str(count))
        en.runAndWait()
        count += 1
        time.sleep(1)

if __name__ == "__main__":
    # straight_count(num=10)
    
    laps(num)