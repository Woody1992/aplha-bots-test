from aiogram import Bot, Dispatcher, executor, types
import requests

from config import BOT_TOKEN_TASK_2, HOST

bot = Bot(token=BOT_TOKEN_TASK_2)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def connect(message: types.Message):
    referral_code = message.get_args()
    if referral_code:
        response = requests.get(f'{HOST}/api/referral/{referral_code}')
        if response.status_code == 200:
            user = response.json()
            text = f"Приветствую {user['name']}! Твой уникальный код - {user['id']} "
            await bot.send_message(message.from_user.id, text)
        else:
            await bot.send_message(message.from_user.id, "Ваш реферальный код не действителен")
    else:
        await bot.send_message(message.from_user.id, 'Вы не можете начать использовать бот без реферальной ссылки. '
                                                     'Перейдите в бот с помощью реферальной ссылки')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
