import telebot
from telebot import types
from PIL import Image, UnidentifiedImageError
import io
import logging
import os

# Установите уровень логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Замените на токен вашего бота
BOT_TOKEN = "ВАШ_ТОКЕН" #введите ваш токен
# Путь к фоновому изображению
BACKGROUND_IMAGE = "rek.png"  # замените, если нужно
ALPHA = 0.7
# На сколько увеличить фон
PADDING = 200 # пикселей

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отправляет приветственное сообщение при запуске бота."""
    bot.reply_to(
        message,
        'Привет! Отправь мне квадратное изображение, и я наложу его на фон с прозрачностью.',
    )


@bot.message_handler(content_types=['photo'])
def handle_image(message):
    """Обрабатывает полученное изображение."""
    if not message.photo:
        bot.reply_to(message, 'Пожалуйста, отправьте мне изображение.')
        return
    
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        image_bytes = bot.download_file(file_info.file_path)
    except Exception as e:
        logger.error(f"Ошибка загрузки файла: {e}")
        bot.reply_to(message, 'Произошла ошибка при загрузке файла. Попробуйте еще раз.')
        return

    try:
        user_image = Image.open(io.BytesIO(image_bytes))
    except UnidentifiedImageError as e:
        logger.error(f"Ошибка обработки изображения: {e}")
        bot.reply_to(message, 'Не удалось открыть изображение. Убедитесь, что это изображение')
        return

    if user_image.width != user_image.height:
        bot.reply_to(message, 'Изображение должно быть квадратным.')
        return
    
    try:
      background_image = Image.open(BACKGROUND_IMAGE)
    except FileNotFoundError:
        logger.error(f"Фон не найден по пути: {BACKGROUND_IMAGE}")
        bot.reply_to(message, 'Фон не найден, поместите фон в папку с ботом')
        return
    except Exception as e:
        logger.error(f"Ошибка при открытии фонового изображения: {e}")
        bot.reply_to(message, 'Произошла ошибка при открытии фона. Убедитесь, что он существует')
        return

    try:
        # Выводим размеры и режимы
        logger.info(f"User image mode: {user_image.mode}")
        logger.info(f"Background image mode: {background_image.mode}")

        # Убедимся что оба изображения формата RGB
        if user_image.mode != "RGB":
           user_image = user_image.convert("RGB")
        if background_image.mode != "RGB":
          background_image = background_image.convert("RGB")
        
        # Расширяем фон
        new_width = user_image.width + 2 * PADDING
        new_height = user_image.height + 2 * PADDING
        
        # Создаем новое изображение с прозрачной заливкой
        resized_background = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

        # Изменяем размер фона
        resized_background_temp = background_image.resize((new_width, new_height))
        
        # Накладываем на прозрачный фон фон
        resized_background.paste(resized_background_temp, (0,0))

        # Помещаем изображение пользователя на фон
        paste_x = PADDING
        paste_y = PADDING
        resized_background.paste(user_image, (paste_x, paste_y))

        # Наложение изображения пользователя на фон с прозрачностью
        final_image = Image.blend(resized_background, resized_background, alpha=ALPHA)
    except Exception as e:
        logger.error(f"Ошибка при наложении изображений: {e}")
        bot.reply_to(message, 'Произошла ошибка при обработке изображений. Попробуйте еще раз.')
        return
    
    # Отправка результирующего изображения
    try:
      output_buffer = io.BytesIO()
      final_image.save(output_buffer, format='PNG')
      output_buffer.seek(0)
      bot.send_photo(message.chat.id, photo=output_buffer)
    except Exception as e:
        logger.error(f"Ошибка при отправке файла: {e}")
        bot.reply_to(message, 'Произошла ошибка при отправке результата. Попробуйте еще раз.')
        return


if __name__ == '__main__':
    logger.info('Бот запущен')
    bot.polling(none_stop=True)
