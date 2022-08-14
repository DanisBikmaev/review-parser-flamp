# review-parser-flamp
Eng/Ru

<h2>Review Parser Flam - a script for collecting new reviews about companies from the Flamp.ru website and sending them to the telegram channel.</h2>

<h2>Description</h2>
The script collects data such as:
<ol>
  <li>Review link</li>
  <li>Review author</li>
  <li>Date and time of the recall</li>
  <li>Review rating (from 1 to 5)</li>
  <li>Review text</li>
</ol>

New reviews are recorded in an Excel file and sent to the telegram channel as a post.

<h2>Script settings</h2>

<h3>Setting up sending messages to telegrams</h3>
<ul>
<li>Enter TOKEN for telegram bot (parser.py -> line 19), <a href="https://core.telegram.org/bots">how to get TOKEN you can read here.</a></li >
<li>Enter the chat telegram id (parser.py -> line 20), how to get the chat id is described below.</li>
<details>
   <summary>How to get chat id</summary>
    To get the Telegram ID of a public chat or group, use the @username_to_id_bot bot. Step-by-step instruction:
    <ul>
    <li>Looking for @username_to_id_bot through the Telegram search bar.</li>
    <li>Launch the bot by pressing the "Start" button.</li>
    <li>We go to the chat or group, information about which we want to know.
    <li>Copy the link to the chat. It can be found in the chat / group settings by clicking on the "Invite" button. The link will be at the top of the window that opens.</li>
    <li>Next, we return to our bot and send it the link we copied earlier.</li>
    <li>In the response message, we get the basic data about the chat/group. The bottom line will be ID.</li>
    </ul>
</details>
<li>Set the time to receive updates (parser.py -> line 92, default is: every day at 12:00)</li>
<li>Specify search city (main.py -> line 14)</li>
<li>Run parser.py</li>
<li>Enter the name of a company that is in the flamp.ru database, if there is no such company, the script will search for reviews on companies similar in name</li>

<h2>Review Parser Flam - скрипт для сбора новых отзывов о компаниях c сайта Flamp.ru и отправка на телеграмм канал.</h2>

<h2>Описание</h2>
Скрипт собирает такие данные, как:
<ol>
  <li>Ссылка на отзыв</li>
  <li>Автор отзыва</li>
  <li>Дата и время отзыва</li>
  <li>Рейтинг отзыва (от 1 до 5)</li>
  <li>Текст отзыва</li>
</ol>

Новые отзывы записываются в Excel файл и отправляются на телеграмм канал в виде поста.

<h2>Настройка скрипта</h2>

<h3>Настройка отправки сообщений на телеграмм</h3>
<ul>
<li>Ввести TOKEN для телеграмм бота (parser.py -> строка 19), <a href="https://core.telegram.org/bots">как получить TOKEN можно почитать тут.</a></li>
<li>Ввести id телеграмм чата (parser.py -> строка 20), как получить id чата расписано ниже.</li> 
<details>
   <summary>Как получить id чата</summary>  
    Чтобы получить ID Telegram публичного чата или группы, воспользуйтесь ботом @username_to_id_bot. Пошаговая инструкция:
    <ul>
    <li>Ищем @username_to_id_bot через поисковую строку Telegram.</li>
    <li>Запускаем бот нажатием кнопки «Начать».</li>
    <li>Заходим в чат или группу, информацию о которой хотим узнать.
    <li>Копируем ссылку на чат. Её можно найти в настройках чата/группы при нажатии на кнопку «Пригласить». Ссылка будет находиться в верхней части открывшегося окна.</li>
    <li>Далее возвращаемся к нашему боту и отправляем ему скопированную ранее ссылку.</li>
    <li>В ответном сообщении получаем основные данные о чате/группе. В нижней строке будет ID.</li>
    </ul>
</details>
<li>Установить время для получения обновений(parser.py -> строка 92, по умолчанию установлено: каждый день в 12:00)</li>
<li>Указать город поиска (main.py -> строка 14)</li>
<li>Запустить parser.py</li>
<li>Введите название компании, которая есть в базе flamp.ru, если такой компании нет, скрипт будет искать отзывы на похожие по названию компании</li>

