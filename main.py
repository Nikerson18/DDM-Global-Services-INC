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
    "🚛 Диспетчер Andrew": ["Водитель RAMIL KHAFIZOV", "Водитель OLEG RESHAEV", "Водитель OLEH SEMENENNKO", "Водитель ILLIA HORBATOK", "Водитель RUSTAM TAMBIEV"],
    "🚚 Диспетчер David": ["Водитель ALEKSEI LAMATKHANOV", "Водитель ALEKSANDR PAVLOV", "Водитель LATIPOV PARVIZ", "Водитель BAIR DABAIN", "Водитель BILIKTO LAMATKHANOV", "Водитель GREENGREYLINE KALCHUK GRYGORII"],
    "🚌 Диспетчер Serghei": ["Водитель VITALII HONCHAROV", "Водитель GRIGORII MOSKALETS", "Водитель RUSTAM TAMBIEV", "Водитель IHOR KIRSHAK"],
    "🚋 Диспетчер Vick": ["Водитель DARMAN ORUZBAEV", "Водитель GREENGREYLINE SHALIMOV IVAN", "Водитель ERDEM DORZHIEV", "Водитель TOTRAZ ABAEV", "Водитель YERKEBULAN BOSHAIBEKOV", "Водитель YAROSLAV PANEVNYK", "Водитель MARIN GULIA"],
    "🏍 Диспетчер Nick": ["Водитель ALBERT ABAIKHANOV", "Водитель MIM Logistics INC ANVAR BIDZHIEV", "Водитель MUKHAMED ADZHIEV"],
    "🚂 Диспетчер Peter": ["Водитель TSYDEN TOBODORZHIEV", "Водитель VIKTOR ATANOV", "Водитель AZAT AZAMAT", "Водитель DIONISIE COTOVICI", "Водитель AZAT BORONCHIEV"],
    "🚀 Диспетчер Dima": ["Водитель GEORGII RIONELI", "Водитель DENIS COLESNICENCO", "Водитель IGOR BALAKIN", "Водитель TAULAN TOTORKULOV", "Водитель EVGENY SYROMITSKII", "Водитель SERHII HONCHARENKO"],
    "✈ Диспетчер Max": ["Водитель SOSLAN GAGLOEV", "Водитель (DOS) DASTAN MASYLKANOV", "Водитель MIRBEK ALOEV"],
    "🎈 Диспетчер NONE": ["Водитель (Said) MAGOMEDSAID GABIBULAEV", "Водитель YEVHENII MATVIEIEV", "Водитель SRV URUZMAG TSAKOEV", "Водитель MIM Logistics INC VALENTIN NEIZHKO", "Водитель SRV Trust Way INC GEORGII DZOTOV"]
}

