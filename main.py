from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
import telegram.error

# 🔒 Список разрешённых пользователей (замени ID на реальные)
ALLOWED_USERS = {5538804267, 8026256981, 7275611563, 723670550, 5636776284}  # Замени на свои ID

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
    "🚌 Диспетчер Serghei": ["Водитель RADZHAB MAGOMEDOV", "Водитель OLEH SEMENENKO", "Водитель IHOR PIKHURETS", "Водитель MYKOLA MYKYTYUK", "Водители AIDAR & GUZEL"],
    "🚋 Диспетчер Vick": ["Водитель DARMAN ORUZBAEV", "Водитель ERDEM DORZHIEV", "Водитель TOTRAZ ABAEV", "Водитель (DOS) DASTAN MASYLKANOV", "Водитель NURLAN BAINEYEV"],
    "🚂 Диспетчер Peter": ["Водитель BALZHIR RINCHINDORZHIEV", "Водитель RUSLAN SATBAYEV", "Водитель ALEXANDER ARBUZOV", "Водитель GRIGORII MOSKALETS", "Водитель RAMZAN DZHABRAILOV"],
    "🚀 Диспетчер Dima": ["Водитель GEORGII RIONELI", "Водитель ALEKSANDR PAVLOV", "Водитель SERGHEI CIOBANU", "Водитель ALBERT ABAIKHANOV", "Водитель CARVIS SMITH Jr" ],
    "✈ Диспетчер Max": ["Водитель ALEKSEI LAMATKHANOV", "Водитель OLEG RESHAEV", "Водитель SOSLAN GAGLOEV"]
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
    "Водитель ALEKSANDR PAVLOV": (
        "📌 Driver Name: ALEKSANDR PAVLOV \n"
        "📞 Phone Number: 929-721-9669 \n"
        "🚛 Truck Number: 1 \n"
        "🚂 Trailer Number: 1 \n"
        "🔑 VIN:1GC4KTEY7SF130031 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9480lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель ALEXANDER ARBUZOV": (
        "📌 Driver Name: ALEXANDER ARBUZOV \n"
        "📞 Phone Number: 765-568-3634 \n"
        "🚛 Truck Number: 2 \n"
        "🚂 Trailer Number: 2 \n"
        "🔑 VIN:3C63RRHL2RG108058 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8800lb \n"
        "🅱 Owner: Sergiu Zambrean"
    ),
    "Водитель RUSLAN SATBAYEV": (
        "📌 Driver Name: RUSLAN SATBAYEV \n"
        "📞 Phone Number: 786-651-9828 \n"
        "🚛 Truck Number: 18 \n"
        "🚂 Trailer Number: 42 \n"
        "🔑 VIN:1FT7W2BT2REC20983 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner operator"
    ),
    "Водитель OLEH SEMENENKO": (
        "📌 Driver Name: OLEH SEMENENNKO \n"
        "📞 Phone Number: 701-971-4705 \n"
        "🚛 Truck Number: 25 \n"
        "🚂 Trailer Number: 25 \n"
        "🔑 VIN:3C63RRHL3RG301237 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Radu Bragari"
    ),
    "Водитель IHOR PIKHURETS": (
        "📌 Driver Name: IHOR PIKHURETS \n"
        "📞 Phone Number: 470-232-4231 \n"
        "🚛 Truck Number: 29 \n"
        "🚂 Trailer Number: 29 \n"
        "🔑 VIN:1FT8W3DT4SEC33747 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8720lb \n"
        "🅱 Owner: Alex Bizga"
    ),
    "Водитель (DOS) DASTAN MASYLKANOV": (
        "📌 Driver Name: DASTAN MASYLKANOV \n"
        "📞 Phone Number: 917-704-3848 \n"
        "🚛 Truck Number: 27 \n"
        "🚂 Trailer Number: 37 \n"
        "🔑 VIN:1GC4KTEYXSF340641 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8640lb \n"
        "🅱 Owner: Alex Bizga"
    ),
    "Водитель NURLAN BAINEYEV": (
        "📌 Driver Name: NURLAN BAINEYEV \n"
        "📞 Phone Number: 305-434-2101 \n"
        "🚛 Truck Number: 19 \n"
        "🚂 Trailer Number: 30 \n"
        "🔑 VIN: 1FT8W3DT3TEC72119 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель MYKOLA MYKYTYUK": (
        "📌 Driver Name: MYKOLA MYKYTYUK \n"
        "📞 Phone Number: 313-349-8477 \n"
        "🚛 Truck Number: 30 \n"
        "🚂 Trailer Number: 40 \n"
        "🔑 VIN:1FT8W3DTOTEC24478 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9380lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель DARMAN ORUZBAEV": (
        "📌 Driver Name: DARMAN ORUZBAEV \n"
        "📞 Phone Number: 718-344-0617 \n"
        "🚛 Truck Number: 4 \n"
        "🚂 Trailer Number: 4 \n"
        "🔑 VIN:1FT8W3DT5TEC15632 \n"
        "⚓ Ramps: Mega Ramps \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Alex Bizga"
    ),
    "Водитель ERDEM DORZHIEV": (
        "📌 Driver Name: ERDEM DORZHIEV \n"
        "📞 Phone Number: 412-304-4565 \n"
        "🚛 Truck Number: 1 \n"
        "🚂 Trailer Number: 8 \n"
        "🔑 VIN:3C63RRGL2SG526742 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator"
    ),
      "Водитель TOTRAZ ABAEV": (
        "📌 Driver Name: TOTRAZ ABAEV \n"
        "📞 Phone Number: 754-286-7577 \n"
        "🚛 Truck Number: 11 \n"
        "🚂 Trailer Number: 11 \n"
        "🔑 VIN:3C63RRGL4RG396229 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Stas"
    ),
    "Водитель CARVIS SMITH Jr": (
        "📌 Driver Name: CARVIS SMITH Jr \n"
        "📞 Phone Number: 616 323 7906 \n"
        "🚛 Truck Number: 8 \n"
        "🚂 Trailer Number: 1 \n"
        "🔑 VIN:3C63RPGL7DG611096 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель OLEG RESHAEV": (
        "📌 Driver Name: OLEG RESHAEV \n"
        "📞 Phone Number: 279-789-4042 \n"
        "🚛 Truck Number: 23 \n"
        "🚂 Trailer Number: 23 \n"
        "🔑 VIN:1FT8W3DT0SED25518 \n"
        "⚓ Ramps: 12ft \n"
        "⚖ Weight: 9200lb \n"
        "🅱 Owner: Alex Bizga"
    ),
    "Водитель RAMZAN DZHABRAILOV": (
        "📌 Driver Name: RAMZAN DZHABRAILOV \n"
        "📞 Phone Number: 786 960 2200 \n"
        "🚛 Truck Number: 23 \n"
        "🚂 Trailer Number: 23 \n"
        "🔑 VIN:1FT8W3DT0SED25518 \n"
        "⚓ Ramps: 12ft \n"
        "⚖ Weight: 9200lb \n"
        "🅱 Owner: Alex Bizga"
    ),
    "Водитель BALZHIR RINCHINDORZHIEV": (
        "📌 Driver Name: BALZHIR RINCHINDORZHIEV \n"
        "📞 Phone Number: 312-481-1956 \n"
        "🚛 Truck Number: 15 \n"
        "🚂 Trailer Number: 42 \n"
        "🔑 VIN:1FT8W3DT3TEC24331 \n"
        "⚓ Ramps: 12ft \n"
        "⚖ Weight: 9100lb \n"
        "🅱 Owner: Dumitru Ou"
    ),
    "Водитель GRIGORII MOSKALETS": (
        "📌 Driver Name: GRIGORII MOSKALETS \n"
        "📞 Phone Number: 754-284-6442 \n"
        "🚛 Truck Number: 120 \n"
        "🚂 Trailer Number: 27 \n"
        "🔑 VIN:1FT8W3DT9SEC54495 \n"
        "⚓ Ramps: 12ft \n"
        "⚖ Weight: 9300lb \n"
        "🅱 Owner: Dumitru Ou"
    ),
    "Водители AIDAR & GUZEL": (
        "📌 Driver Name: AIDAR KHABIBULLIN и SHARAFUTDINOVA GUZEL \n"
        "📞 Phone Number: 619-951-6457 and 619-951-6836 \n"
        "🚛 Truck Number: 3 \n"
        "🚂 Trailer Number: 3 \n"
        "🔑 VIN:3C63RRGL0SG554913 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9400lb \n"
        "🅱 Owner: Owner Operator"
    ),
    "Водитель RADZHAB MAGOMEDOV": (
        "📌 Driver Name: RADZHAB MAGOMEDOV \n"
        "📞 Phone Number: 541-800-9999 \n"
        "🚛 Truck Number: 26 \n"
        "🚂 Trailer Number: 26 \n"
        "🔑 VIN:1FT8W3DT1RED22119 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 9700lb \n"
        "🅱 Owner: Owner operator"
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
    "Водитель SERGHEI CIOBANU": (
        "📌 Driver Name: SERGHEI CIOBANU \n"
        "📞 Phone Number: 224-343-1680 \n"
        "🚛 Truck Number: 16 \n"
        "🚂 Trailer Number: 38 \n"
        "🔑 VIN:3C63RRHL7RG337075 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner operator"
    ),
    "Водитель ALBERT ABAIKHANOV": (
        "📌 Driver Name: ALBERT ABAIKHANOV \n"
        "📞 Phone Number: 347-739-8531 \n"
        "🚛 Truck Number: 22 \n"
        "🚂 Trailer Number: 22 \n"
        "🔑 VIN:3C63RRHL9KG642308 \n"
        "⚓ Ramps: 8ft \n"
        "⚖ Weight: 8860lb \n"
        "🅱 Owner: Rasul"
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
        "photo": "https://drive.google.com/file/d/1gjpo3VgvjGobRuNsjRBeRfdRZpLBCjud/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1wIiX2huhoeTQUT4MLZ9YoX5a7k-bXwzA/view?usp=drive_link"
    },
    "Водитель ALEKSANDR PAVLOV": {
        "photo": "https://drive.google.com/file/d/1CxXCHz5L6hogjHAsQ-Fb60r2U4mODuId/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1wFHZryy0XO1sNrF5uMBokhMLaWTjsx-k/view?usp=drive_link"
    },
    "Водитель ALEXANDER ARBUZOV": {
        "photo": "https://drive.google.com/file/d/1hLatH-VAeTsUWYlFXVsGTsY0qQu8xQg9/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1xoOMo5NNtG0Dj6B3Aj3WAXbEd2NrsIcj/view?usp=drive_link"
    },
    "Водитель RUSLAN SATBAYEV": {
        "photo": "https://drive.google.com/file/d/1QdoekziBT4Ig5UlvlQtRIQsBR86f1JCQ/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1nRUum9Vk021IMrrPC3_--ukSo7ZLDZSQ/view?usp=drive_link"
    },
    "Водитель OLEH SEMENENKO": {
        "photo": "https://drive.google.com/file/d/17e18kZ1O8RPz3-4xkpAgj_Rsev2icA0p/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1355yJvYbY8onkEGG5-sRFvK2Rhxu15Ii/view?usp=drive_link"
    },
    "Водитель IHOR PIKHURETS": {
        "photo": "https://drive.google.com/file/d/1rPj2F3N91EW3IYQCJ4vxEgNf7fdJbQtP/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1vpyJIhiHsO4C5z5QbeOZgFpHKiBKB3s-/view?usp=drive_link"
    },
    "Водитель (DOS) DASTAN MASYLKANOV": {
        "photo": "https://drive.google.com/file/d/1laZ-h8AnpAxDuYKA9gg3zrYfML-JShBg/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1OPfSrp256GnBeTjZwOHF5wr5_w7o-QfP/view?usp=drive_link"
    },
    "Водитель NURLAN BAINEYEV": {
        "photo": "https://drive.google.com/file/d/1p5erR4O8JZnTFYQR5m5o2Vmfl3tojWTZ/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1AYeKIQ4YT6WaNp464k96hBXuvZKtztej/view?usp=drive_link"
    },
    "Водитель MYKOLA MYKYTYUK": {
        "photo": "https://drive.google.com/file/d/1w48QLL9mRPKqGkZ1blOyMfhp5kE67JaY/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1z3oXWE_850_UgLovJf9PPKxgv53PY2xm/view?usp=drive_link"
    },
    "Водитель DARMAN ORUZBAEV": {
        "photo": "https://drive.google.com/file/d/1-_9957CAuAIYgqxLmKxF4iWyT-YIIJv4/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1-SuxUNxII8U1jBxaY_Zb16VUD4rgSpd3/view?usp=drive_link"
    },
    "Водитель SOSLAN ALBOROV": {
        "photo": "https://drive.google.com/file/d/1DIyt2OsfPobeWOdoJ4xAEQLugdRAPaDs/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1qkehe1UDFOwQ0yguuTvSBv2P1bTbE-c8/view?usp=drive_link"
    },
    "Водитель ERDEM DORZHIEV": {
        "photo": "https://drive.google.com/file/d/1-xI2Xysnd19jiFp65Fwu4XenVHKjbAut/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1oiI50PVqoaNe1efDTzj5WaAokGqK5eZL/view?usp=drive_link"
    },
    "Водитель TOTRAZ ABAEV": {
        "photo": "https://drive.google.com/file/d/1ymKwY80eRZziGw8svzLw3ZSsLC4QorcX/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1YyluJIYytnh7DssNocZPfqvJsMwnVR8E/view?usp=drive_link"
    },
   "Водитель CARVIS SMITH Jr": {
        "photo": "https://drive.google.com/file/d/1pEsL092Q2Db129Xv8_hP8bts04gQzqy8/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1fGcK_fE66WzNZcs8Ft8mlPWTBhFdDenY/view?usp=drive_link"
    },
    "Водитель OLEG RESHAEV": {
        "photo": "https://drive.google.com/file/d/1hh9pjA3WKuW1y6lMqEjQ5MI8oVgJsUXq/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1sMQYx819pI9DRtoh6bK1oBYtBMDl4Zhi/view?usp=drive_link"
    },
    "Водитель RAMZAN DZHABRAILOV": {
        "photo": "https://drive.google.com/file/d/1UL68GNL2n_QgqNO4dM__4l_wWvR9M0QB/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1sMQYx819pI9DRtoh6bK1oBYtBMDl4Zhi/view?usp=drive_link"
    },
    "Водитель BALZHIR RINCHINDORZHIEV": {
        "photo": "https://drive.google.com/file/d/1fi0Erh2cT-f8PzNWq9Nzrk8gQC5pwgX7/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1grr1tG9jW0fe0kx8BOKu8C94zR-DoCsh/view?usp=drive_link"
    },
    "Водитель GRIGORII MOSKALETS": {
        "photo": "https://drive.google.com/file/d/1BKyWXI6KqUz_QHBHUZjJluL7LPbd1CxN/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/14LAC43biwNbVdtC1BYYPAJuVBXl41Fai/view?usp=drive_link"
    },
    "Водители AIDAR & GUZEL": {
        "photo": "https://drive.google.com/file/d/1IayD23MhwuBumdnU0Elp0rt4nf8juqtb/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1Qnf4XsQi4foITTFYDohqif1JvqOCFtLi/view?usp=drive_link"
    },
    "Водитель RADZHAB MAGOMEDOV": {
        "photo": "https://drive.google.com/file/d/1ZkQQAhZD2eufBwiAr1SVJME8ffp-nK1m/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1-PKgg6VYVUK3kPy8waWwVZvUxOTQjv0b/view?usp=drive_link"
    },
    "Водитель GEORGII RIONELI": {
        "photo": "https://drive.google.com/file/d/1gi0RkYOlGyH_TSgs0MhTATcNsaamiyJD/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1keW4Iuhc72asf0PnfO_cnzAHoAhfhgOA/view?usp=drive_link"
    },
    "Водитель SERGHEI CIOBANU": {
        "photo": "https://drive.google.com/file/d/1B5yeo6F1-IiQiAXYuzc3lG8VbQsfNCxR/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1YyD-xu-FXuRxNfRKfbNJMO6acFeVboyu/view?usp=drive_link"
    },
    "Водитель TAULAN TOTORKULOV": {
        "photo": "https://drive.google.com/file/d/1hrVycBVGxxXq9-aNZWfW40hk93F82_mw/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1muoSC2fmHMo8Rf05JQgpyhs6XxkTjY0m/view?usp=drive_link"
    },
    "Водитель ALBERT ABAIKHANOV": {
        "photo": "https://drive.google.com/file/d/10D25opmpC3DDgeWYPri8HzHUQfAs3dU9/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1rEFHyVORCmCd5bOz7lCt9QJ8Ir2mzovN/view?usp=drive_link"
    },
    "Водитель SOSLAN GAGLOEV": {
        "photo": "https://drive.google.com/file/d/1GvuTMUKgNdgcR9bsmThZR9dx7bvZCgEY/view?usp=drive_link",
        "files": "https://drive.google.com/file/d/1dyDS9_vUxBnQqpkM8lQBRW0mGCQtHjt-/view?usp=drive_link"
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
app = Application.builder().token("7656171707:AAEuL0NcHIFsAG5vRgYZ2GizY0JQN4kQwRc").build()

# Регистрация обработчиков
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_driver))
app.add_handler(CallbackQueryHandler(button_handler))

if __name__ == "__main__":
    print("Бот запущен...")
    app.run_polling()
