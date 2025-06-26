import main

def knee():
    main.en.say("First Knee Exercise")
    main.en.runAndWait()
    main.laps(num = 20)

def pillow():
    main.en.say("Second Pillow Exercise")
    main.en.runAndWait()
    main.laps(num = 8)

def strenghtening():
    main.en.say("Third Exercise Strengthening your leg")
    main.en.runAndWait()
    main.laps(num = 15)

def folding():
    main.en.say("Fourth Exercise Folding the Led")
    main.en.runAndWait()
    main.straight_count(num = 30)

def bending():
    main.en.say("Fifth Exercise Bending the Legs to side wise")
    main.en.runAndWait()
    main.straight_count(num = 30)

def hip_up():
    main.en.say("Sixth Exercise Hip Upward")
    main.en.runAndWait()
    main.laps(num = 8)

def hip_side():
    main.en.say("Seventh Excercise Hip Side wise")
    main.en.runAndWait()
    main.laps(num = 8)

def hip_down():
    main.en.say("Eighth Exercise Hip Downward")        
    main.en.runAndWait()
    main.laps(num = 8)

if __name__ == "__main__":
    knee()
    main.en.say("Next Exercise  ")
    main.en.runAndWait()
    main.time.sleep(3)
    pillow()
    main.en.say("Next Exercise  ")
    main.en.runAndWait()
    main.time.sleep(3)
    strenghtening()
    main.en.say("Next Exercise  ")
    main.en.runAndWait()
    main.time.sleep(3)

    folding()
    main.en.say("Next Excercise  ")
    main.en.runAndWait()
    main.time.sleep(3)
    bending()
    main.en.say("Next Excercise  ")
    main.en.runAndWait()
    main.time.sleep(3)

    hip_up()
    main.en.say("Next Exercise  ")
    main.en.runAndWait()
    main.time.sleep(3)
    hip_side()
    main.en.say("Next Exercise  ")
    main.en.runAndWait()
    main.time.sleep(3)
    hip_down()
    main.en.say("Next Exercise  ")
    main.en.runAndWait()
    main.time.sleep(3)

    main.en.say("Congratulations! completed all exercises")
    main.en.runAndWait()