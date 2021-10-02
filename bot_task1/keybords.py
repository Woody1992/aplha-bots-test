from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Кнопка начала анкеты
start_form_btn = InlineKeyboardButton('Пройти анкету', callback_data='start_form_bnt')
start_form_kb = InlineKeyboardMarkup().add(start_form_btn)

# Кнопки ответов
choice_btn_1 = InlineKeyboardButton('Python', callback_data='python')
choice_btn_2 = InlineKeyboardButton('JavaScript', callback_data='javascript')
choice_btn_3 = InlineKeyboardButton('C++', callback_data='c++')
close_btn = InlineKeyboardButton('Завершить анкету', callback_data='close_choices')
choices_kb = InlineKeyboardMarkup().add(choice_btn_1).add(choice_btn_2).add(choice_btn_3).add(close_btn)

