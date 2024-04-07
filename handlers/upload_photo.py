from aiogram import types
from loader import db, dp
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="Rasm joylash")
async def user_add_photo_bot(message: types.Message, state: FSMContext):
    data_photo = db.get_chat_id_photo_users(chat_id=message.chat.id)
    if data_photo:
        text = "Yuklagan rasimingiz !!! !!!"
        await message.answer_photo(photo=data_photo[2])
    else:
        text = "Rasm yuklang !!!"
        await state.set_state('upload-photo-bot')
    await message.answer(text=text)
    
@dp.message_handler(state='upload-photo-bot', content_types=types.ContentTypes.PHOTO)
async def upload_photo_bot_handler(message: types.Message, state: FSMContext):
    await message.answer(text='Yuklandi !!')
    await state.update_data(photo_id= message.photo[-1].file_id, chat_id = message.chat.id)
    data = await state.get_data()
    print(data)
    if db.add_photo(data):
        text = "Rasm muffaqiyatli yuklandi !!!"
        
    else:
        text = "Rasm yuklanmadi !!!"
    
    
    
    await message.answer(text=text)
    await state.finish()
    
    
@dp.message_handler(text="Rasmlar")
async def random_photo(message: types.Message):
    r_p = db.get_random_photo()
    if r_p:
        await message.answer_photo(photo=r_p[2])
    else:
        await message.answer("Rasm topilmadi")