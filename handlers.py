import keyboards as kb

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, чем я могу вам помочь?', reply_markup=kb.main)

@router.callback_query(F.data=='main')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Привет, чем я могу вам помочь?', reply_markup=kb.main)

@router.callback_query(F.data=='exams')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Выберите направление.', reply_markup=kb.exam)

@router.callback_query(F.data=='portals')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Вот 3 самые популярные платформы для подготовки к экзаменам:',
                                     reply_markup=kb.portal)
helpexam = "Здесь вы можете найти всё, что пригодится на экзамене.\nПросто выберите любой предмет и всё."

@router.callback_query(F.data=='dops')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(helpexam, reply_markup=kb.dop)

examen1 = 'Вот что сдавать на это направление:\n1. Математика(Профиль)\n2. Информатика\n3. Русский язык'
examen2 = 'Вот что сдавать на это направление:\n1. Математика(База)\n2. Обществознание\n3. Русский язык\n4. История'
examen3 = 'Вот что сдавать на это направление:\n1. Математика(Профиль)\n2. Обществознание\n 3. Русский язык'
examen4 = 'Вот что сдавать на это направление:\n1. Математика(Профиль)\n2. Химия\n3. Русский язык\n4. Биология'


@router.callback_query(F.data=='it')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(examen1, reply_markup=kb.It)

@router.callback_query(F.data=='gum')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(examen2, reply_markup=kb.Gum)

@router.callback_query(F.data=='soc')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(examen3, reply_markup=kb.Soc)

@router.callback_query(F.data=='himbio')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(examen4, reply_markup=kb.Himbio)

choice = 'Выберите, что хотите знать:'

@router.callback_query(F.data=='matem')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(choice, reply_markup=kb.Matem)

@router.callback_query(F.data=='inform')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(choice, reply_markup=kb.Inform)

@router.callback_query(F.data=='russian')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(choice, reply_markup=kb.Russian)

@router.callback_query(F.data=='society')
async def exams(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(choice, reply_markup=kb.Society)

