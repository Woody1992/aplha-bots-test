from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import requests

from google_sheet import add_to_spread_sheet, make_sorted_srt_from_list
import keybords as kb
from config import BOT_TOKEN_TASK_1, HOST

bot = Bot(token=BOT_TOKEN_TASK_1)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    name = State()
    phone_number = State()
    language = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, заполнить анкету?", reply_markup=kb.start_form_kb)


@dp.callback_query_handler(lambda c: c.data == 'start_form_bnt')
async def process_callback_start_form(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await Form.name.set()
    await bot.send_message(callback_query.from_user.id, 'Как вас зовут?')


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        data['language'] = []
        kb.choice_btn_1.text = 'Python'
        kb.choice_btn_2.text = 'JavaScript'
        kb.choice_btn_3.text = 'C++'
    await Form.next()
    await bot.send_message(message.from_user.id, "Введите номер телефона?")


@dp.message_handler(state=Form.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    await Form.next()
    await state.update_data(phone_number=message.text)

    await bot.send_message(message.from_user.id, "Любимые языки программирования. Выберете один или больше вариантов",
                           reply_markup=kb.choices_kb)


@dp.callback_query_handler(lambda c: c.data == 'python', state=Form.language)
async def get_answer_1(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        language_list = data['language']

    if callback_query.data in data['language']:
        language_list.remove(callback_query.data)
        kb.choice_btn_1.text = 'Python'
    else:
        language_list.append(callback_query.data)
        kb.choice_btn_1.text = u'\U00002714' + 'Python'

    await state.update_data(language=language_list)

    await bot.send_message(callback_query.from_user.id, "Любимые языки программирования. Выберете один или больше "
                                                        "вариантов", reply_markup=kb.choices_kb)


@dp.callback_query_handler(lambda c: c.data == 'javascript', state=Form.language)
async def get_answer_2(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        language_list = data['language']

    if callback_query.data in data['language']:
        language_list.remove(callback_query.data)
        kb.choice_btn_2.text = 'JavaScript'
    else:
        language_list.append(callback_query.data)
        kb.choice_btn_2.text = u'\U00002714' + 'JavaScript'

    await state.update_data(language=language_list)

    await bot.send_message(callback_query.from_user.id, "Любимые языки программирования. Выберете один или больше "
                                                        "вариантов", reply_markup=kb.choices_kb)


@dp.callback_query_handler(lambda c: c.data == 'c++', state=Form.language)
async def get_answer_3(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        language_list = data['language']

    if callback_query.data in data['language']:
        language_list.remove(callback_query.data)
        kb.choice_btn_3.text = 'C++'
    else:
        language_list.append(callback_query.data)
        kb.choice_btn_3.text = u'\U00002714' + 'C++'

    await state.update_data(language=language_list)

    await bot.send_message(callback_query.from_user.id, "Любимые языки программирования. Выберете один или больше "
                                                        "вариантов", reply_markup=kb.choices_kb)


@dp.callback_query_handler(lambda c: c.data == 'close_choices', state=Form.language)
async def finish_form(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        if not data['language']:
            await bot.send_message(callback_query.from_user.id, "Пожалуйста выберете хотя бы один из вариантов",
                                   reply_markup=kb.choices_kb)
        else:
            # save data to Google Sheets
            add_to_spread_sheet(chat_id=callback_query.from_user.id,
                                tg_username=callback_query.from_user.username,
                                data=data)

            # Save data to database
            languages = make_sorted_srt_from_list(data)
            payload = {
                "chat_id": callback_query.from_user.id,
                "tg_username": callback_query.from_user.username,
                "name": data['name'],
                "phone_number": data['phone_number'],
                "answers": languages,
            }
            response = requests.post(f'{HOST}/api/postform/', data=payload)

            await bot.send_message(callback_query.from_user.id, "Спасибо за ответы!")
            await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
