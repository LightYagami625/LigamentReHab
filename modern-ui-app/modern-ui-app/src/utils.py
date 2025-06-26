def update_timer(label):
    import time
    for seconds in range(60):  # Update for 60 seconds
        label.config(text=f"Seconds: {seconds}")
        time.sleep(1)  # Simulate a delay for the timer update

def display_message(label, message):
    label.config(text=message)