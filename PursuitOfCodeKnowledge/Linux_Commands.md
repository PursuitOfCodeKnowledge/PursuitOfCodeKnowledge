******************************************************************Погоня за Кодовым Знанием*******************************************************************************
Перед тем как выполнять любые команды, вам нужно распаковать архив без пароля PursuitOfCodeKnowledge.7z:

Kогда откроешь терминал в первый раз проверь что у тебя с правами на учётку, потому что тебе нужно будет запускать с sudo:
команда whoami покажет как у тебя учетка называется например:
whoami
sergey
Значит учётка у тебя sergey называется, дальше введи команду groups чтобы посмотреть в каких группах состоишь, должна быть группа sudo там:
groups sergey
после этой команды у тебя появятся разные группы и посмотри если есть sudo, если нет sudo,
 то выполни команду su и введи пароль от root(своей учётки sergey, если пароли не делал разными для root и sergey) и не забудь в терминале не отображаются пароли, когда будешь вводить их:
 su
После того как зайдёшь под root, выполни команду чтобы добавить пользователя своего sergey в группу sudo:
sudo usermod -aG sudo sergey
Затем перезагрузи компьютер или ноутбук, или просто выйди из учетки и заново зайди и после этого открой терминал и введи команду sudo whoami, должно отобразиться root:
sudo whoami
root

Установите p7zip-full (если он еще не установлен) в терминале:
sudo apt update
sudo apt install p7zip-full
--------------------Распаковка архивa без пароля-----
7z x PursuitOfCodeKnowledge.7z
-------------
Перед тем как выполнять любые команды, вам нужно распаковать архив Game.7z с паролем в текущем каталоге PursuitOfCodeKnowledge:

7z x Game.7z -pPASSWORD

вместо слова PASSWORD, нужно вставить пароль который вы должны узнать из игры или посмотреть в ответе (Start_Answer.md)
-------------
Если вы сомневаетесь, в каком каталоге находитесь, вы можете использовать команду pwd (Print Working Directory), чтобы получить абсолютный путь
текущего каталога, пример команды:

pwd

Напишите в терминале pwd, а затем нажмите клаишу enter на клавиатуре и вы получите ответ что вы находитесь в каталоге PursuitOfCodeKnowledge:
/home/sergey/PursuitOfCodeKnowledge
-------------
Команда ls нужна чтобы посмотреть какие файлы и папки лежат в вашем пространстве PursuitOfCodeKnowledge:

ls

Напишите в терминале ls, а затем нажмите клаишу enter на клавиатуре и вы получите ответ:
Game  Game.zip  InstructionAboutGame.txt  Linux_Commands.md  Start_Answer.md  Start.md
------------
Навигация

Две основные команды cd и ls для перемещения по каталогам

Команда cd - это команда для перехода в другой каталог. пример команды:

cd Game

Вы перейдете в каталог Game

cd ..

Используя две точки вы возвратитесь назад в каталог PursuitOfCodeKnowledge

Используйте команду ls если вы хотите узнать что хранится в другом каталоге, например вы находитесь в каталоге PursuitOfCodeKnowledge и чтобы узнать какие папки и файлы
 лежат в каталоге Game наберите команду:

ls Game

И вы увидите LevelOne.7z  LevelZero

Затем вы набираете команду:

cd Game/LevelZero

И вы переходите сразу из каталога PursuitOfCodeKnowledge в каталог LevelZero, не  заходя в каталог Game.
-------------
Для просмотра информации которая содержится в файле, используйте команды cat и less:

cat Start.md

И вы получите ответ: 
******************************************************************Погоня за Кодовым Знанием*******************************************************************************

Привет Старина! Добро пожаловать в кибермир! Если читаешь эти строки, то ты уже в погоне за кодовым знанием! Чтобы начать играть, тебе нужно распаковать пакет с игрой.
Но есть трудность пакет с паролем. Твоя задача узнать пароль от пакета, ответь на простой вопрос: "В каком году появилась Русь?".

**************************************************************************************************************************************************************************

less Start.md

Вы увидите информацию внутри файла, затем чтобы выйти из файла нажмите на клавиатуре ctrl + z
-------------
При вводе каталога или имени файла вы можете нажать клавишу 'Tab', чтобы автоматически завершить его, если это возможно. Например, в каталоге, если вы введете:

