from time import sleep
from random import randint

class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon + '\n')
    
    def strike(self, enemy):
        power = randint(1, self.power)
        enemy.armor -= power
        print('-> УДАР! ' + self.name + ' атакует ' + enemy.name + " с силой " + str(power) + ', используя ' + self.weapon)
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(enemy.name + ' Покачнулся. \n Класс его брони упал до ' + str(enemy.armor) + ', Уровень здоровья упал до ' + str(enemy.health) + '\n') 

    def fight(self, enemy):
        print('ДА НАЧНЕТСЯ БИТВА! \n')
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name + ' пал в этом нелегком бою \n')
                break
            sleep(2)
            enemy.strike(self)
            if self.health <= 0:
                print(self.name + ' пал в этом нелегком бою \n')
                break
            sleep(2)
# для использования без файла fight.py
# knight = Hero('Ричард', 30, 20, 10, 'меч')
# knight.print_info()
# sleep(2)
# rascle1 = Hero('Джек', 20, 10, 5, 'нож')
# rascle1.print_info()
# sleep(2)
# rascle2 = Hero('воробей', 20, 10, 5, 'нож')
# rascle2.print_info()
# sleep(2)

# while knight.health > 0 and (rascle1.health > 0 or rascle2.health > 0):
#     fight = input('Кого ударим? ' + rascle1.name + ' - 1, ' + rascle2.name + ' - 2')
#     if fight == '1':
#         knight.strike(rascle1)
#     else:
#         knight.strike(rascle2)
#     if rascle1.health > 0:
#         rascle1.strike(knight)
#     sleep(1)
#     if rascle2.health > 0:
#         rascle2.strike(knight)
# if knight.health > 0:
#     print('Вы победили!')
# else:
#     print('Вы проиграли!')
