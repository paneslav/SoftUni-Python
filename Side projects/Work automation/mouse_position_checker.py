import pyautogui
import time

print("Move your mouse to the desired position.")
print("The program will display the coordinates every 2 seconds.")
print("Press Ctrl+C to exit.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}", end='\r')
        time.sleep(2)
except KeyboardInterrupt:
    print("\nDone.")