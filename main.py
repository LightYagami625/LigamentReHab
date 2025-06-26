import time
import pyttsx3 as txt

en = txt.init()
en.setProperty('rate', 150)
en.say("Let's START")
en.runAndWait()

num = 2

def laps(num):
    en.say(f"This exercise contains {num} of Laps")
    en.runAndWait()
    time.sleep(1)
    count = 0
    lap = num
    while lap != -1:
        
        # print("Second:", count)
        en.say(str(count))
        en.runAndWait()
        count += 1
        if count % 5 == 0: # reset section
            lap = lap - 1
            if lap == 0:
                en.say("Take your Leg Down, Moving towards ")
                en.runAndWait()
                break
            en.say("Take your Leg down")
            en.runAndWait()
            
            print(f"{lap} Laps Remaining")
            en.say(f"{lap} lap remaining")
            en.runAndWait()
            time.sleep(3)
            count = 0
            en.say("Now Please Take your Leg Up")
            en.runAndWait()    
        time.sleep(0.8)


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