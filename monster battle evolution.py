import os
import sys
import time
import random

if not os.path.exists('User Info.txt') :
    name = input('Enter your name : ')
    id = input('Set your id : ')
    password = input('Set your password : ')
    print('\nHere are the rules :- \n')
    rules = """ 1. The monsters take turns attacking each other.
2. The attack power of the attacking monster is subtracted from the defense power of the defending monster.
3. If the defending monster's defense power is greater than the attacking monster's attack power, the defending monster takes no damage.
4. If the defending monster's defense power is less than or equal to the attacking monster's attack power, the defending monster takes damage equal to the difference.
5. The battle continues until one monster's health reaches zero.
"""
    print(rules)
    with open('User Info.txt','w') as ui :
        ui.write(name + '\n' + id + '\n' + password)

f = open('User Info.txt','r') 
info = f.read().splitlines()
name = info[0]
id = info[1]
password = info[2]

if not os.path.exists('User level.txt') :
    
    with open('User level.txt','w') as ul :
        ul.write('1')

with open('User level.txt','r') as ul :
    level = int(ul.read()) 

if not os.path.exists('User power boosts.txt') :

    with open('User power boosts.txt','w') as pb :
        pb.write('0')
        
with open('User power boosts.txt','r') as pb :
    power_boosts = int(pb.read())

user_health = level * 10 + power_boosts

enemies = [
    'Dragon', 'De Morgan','Griffin', 'Minotaur', 'Hydra', 'Sphinx','Centaur', 'Harpy', 'Mermaid', 'Yeti', 'Goblin', 'Troll', 'Orc','Elf', 'Dwarf', 'Werewolf', 'Vampire', 'Zombie', 'Skeleton', 'Mummy', 'Kraken', 'Leviathan', 'Basilisk', 'Cockatrice', 'Wyvern', 'Phoenix', 'Thunderbird', 'Jackalope', 'Chupacabra', 'Mothman', 'Cthulhu', 'Shoggoth','Mantis', 'Scorpion', 'Tarantula', 'Wererat', 'Wraith', 'Ghoul', 'Revenant', 'Abomination', 'Goomba', 'Koopa', 'Bullet Bill', 'Bob-omb', 'Chain Chomp', 'Boo', 'Shy Guy', 'Magikoopa', 'Lakitu', 'Cheep Cheep', 'Godzilla', 'King Kong', 'Frankenstein\'s Monster', 'Dracula', 'The Mummy', 'The Creature from the Black Lagoon', 'The Invisible Man', 'The Wolf Man', 'The Bride of Frankenstein', 'The Phantom of the Opera', 'Pikachu', 'Charizard', 'Blastoise', 'Venusaur', 'Dragonite', 'Tyranitar', 'Gyarados', 'Lucario', 'Giratina', 'Dialga', 'Behemoth', 'Leviathan', 'Cerberus', 'Chimera', 'Hydra',  'Gorgon', 'Harpy', 'Minotaur', 'Sphinx', 'Cyclops', 'Troll', 'Ogre', 'Goblin', 'Imp', 'Demon', 'Devil', 'Baphomet', 'Asmodeus', 'Beezle', 'Lucifer', 'Zombie', 'Skeleton', 'Mummy', 'Vampire', 'Werewolf', 'Frankenstein\'s Monster', 'Bride of Frankenstein', 'Alien', 'Predator', 'Terminator', 'RoboCop', 'Cyborg', 'Android', 'Robot', 'Machine', 'Droid', 'Clone', 'Ghost', 'Spirit', 'Specter', 'Phantom', 'Apparition', 'Poltergeist', 'Haunt', 'Entity', 'Being', 'Soul', 'Abomination', 'Mutation', 'Freak', 'Monster', 'Creature', 'Beast', 'Animal', 'Mutant', 'Hybrid', 'Chimera', 'Medusa', 'Hydra', 'Sphinx', 'Minotaur', 'Gorgon', 'Cyclops', 'Cerberus', 'Dragon', 'Wyvern', 'Griffin', 'Phoenix', 'Thunderbird', 'Jackalope', 'Chupacabra', 'Mothman', 'Skunk Ape', 'Sasquatch', 'Giant Spider', 'Giant Scorpion', 'Giant Centipede', 'Giant Snake', 'Giant Crocodile', 'Giant Shark', 'Giant Octopus', 'Giant Squid', 'Kraken', 'Leviathan','Voldemort','Blob','The Thing','Jörmungandr', 'Fenrir', 'Nuckelavee', 'Wendigo', 'Baba Yaga', 'Gashadokuro','Kitsune', 'Tsuchigumo', 'Tikbalang', 'Manananggal', 'Pontianak', 'Jiangshi','Dybbuk', 'Sirens', 'Dullahan', 'Xenomorph', 'The Demogorgon', 'Slenderman', 'The Rake', 'Cloverfield Monster','The Babadook', 'Pennywise', 'The Headless Horseman', 'Mind Flayer', 'Gelatinous Cube', 'Beholder', 'Lich', 'Gnoll', 'Basilisk','Tarrasque', 'Shadow People', 'Gargoyle', 'Naga','Banshee', 'Kelpie', 'Charybdis', 'Scylla', 'Amarok', 'Adlet', 'Kappa', 'Onryo','Tengu', 'Gumiho', 'Nian', 'Jubokko', 'Ciguapa', 'Mapinguari', 'Encantado',  'Abarimon', 'Tikoloshe', 'Inkanyamba', 'Ahuizotl', 'Camazotz', 'Mo\'o', 'Ittan-momen','Krampus', 'Spring-Heeled Jack', 'The Slender Man', 'The Backrooms Entity','The Rake', 'The SCP-096', 'SCP-173', 'SCP-682', 'The Thing from Another World','Hollow Man', 'Zalgo', 'The Pale Man', 'The Crooked Man', 'The Smiling Man',  'The Bye Bye Man', 'Mimic','Shoggoth', 'Dark Young of Shub-Niggurath', 'Formless Spawn', 'Night Gaunt','Doppelgänger', 'Rakshasa', 'Balrog', 'Otyugh', 'Displacer Beast', 'Umber Hulk',  'Roper', 'Remorhaz', 'Slaad', 'Githyanki', 'Drider', 'Yuan-ti', 'Nightmare','Barghest', 'Hellhound', 'Quasit', 'Nuckelavee', 'Fetch', 'Gholem', 'Ifrit','Efreeti', 'Marid', 'Djinn', 'Huldra', 'Leshy', 'Domovoi', 'Myling', 'Strigoi']

