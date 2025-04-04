from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Онлайн-курсы для подготовки🖥️',
                                                                   url='https://academika.ru/catalog/?free')],
                                             [InlineKeyboardButton(text='Что сдавать на экзамене?🔎',
                                                                   callback_data='exams')],
                                             [InlineKeyboardButton(text='Порталы для подготовки к ОГЭ/ЕГЭ🌐',
                                                                   callback_data='portals')],
                                             [InlineKeyboardButton(text='Дополнительно📌',
                                                                   callback_data='dops')]])

exam = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='IT-технологии👨🏻‍💻',
                                                                   callback_data='it')],
                                             [InlineKeyboardButton(text='Гуманитарные науки🎓',
                                                                   callback_data='gum')],
                                             [InlineKeyboardButton(text='Социальные науки👨‍👩‍👧‍👦',
                                                                   callback_data='soc')],
                                             [InlineKeyboardButton(text='Химико-биологические науки🧬',
                                                                   callback_data='himbio')],
                                             [InlineKeyboardButton(text='Назад', callback_data='main')]])

It = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад🔙', callback_data='exams')]])
Gum = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад🔙', callback_data='exams')]])
Soc = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад🔙', callback_data='exams')]])
Himbio = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад🔙', callback_data='exams')]])

portal = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='СДАМ ГИА', url='https://sdamgia.ru/')],
                                               [InlineKeyboardButton(text='Skysmart', url='https://skysmart.ru/')],
                                               [InlineKeyboardButton(text='КЕГЭ', url='https://kompege.ru')],
                                               [InlineKeyboardButton(text='Назад🔙', callback_data='main')]])

dop = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Математика📐', callback_data='matem'),
                                            InlineKeyboardButton(text='Информатика🗂️', callback_data='inform')],
                                            [InlineKeyboardButton(text='Русский язык📖', callback_data='russian')],
                                            [InlineKeyboardButton(text='Обществознание🧑🏻', callback_data='society')],
                                            [InlineKeyboardButton(text='Физика⚛️',
                          url='https://fizikaiis.ucoz.ru/fizika_v_formulakh_i_opredelenijakh_krapivkina_m.d.pdf')],
                                            [InlineKeyboardButton(text='Биология🦠',
                          url='https://4ege.ru/biologi/51417-spravochnye-materialy-po-obschey-biologii.html'),
                                             InlineKeyboardButton(text='Химия⚗️',
                          url='https://100ballnik.com/wp-content/uploads/2021/08/spravochnik-ege2022-himiya-1.pdf')],
                                            [InlineKeyboardButton(text='Назад🔙', callback_data='main')]])

Matem = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ОГЭ',
url='https://shkolapaska-r43.gosweb.gosuslugi.ru/netcat_files/30/66/Spravochnye_materialy_OGE_ShKOLA_PIFAGORA.pdf'),
                                               InlineKeyboardButton(text='ЕГЭ',
url='https://gipotenuza.ucoz.net/matematika/Spravochnye_materialy_EGE_profil_ShKOLA_PIFAGORA.pdf')],
                                              [InlineKeyboardButton(text='Назад🔙', callback_data='dops')]])

Inform = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ОГЭ',
url='https://multiurok.ru/files/shpargalka-po-informatike.html?ysclid=m7ak5llhff649996515'),
                                                InlineKeyboardButton(text='ЕГЭ',
url='https://4ege.ru/informatika/65216-shpargalka-po-informatike.html')],
                                               [InlineKeyboardButton(text='Python',
url='https://pymanual. pgithub.io/?ysclid=m7akyxga8y950212608')],
                                               [InlineKeyboardButton(text='Назад🔙', callback_data='dops')]])

Russian = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ОГЭ',
url='https://krbor.tsn.47edu.ru/images/doc/shmo/spravochnik_oge.pdf'),
                                                 InlineKeyboardButton(text='ЕГЭ',
url='https://publishing.intelgr.com/archive/Polnii-spravochnik-po-russkomu-yaziku.pdf')],
                                                [InlineKeyboardButton(text='Назад🔙', callback_data='dops')]])

Society = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ОГЭ',
url='https://multiurok.ru/index.php/files/materialy-dlia-podgotovki-k-oge-shpargalki.html?ysclid=m7al3oekiq478001571'),
                                                 InlineKeyboardButton(text='ЕГЭ',
url='https://4ege.ru/obshestvoznanie/65471-shpargalka-po-obschestvoznaniju.html')],
                                                [InlineKeyboardButton(text='Назад🔙', callback_data='dops')]])