import random

name = input("What's up new guy, welcome to 67 RNG. What's your name?\n ")
start = input(f"Nice to meet you {name}, do you wanna play the game? \n 1 - yes \n 2 - no \n").strip()

if start == "1":
    print("Great, now let us start. \n")
elif start == '2':
    print("Whatever bozo.")
    exit()
    
class user:
    def __init__(self, name):
         self.name = name
         self.luck = 1
         self.money = 0
         self.potions = 1

player1 = user(name)


auras = {
  'uncommon': 0,
  'rare': 0,
  'epic': 0,
  'legendary': 0,
  'mythical': 0
}

def stats():
  print(f"-----User's Stats----- \n Name: {player1.name}    \n Luck: {player1.luck} \n Money: {player1.money}         \n Luck Potions: {player1.potions}")
            

def roll():
    global auras
    print("You rolled an aura")
    chance = random.randint(player1.luck, 100)
    if chance <= 50:
        print("You got an uncommon aura.")
        auras['uncommon'] += 1
    elif chance in range(51, 81): 
        print("You got an rare aura.")
        auras['rare'] += 1
    elif chance in range(81, 91):
        print("You got an epic aura.")
        auras['epic'] += 1
    elif chance in range(91, 95):
        print("You got an legendary aura.")
        auras['legendary'] += 1
    elif chance == 100:
        print("You got an mythical aura.")
        auras['mythical'] += 1
    else:
        print("You got nothing lol")
        
    
def inventory():
         
    print("-----Your auras----- \n")
    for aura, amount in auras.items():
      print(f'{aura}, {amount}')
    
def shop():
    global start
    global auras
    do = ''
    while do != '3':
        print('-----The Sigma Shop-----')
        do = input('What do you want to do? \n 1 - buy potions \n 2 - sell auras \n 3 - exit the shop \n')
        if do == "1":
            amount = int(input('How many?\n '))
            if player1.money >= amount * 50:
                player1.money -= amount * 50
                player1.potions += amount
                stats()
            else:
                print("You don't have enough money \n")
        elif do == "2":
            inventory()
            sold = input('\nWhich aura are you going to sell?\n')
            if sold in auras:
                quantity = int(input('\nHow many?\n'))
                if quantity > auras[sold] or quantity <= 0:
                    print("You don't have that many auras.\n")
                else:
                    if sold == 'mythical':
                        player1.money += 50 * quantity
                        auras['mythical'] -= quantity
                    elif sold  == 'legendary':
                        player1.money += 20 * quantity
                        auras['legendary'] -= quantity
                    elif sold  == 'epic':
                        player1.money += 10 * quantity
                        auras['epic'] -= quantity
                    elif sold  == 'rare':
                        player1.money += 5 * quantity
                        auras['rare'] -= quantity
                    elif sold  == 'uncommon':
                        player1.money += 1 * quantity
                        auras['uncommon'] -= quantity
                    stats()
            else:
                pass
                
        elif do == '3':
            start = "1"
        else:
            pass
            

def main():
    global start
    global stats
  
    while start == "1":
        inp = input("\n-----Actions----- \n 1 - Roll an aura \n 2 - Check inventory \n 3 - Check stats \n 4 - Shop \n 5 - drink a potion \n 6 - Exit \n")
        if inp == "1":
            roll()
        elif inp == "2":
            inventory()
        elif inp == "3":
            stats()
        elif inp == "4":
            start = "0"
            shop()
        elif inp == "5":
            if player1.potions == 0:
                print("you don't have any potions")
            else:
                player1.potions -= 1
                player1.luck += 5
                print("you drank a potion. luck +5")
        elif inp == '6':
            exit()
        else:
            pass
            

main()