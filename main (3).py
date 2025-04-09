from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes, CallbackContext
import telegram.error

async def button_handler(update: Update, context):
    query = update.callback_query
    try:
        await query.answer()
    except telegram.error.BadRequest:
        pass

# 🔒 Список разрешённых пользователей (замени ID на реальные)
ALLOWED_USERS = {5538804267, 1430105405, 6932066810, 8026256981, 7275611563, 723670550, 5880565984, 5636776284, 1430105405 }  # Замени на свои ID

# 🔐 Функция проверки доступа
async def check_access(update: Update) -> bool:
    user_id = update.effective_user.id
    if user_id not in ALLOWED_USERS:
        if update.message:
            await update.message.reply_text("🚫 Доступ запрещён. Свяжитесь с администратором.")
        elif update.callback_query:
            await update.callback_query.message.reply_text("🚫 Доступ запрещён.")
        return False
    return True  # Если пользователь в списке, возвращаем True

# 🚀 Функция /start и при определённых словах
async def start(update: Update, context: CallbackContext):
    if update.message is None or update.message.text is None:  # Если нет текста, выходим
        return

    text = update.message.text.lower()  # Определяем text сразу
    trigger_words = ["привет", "hi", "salut", "начать", "старт"]

    # Выводим отладочную информацию
    print(f"Проверяем текст: {text}")

    if any(word in text.split() for word in trigger_words) or text.startswith("/"):
        if not await check_access(update):  # Проверяем доступ
            return  # Если доступа нет, выходим

        await update.message.reply_text("✅ Доступ разрешён. Добро пожаловать!")  # Добавляем сообщение о доступе
        keyboard = [[InlineKeyboardButton("👥 Список диспетчеров", callback_data='dispatchers')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("🚛 Главное меню:", reply_markup=reply_markup)
        return  # Выход после отправки меню

        # 🚛 Если триггерные слова не сработали, ищем водителя
    driver_name = text
    drivers_info_lower = {key.lower(): value for key, value in drivers_info.items()}
    info = drivers_info_lower.get(driver_name)

    if info:
        await update.message.reply_text(info, parse_mode='HTML')

# 🔄 Главное меню (пример)
def main_menu():
    keyboard = [[InlineKeyboardButton("📋 Список водителей", callback_data='drivers')]]
    return InlineKeyboardMarkup(keyboard)

# Данные (пока вручную)
dispatchers = {
    "🚛 Диспетчер Andrew": ["Водитель RAMIL KHAFIZOV", "Водитель OLEG RESHAEV", "Водитель OLEH SEMENENNKO", "Водитель MUKHAMED ADZHIEV"],
    "🚚 Диспетчер David": ["Водитель ALEKSEI LAMATKHANOV", "Водитель BAIR DABAIN", "Водитель MARAT KAZIEV", "Водитель AZAT BORONCHIEV", "Водитель MUKHAR KHUGAEV", "Водитель ALEKSANDR PAVLOV", "Водитель INAL VALIEV"],
    "🚌 Диспетчер Serghei": ["Водитель VITALII HONCHAROV", "Водитель SERGHEI CIOBANU", "Водитель SERHII HONCHARENKO", "Водитель GRIGORII MOSKALETS"],
    "🚋 Диспетчер Vick": ["Водитель DARMAN ORUZBAEV", "Водитель TOTRAZ ABAEV", "Водитель YERKEBULAN BOSHAIBEKOV", "Водитель MARIN GULIA", "Водитель MIRBEK ALOEV"],
    "🏍 Диспетчер Nick": ["Водитель ALBERT ABAIKHANOV", "Водитель ASKHABALI SHABANOV", "Водитель ILLIA HORBATOK"],
    "🚂 Диспетчер Peter": ["Водитель TSYDEN TOBODORZHIEV", "Водитель VIKTOR ATANOV", "Водитель AZAT AZAMAT", "Водитель DIONISIE COTOVICI"],
    "🚀 Диспетчер Dima": ["Водитель GEORGII RIONELI", "Водитель DENIS COLESNICENCO", "Водитель IGOR BALAKIN", "Водитель TAULAN TOTORKULOV"],
    "✈ Диспетчер Max": ["Водитель ERDEM DORZHIEV", "Водитель (Said) MAGOMEDSAID GABIBULAEV", "Водитель (DOS) DASTAN MASYLKANOV", "Водитель SOSLAN GAGLOEV"]

}

drivers_info = {
    "Водитель RAMIL KHAFIZOV": (
        "📌 Driver Name: RAMIL KHAFIZOV \n"
        "📞 Phone Number: 916-282-8457 \n"
        "🚛 Truck Number: 34 \n"
        "🚂 Trailer Number: 34 \n"
        "🔑 VIN:3C6UR5KL2FG537458 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Marin"
    ),
    "Водитель OLEH SEMENENNKO": (
        "📌 Driver Name: OLEH SEMENENNKO \n"
        "📞 Phone Number: 786-843-1879 \n"
        "🚛 Truck Number: 25 \n"
        "🚂 Trailer Number: 25 \n"
        "🔑 VIN:3C63RRHL2RG307630 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Radu"
    ),
    "Водитель OLEG RESHAEV": (
        "📌 Driver Name: OLEG RESHAEV \n"
        "📞 Phone Number: 279-789-4042 \n"
        "🚛 Truck Number: 23 \n"
        "🚂 Trailer Number: 23 \n"
        "🔑 VIN:3C63RRHL1RG289668 \n" 
        "⚓Ramps: 10ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель MUKHAMED ADZHIEV": (
        "📌 Driver Name: MUKHAMED ADZHIEV \n"
        "📞 Phone Number: 786-843-1879 \n"
        "🚛 Truck Number: 3 \n"
        "🚂 Trailer Number: 3 \n"
        "🔑 VIN:3C63RRHL8RG307633 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Dumitru Ou"
    ),
    "Водитель ALEKSEI LAMATKHANOV": (
        "📌 Driver Name: ALEKSEI LAMATKHANOV \n"
        "📞 Phone Number: 323-219-9464 \n"
        "🚛 Truck Number: 9 \n"
        "🚂 Trailer Number: 9 \n"
        "🔑 VIN:3C63RRGL2RG112628 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель MARAT KAZIEV": (
        "📌 Driver Name: MARAT KAZIEV \n"
        "📞 Phone Number: 754-280-7200 \n"
        "🚛 Truck Number: 14 \n"
        "🚂 Trailer Number: 14 \n"
        "🔑 VIN:3C63RRHL6RG289665 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель AZAT BORONCHIEV": (
        "📌 Driver Name: AZAT BORONCHIEV \n"
        "📞 Phone Number: 929-627-1722 \n"
        "🚛 Truck Number: 21 \n"
        "🚂 Trailer Number: 21 \n"
        "🔑 VIN:3C63RRGL3RG109933 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Alexei Lamatkhanov"
    ),
    "Водитель INAL VALIEV": (
        "📌 Driver Name: INAL VALIEV \n"
        "📞 Phone Number: 708-969-9882 \n"
        "🚛 Truck Number: 24 \n"
        "🚂 Trailer Number: 24 \n"
        "🔑 VIN:3C63RRHL4RG289664 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель ALEKSANDR PAVLOV": (
        "📌 Driver Name: ALEKSANDR PAVLOV \n"
        "📞 Phone Number: 929-721-9669 \n"
        "🚛 Truck Number: 1 \n"
        "🚂 Trailer Number: 1 \n"
        "🔑 VIN:1GC4KTEY7SF130031 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель MUKHAR KHUGAEV": (
        "📌 Driver Name: MUKHAR KHUGAEV \n"
        "📞 Phone Number: 224-651-5069 \n"
        "🚛 Truck Number: 31 \n"
        "🚂 Trailer Number: 31 \n"
        "🔑 VIN:3C63RRJLLXNG152569 \n"
        "⚓Ramps: 10ft \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель BAIR DABAIN": (
        "📌 Driver Name: BAIR DABAIN \n"
        "📞 Phone Number: 470-978-5585 \n"
        "🚛 Truck Number: 10 \n"
        "🚂 Trailer Number: 10 \n"
        "🔑 VIN:3C63RRGL6RG109909 \n"
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Alexei Lamatkhanov"
    ),
    "Водитель VITALII HONCHAROV": (
        "📌 Driver Name: VITALII HONCHAROV \n"
        "📞 Phone Number: 904-333-2447 \n"
        "🚛 Truck Number: 33 \n"
        "🚂 Trailer Number: 33 \n"
        "🔑 VIN:3C63RRHL9RG301260 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9620lb \n"
        "🅱 Owner: "
    ),
    "Водитель SERGHEI CIOBANU": (
        "📌 Driver Name: SERGHEI CIOBANU \n"
        "📞 Phone Number: 224-343-1680 \n"
        "🚛 Truck Number: 28 \n"
        "🚂 Trailer Number: 28 \n"
        "🔑 VIN:3C63RRHL5RG337088 \n" 
        "⚓Ramps: 14ft \n"
        "⚖ Weight: 9220lb \n"
        "🅱 Owner: Dumitru OU"
    ),
        "Водитель GRIGORII MOSKALETS": (
        "📌 Driver Name: GRIGORII MOSKALETS \n"
        "📞 Phone Number: 754-284-6442 \n"
        "🚛 Truck Number: 15 \n"
        "🚂 Trailer Number: 15 \n"
        "🔑 VIN:3C63RRHL2RG341423 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9220lb \n"
        "🅱 Owner: Dumitru OU"
    ),
    "Водитель SERHII HONCHARENKO": (
        "📌 Driver Name: SERHII HONCHARENKO \n"
        "📞 Phone Number: 386-225-1619 \n"
        "🚛 Truck Number: 19 \n"
        "🚂 Trailer Number: 19 \n"
        "🔑 VIN:3C63RRGL2RG219808 \n" 
        "⚓Ramps: 14ft \n"
        "⚖ Weight: 8200lb \n"
        "🅱 Owner: Ruslan"
    ),
    "Водитель DARMAN ORUZBAEV": (
        "📌 Driver Name: DARMAN ORUZBAEV \n"
        "📞 Phone Number: 718-344-0617 \n"
        "🚛 Truck Number: 4 \n"
        "🚂 Trailer Number: 4 \n"
        "🔑 VIN:3C63RRHLXRG341413 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель TOTRAZ ABAEV": (
        "📌 Driver Name: TOTRAZ ABAEV \n"
        "📞 Phone Number: 754-286-7577 \n"
        "🚛 Truck Number: 16 \n"
        "🚂 Trailer Number: 16 \n"
        "🔑 VIN:3C63RRHL2PG643033 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Stas"
    ),
    "Водитель YERKEBULAN BOSHAIBEKOV": (
        "📌 Driver Name: YERKEBULAN BOSHAIBEKOV \n"
        "📞 Phone Number: 773-751-9292 \n"
        "🚛 Truck Number: 18 \n"
        "🚂 Trailer Number: 18 \n"
        "🔑 VIN:3C63RRHL0RG289662 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8100lb \n"
        "🅱 Owner: Dumitru OU"
    ),
    "Водитель MIRBEK ALOEV": (
        "📌 Driver Name: MIRBEK ALOEV \n"
        "📞 Phone Number: 916-767-6753 \n"
        "🚛 Truck Number: 32 \n"
        "🚂 Trailer Number: 32 \n"
        "🔑 VIN:3C63RRHL2RG289436 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Stas"
    ),
    "Водитель MARIN GULIA": (
        "📌 Driver Name: MARIN GULIA \n"
        "📞 Phone Number: 916-912-7398 \n"
        "🚛 Truck Number: 26 \n"
        "🚂 Trailer Number: 26 \n"
        "🔑 VIN:1GT49LEY8RF467913 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель ALBERT ABAIKHANOV": (
        "📌 Driver Name: ALBERT ABAIKHANOV \n"
        "📞 Phone Number: 347-739-8531 \n"
        "🚛 Truck Number: 22 \n"
        "🚂 Trailer Number: 22 \n"
        "🔑 VIN:3C63RRHL9KG642308 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8860lb \n"
        "🅱 Owner: Rassul"
    ),
    "Водитель ASKHABALI SHABANOV": (
        "📌 Driver Name: ASKHABALI SHABANOV \n"
        "📞 Phone Number: 520-994-9999 \n"
        "🚛 Truck Number: 7 \n"
        "🚂 Trailer Number: 7 \n"
        "🔑 VIN:3C63RRHL4RG358188 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9360lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель ILLIA HORBATOK": (
        "📌 Driver Name: ILLIA HORBATOK \n"
        "📞 Phone Number: 701-403-0994 \n"
        "🚛 Truck Number: 2 \n"
        "🚂 Trailer Number: 2 \n"
        "🔑 VIN:3C63RRHL2RG358187 \n"
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8720lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель TSYDEN TOBODORZHIEV": (
        "📌 Driver Name: TSYDEN TOBODORZHIEV \n"
        "📞 Phone Number: 347-232-8827 \n"
        "🚛 Truck Number: 36 \n"
        "🚂 Trailer Number: 36 \n"
        "🔑 VIN:1FT8W3DT3REF83199 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель VIKTOR ATANOV": (
        "📌 Driver Name: VIKTOR ATANOV \n"
        "📞 Phone Number: 929-481-9521 \n"
        "🚛 Truck Number: 39 \n"
        "🚂 Trailer Number: 39 \n"
        "🔑 VIN:1FT8W3DT9REE49099 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель AZAT AZAMAT": (
        "📌 Driver Name: AZAT AZAMAT \n"
        "📞 Phone Number: 253-286-8080 \n"
        "🚛 Truck Number: 29 \n"
        "🚂 Trailer Number: 29 \n"
        "🔑 VIN:3C63RRGL6RG382381 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8680lb \n"
        "🅱 Owner: Owner Operator"
    ),
        "Водитель DIONISIE COTOVICI": (
        "📌 Driver Name: DIONISIE COTOVICI \n"
        "📞 Phone Number: 754-271-3481 \n"
        "🚛 Truck Number: 12 \n"
        "🚂 Trailer Number: 12 \n"
        "🔑 VIN:3C63RRHL6RG341392 \n" 
        "⚓Ramps: ft \n"
        "⚖ Weight: lb \n"
        "🅱 Owner: "
    ),
    "Водитель GEORGII RIONELI": (
        "📌 Driver Name: GEORGII RIONELI \n"
        "📞 Phone Number: 925-440-1503 \n"
        "🚛 Truck Number: 35 \n"
        "🚂 Trailer Number: 35 \n"
        "🔑 VIN:3C63RRGL0NG356465 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель DENIS COLESNICENCO": (
        "📌 Driver Name: DENIS COLESNICENC \n"
        "📞 Phone Number: 630-352-9196 \n"
        "🚛 Truck Number: 38 \n"
        "🚂 Trailer Number: 38 \n"
        "🔑 VIN:3C63RRHL6RG289522 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9600lb \n"
        "🅱 Owner: Gheorghe Balica"
    ),
    "Водитель IGOR BALAKIN": (
        "📌 Driver Name: IGOR BALAKIN \n"
        "📞 Phone Number: 331-229-8750 \n"
        "🚛 Truck Number: 20 \n"
        "🚂 Trailer Number: 20 \n"
        "🔑 VIN:3C63RRGL3KG618197 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 8700lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель TAULAN TOTORKULOV": (
        "📌 Driver Name: TAULAN TOTORKULOV \n"
        "📞 Phone Number: 224-463-0235 \n"
        "🚛 Truck Number: 5 \n"
        "🚂 Trailer Number: 5 \n"
        "🔑 VIN:3C63RRGL9KG700614 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9700lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель ERDEM DORZHIEV": (
        "📌 Driver Name: ERDEM DORZHIEV \n"
        "📞 Phone Number: 412-304-4565 \n"
        "🚛 Truck Number: 8 \n"
        "🚂 Trailer Number: 8 \n"
        "🔑 VIN:3C63R3GL6NG159989 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель (Said) MAGOMEDSAID GABIBULAEV": (
        "📌 Driver Name: MAGOMEDSAID GABIBULAEV \n"
        "📞 Phone Number: 305-391-1839 \n"
        "🚛 Truck Number: 6 \n"
        "🚂 Trailer Number: 6 \n"
        "🔑 VIN:3C63RRGL0RG183858 \n" 
        "⚓Ramps: 12ft \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Ruslan"
    ),
    "Водитель (DOS) DASTAN MASYLKANOV": (
        "📌 Driver Name: DASTAN MASYLKANOV \n"
        "📞 Phone Number: 917-704-3848 \n"
        "🚛 Truck Number: 37 \n"
        "🚂 Trailer Number: 37 \n"
        "🔑 VIN:3C63RRHL6RG307632 \n" 
        "⚓Ramps: n/a \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Alex"
    ),
    "Водитель SOSLAN GAGLOEV": (
        "📌 Driver Name: SOSLAN GAGLOEV \n"
        "📞 Phone Number: 786-868-5690 \n"
        "🚛 Truck Number: 13 \n"
        "🚂 Trailer Number: 13 \n"
        "🔑 VIN:3C63RRGL7RG295329 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    ),
}
# URL для фотографий и файлов
drivers_files = {
    "Водитель RAMIL KHAFIZOV": {
        "photo": "https://drive.google.com/file/d/1RebRt_fdyY9zFgDbNq43MmsYOi5t9G5p/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1bzdQIFsOilY8eHuA4x7gq3xgKAaqoBLa/view?usp=drive_link"
    },
    "Водитель OLEH SEMENENNKO": {
        "photo": "https://drive.google.com/file/d/17e18kZ1O8RPz3-4xkpAgj_Rsev2icA0p/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1BypkUML2-13yC_1zhopir5MakM16y2Z1/view?usp=drive_link"
    },
    "Водитель OLEG RESHAEV": {
        "photo": "https://drive.google.com/file/d/1DHJ2H1BlcwDFzCdTkC2-4gPSSgn3eePE/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1Jog2P7ssILevyBMUeOOQEapT2pwxexGD/view?usp=drive_link"
    },
    "Водитель MUKHAMED ADZHIEV": {
        "photo": "https://drive.google.com/file/d/1WQb3XId7N5Ofwzc3mcDZ2JIpSDhvm2Lo/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1F8zgKUpT6KW4dEd1O9viAAOdVBUi2oHr/view?usp=drive_link"
    },
    "Водитель MARAT KAZIEV": {
        "photo": "https://drive.google.com/file/d/1DoRXI4QLuC0-05Zl5U7tv0ONYE449eEn/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1tf90OVNgaMQA3djkYzsapF1-bgENxgId/view?usp=drive_link"
    },
    "Водитель ALEKSEI LAMATKHANOV": {
        "photo": "https://drive.google.com/file/d/1gjpo3VgvjGobRuNsjRBeRfdRZpLBCjud/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1gjpo3VgvjGobRuNsjRBeRfdRZpLBCjud/view?usp=drive_link"
    },
    "Водитель AZAT BORONCHIEV": {
        "photo": "https://drive.google.com/file/d/1fa58slTENamCbpZ4hUMeJhtVIXsXJJjk/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1N3IdZjiMWHZDRCIJK21cNSUM2PlKTOUT/view?usp=drive_link"
    },
    "Водитель INAL VALIEV": {
        "photo": "https://drive.google.com/file/d/1Vz86bB-jcE0OAjrWxkMgqV-zEIYIKLXy/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1Zjrs0cPAl9p2z8BfLb150pxOm-FgLZkQ/view?usp=drive_link"
    },
    "Водитель ALEKSANDR PAVLOV": {
        "photo": "https://drive.google.com/file/d/1CxXCHz5L6hogjHAsQ-Fb60r2U4mODuId/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/11Opx2TN6ScaJ31YjHyB1IQ6ktOq26KM9/view?usp=drive_link"
    },
    "Водитель MUKHAR KHUGAEV": {
        "photo": "https://drive.google.com/file/d/1bjLiM3Ojt880hei6Jeb7_nbSh2r2NyJ_/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1Gspmhy-V8uvniWVRFNYF-0y3OgKODF_F/view?usp=drive_link"
    },
    "Водитель BAIR DABAIN": {
        "photo": "https://drive.google.com/file/d/1EiLW7-ITrIKjqefHMU1MtHBTwFM-V7yG/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1qoV0MKrI3dycrH8eKHn1wy6MSalNgErn/view?usp=drive_link"
    },
    "Водитель VITALII HONCHAROV": {
        "photo": "https://drive.google.com/file/d/1CsUw9bnJflnnpGFcEg4GWnb_4pZGwSYF/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1CsUw9bnJflnnpGFcEg4GWnb_4pZGwSYF/view?usp=drive_link"
    },
    "Водитель SERGHEI CIOBANU": {
        "photo": "https://drive.google.com/file/d/1B5yeo6F1-IiQiAXYuzc3lG8VbQsfNCxR/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1OoSZcQYjrCdtpoFk3H8CxUEdkOYYvWYC/view?usp=drive_link"
    },
    "Водитель GRIGORII MOSKALETS": {
        "photo": "https://drive.google.com/file/d/13kkj2hoPUbK2-8O7RlWCvuDNDnb17Pgy/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/13kkj2hoPUbK2-8O7RlWCvuDNDnb17Pgy/view?usp=drive_link"
    },
    "Водитель VITALII HONCHAROV": {
        "photo": "https://drive.google.com/file/d/1hUtSdZNcEMa__yG1kPCbFNUcNpgOAvIU/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/13kkj2hoPUbK2-8O7RlWCvuDNDnb17Pgy/view?usp=drive_link"
    },
    "Водитель SERHII HONCHARENKO": {
        "photo": "https://drive.google.com/file/d/14CpboA9pYKyLWuxijf9gD6Ok7nDaGTIW/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1o5hiNiTsmXdxvH3_FuAZUEkPzZMGjbAr/view?usp=drive_link"
    },
    "Водитель DARMAN ORUZBAEV": {
        "photo": "https://drive.google.com/file/d/1-_9957CAuAIYgqxLmKxF4iWyT-YIIJv4/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1ejFCxUWMC3WylWhZ8s3NbITVfgHriocd/view?usp=drive_link"
    },
    "Водитель TOTRAZ ABAEV": {
        "photo": "https://drive.google.com/file/d/1ymKwY80eRZziGw8svzLw3ZSsLC4QorcX/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1b4fse7ttFAvzwqhy83lu_GtCkcoMQhff/view?usp=drive_link"
    },
    "Водитель YERKEBULAN BOSHAIBEKOV": {
        "photo": "https://drive.google.com/file/d/1mG7YPuGRjU8cFrKPxNW-1gw2-3AwQYoe/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/17oYiD-eOkhHIC9mwAsbXeNvehgJfkWmn/view?usp=drive_link"
    },
    "Водитель MIRBEK ALOEV": {
        "photo": "https://drive.google.com/file/d/138kYd20Lv1KJsTKfLKE1BgncdPbt3drV/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1NYUXFrUXf9DUVk3CRTMQnOS1-OodsI2f/view?usp=drive_link"
    },
    "Водитель MARIN GULIA": {
        "photo": "https://drive.google.com/file/d/1gNGy-qOQQUd7W_DljwzbOBiEM473il1e/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1ykhC1lIoNk7UM3zjJqCUFLWVsOey5oMR/view?usp=drive_link"
    },
    "Водитель ALBERT ABAIKHANOV": {
        "photo": "https://drive.google.com/file/d/10D25opmpC3DDgeWYPri8HzHUQfAs3dU9/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/17M0f3cTycjjtptvjXz119oIkHNd2-DPN/view?usp=drive_link"
    },
    "Водитель ASKHABALI SHABANOV": {
        "photo": "https://drive.google.com/file/d/1rNpG4XpHUSImDMUwMVmTsIRmY8a1_WJ_/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1jDhOocC4s0d1ZaW863WQcTbHm_3Zehig/view?usp=drive_link"
    },
    "Водитель ILLIA HORBATOK": {
        "photo": "https://drive.google.com/file/d/171t2eY0cAwKMXdM4o3wokRqR41cCsrZN/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/171t2eY0cAwKMXdM4o3wokRqR41cCsrZN/view?usp=drive_link"
    },
    "Водитель TSYDEN TOBODORZHIEV": {
        "photo": "https://drive.google.com/file/d/15JGHtHuNOrznk-te8uDWRDkhEvVH5OOd/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1NNJM7lmtpRnh82ICh92xNXHzmr4LGBI4/view?usp=drive_link"
    },
    "Водитель VIKTOR ATANOV": {
        "photo": "https://drive.google.com/file/d/1s1WgBRsMU0Q1roF8OxZsNFBmP8wokmfU/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1GwhxpNl9IHvaNHnIZWiFVQEx2JP2rT9i/view?usp=drive_link"
    },
    "Водитель DIONISIE COTOVICI": {
        "photo": "https://drive.google.com/file/d/1BKMmmiGdM7gm0FnRz2fX2HgIMVlgrJBx/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1BKMmmiGdM7gm0FnRz2fX2HgIMVlgrJBx/view?usp=drive_link"
    },
    "Водитель AZAT AZAMAT": {
        "photo": "https://drive.google.com/file/d/1HyPI1o5c2aMv2PO6R_yE-0xV94D3Q8AO/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1iOLgUSvrvYj0mrB6o5t9Xtq0GTGO-9c2/view?usp=drive_link"
    },
    "Водитель GEORGII RIONELI": {
        "photo": "https://drive.google.com/file/d/1gi0RkYOlGyH_TSgs0MhTATcNsaamiyJD/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1WDlAlIKCRofH0N1Z-Z8N2qNfgaO1FpsK/view?usp=drive_link"
    },
    "Водитель DENIS COLESNICENCO": {
        "photo": "https://drive.google.com/file/d/17kdgaxVAGn6dypn-5azbIsoY6Eu1TXcm/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1OkH_O_LOSUAbOvV1F85sxwJfJpomSowJ/view?usp=drive_link"
    },
    "Водитель IGOR BALAKIN": {
        "photo": "https://drive.google.com/file/d/1InjrQgybbfXYM8cqiEcIAXV2h_dgmgSz/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1VLB3ADySVYgLBm3DGv-utG8xEuHj1Vcv/view?usp=drive_link"
    },
    "Водитель TAULAN TOTORKULOV": {
        "photo": "https://drive.google.com/file/d/1hrVycBVGxxXq9-aNZWfW40hk93F82_mw/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1m0kguCz7qe3-kyB_Qi_NyCNUTgh5ACYU/view?usp=drive_link"
    },
    "Водитель ERDEM DORZHIEV": {
        "photo": "https://drive.google.com/file/d/1-xI2Xysnd19jiFp65Fwu4XenVHKjbAut/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1b3_h2Rk-6_YL2ccvdnojRCTbpemDZ2Ce/view?usp=drive_link"
    },
    "Водитель (Said) MAGOMEDSAID GABIBULAEV": {
        "photo": "https://drive.google.com/file/d/1qVDUgjKnkq5iCG7EHZdl_72xR08jgpWL/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1lft69iT2fdtwZLN3whhknZWuTIYVT5K7/view?usp=drive_link"
    },
    "Водитель (DOS) DASTAN MASYLKANOV": {
        "photo": "https://drive.google.com/file/d/1laZ-h8AnpAxDuYKA9gg3zrYfML-JShBg/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1eMQhFKn0X5NDe0DmDl6pPQDK1VWpOo3a/view?usp=drive_link"
    },
    "Водитель SOSLAN GAGLOEV": {
        "photo": "https://drive.google.com/file/d/1GvuTMUKgNdgcR9bsmThZR9dx7bvZCgEY/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1vs1lmsH4MqphrU5p_GenEtTPQ2PwPXxR/view?usp=drive_link"
    },
}

async def show_dispatchers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton(name, callback_data=name)] for name in dispatchers.keys()]
    keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='start')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text("👥 Выберите диспетчера:", reply_markup=reply_markup)


async def show_drivers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    selected_dispatcher = query.data
    keyboard = [[InlineKeyboardButton(name, callback_data=name)] for name in dispatchers[selected_dispatcher]]
    keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='dispatchers')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(f"🚛 Водители диспетчера {selected_dispatcher}:", reply_markup=reply_markup)

async def show_driver_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    selected_driver = query.data
    keyboard = [
        [InlineKeyboardButton("📸 Фото", url=drivers_files[selected_driver]["photo"]),
         InlineKeyboardButton("📂 Файлы", url=drivers_files[selected_driver]["files"])],
        [InlineKeyboardButton("⬅️ Назад", callback_data='dispatchers')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(f"{drivers_info[selected_driver]}", reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Переход по различным callback_data
    if query.data == 'start':
        await start(update, context)
    elif query.data == 'dispatchers':
        await show_dispatchers(update, context)
    elif query.data in dispatchers:
        await show_drivers(update, context)
    elif query.data in drivers_info:
        await show_driver_info(update, context)
    elif query.data.startswith("photo_"):
        selected_driver = query.data.split("_")[1]

        # Проверяем, есть ли фото для выбранного водителя
        if selected_driver in drivers_files and "photo" in drivers_files[selected_driver]:
            photo_path = drivers_files[selected_driver]["photo"]
            try:
                await query.message.reply_photo(photo=open(photo_path, 'rb'))
            except Exception as e:
                await query.message.reply_text(f"Ошибка при отправке фото: {e}")
        else:
            await query.message.reply_text("Фото не найдено для этого водителя.")
    elif query.data.startswith("files_"):
        selected_driver = query.data.split("_")[1]

        # Проверяем, есть ли документ для выбранного водителя
        if selected_driver in drivers_files and "document" in drivers_files[selected_driver]:
            file_path = drivers_files[selected_driver]["document"]
            try:
                await query.message.reply_document(document=open(file_path, 'rb'))
            except Exception as e:
                await query.message.reply_text(f"Ошибка при отправке документа: {e}")
        else:
            await query.message.reply_text("Документы не найдены для этого водителя.")


# Создание приложения
app = Application.builder().token("8109632757:AAHJDDDcfidBLLym_ZDYIu4bH001P1LkcKE").build()

# Добавление обработчиков
app.add_handler(CallbackQueryHandler(show_dispatchers, pattern="^dispatchers$"))
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    app.run_polling()