used_attack = set()
used_defence = set()    

def stimulate_battle(enemy, enemy_health) :
    
    """Simulates a battle between the user and the enemy.

    Args:
        enemy (str): The name of the enemy.
        enemy_health (int): The health of the enemy.

    Returns:
        int: The updated health of the user."""
    
    global user_health
    global level
    global power_boosts    
    global used_attack
    global used_defence
    
    while True :
        try :
            while True :
                
                user_attack = int(input(f'\nEnter your attack power (1 - {user_health}) : '))
                
                if user_attack in used_attack :
                    print('You have already used this attack. Please choose a different one. ')
                    continue
                
                else :
                    used_attack.add(user_attack)
                    break
                
            enemy_defence = random.randint(1, enemy_health)
            print(f'Defence of {enemy} : {enemy_defence}')
            
            if (user_attack < user_health) :
                
                print (f'{name} attacks {enemy} for {user_attack} damage!')
                
                if (user_attack > enemy_defence) :    
                    enemy_health = enemy_health - (user_attack - enemy_defence)
                    print (f'{enemy}\'s health : {enemy_health}')
                    if (enemy_health <= 0) :
                        level = level + 1
                        print (f'\nCongratulations!! You win\nLevel up!! You have reached level {level}')
                        with open('User level.txt','w') as ul :
                            ul.write(str(level)) 
                        user_health = level * 10
                        
                        if (level % 10 == 0) :
                            power_boosts = power_boosts + 10
                            with open('User power boosts.txt','w') as pb :
                                pb.write(str(power_boosts))
                            user_health += power_boosts
                            print ('You got 10 power boosts!!') 
                        break
                else :
                    print (f'{enemy} takes no damage')
            
            else :
                print('The attack you have entered is greater than your health!! ')
            
            while True :
            
                user_defence = int(input(f'\nEnter your defence power (1 - {user_health}) : '))
                
                if user_defence in used_defence :
                    print('You have already used this defence number. Please choose a different one.')
                    continue
                
                else :
                    used_defence.add(user_defence)
                    break
                    
            enemy_attack = random.randint(1, enemy_health)
            print(f'Attack of {enemy} : {enemy_attack}')
            
            if (user_defence <= user_health) :
                print(f'{enemy} attacks {name} for {enemy_attack} damage!')
                
                if (enemy_attack > user_defence) :
                    user_health = user_health - (enemy_attack - user_defence)
                    print (f'{name}\'s health : {user_health}')
                    
                    if (user_health <= 0) :
                        print ('Sorry!! You lose!! \nBetter luck next time!! ')
                        user_health = level * 10
                        break
                
                else :
                    print (f'{name} takes no damage')
                
            else :
                print('The defence you have applied is greater than your health!! ')
        
        except Exception as e :
            print(f'Sorry, some error occurred.\nError : {e}')
    return user_health