drivers_info = {
    "Водитель RAMIL KHAFIZOV": (
        "📌 Driver Name: RAMIL KHAFIZOV \n"
        "📞 Phone Number: 916-282-8457 \n"
        "🚛 Truck Number: 34 \n"
        "🚂 Trailer Number: 34 \n"
        "🔑 VIN:3C6UR5KL2FG537458 \n"
        "⚓ Ramps: Mega Ramps \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Marin"
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
    "Водитель MUKHAMED ADZHIEV": (
        "📌 Driver Name: MUKHAMED ADZHIEV \n"
        "📞 Phone Number: 224-474-0482 \n"
        "🚛 Truck Number: 3 \n"
        "🚂 Trailer Number: 3 \n"
        "🔑 VIN:3C63RRHL8RG307633 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Dumitru Ou"
    ),
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
    "Водитель SRV URUZMAG TSAKOEV": (
        "📌 Driver Name: URUZMAG TSAKOEV \n"
        "📞 Phone Number: 224-284-9071 \n"
        "🚛 Truck Number:  \n"
        "🚂 Trailer Number:  \n"
        "🔑 VIN: \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Stas"
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
    "Водитель VITALII HONCHAROV": (
        "📌 Driver Name: VITALII HONCHAROV \n"
        "📞 Phone Number: 904-333-2447 \n"
        "🚛 Truck Number: 33 \n"
        "🚂 Trailer Number: 33 \n"
        "🔑 VIN:3C63RRHL9RG301260 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9620lb \n"
        "🅱 Owner: "
    ),
    "Водитель RUSTAM TAMBIEV": (
        "📌 Driver Name: RUSTAM TAMBIEV \n"
        "📞 Phone Number: 224-443-3233 \n"
        "🚛 Truck Number: 41 \n"
        "🚂 Trailer Number: 41 \n"
        "🔑 VIN:1FT8W3DT7PEC16514 \n"
        "⚓ Ramps: Mega Ramps \n"
        "⚖ Weight: 9620lb \n"
        "🅱 Owner: NAZAR "
    ),
    "Водитель IHOR KIRSHAK": (
        "📌 Driver Name: IHOR KIRSHAK \n"
        "📞 Phone Number: 929-786-5509 \n"
        "🚛 Truck Number: 28 \n"
        "🚂 Trailer Number: 28 \n"
        "🔑 VIN:3C63RRHL5RG337088 \n"
        "⚓ Ramps: 14ft \n"
        "⚖ Weight: 9220lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель GRIGORII MOSKALETS": (
        "📌 Driver Name: GRIGORII MOSKALETS \n"
        "📞 Phone Number: 754-284-6442 \n"
        "🚛 Truck Number: 15 \n"
        "🚂 Trailer Number: 15 \n"
        "🔑 VIN:3C63RRHL0RG280427 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9220lb \n"
        "🅱 Owner: Dumitru OU"
    ),
    "Водитель SERHII HONCHARENKO": (
        "📌 Driver Name: SERHII HONCHARENKO \n"
        "📞 Phone Number: 386-225-1619 \n"
        "🚛 Truck Number: 19 \n"
        "🚂 Trailer Number: 19 \n"
        "🔑 VIN:3C63RRGL2RG219808 \n"
        "⚓ Ramps: 14ft \n"
        "⚖ Weight: 8200lb \n"
        "🅱 Owner: Ruslan"
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
    "Водитель TOTRAZ ABAEV": (
        "📌 Driver Name: TOTRAZ ABAEV \n"
        "📞 Phone Number: 754-286-7577 \n"
        "🚛 Truck Number: 16 \n"
        "🚂 Trailer Number: 16 \n"
        "🔑 VIN:3C63RRHL2PG643033 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Stas"
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
    "Водитель (Said) MAGOMEDSAID GABIBULAEV": (
        "📌 Driver Name: MAGOMEDSAID GABIBULAEV \n"
        "📞 Phone Number: 305-391-1839 \n"
        "🚛 Truck Number: 6 \n"
        "🚂 Trailer Number: 6 \n"
        "🔑 VIN:3C63RRGL0RG183858 \n"
        "⚓ Ramps: 12ft \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Ruslan"
    ),
    "Водитель YAROSLAV PANEVNYK": (
        "📌 Driver Name: YAROSLAV PANEVNYK \n"
        "📞 Phone Number: 916-940-5888 \n"
        "🚛 Truck Number: 26 \n"
        "🚂 Trailer Number: 26 \n"
        "🔑 VIN:1GT49LEY8RF467913 \n"
        "⚓ Ramps: Mega Ramps \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Owner Operator"
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
    "Водитель MIM Logistics INC ANVAR BIDZHIEV": (
        "📌 Driver Name: ANVAR BIDZHIEV \n"
        "📞 Phone Number: 224-422-3658 \n"
        "🚛 Truck Number: 03 \n"
        "🚂 Trailer Number: 03 \n"
        "🔑 VIN:1FT8W3DT5NEG00613 \n"
        "⚓ Ramps: n/a \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner"
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
    "Водитель RUSTAM TAMBIEV": (
        "📌 Driver Name: RUSTAM TAMBIEV \n"
        "📞 Phone Number: 224-443-3233 \n"
        "🚛 Truck Number: 41 \n"
        "🚂 Trailer Number: 41 \n"
        "🔑 VIN:1FT8W3DT7PEC16514 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: "
    ),
    "Водитель TSYDEN TOBODORZHIEV": (
        "📌 Driver Name: TSYDEN TOBODORZHIEV \n"
        "📞 Phone Number: 347-232-8827 \n"
        "🚛 Truck Number: 36 \n"
        "🚂 Trailer Number: 36 \n"
        "🔑 VIN:1FT8W3DT3REF83199 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель VIKTOR ATANOV": (
        "📌 Driver Name: VIKTOR ATANOV \n"
        "📞 Phone Number: 929-481-9521 \n"
        "🚛 Truck Number: 39 \n"
        "🚂 Trailer Number: 39 \n"
        "🔑 VIN:1FT8W3DT9REE49099 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель AZAT AZAMAT": (
        "📌 Driver Name: AZAT AZAMAT \n"
        "📞 Phone Number: 253-286-8080 \n"
        "🚛 Truck Number: 29 \n"
        "🚂 Trailer Number: 29 \n"
        "🔑 VIN:3C63RRGL6RG382381 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8680lb \n"
        "🅱 Owner: Owner Operator"
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
    "Водитель AZAT BORONCHIEV": (
        "📌 Driver Name: AZAT BORONCHIEV \n"
        "📞 Phone Number: 929-627-1722 \n"
        "🚛 Truck Number: 14 \n"
        "🚂 Trailer Number: 14 \n"
        "🔑 VIN:3C63R3HL7RG339129\n"
        "⚓ Ramps: ft \n"
        "⚖ Weight: 8500lb \n"
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
    "Водитель DENIS COLESNICENCO": (
        "📌 Driver Name: DENIS COLESNICENCO \n"
        "📞 Phone Number: 630-352-9196 \n"
        "🚛 Truck Number: 38 \n"
        "🚂 Trailer Number: 38 \n"
        "🔑 VIN:3C63RRHL6RG289522 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9600lb \n"
        "🅱 Owner: Kiril"
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
    "Водитель MIRBEK ALOEV": (
        "📌 Driver Name: MIRBEK ALOEV \n"
        "📞 Phone Number: 916-767-6753 \n"
        "🚛 Truck Number: 32 \n"
        "🚂 Trailer Number: 32 \n"
        "🔑 VIN:3C63RRHL2RG289436 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Stas"
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
    "Водитель SOSLAN GAGLOEV": (
        "📌 Driver Name: SOSLAN GAGLOEV \n"
        "📞 Phone Number: 786-868-5690 \n"
        "🚛 Truck Number: 13 \n"
        "🚂 Trailer Number: 13 \n"
        "🔑 VIN:3C63RRGL7RG295329 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель GREENGREYLINE SHALIMOV IVAN": (
        "📌 Driver Name: SHALIMOV IVAN \n"
        "📞 Phone Number: 347-845-5604 \n"
        "🚛 Truck Number: 333 \n"
        "🚂 Trailer Number: 927 \n"
        "🔑 VIN:3AKJHHDR2SSWH0860 \n"
        "⚓ Ramps: 16ft \n"
        "⚖ Weight: 45000lb \n"
        "🅱 Owner: Ruslan 804-405-7438"
    ),
    "Водитель GREENGREYLINE KALCHUK GRYGORII": (
        "📌 Driver Name: KALCHUK GRYGORII \n"
        "📞 Phone Number: 872-240-7229 \n"
        "🚛 Truck Number: 29 \n"
        "🚂 Trailer Number: 29 \n"
        "🔑 VIN:3AKJHHDR0TSWL2968 \n"
        "⚓ Ramps: 16ft \n"
        "⚖ Weight: 45000lb \n"
        "🅱 Owner: Owner Mihail 267-997-8913"
    ),
    "Водитель MIM Logistics INC VALENTIN NEIZHKO": (
        "📌 Driver Name: VALENTIN NEIZHKO \n"
        "📞 Phone Number: 331-271-7110 \n"
        "🚛 Truck Number: 40 \n"
        "🚂 Trailer Number: 40 \n"
        "🔑 VIN:3C63RRHL4JG201345 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель SRV Trust Way INC GEORGII DZOTOV": (
        "📌 Driver Name: GEORGII DZOTOV \n"
        "📞 Phone Number: 224-284-4234 \n"
        "🚛 Truck Number: 45 \n"
        "🚂 Trailer Number: 45 \n"
        "🔑 VIN:3C63RRGL1RG416890 \n"
        "⚓ Ramps: n/a \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Stas"
    ),
    "Водитель YEVHENII MATVIEIEV": (
        "📌 Driver Name: YEVHENII MATVIEIEV \n"
        "📞 Phone Number: 689-233-2513 \n"
        "🚛 Truck Number: 31 \n"
        "🚂 Trailer Number: 31 \n"
        "🔑 VIN:3C63RRJLXNG152569 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Radu"
    )
}

# URL для фотографий и файлов водителей
drivers_files = {
    "Водитель RAMIL KHAFIZOV": {
        "photo": "https://drive.google.com/file/d/1RebRt_fdyY9zFgDbNq43MmsYOi5t9G5p/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1bzdQIFsOilY8eHuA4x7gq3xgKAaqoBLa/view?usp=sharing"
    },
    "Водитель OLEH SEMENENNKO": {
        "photo": "https://drive.google.com/file/d/17e18kZ1O8RPz3-4xkpAgj_Rsev2icA0p/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1BypkUML2-13yC_1zhopir5MakM16y2Z1/view?usp=sharing"
    },
    "Водитель OLEG RESHAEV": {
        "photo": "https://drive.google.com/file/d/1DHJ2H1BlcwDFzCdTkC2-4gPSSgn3eePE/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1Jog2P7ssILevyBMUeOOQEapT2pwxexGD/view?usp=sharing"
    },
    "Водитель MUKHAMED ADZHIEV": {
        "photo": "https://drive.google.com/file/d/1WQb3XId7N5Ofwzc3mcDZ2JIpSDhvm2Lo/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель BILIKTO LAMATKHANOV": {
        "photo": "https://drive.google.com/file/d/1iAjETTrVD9vGrDCFKzKxSlTTLqTzGGw7/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1mGZk0yIansjtMHwbDUVwDf6muQcy4u7E/view?usp=drive_link"
    },
    "Водитель ALEKSEI LAMATKHANOV": {
        "photo": "https://drive.google.com/file/d/1gjpo3VgvjGobRuNsjRBeRfdRZpLBCjud/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель SRV URUZMAG TSAKOEV": {
        "photo": "https://drive.google.com/file/d/1EwNJ1SbDCL-ivNs7xAHGczTAsCsDara4/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1SaOVT-NEnEpBCXDgIF2lcceIROyb1dz7/view?usp=drive_link"
    },
    "Водитель LATIPOV PARVIZ": {
        "photo": "https://drive.google.com/file/d/1xdc15lyPYEd-rTVWjq5wlun3U2Xoi6Nn/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1ZDXRZhdWKx1yZodyt_eVKtl4x7RnCe0-/view?usp=drive_link"
    },
    "Водитель ALEKSANDR PAVLOV": {
        "photo": "https://drive.google.com/file/d/1CxXCHz5L6hogjHAsQ-Fb60r2U4mODuId/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/11Opx2TN6ScaJ31YjHyB1IQ6ktOq26KM9/view?usp=sharing"
    },
    "Водитель BAIR DABAIN": {
        "photo": "https://drive.google.com/file/d/1EiLW7-ITrIKjqefHMU1MtHBTwFM-V7yG/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1qoV0MKrI3dycrH8eKHn1wy6MSalNgErn/view?usp=sharing"
    },
    "Водитель VITALII HONCHAROV": {
        "photo": "https://drive.google.com/file/d/1hUtSdZNcEMa__yG1kPCbFNUcNpgOAvIU/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель IHOR KIRSHAK": {
        "photo": "https://drive.google.com/file/d/15ZKnXzvDmfuwj_02swAd9nHmuJQW5kbB/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1OoSZcQYjrCdtpoFk3H8CxUEdkOYYvWYC/view?usp=drive_link"
    },
    "Водитель RUSTAM TAMBIEV": {
        "photo": "https://drive.google.com/file/d/1D0thrbgcIYfKIWF7ScDydKwdsPH3imGV/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1fKweFaG7mYN1HxQNTlghmoVqT-QkfeIY/view?usp=drive_link"
    },
    "Водитель GRIGORII MOSKALETS": {
        "photo": "https://drive.google.com/file/d/13kkj2hoPUbK2-8O7RlWCvuDNDnb17Pgy/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1R-7_hXIvAOXpUIJOUEBXmjFDTAv3tplo/view?usp=drive_link"
    },
    "Водитель SERHII HONCHARENKO": {
        "photo": "https://drive.google.com/file/d/14CpboA9pYKyLWuxijf9gD6Ok7nDaGTIW/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1o5hiNiTsmXdxvH3_FuAZUEkPzZMGjbAr/view?usp=sharing"
    },
    "Водитель DARMAN ORUZBAEV": {
        "photo": "https://drive.google.com/file/d/1-_9957CAuAIYgqxLmKxF4iWyT-YIIJv4/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1ejFCxUWMC3WylWhZ8s3NbITVfgHriocd/view?usp=sharing"
    },
    "Водитель TOTRAZ ABAEV": {
        "photo": "https://drive.google.com/file/d/1ymKwY80eRZziGw8svzLw3ZSsLC4QorcX/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель YERKEBULAN BOSHAIBEKOV": {
        "photo": "https://drive.google.com/file/d/1mG7YPuGRjU8cFrKPxNW-1gw2-3AwQYoe/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/17oYiD-eOkhHIC9mwAsbXeNvehgJfkWmn/view?usp=sharing"
    },
    "Водитель (Said) MAGOMEDSAID GABIBULAEV": {
        "photo": "https://drive.google.com/file/d/1qVDUgjKnkq5iCG7EHZdl_72xR08jgpWL/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1lft69iT2fdtwZLN3whhknZWuTIYVT5K7/view?usp=sharing"
    },
    "Водитель YAROSLAV PANEVNYK": {
        "photo": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1ykhC1lIoNk7UM3zjJqCUFLWVsOey5oMR/view?usp=drive_link"
    },
    "Водитель MARIN GULIA": {
        "photo": "https://drive.google.com/file/d/1gNGy-qOQQUd7W_DljwzbOBiEM473il1e/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель ALBERT ABAIKHANOV": {
        "photo": "https://drive.google.com/file/d/10D25opmpC3DDgeWYPri8HzHUQfAs3dU9/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/17M0f3cTycjjtptvjXz119oIkHNd2-DPN/view?usp=sharing"
    },
    "Водитель MIM Logistics INC ANVAR BIDZHIEV": {
        "photo": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1cTtZhzYBYQS37RlTXo9XPtAwh68Mv870/view?usp=drive_link"
    },
    "Водитель ILLIA HORBATOK": {
        "photo": "https://drive.google.com/file/d/171t2eY0cAwKMXdM4o3wokRqR41cCsrZN/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель RUSTAM TAMBIEV": {
        "photo": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель TSYDEN TOBODORZHIEV": {
        "photo": "https://drive.google.com/file/d/15JGHtHuNOrznk-te8uDWRDkhEvVH5OOd/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1NNJM7lmtpRnh82ICh92xNXHzmr4LGBI4/view?usp=sharing"
    },
    "Водитель VIKTOR ATANOV": {
        "photo": "https://drive.google.com/file/d/1s1WgBRsMU0Q1roF8OxZsNFBmP8wokmfU/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1GwhxpNl9IHvaNHnIZWiFVQEx2JP2rT9i/view?usp=drive_link"
    },
    "Водитель AZAT AZAMAT": {
        "photo": "https://drive.google.com/file/d/1HyPI1o5c2aMv2PO6R_yE-0xV94D3Q8AO/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1iOLgUSvrvYj0mrB6o5t9Xtq0GTGO-9c2/view?usp=sharing"
    },
    "Водитель DIONISIE COTOVICI": {
        "photo": "https://drive.google.com/file/d/15t4skooNi866yUtfnLNdcwZUm-AIupU7/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1l69IMPNIjICw8lX_gJtT7kwTSgSfM1pE/view?usp=drive_link"
    },
    "Водитель AZAT BORONCHIEV": {
        "photo": "https://drive.google.com/file/d/1fa58slTENamCbpZ4hUMeJhtVIXsXJJjk/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель GEORGII RIONELI": {
        "photo": "https://drive.google.com/file/d/1gi0RkYOlGyH_TSgs0MhTATcNsaamiyJD/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1WDlAlIKCRofH0N1Z-Z8N2qNfgaO1FpsK/view?usp=sharing"
    },
    "Водитель DENIS COLESNICENCO": {
        "photo": "https://drive.google.com/file/d/17kdgaxVAGn6dypn-5azbIsoY6Eu1TXcm/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1OkH_O_LOSUAbOvV1F85sxwJfJpomSowJ/view?usp=sharing"
    },
    "Водитель IGOR BALAKIN": {
        "photo": "https://drive.google.com/file/d/1InjrQgybbfXYM8cqiEcIAXV2h_dgmgSz/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель TAULAN TOTORKULOV": {
        "photo": "https://drive.google.com/file/d/1hrVycBVGxxXq9-aNZWfW40hk93F82_mw/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1m0kguCz7qe3-kyB_Qi_NyCNUTgh5ACYU/view?usp=sharing"
    },
    "Водитель EVGENY SYROMITSKII": {
        "photo": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель ERDEM DORZHIEV": {
        "photo": "https://drive.google.com/file/d/1-xI2Xysnd19jiFp65Fwu4XenVHKjbAut/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1b3_h2Rk-6_YL2ccvdnojRCTbpemDZ2Ce/view?usp=sharing"
    },
    "Водитель MIRBEK ALOEV": {
        "photo": "https://drive.google.com/file/d/138kYd20Lv1KJsTKfLKE1BgncdPbt3drV/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1NYUXFrUXf9DUVk3CRTMQnOS1-OodsI2f/view?usp=sharing"
    },
    "Водитель (DOS) DASTAN MASYLKANOV": {
        "photo": "https://drive.google.com/file/d/1laZ-h8AnpAxDuYKA9gg3zrYfML-JShBg/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1pTL-8UQs717x0bvnvszmg29bZxNeXBtQ/view?usp=drive_link"
    },
    "Водитель SOSLAN GAGLOEV": {
        "photo": "https://drive.google.com/file/d/1GvuTMUKgNdgcR9bsmThZR9dx7bvZCgEY/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1vs1lmsH4MqphrU5p_GenEtTPQ2PwPXxR/view?usp=sharing"
    },
    "Водитель GREENGREYLINE SHALIMOV IVAN": {
        "photo": "https://drive.google.com/file/d/1odDV94XYFwtdTNmDcAyqxEH_E-rSyQGR/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1YAOqn90HQX8N7lhnmkFUiqjF5Zm0KrCz/view?usp=drive_link"
    },
    "Водитель GREENGREYLINE KALCHUK GRYGORII": {
        "photo": "https://drive.google.com/file/d/1tdYfeeDdw4xcvt9v3zp1irOUSbeJPbWo/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1-fH8II7dtc9cFbFjol30K213XtxWw1zg/view?usp=drive_link"
    },
    "Водитель MIM Logistics INC VALENTIN NEIZHKO": {
        "photo": "https://drive.google.com/file/d/1EaKXoCfbpe3rpTKVgAHTk2ojwI-NGZDr/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1mEEqePzPBUNPPSAhwfyyH81VRxuXU4sR/view?usp=drive_link"
    },
    "Водитель SRV Trust Way INC GEORGII DZOTOV": {
        "photo": "https://drive.google.com/file/d/1BU52Ri3tOMsRj22Wm02-hFocrNc8vfFJ/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1X8D66asKoBZuSJo5b5KAvVPH_6AFeHn-/view?usp=drive_link"
    },
    "Водитель YEVHENII MATVIEIEV": {
        "photo": "https://drive.google.com/file/d/159qThglnM__npOf28XPXvRHUdLSCNc1P/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1r4pT2_LlK6esYlFmelHWO3LbmenmT9eC/view?usp=drive_link"
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
