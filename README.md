# photo_ramka
▌Как запустить бота 
 
1.  Получите токен Telegram-бота: 
    -   Обратитесь к @BotFather в Telegram. 
    -   Следуйте инструкциям для создания нового бота и получите его токен. 
 
2.  Замените BOT_TOKEN в коде: 
    -   Откройте файл скрипта (.py) в текстовом редакторе. 
    -   Найдите строку BOT_TOKEN = "ВАШ_ТОКЕН" и замените значение на токен вашего бота, который вы получили от BotFather. Например BOT_TOKEN = "YOUR_BOT_TOKEN". 
    
3.  Поместите фоновое изображение: 
    -   Убедитесь, что у вас есть фоновое изображение (по умолчанию rek.png). Поместите его в ту же папку, где находится файл скрипта. Если вы хотите использовать другое изображение или другой путь, замените имя файла в переменной BACKGROUND_IMAGE. 
     
4.  Запуск скрипта: 
    -  Откройте терминал или командную строку. 
    -  Перейдите в папку с файлом скрипта. 
    -  Запустите скрипт, используя команду: 
         
         
Bash 
 
 
        python your_script_name.py 
         
         
       (Замените your_script_name.py на имя вашего файла скрипта). 
 
5.  Использование бота: 
    -   Откройте Telegram и найдите вашего бота. 
    -   Начните общение с ним. 
    -   Отправьте команду /start, чтобы получить приветственное сообщение. 
    -   Отправьте боту квадратное изображение. 
    -   Бот вернет вам изображение с наложенным на фон прозрачным слоем. 
 
▌Настройка параметров 
 
В коде есть несколько параметров, которые можно настроить: 
 
-   BACKGROUND_IMAGE: Путь к фоновому изображению. 
-   ALPHA: Уровень прозрачности накладываемого изображения (значение от 0.0 до 1.0). 
-   PADDING: На сколько пикселей увеличить фон от сторон, для наложения основного изображения. 
-   BOT_TOKEN: Токен вашего бота из BotFather. 
 
▌Логирование 
 
Бот использует модуль logging для записи информации о действиях и ошибках. Логи будут сохраняться в консоли. 
 
▌Зависимости 
 
-   telebot: Для работы с Telegram API. 
-   Pillow: Для обработки изображений. 
-   io: Для работы с байтовыми потоками. 
-   logging: Для логирования работы бота. 
-   os: Для работы с файловой системой 
 
▌Примечания 
 
-   Убедитесь, что ваше фоновое изображение и изображение пользователя имеют формат RGB 
-   Скрипт не обрабатывает смену фонового изображения в процессе работы. Необходимо перезапустить скрипт, если вы хотите сменить фон. 
-   Бот разработан как простой пример и может быть улучшен для добавления новых функций или более сложной обработки. 
 
▌Лицензия 
 
Данный код распространяется под свободной лицензией. Вы можете использовать и изменять его в соответствии с вашими потребностями. 
``` 
```
