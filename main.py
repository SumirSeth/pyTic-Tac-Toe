from time import sleep
game = {
    "1":"⬜",
    "2":"⬜",
    "3":"⬜",
    "4":"⬜",
    "5":"⬜",
    "6":"⬜",
    "7":"⬜",
    "8":"⬜",
    "9":"⬜"
}
def board():
    i = 1
    while (i<9):
        print(game[str(i)]+game[str(i+1)]+game[str(i+2)])
        i = i+3
def check():
    if ((game["1"] == "❌" and game["4"] == "❌" and game["7"] == "❌") or (game["2"] == "❌" and game["5"] == "❌" and game["8"] == "❌") or (game["3"] == "❌" and game["6"] == "❌" and game["9"] == "❌") or (game["1"] == "❌" and game["2"] == "❌" and game["3"] == "❌") or (game["4"] == "❌" and game["5"] == "❌" and game["6"] == "❌") or (game["7"] == "❌" and game["8"] == "❌" and game["9"] == "❌") or (game["1"] == "❌" and game["5"] == "❌" and game["9"] == "❌") or (game["3"] == "❌" and game["5"] == "❌" and game["7"] == "❌")):
        print(f"{user1} wins")
        exit()
    if ((game["1"] == "⭕" and game["4"] == "⭕" and game["7"] == "⭕") or (game["2"] == "⭕" and game["5"] == "⭕" and game["8"] == "⭕") or (game["3"] == "⭕" and game["6"] == "⭕" and game["9"] == "⭕") or (game["1"] == "⭕" and game["2"] == "⭕" and game["3"] == "⭕") or (game["4"] == "⭕" and game["5"] == "⭕" and game["6"] == "⭕") or (game["7"] == "⭕" and game["8"] == "⭕" and game["9"] == "⭕") or (game["1"] == "⭕" and game["5"] == "⭕" and game["9"] == "⭕") or (game["3"] == "⭕" and game["5"] == "⭕" and game["7"] == "⭕")):
        print(f"{user2} wins")
        exit()
def welcome():        
    welcomestring = "-------------------------------\n\nWelcome to Tic-Tac-Toe\n\n-------------------------------"
    print(welcomestring)
    sleep(2.8)
    print("\nThis is your board: ")
    board()
def users():
    global user1, user2
    user1 = input("Who is user 1? ")
    user2 = input("Who is user 2? ")

welcome()
print("\n")
sleep(2)
users()
print("\n")

sleep(2)
ch1=0
ch2=0
# for i in range(2):
#     ch1 = int(input("Enter choice for user 1: "))
    
#     game[str(ch1)] = "❌"
#     board()
#     ch2= int(input("Enter choice for user 2: "))
#     game[str(ch2)] = "⭕"
#     board()

while True:
    ch1 = int(input("Enter choice for user 1: "))
    game[str(ch1)] = "❌"
    board()  
    check()
    ch2= int(input("Enter choice for user 2: "))
    game[str(ch2)] = "⭕"
    board()
    check()
