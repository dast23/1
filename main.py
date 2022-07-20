ostatok_palok = True

while ostatok_palok:
    palo4ki = int(input('введите кол-во палочек: '))
    igrok1_name = input('введите имя игрок 1: ')
    igrok2_name = input('введите имя игрок 2: ')
    while ostatok_palok:
          if palo4ki <=0:
             print(f'палочек меньше чем надо:{palo4ki}\nконец')
             break
          if  palo4ki > 0:
              igrok1 = int(input(f'{igrok1_name} введите от 1 до 3 палочек : '))
              palo4ki = palo4ki - igrok1
              print(f'палок осталось:{palo4ki}')
          if  palo4ki <=0:
              print(f'{igrok2_name} выйграл\n{igrok1_name} пройграл')
              break
          if  palo4ki > 0:
              igrok2 = int(input(f'{igrok2_name} введите от 1 до 3 палочек : '))
              palo4ki = palo4ki - igrok2
              print(f'палок осталось:{palo4ki}')
          if  palo4ki <=0 :
              print(f'{igrok1_name} выйграл\n{igrok2_name} пройграл')
              break
    ostatok_palok = input('хотите сыграть еще раз? [да] или [нет] : ').lower() == 'да'
