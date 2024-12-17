""" print("задание 1")
import random
rndNum = random.randint(1, 10)
attempts = 0
while True:
    a = int(input("введите число от 1 до 10: "))
    attempts += 1
    if a > rndNum:
        print("ты написал число выше загаданного")
    elif a < rndNum:
        print("ты написал число ниже загаданного")
    elif a == rndNum:
        print(f"ты угадал число за {attempts} попыток!")
        break
    else:
        print("error") """
        
""" print("задание 2")
a = "сссоооссиииискккаааа"
symbol = list(a)
groupSymbols = []
for char in symbol:
    if not groupSymbols or groupSymbols[-1][-1] != char:
        groupSymbols.append([char])
    else:
        groupSymbols[-1].append(char)
print(groupSymbols) """

print("задание 3")
import random
deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(deck)
score = 0
print("Добро пожаловать в игру 'Очко'!")
while True:
    choice = input("Будете брать карту? (y/n): ").strip().lower()
    if choice == 'n':
        print(f"Вы набрали {score} очков.")
        break
    elif choice == 'y':
        card = deck.pop()
        score += card
        print(f"Вы взяли карту достоинством {card}. Ваши текущие очки: {score}.")
        if score > 21:
            print("Вы проиграли! Ваши очки превысили 21.")
            break
        elif score == 21:
            print("Поздравляю! Вы выиграли!")
            break
    else:
        print("Неверный ввод. Пожалуйста, введите 'y' или 'n'.")
print("Спасибо за игру!")