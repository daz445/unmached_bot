# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, types#pip install aiogram
from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.dispatcher import FSMContext
import asyncio
import randoms_person as rp
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from datetime import *
import texts
import sql
from randoms_person import get_results


from aiogram import Bot, Dispatcher, types#pip install --force-reinstall -v "aiogram==2.23.1"
import config 
import asyncio
from aiogram import Bot, Dispatcher, executor, types





#Конфигурация лога
logging.basicConfig(level=logging.INFO, filename=config.log_path, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info('Старт работы бота')




#Объявление бота 
bot = Bot(config.bot_token)
dp = Dispatcher(bot,storage=MemoryStorage())

#Состояние бота 
class Form(StatesGroup):
    TypeBatle = State()
    Players = State()



#Реагирование на ошибку
@dp.errors_handler()
async def errors_handler(update: types.Update, exception: Exception):
  logging.error(f'Ошибка при обработке запроса {update}: {exception}')


#БЛОК ОБРАБОТКИ СООБЩЕНИЙ  



#Старт чата
@dp.message_handler(commands=["start"])
async def start_chat(message):
       await bot.send_message(message.chat.id,texts.Welcome_text)


#Генирация партии 
@dp.message_handler(commands=["generate"])
async def add_person_chat(message):
    player_to_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for x in sql.get_all_persons():
        player_to_button.add(types.KeyboardButton(x+" ✅"))
    player_to_button.add(types.KeyboardButton("Готово"))
    await bot.send_message(message.chat.id,texts.Addperson_text_1, reply_markup=player_to_button)
    await Form.Players.set()







@dp.message_handler(state=Form.Players) 
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        if "players" not in proxy:
            proxy["players"] = [x+" ✅" for x in sql.get_all_persons()]
        if "✅" in message.text:
            proxy["players"][proxy["players"].index(message.text)] = proxy["players"][proxy["players"].index(message.text)].replace(" ✅","")

            player_to_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for x in proxy["players"]:
                player_to_button.add(types.KeyboardButton(x))
            player_to_button.add(types.KeyboardButton("Готово"))
            await bot.send_message(message.chat.id,texts.Addperson_text_1, reply_markup=player_to_button)
        
        if message.text in sql.get_all_persons():
            proxy["players"][proxy["players"].index(message.text)] +=" ✅"
            player_to_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for x in proxy["players"]:
                player_to_button.add(types.KeyboardButton(x))
            player_to_button.add(types.KeyboardButton("Готово"))
            await bot.send_message(message.chat.id,texts.Addperson_text_1, reply_markup=player_to_button)

        if len(proxy["players"]) == 5 and message.text.lower() == "готово":
            await Form.TypeBatle.set()  
        if message.text.lower() == "готово":
            await bot.send_message(message.chat.id,get_results([x.replace(" ✅","") for x in proxy["players"] if "✅" in x ]), reply_markup=types.ReplyKeyboardRemove())
            await state.finish()
              
        

@dp.message_handler(state=Form.TypeBatle) 
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy: 
        pass 




#Запуск бота 
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.create_task(infinity())
    executor.start_polling(dp,skip_updates=False, loop=loop)