def BattleWithCastle(enemy,castle_durability) :
    
    """Simulates a battle between the user and the enemy's castle.

    Args:
        enemy (str): The name of the enemy.
        castle_durability (int): The durability of the castle.

    Returns:
        int: The updated health of the user.
    """
    
    global user_health
    global used_attack
    global used_defence
    
    print(f'\nYou have to break {enemy}\'s Castle first to reach him\nBe Careful!! Castle\'s Attack and Defence System is activated')
    
    print(f'\nCastle\'s Durability : {castle_durability}')
    
    while True :
        try :
            while True :
                
                user_attack = int(input(f'\nEnter your attack power (1 - {user_health}) : '))
                
                if user_attack in used_attack :
                    print('You have already used this attack. Please choose a different one. ')
                    continue
                    
                elif user_attack >= user_health :
                    print('The attack you have entered is greater than your health. Kindly choose another one.')
                    continue
                
                else :
                    used_attack.add(user_attack)
                    break 
            
            castle_defence = random.randint(1,castle_durability)
            print(f"Defence System of Castle : {castle_defence}")
            print(f'{name} attacked {enemy} for {user_health} damage!')
            if user_attack > castle_defence :
                castle_durability = castle_durability - (user_attack - castle_defence)
                print (f'Castle\'s Durability : {castle_durability}') 
                
                if castle_durability <= 0 :
                    print (f'\nCongratulations! You have destroyed {enemy}\'s castle\nNow you have to kill {enemy}')  
                    break
            else :
                print('No damage done to Castle')  
                     
            while True :
                user_defence = int(input(f'\nEnter your defence power (1 - {user_health}) : '))
                
                if user_defence in used_defence :
                    print('You have already used this defence number. Please choose a different one.')
                    continue
                
                elif user_defence > user_health :
                    print('The defence you have entered is greater than your health. Kindly choose another one. ')
                    continue
                
                else :
                    used_defence.add(user_defence)
                    break
            castle_attack = random.randint(1,castle_durability)
            print(f'Attack by Castle : {castle_attack}')
            print(f'Castle attacks {name} for {castle_attack} damage!')

            if user_defence < castle_attack :
                 user_health = user_health - (castle_attack - user_defence)
                 print (f'{name}\'s health : {user_health}')  
                 if user_health <= 0 :
                     print ('\nSorry!! You lose!! \nBetter luck next time!! ')
                     break 
                        
            else :
                 print(f'{name} takes no damage') 
                 
        except Exception as e :
             print(f'Sorry!! Some error occurred!\nError : {e}')
    return user_health  

