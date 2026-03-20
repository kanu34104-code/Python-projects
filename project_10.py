8. #Desktop Notification using Python
from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="****Take a Break****",
            message="It's important to take regular breaks to rest your eyes and stretch your body.",
            timeout=10  # notification stays for 10 seconds
        )
        time.sleep(20)  
