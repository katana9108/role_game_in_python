import random

PLAYER_POINTS =50
ENEMY_POINTS =50
POTIONS_NUMBERS=3
TURN_PLAYERS =False

print("Bienvenue dans votre espace de combat 😎")

pseudo= input("laissez nous mettre un nom sur votre joueur😉: ?")

while True:
    if TURN_PLAYERS:
        print(f"Vous passez votre tour {pseudo}, 😣...")
        TURN_PLAYERS=False
    else:
        user_choice=""
        print(f"C'est partie on peut commencer {pseudo}😎 ! ")
        while user_choice not in ["1","2"]:
            user_choice= input(f"Souhaitez vous attaquer (1)💚 ou Prendre une potion 🌡 (2) {pseudo} ?".capitalize())
        if user_choice=="1":
            attack= random.randint(5,10)
            ENEMY_POINTS-= attack
            print(f"Vous avez infligé une attaque de {attack} points de dégats à votre ennemi 😱!")
        elif user_choice=="2":
            if POTIONS_NUMBERS>0:
                potion_health= random.randint(15,50)
                PLAYER_POINTS+=potion_health
                POTIONS_NUMBERS-=1
                TURN_PLAYERS=True
                print(f"Vous venez de gagner {potion_health} points de vie💚 et il vous reste {POTIONS_NUMBERS} potions restantes !")
            else:
                print(f"Désolé vous n'avez plus de potion {pseudo}")
                continue
        if ENEMY_POINTS<=0:
            print(f"Bien jouer {pseudo} vous avez ganer ! 🤑")
            break

        ennemy_attack = random.randint(5,15)
        PLAYER_POINTS-=ennemy_attack
        print(f"L'énnemi vous a infliger {ennemy_attack} points de dégats")

        if PLAYER_POINTS<=0:
            print(f" Désolé vous avez perdu {pseudo} il vous reste {PLAYER_POINTS} de vie !")
            break
        print(f"Il vous reste {PLAYER_POINTS} points de vie")
        print(f"Il reste a votre ennemi {ENEMY_POINTS} points de vie")
        print("-"*50)
print("End Game...")
    

        
        


