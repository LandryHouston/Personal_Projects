import time
from termcolor import colored


def countdown(x):
    while x > 0:
        print(x)
        x -= 1
        time.sleep(1)


print("Start countdown in seconds: ")
seconds = input()
while not seconds.isdigit():
    print("Please enter an integer: ")
    seconds = input()
seconds = int(seconds)
countdown(seconds)


print(colored("BLASTOFF!", ("red"), attrs=["bold"]))

time.sleep(3)
start = [
    "Ready?",
    "Set?",
]

for second in start:
    time.sleep(1)
    print(colored(second, ("yellow")))
time.sleep(1)
print(colored("GO!", ("green"), attrs=["bold"]))
