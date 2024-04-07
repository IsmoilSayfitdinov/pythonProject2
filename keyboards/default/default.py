from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

about_profil = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton('About'), KeyboardButton('Qidiruv')],
    [KeyboardButton('Rasmlar'), KeyboardButton('Rasm joylash')]
],
    resize_keyboard=True,
    one_time_keyboard=True

)

back = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton('Orqaga qaytish')]
],
resize_keyboard=True,
one_time_keyboard=True
)


followers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Follower", callback_data="follower")
        ]
    ]
)