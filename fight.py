from hero import Hero

knight = Hero('Ричард', 50, 25, 20, 'меч')
rascle = Hero('Питер', 20, 5, 5, 'нож')
dragon = Hero('Дракон', 100, 25, 10, 'пламя')

print('Средиземноморье в опасности, на помощь спешит рыцарь!')
knight.print_info()
print(knight.name, 'идет по лесу, вдруг на встречу идет воришка...')
rascle.print_info()
knight.fight(rascle)
if knight.health > 0:
    knight.health = 50
    knight.armor = 50
    knight.power *= 2
    print('\n', knight.name, 'восстановил силы и стал опытнее, теперь сила его удара: ' + str(knight.power) + ', а класс брони: ' + str(knight.armor) + '\n')
    print('Наконец! ' + knight.name + ' добрался до подземелья')
    dragon.print_info()
    knight.fight(dragon)
    if knight.health > 0:
        print('Вы выйграли эту битву!')
    else:
        print('Вы проиграли!')
else:
    print('Вы проиграли!')
