import pyautogui
import time
import random


def send_reply(n):
    if n > 8:
        # Send and close
        pyautogui.click(x=2570, y=251)  # Adjust coordinates as needed
        time.sleep(2)  # Short delay to ensure the click is registered
    else:
        # Send and close
        pyautogui.click(x=2570, y=215)  # Adjust coordinates as needed
        time.sleep(2)  # Short delay to ensure the click is registered

    # Confirm button
    pyautogui.click(x=2921, y=642)  # Adjust coordinates as needed
    time.sleep(1)  # Short delay to ensure the click is registered


# Main loop
num_tickets = 8  # Adjust this to the number of tabs/tickets you have open

while num_tickets != 0:
    send_reply(num_tickets)
    timeout = random.uniform(5 * 60, 10 * 60)
    print(f"Waiting {timeout / 60:.2f} minutes")
    time.sleep(timeout)
    num_tickets -= 1
