from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
import telegram.error

# 🔒 Список разрешённых пользователей (замени ID на реальные)
ALLOWED_USERS = {5538804267, 1430105405, 485947883, 6932066810, 8026256981,
                7275611563, 723670550, 5880565984, 5636776284, 1611992582,
                6623251898, 5801420584, 8095108194}  # Замени на свои ID

# 🔐 Функция проверки доступа по ID
async def check_access(update: Update) -> bool:
    user_id = update.effective_user.id
    if user_id not in ALLOWED_USERS:
        # В зависимости от типа обновления отправляем сообщение об отказе
        if update.message:
            await update.message.reply_text("🚫 Доступ запрещён. Свяжитесь с администратором.")
        elif update.callback_query:
            await update.callback_query.message.reply_text("🚫 Доступ запрещён.")
        return False
    return True  # Доступ разрешён, если ID пользователя в списке

# 🚀 Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return  # Если нет текстового сообщения, выходим (например, callback вызвал start)
    # Проверяем доступ по ID
    if not await check_access(update):
        return
    # Приветствие и главное меню
    await update.message.reply_text("✅ Доступ разрешён. Добро пожаловать!")
    keyboard = [[InlineKeyboardButton("👥 Список диспетчеров", callback_data='dispatchers')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🚛 Главное меню:", reply_markup=reply_markup)

# Данные о диспетчерах и водителях (из исходного кода)
dispatchers = {
    "🚚 Диспетчер David": ["Водитель ALEKSEI LAMATKHANOV", "Водитель ALEKSANDR PAVLOV", "Водитель BAIR DABAIN", "Водитель BILIKTO LAMATKHANOV", ],
    "🚌 Диспетчер Serghei": ["Водитель LATIPOV PARVIZ", , "Водитель OLEH SEMENENNKO", "Водитель ILLIA HORBATOK", "Водитель (DOS) DASTAN MASYLKANOV"],
    "🚋 Диспетчер Vick": ["Водитель DARMAN ORUZBAEV",  "Водитель ERDEM DORZHIEV", "Водитель YERKEBULAN BOSHAIBEKOV", "Водитель MARIN GULIA"],
    "🚂 Диспетчер Peter": ["Водитель OLEG RESHAEV", "Водитель DIONISIE COTOVICI", "Водитель EVGENY SYROMITSKII", "Водитель RADZHAB MAGOMEDOV"],
    "🚀 Диспетчер Dima": ["Водитель GEORGII RIONELI", "Водитель IGOR BALAKIN", "Водитель SERGEI CIOBANU", "Водитель TAULAN TOTORKULOV", "Водитель ALBERT ABAIKHANOV", ],
    "✈ Диспетчер Max": [],
    "🎈 Диспетчер NONE": ["Водитель SOSLAN GAGLOEV"]
}

drivers_info = {
    "Водитель ALEKSEI LAMATKHANOV": (
        "📌 Driver Name: ALEKSEI LAMATKHANOV \n"
        "📞 Phone Number: 323-219-9464 \n"
        "🚛 Truck Number: 9 \n"
        "🚂 Trailer Number: 9 \n"
        "🔑 VIN:3C63RRGL2RG112628 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель BILIKTO LAMATKHANOV": (
        "📌 Driver Name: BILIKTO LAMATKHANOV \n"
        "📞 Phone Number: 224-716-4847 \n"
        "🚛 Truck Number: 21 \n"
        "🚂 Trailer Number: 21 \n"
        "🔑 VIN:3C63RRGL3RG109933 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Company"
    ),
    "Водитель ALEKSANDR PAVLOV": (
        "📌 Driver Name: ALEKSANDR PAVLOV \n"
        "📞 Phone Number: 929-721-9669 \n"
        "🚛 Truck Number: 1 \n"
        "🚂 Trailer Number: 1 \n"
        "🔑 VIN:1GC4KTEY7SF130031 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель BAIR DABAIN": (
        "📌 Driver Name: BAIR DABAIN \n"
        "📞 Phone Number: 470-978-5585 \n"
        "🚛 Truck Number: 10 \n"
        "🚂 Trailer Number: 10 \n"
        "🔑 VIN:3C63RRGL6RG109909 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Alexei Lamatkhanov"
    ),
    "Водитель BULAT TSYRENOV": (
        "📌 Driver Name: BULAT TSYRENOV \n"
        "📞 Phone Number:  \n"
        "🚛 Truck Number:  \n"
        "🚂 Trailer Number:  \n"
        "🔑 VIN: \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight:  \n"
        "🅱 Owner: "
    ),
    "Водитель OLEH SEMENENNKO": (
        "📌 Driver Name: OLEH SEMENENNKO \n"
        "📞 Phone Number: 701-971-4705 \n"
        "🚛 Truck Number: 25 \n"
        "🚂 Trailer Number: 25 \n"
        "🔑 VIN:3C63RRHL2RG307630 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Radu"
    ),
    "Водитель LATIPOV PARVIZ": (
        "📌 Driver Name: LATIPOV PARVIZ \n"
        "📞 Phone Number: 267-574-4243 \n"
        "🚛 Truck Number: 31 \n"
        "🚂 Trailer Number: 31 \n"
        "🔑 VIN:3C63RRJLLXNG152569 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель ILLIA HORBATOK": (
        "📌 Driver Name: ILLIA HORBATOK \n"
        "📞 Phone Number: 701-403-0994 \n"
        "🚛 Truck Number: 2 \n"
        "🚂 Trailer Number: 2 \n"
        "🔑 VIN:3C63RRHL2RG358187 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8720lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель (DOS) DASTAN MASYLKANOV": (
        "📌 Driver Name: DASTAN MASYLKANOV \n"
        "📞 Phone Number: 917-704-3848 \n"
        "🚛 Truck Number: 37 \n"
        "🚂 Trailer Number: 37 \n"
        "🔑 VIN:3C63RRHL6RG307632 \n"
        "⚓ Ramps: n/a \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель DARMAN ORUZBAEV": (
        "📌 Driver Name: DARMAN ORUZBAEV \n"
        "📞 Phone Number: 718-344-0617 \n"
        "🚛 Truck Number: 4 \n"
        "🚂 Trailer Number: 4 \n"
        "🔑 VIN:3C63RRHLXRG341413 \n"
        "⚓ Ramps: Mega Ramps \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель YERKEBULAN BOSHAIBEKOV": (
        "📌 Driver Name: YERKEBULAN BOSHAIBEKOV \n"
        "📞 Phone Number: 773-751-9292 \n"
        "🚛 Truck Number: 18 \n"
        "🚂 Trailer Number: 18 \n"
        "🔑 VIN:3C63RRHL0RG289662 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8100lb \n"
        "🅱 Owner: Dumitru OU"
    ),
    "Водитель MARIN GULIA": (
        "📌 Driver Name: MARIN GULIA \n"
        "📞 Phone Number: 916-912-7398 \n"
        "🚛 Truck Number: 42 \n"
        "🚂 Trailer Number: 42 \n"
        "🔑 VIN:1GT4USEY5SF221416 \n"
        "⚓ Ramps: Mega Ramps \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель ERDEM DORZHIEV": (
        "📌 Driver Name: ERDEM DORZHIEV \n"
        "📞 Phone Number: 412-304-4565 \n"
        "🚛 Truck Number: 8 \n"
        "🚂 Trailer Number: 8 \n"
        "🔑 VIN:3C63R3GL6NG159989 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель OLEG RESHAEV": (
        "📌 Driver Name: OLEG RESHAEV \n"
        "📞 Phone Number: 279-789-4042 \n"
        "🚛 Truck Number: 23 \n"
        "🚂 Trailer Number: 23 \n"
        "🔑 VIN:3C63RRHL1RG289668 \n"
        "⚓ Ramps: 10ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель DIONISIE COTOVICI": (
        "📌 Driver Name: DIONISIE COTOVICI \n"
        "📞 Phone Number: 954-295-6482 \n"
        "🚛 Truck Number: 12 \n"
        "🚂 Trailer Number: 12 \n"
        "🔑 VIN:3C63RRHL6RG341392 \n"
        "⚓ Ramps: ft \n"
        "⚖ Weight: lb \n"
        "🅱 Owner: Dumitru Ou"
    ),
    "Водитель EVGENY SYROMITSKII": (
        "📌 Driver Name: EVGENY SYROMITSKII \n"
        "📞 Phone Number: 754-600-7170 \n"
        "🚛 Truck Number: 2 \n"
        "🚂 Trailer Number: 2 \n"
        "🔑 VIN:3C63RRHL2RG358187 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8800lb \n"
        "🅱 Owner: Radu"
    ),
    "Водитель RADZHAB MAGOMEDOV": (
        "📌 Driver Name: RADZHAB MAGOMEDOV \n"
        "📞 Phone Number:  \n"
        "🚛 Truck Number:  \n"
        "🚂 Trailer Number:  \n"
        "🔑 VIN: \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight:  \n"
        "🅱 Owner: "
    ),
    "Водитель GEORGII RIONELI": (
        "📌 Driver Name: GEORGII RIONELI \n"
        "📞 Phone Number: 925-440-1503 \n"
        "🚛 Truck Number: 35 \n"
        "🚂 Trailer Number: 35 \n"
        "🔑 VIN:3C63RRGL0NG356465 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель IGOR BALAKIN": (
        "📌 Driver Name: IGOR BALAKIN \n"
        "📞 Phone Number: 331-229-8750 \n"
        "🚛 Truck Number: 20 \n"
        "🚂 Trailer Number: 20 \n"
        "🔑 VIN:3C63RRGL3KG618197 \n"
        "⚓ Ramps: Mega Ramps \n"
        "⚖ Weight: 8700lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель SERGIU CIOBANU": (
        "📌 Driver Name: SERGIU CIOBANU \n"
        "📞 Phone Number:  \n"
        "🚛 Truck Number:  \n"
        "🚂 Trailer Number:  \n"
        "🔑 VIN: \n"
        "⚓ Ramps:  \n"
        "⚖ Weight:  \n"
        "🅱 Owner: "
    ),
    "Водитель TAULAN TOTORKULOV": (
        "📌 Driver Name: TAULAN TOTORKULOV \n"
        "📞 Phone Number: 224-463-0235 \n"
        "🚛 Truck Number: 5 \n"
        "🚂 Trailer Number: 5 \n"
        "🔑 VIN:3C63RRGL9KG700614 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9700lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель ALBERT ABAIKHANOV": (
        "📌 Driver Name: ALBERT ABAIKHANOV \n"
        "📞 Phone Number: 347-739-8531 \n"
        "🚛 Truck Number: 22 \n"
        "🚂 Trailer Number: 22 \n"
        "🔑 VIN:3C63RRHL9KG642308 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8860lb \n"
        "🅱 Owner: Rassul"
    ),
    "Водитель SOSLAN GAGLOEV": (
        "📌 Driver Name: SOSLAN GAGLOEV \n"
        "📞 Phone Number: 786-868-5690 \n"
        "🚛 Truck Number: 13 \n"
        "🚂 Trailer Number: 13 \n"
        "🔑 VIN:3C63RRGL7RG295329 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    )
}

# URL для фотографий и файлов водителей
drivers_files = {
    "Водитель ALEKSEI LAMATKHANOV": {
        "photo": "",
        "files": ""
    },
    "Водитель BILIKTO LAMATKHANOV": {
        "photo": "",
        "files": ""
    },
    "Водитель ALEKSANDR PAVLOV": {
        "photo": "",
        "files": ""
    },
    "Водитель BAIR DABAIN": {
        "photo": "",
        "files": ""
    },
    "Водитель BULAT TSYRENOV": {
        "photo": "",
        "files": ""
    },
    "Водитель OLEH SEMENENNKO": {
        "photo": "",
        "files": ""
    },
    "Водитель LATIPOV PARVIZ": {
        "photo": "",
        "files": ""
    },
    "Водитель ILLIA HORBATOK": {
        "photo": "",
        "files": ""
    },
    "Водитель (DOS) DASTAN MASYLKANOV": {
        "photo": "",
        "files": ""
    },
    "Водитель DARMAN ORUZBAEV": {
        "photo": "",
        "files": ""
    },
    "Водитель YERKEBULAN BOSHAIBEKOV": {
        "photo": "",
        "files": ""
    },
    "Водитель MARIN GULIA": {
        "photo": "",
        "files": ""
    },
    "Водитель ERDEM DORZHIEV": {
        "photo": "",
        "files": ""
    },
    "Водитель OLEG RESHAEV": {
        "photo": "",
        "files": ""
    },
    "Водитель DIONISIE COTOVICI": {
        "photo": "",
        "files": ""
    },
    "Водитель EVGENY SYROMITSKII": {
        "photo": "",
        "files": ""
    },
    "Водитель RADZHAB MAGOMEDOV": {
        "photo": "",
        "files": ""
    },
    "Водитель GEORGII RIONELI": {
        "photo": "",
        "files": ""
    },
    "Водитель IGOR BALAKIN": {
        "photo": "",
        "files": ""
    },
    "Водитель SERGIU CIOBANU": {
        "photo": "",
        "files": ""
    },
    "Водитель TAULAN TOTORKULOV": {
        "photo": "",
        "files": ""
    },
    "Водитель ALBERT ABAIKHANOV": {
        "photo": "",
        "files": ""
    },
    "Водитель SOSLAN GAGLOEV": {
        "photo": "",
        "files": ""
    }
}

# 🔎 Обработчик текстовых сообщений для поиска водителя по имени
async def search_driver(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()
    # Если сообщение содержит приветствие или команду, обрабатываем как /start (гreeting)
    trigger_words = ["привет", "hi", "salut", "начать", "старт"]
    if any(word in text.split() for word in trigger_words) or text.startswith("/"):
        # Проверяем доступ и показываем меню (используем функциональность /start)
        await start(update, context)
        return
    # Проверка доступа для обычного запроса (чтобы не отвечать неавторизованным)
    if not await check_access(update):
        return
    # Поиск информации о водителе по имени (нечувствителен к регистру, поиск по подстроке)
    matches = [(name, info) for name, info in drivers_info.items() if text in name.lower()]
    if not matches:
        await update.message.reply_text("🚫 Водитель не найден.")
    elif len(matches) == 1:
        # Единственное совпадение – выводим информацию о водителе
        await update.message.reply_text(matches[0][1], parse_mode='HTML')
    else:
        # Несколько совпадений – перечисляем найденных водителей
        found_names = "\n".join(name for name, info in matches)
        await update.message.reply_text(f"🔎 Найдено несколько водителей:\n{found_names}")

# 👥 Показывает список диспетчеров (при нажатии на кнопку "Список диспетчеров")
async def show_dispatchers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton(name, callback_data=name)] for name in dispatchers.keys()]
    keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='start')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text("👥 Выберите диспетчера:", reply_markup=reply_markup)

# 🚛 Показывает список водителей выбранного диспетчера
async def show_drivers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    selected_dispatcher = query.data  # имя диспетчера из callback_data
    keyboard = [[InlineKeyboardButton(driver, callback_data=driver)] for driver in dispatchers[selected_dispatcher]]
    keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='dispatchers')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(f"🚛 Водители диспетчера {selected_dispatcher}:", reply_markup=reply_markup)

# 📋 Показывает информацию о выбранном водителе и клавиатуру (Фото, Файлы, Назад)
async def show_driver_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    selected_driver = query.data  # имя водителя из callback_data
    # Определяем, к какому диспетчеру относится этот водитель (для корректной работы кнопки "Назад")
    parent_dispatcher = None
    for dispatcher_name, drivers_list in dispatchers.items():
        if selected_driver in drivers_list:
            parent_dispatcher = dispatcher_name
            break
    # Формируем клавиатуру: Фото, Файлы (ссылки) и Назад (в список водителей диспетчера)
    keyboard_buttons = [
        InlineKeyboardButton("📸 Фото", url=drivers_files.get(selected_driver, {}).get("photo", "")),
        InlineKeyboardButton("📂 Файлы", url=drivers_files.get(selected_driver, {}).get("files", ""))
    ]
    # Кнопки "Фото" и "Файлы" открывают ссылки; кнопка "Назад" возвращает к списку водителей того же диспетчера
    keyboard = [keyboard_buttons, [InlineKeyboardButton("⬅️ Назад", callback_data=parent_dispatcher or 'dispatchers')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Отправляем информацию о водителе (с форматированием HTML, если есть)
    await query.message.edit_text(drivers_info[selected_driver], reply_markup=reply_markup, parse_mode='HTML')

# 🔄 Общий обработчик всех нажатий на кнопки (CallbackQuery)
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    # Попытка быстро ответить на запрос (чтобы убрать "часики" у кнопки)
    try:
        await query.answer()
    except telegram.error.BadRequest:
        pass
    # Обработка нажатия в зависимости от callback_data
    data = query.data
    if data == 'start':
        # Вернуться в главное меню
        keyboard = [[InlineKeyboardButton("👥 Список диспетчеров", callback_data='dispatchers')]]
        await query.message.edit_text("🚛 Главное меню:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif data == 'dispatchers':
        await show_dispatchers(update, context)
    elif data in dispatchers:
        await show_drivers(update, context)
    elif data in drivers_info:
        await show_driver_info(update, context)
    # (Обработка кнопок "Фото" и "Файлы" через callback_data не нужна,
    # т.к. они реализованы как ссылки. Если бы они были callback,
    # можно было бы добавить условия data.startswith("photo_") и data.startswith("files_").)

# Создание и запуск приложения Telegram Bot
app = Application.builder().token("7931949571:AAEYdSWhL_ksOCK17RhFgF2gvlPqlwEgj0U").build()

# Регистрация обработчиков
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_driver))
app.add_handler(CallbackQueryHandler(button_handler))

if __name__ == "__main__":
    print("Бот запущен...")
    app.run_polling()
