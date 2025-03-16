******************************************************************Погоня за Кодовым Знанием*******************************************************************************
Об игре Погоня за кодовым знанием для Терминала Linux:
Привет Старина!Если ты держишь в руках это послание, значит, ты уже на пути к завоеванию господства в безбрежном океане терминала Linux.
 Да-да, речь идет о грандиозной битве, в которой столкнутся не только машины и механические создания,
 но и полный спектр существ, населяющих этот виртуальный мир. Тебя ждут встречи с ботами, роботами, людьми, а также полулюдьми и полуживотными.
 И, конечно же, нельзя забывать об искусственном интеллекте, который с одинаковым интересом будет читать все строки нашего повествования и принимать участие в этой захватывающей схватке!

В игре "Погоня за кодовым знанием" тебе предстоит бросить вызов не только соперникам, но и самому себе. Каждый шаг в этой захватывающей виртуальной реальности требует от тебя смекалки,
 знаний и страсти к исследованию. В центре событий окажется главный терминал — черный ящик, в котором скрываются сокровища кодового мира.
 Здесь, в одном из самых интригующих уголков киберпространства, наступает момент, когда каждый участник, от наивного новичка до опытного хакера, имеет шанс проявить свое мастерство и блеснуть знаниями.

Никогда не стоит недооценивать мощь игры, в которой сойдутся не только технологии, но и человеческий разум. Тебе придется освоить команду за командой, погружаясь в тайны и секреты,
 чтобы в конечном итоге выступить в роли истинного лидера на поле боя. Но не забудь: даже самый простой узел может скрывать в себе загадку, способную изменить ход всей игры.
 И чем больше ты будешь расширять свои знания, тем сильнее и влиятельнее станешь в этом виртуальном конфликте.

Так что, да прибудет с нами сила — сила знаний, креативности и, конечно, игр разума! Отважься бросить вызов как самому себе, так и своим оппонентам в этой потрясающей погоне за кодом.
 Вперед, к непознанным вершинам и увлекательным открытиям! Каждый матч — это новая возможность не просто одержать победу, но и научиться чему-то новому, погружаясь в удивительный мир возможностей,
 который предлагает терминал Linux.

Да и забыл сказать, когда откроешь терминал в первый раз проверь что у тебя с правами на учётку, потому что тебе нужно будет запускать с sudo:
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

А теперь открывай терминал, и установи p7zip-full (если он еще не установлен) в терминале:
sudo apt update
sudo apt install p7zip-full
А затем распаковывай архив PursuitOfCodeKnowledge.7z без пароля:
7z x PursuitOfCodeKnowledge.7z

Да прибудет с нами сила в игры разума!

About game Pursuit Of Code Knowledge for Terminal Linux:
Hello Old Man! If you are holding this message in your hands, it means that you are already on your way to gaining dominance in the vast ocean of the Linux terminal. 
 Yes, yes, we are talking about a grand battle in which not only machines and mechanical creatures will collide., 
 but also the full range of creatures inhabiting this virtual world. You will encounter bots, robots, humans, as well as half-humans and half-animals. 
 And, of course, we must not forget about artificial intelligence, which will read all the lines of our narrative with equal interest and take part in this exciting battle!

In the game "Chasing code knowledge" you have to challenge not only your rivals, but also yourself. Every step in this immersive virtual reality requires you to be smart., 
 knowledge and passion for research. At the center of the action will be the main terminal, a black box that hides the treasures of the code world. 
 Here, in one of the most intriguing corners of cyberspace, there comes a moment when every participant, from the naive novice to the experienced hacker,
 has a chance to show their skills and show off their knowledge.

Never underestimate the power of a game that brings together not only technology, but also the human mind. You'll have to master team after team, diving into mysteries and secrets., 
 to eventually act as a true leader on the battlefield. But don't forget: even the simplest node can hide a mystery that can change the course of the whole game. 
 And the more you expand your knowledge, the stronger and more influential you will become in this virtual conflict.

So, may the power come with us — the power of knowledge, creativity and, of course, mind games! Dare to challenge both yourself and your opponents in this amazing code chase. 
 Forward to unknown peaks and exciting discoveries! Each match is a new opportunity not only to win, but also to learn something new, immersing yourself in an amazing world of possibilities., 
 which offers a Linux terminal.

And I forgot to tell you, when you open the terminal for the first time, check that you have account rights, because you will need to run with sudo.:
the whoami command will show you what your account is called, for example:
whoami
sergey
So your account is called sergey, then enter the groups command to see which groups you belong to, there should be a sudo group there.:
groups sergey
after this command, you will have different groups and see if there is sudo, if there is no sudo,
 then run the su command and enter the password from root (your sergey account, if you did not make the passwords different for root and sergey)
 and do not forget that passwords are not displayed in the terminal when you enter them:
su
After you log in as root, run the command to add your sergey user to the sudo group:
sudo usermod -aG sudo sergey
Then restart your computer or laptop, or just log out and log in again, and after that open the terminal and enter the command sudo whoami, root should be displayed:
sudo whoami
root

Now open the terminal and install p7zip-full (if it is not already installed) in the terminal:
sudo apt update
sudo apt install p7zip-full
And then unpack the archive PursuitOfCodeKnowledge.7z without a password:
7z x PursuitOfCodeKnowledge.7z

May the power of mind games come with us!
**************************************************************************************************************************************************************************
