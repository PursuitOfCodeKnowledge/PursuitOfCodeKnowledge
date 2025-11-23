******************************************************************Погоня за Кодовым Знанием*******************************************************************************

Принято считать, что Русь образовалась в 862 году. Это условная дата. По одной из версий год выбран неизвестным летописцем в XI веке.

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

Выполните команду чтобы распаковать архив Game.7z:
Установите p7zip-full (если он еще не установлен) в терминале :
sudo apt update
sudo apt install p7zip-full
--------------------Распаковка архива Game.7z с паролем-----
7z x Game.7z -p862
Затем перейдите при помощи команды cd в каталог Game:
cd Game
Затем перейдите на нулевой уровень в каталог LevelZero:
cd LevelZero

It is generally believed that Russia was formed in 862. This is a conditional date. According to one version, the year was chosen by an unknown chronicler in the 11th century.

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

Run the command to unzip the Game.7z:
Install p7zip-full (if it is not already installed) in the terminal :
sudo apt update
sudo apt install p7zip-full

Unpacking the Game.7z with password:
7z x Game.7z -p862
Then use the cd command to navigate to the Game directory:
cd Game
Then go to Level Zero in the Level Zero directory.:
cd LevelZero

**************************************************************************************************************************************************************************
**************************************************************************************************************************************************************************