cd G

и нажмете клавишу 'Tab', он дополнит оставшееся и покажет вам:

cd Game

Однако, если существует несколько файлов/каталогов, которые совпадают по введенной части, это не сработает. Поэтому если название полностью  не подставилось,
 то добавляйте по одному символу(букве) и нажимайте клавишу Tab, пока не появится что вам нужно.
-------------
Очистка терминала

Используйте команду clear, чтобы очистить терминал:

clear
------------
Чтобы вставить что-нибудь в терминале используй клавиши на клавиатуре: ctrl+shift+v
-----------
Before executing any commands, you need to unpack the archive without a password PursuitOfCodeKnowledge.7z:

When you open the terminal for the first time, check that you have account rights, because you will need to run with sudo.:
the whoami command will show you what your account is called, for example:
whoami
sergey
So your account is called sergey, then enter the groups command to see which groups you belong to, there should be a sudo group there.:
groups sergey
after this command, you will have different groups and see if there is sudo, if there is no sudo,
 then run the su command and enter the password from root (your sergey account, if you did not make the passwords different for root and sergey) and do not forget that passwords are not displayed in the terminal when you enter them:
su
After you log in as root, run the command to add your sergey user to the sudo group:
sudo usermod -aG sudo sergey
Then restart your computer or laptop, or just log out and log in again, and then open the terminal and enter the sudo whoami command, root should be displayed.:
sudo whoami
root

Install p7zip-full (if it is not already installed) in the terminal:
sudo apt update
sudo apt install p7zip-full

Unpacking the archive without a password:
7z x PursuitOfCodeKnowledge.7z

Before executing any commands, you need to unpack the Game.7z with a password in the current PursuitOfCodeKnowledge directory:
7z x Game.7z -pPASSWORD
instead of the word PASSWORD, you need to insert the password that you need to learn from the game or see in the response (Start_Answer.md )

If you are in doubt which directory you are in, you can use the pwd (Print Working Directory) command to get the absolute path
of the current directory, example command:
pwd
Write pwd in the terminal, and then press enter on the keyboard and you will receive an answer that you are in the PursuitOfCodeKnowledge directory:
/home/sergey/PursuitOfCodeKnowledge

The ls command is needed to see which files and folders are in your PursuitOfCodeKnowledge space:
ls
Write ls in the terminal, and then press the enter key on the keyboard and you will receive an answer.:
Game  Game.zip  InstructionAboutGame.txt  Linux_Commands.md  Start_Answer.md  Start.md

Navigation
The two main commands cd and ls are for moving through directories
The cd command is a command to move to another directory, an example command is:
cd Game
You will be redirected to the Game:
cd ..
Using two dots, you will return back to the PursuitOfCodeKnowledge catalog.
Use the ls command if you want to find out what is stored in another directory, for example, you are in the PursuitOfCodeKnowledge directory and to find out which folders and files
are in the Game directory, type the command:
ls Game
And you will see LevelOne.7z  LevelZero
Then you type the command:
cd Game/LevelZero
And you go straight from the PursuitOfCodeKnowledge catalog to the LevelZero catalog without going into the Game catalog.

To view the information contained in the file, use the cat and less commands.:
cat Start.md
And you will get the answer:
Hello Old Man! Welcome to the cyberworld! If you are reading these lines, then you are already in pursuit of code knowledge! To start playing, you need to unpack the game package.
But there is a difficulty with the password package. Your task is to find out the password from the package, answer a simple question: "In what year did Russia appear?".
less Start.md
You will see the information inside the file, then press ctrl + z on your keyboard to exit the file.

When you enter a directory or a file name, you can press the 'Tab' key to end it automatically, if possible. For example, in a directory, if you type:
cd G
and press the 'Tab' key, it will complete the rest and show you:
cd Game
However, if there are several files/directories that match the entered part, this will not work. Therefore, if the name is not completely substituted,
 then add one character (letter) at a time and press the Tab key until you see what you need.

Clearing the terminal
Use the clear command to clear the terminal:
clear

To insert something in the terminal, use the keyboard keys: ctrl+shift+v
**************************************************************************************************************************************************************************
