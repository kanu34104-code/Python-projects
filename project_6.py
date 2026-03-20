5. #Speed Calculator
distance = float(input("Enter the distance traveled (in kilometeres): "))
time = float(input("Enter the time taken (in hours): "))
if time > 0:
    speed = distance / time
    print(f"The speed is {speed} km/h")
else:
    print("Time must be greater than zero to calculate speed.")
        