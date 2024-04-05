from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

about_profil = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton('About'), KeyboardButton('Qidiruv')]
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


followers = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton('Follower'), KeyboardButton('UnFollow')]
    ]
    ,
    resize_keyboard=True,
    one_time_keyboard=True
)


