import random

messages = [
    "1. No one is perfect - that’s why pencils have erasers. - Wolfgang Riebe",
    "2. Have no fear of perfection - you'll never reach it. - Salvador Dali",
    "3. The tallest mountain started as a stone. - One Punch Man Intro",
    "4. Make it work. Make it nice. Make it fast. Always obey this order! - kiraa",
    "5. A good programmer is someone who always looks both ways before crossing a one-way street. – Doug Linder",
    "6. If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Edsger W. Dijkstra"
]


def printRandomMessage(_messages):
    keep_running = True

    while keep_running:
        user_input = input("Spielt den selben Song nochmal? y/n ")
        if user_input == "y":
            random.shuffle(_messages)

            for i in range(len(_messages)):
                print(_messages[i])
            print("*" * 10)
        else:
            import sys
            sys.exit()


printRandomMessage(messages)
