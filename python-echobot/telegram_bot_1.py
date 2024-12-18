import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '7363199840:AAESKa_dKLknB5106-0UF2KX5OHxKHQpQ1k'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Глобальные переменные для игры
deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
user_score = 0

# Клавиатура для выбора действий
keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Взять карту')], [KeyboardButton(text='Закончить игру')]], resize_keyboard=True)

# Клавиатура для кнопки "Сыграть заново"
restart_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Сыграть заново')]], resize_keyboard=True)

@dp.message(Command(commands=['start']))
async def send_welcome(message: types.Message):
    global deck, user_score
    random.shuffle(deck)
    user_score = 0
    await message.reply("Добро пожаловать в игру 'Очко'!", reply_markup=keyboard)

@dp.message(lambda message: message.text == 'Взять карту')
async def take_card(message: types.Message):
    global deck, user_score

    if len(deck) == 0:
        await message.reply("Колода пуста. Начните новую игру с командой /start.")
        return

    card = deck.pop()
    user_score += card

    if user_score > 21:
        await message.reply(f"Вы взяли карту достоинством {card}. Ваши текущие очки: {user_score}. Вы проиграли! Ваши очки превысили 21.", reply_markup=restart_keyboard)
        user_score = 0
    elif user_score == 21:
        await message.reply(f"Вы взяли карту достоинством {card}. Ваши текущие очки: {user_score}. Поздравляю! Вы выиграли!", reply_markup=restart_keyboard)
        user_score = 0
    else:
        await message.reply(f"Вы взяли карту достоинством {card}. Ваши текущие очки: {user_score}.", reply_markup=keyboard)

@dp.message(lambda message: message.text == 'Закончить игру')
async def end_game(message: types.Message):
    global user_score
    await message.reply(f"Вы закончили игру. Ваши очки: {user_score}. Спасибо за игру!", reply_markup=restart_keyboard)
    user_score = 0

@dp.message(lambda message: message.text == 'Сыграть заново')
async def restart_game(message: types.Message):
    global deck, user_score
    random.shuffle(deck)
    user_score = 0
    await message.reply("Начинаем новую игру!", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