def BattleWithArmy(enemy, army_health) :
    
    """Simulates a battle between the user and the enemy's army.

    Args:
        enemy (str): The name of the enemy.
        army_health (int): The health of the army.

    Returns:
        int: The updated health of the user.
    """
    
    global user_health
    global used_attack
    global used_defence    
    
    print('\nYour quest begins! To reach the Monster\'s castle, you must first defeat the Dark Army that guards the entrance.')
    print(f'\nArmy Health : {army_health}')
    
    while True :
        try :
            while True :
                
                user_attack = int(input(f'\nEnter your attack power (1 - {user_health}) : '))
                
                if user_attack in used_attack :
                    print('You have already used this attack. Please choose a different one. ')
                    continue
                    
                if user_attack >= user_health :
                    print('The attack you have entered is greater than your health. Kindly choose another one.')
                    continue
                
                else :
                    used_attack.add(user_attack)
                    break
           
            army_defence = random.randint(1, army_health)
            
            print(f'Defence of {enemy}\'s Army : {army_defence}')
            print (f'{name} attacks {enemy}\'s Army for {user_attack} damage!')
            
            if user_attack > army_defence :
                army_health = army_health - (user_attack - army_defence)
                print(f'Army\'s health : {army_health}')
                if army_health <= 0 :
                    print ('\nCongratulations! You have defeated the Dark Army\nHowever,the real challenge lies ahead.The Monster\'s castle remains, and the monster\'s power grows by the minute. You must press on and claim Victory!')
                    break
            else :
                print('No damage done to Army')
                
            while True :
                user_defence = int(input(f'\nEnter your defence power (1 - {user_health}) : '))
                
                if user_defence in used_defence :
                    print('You have already used this defence number. Please choose a different one.')
                    continue
                
                if user_defence > user_health :
                    print('The defence you have entered is greater than your health. Kindly choose another one. ')
                    continue
                
                else :
                    used_defence.add(user_defence)
                    break
            army_attack = random.randint(1,army_health)
            print(f'Attack by Army : {army_attack}')
            print(f'Army attacks {name} for {army_attack} damage!')

            if user_defence < army_attack :
                 user_health = user_health - (army_attack - user_defence)
                 print (f'{name}\'s health : {user_health}')  
                 if user_health <= 0 :
                     print ('\nSorry!! You lose!! \nBetter luck next time!! ')
                     break 
                        
            else :
                 print(f'{name} takes no damage')   
                
        except Exception as e :
            print(f'Sorry! Some error occurred\nError : {e}')

    return user_health

def main() :
    
    ''' The main function of the program.

    It handles user authentication, level selection, and battle simulation.'''
    
    global user_health
    print('\t𝗠𝗢𝗡𝗦𝗧𝗘𝗥 𝗕𝗔𝗧𝗧𝗟𝗘 𝗘𝗩𝗢𝗟𝗨𝗧𝗜𝗢𝗡')
   
    try :
        entered_password = input('\nEnter your password: ')
        if password == entered_password :
            while True :
                print('\nDo you want to start next battle\nPress 1 to begin the battle and 0 to      cancel')
                user_input = int(input('>>> ')) 
                if user_input == 1 :
                
                    with open('User level.txt','r') as ul :
                        level = int(ul.read())
                    
                    with open('User power boosts.txt','r') as pb :
                        power_boosts = int(pb.read())
                    user_health = level * 10 + power_boosts
                    print(f'\nStarting level {level}\n')          
                    print('Selecting opponent...')
                    time.sleep(3)
                    enemy = random.choice(enemies)
                
                    if level < 10 :
                        enemy_health = random.randint(user_health - 5,user_health)
                
                    else :
                        enemy_health = random.randint(user_health, user_health + 50)

                    print(name, end='')
                    print('        vs        ', end='')
                    sys.stdout.flush()
                    time.sleep(3)
                    print(enemy)
                    print (f'\nYour health : {user_health}')
                    print (f'{enemy}\'s health : {enemy_health}')
                    print('\nStarting battle... ')
                    time.sleep(3)
                    
                    if level < 50 :              
                        user_health = stimulate_battle(enemy, enemy_health)
                        used_attack.clear()
                        used_defence.clear()
                    elif level >= 50 and level < 100 :
                        castle_durability = random.randint(user_health + 25, user_health + 100)
                        user_health = BattleWithCastle (enemy, castle_durability)   
 
                        if user_health <= 0 :
                            break
                        else :     
                            user_health = stimulate_battle(enemy, enemy_health)
                            used_attack.clear()
                            used_defence.clear()  
                    else :
                        army_health = random.randint(user_health + 50,user_health + 200)
                        user_health = BattleWithArmy(enemy, army_health)
                        if user_health <= 0 :
                            break
                        else :
                            castle_durability = random.randint(user_health + 25, user_health + 100)
                            user_health = BattleWithCastle (enemy, castle_durability)
                            if user_health <= 0 :
                                break
                            else :     
                                user_health = stimulate_battle(enemy, enemy_health)
                                used_attack.clear()
                                used_defence.clear()
                                   
                elif user_input == 0:
                    break
                
                else :
                    print('Kindly enter a valid number. ')
            
        else :
            print('Wrong password') 
    
    except Exception as e :
        print(f'Sorry, some error occurred.\nError : {e}')
   
if __name__ == '__main__' : 
    main()