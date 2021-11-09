import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='5dc51a59f21a8ce97d7668ef6b048b2ae00a60dfed74fbddf9fabc3a247e640b61e426bbb50c84d1c3f1a')
from vk_api.bot_longpoll import VkBotLongPoll
longpoll = VkBotLongPoll(vk_session, 87865876)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

start = VkKeyboard(one_time=True)
start.add_button('Начать', color=VkKeyboardColor.NEGATIVE)

keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Создатели загрузочных флешек 💿', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Linux 🐧', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('Windows 🪟', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('Гайды 💁‍️', color=VkKeyboardColor.SECONDARY)


linux = VkKeyboard(one_time=False)
linux.add_button('Дистрибутивы', color=VkKeyboardColor.PRIMARY)
linux.add_line()
linux.add_button('Оболочки', color=VkKeyboardColor.SECONDARY)
linux.add_button('Консоль', color=VkKeyboardColor.SECONDARY)
linux.add_line()
linux.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)


windows = VkKeyboard(one_time=False)
windows.add_button('Ссылки', color=VkKeyboardColor.PRIMARY)
windows.add_line()
windows.add_button('Коммандная строка', VkKeyboardColor.SECONDARY)
windows.add_line()
windows.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)


iso = VkKeyboard(one_time=False)
iso.add_button('Для одного Файла', color=VkKeyboardColor.PRIMARY)
iso.add_line()
iso.add_button('Мультизагрузочная', color=VkKeyboardColor.PRIMARY)
iso.add_line()
iso.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)


guid = VkKeyboard(one_time=False)
guid.add_button('Установка Windows', color=VkKeyboardColor.SECONDARY)
guid.add_line()
guid.add_button('Установка Ubuntu и производных', color=VkKeyboardColor.SECONDARY)
guid.add_line()
guid.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)


winurl = VkKeyboard(one_time=False)
winurl.add_openlink_button(label='Windows 10 (Microsoft)', link='https://www.microsoft.com/ru-ru/software-download/windows10ISO')
winurl.add_line()
winurl.add_openlink_button(label='Windows 11 (BETA)', link='https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewiso?wa=wsignin1.0')
winurl.add_line()
winurl.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)


distr = VkKeyboard(one_time=False)
distr.add_button('Debian-подобные', color=VkKeyboardColor.PRIMARY)
distr.add_line()
distr.add_button('Arch-подобные', color=VkKeyboardColor.PRIMARY)
distr.add_line()
distr.add_button('Gentoo', color=VkKeyboardColor.PRIMARY)
distr.add_line()
distr.add_openlink_button(label='Посмотреть все дистрибутивы', link='https://distrowatch.com')
distr.add_line()
distr.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
distr.add_button('Linux 🐧', color=VkKeyboardColor.POSITIVE)


deb = VkKeyboard(one_time=False)
deb.add_button('Ubuntu-подобные', color=VkKeyboardColor.PRIMARY)
deb.add_line()
deb.add_button('Deepin', color=VkKeyboardColor.PRIMARY)
deb.add_button('SteamOS', color=VkKeyboardColor.PRIMARY)
deb.add_line()
deb.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
deb.add_button('Дистрибутивы', color=VkKeyboardColor.POSITIVE)


deepin = VkKeyboard(one_time=False)
deepin.add_openlink_button(label='Оффициальный сайт', link='https://www.deepin.org/en/')
deepin.add_line()
deepin.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
deepin.add_button('Debian-подобные', color=VkKeyboardColor.POSITIVE)


steam = VkKeyboard(one_time=False)
steam.add_openlink_button(label='Оффициальный сайт', link='https://store.steampowered.com/steamos/')
steam.add_line()
steam.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
steam.add_button('Debian-подобные', color=VkKeyboardColor.POSITIVE)

ubp = VkKeyboard(one_time=False)
ubp.add_button('Ubuntu', color=VkKeyboardColor.PRIMARY)
ubp.add_button('KUbuntu', color=VkKeyboardColor.PRIMARY)
ubp.add_line()
ubp.add_button('XUbuntu', color=VkKeyboardColor.PRIMARY)
ubp.add_button('LUbuntu', color=VkKeyboardColor.PRIMARY)
ubp.add_line()
ubp.add_button('Ubuntu Studio', color=VkKeyboardColor.PRIMARY)
ubp.add_button('PopOS!', color=VkKeyboardColor.PRIMARY)
ubp.add_line()
ubp.add_button('Linux Mint', color=VkKeyboardColor.PRIMARY)
ubp.add_line()
ubp.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
ubp.add_button('Debian-подобные', color=VkKeyboardColor.POSITIVE)

ubuntu = VkKeyboard(one_time=False)
ubuntu.add_openlink_button(label='Оффициальный сайт', link='https://ubuntu.com')
ubuntu.add_line()
ubuntu.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
ubuntu.add_button('Ubuntu-подобные', color=VkKeyboardColor.POSITIVE)


kubuntu = VkKeyboard(one_time=False)
kubuntu.add_openlink_button(label='Оффициальный сайт', link='https://kubuntu.org')
kubuntu.add_line()
kubuntu.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
kubuntu.add_button('Ubuntu-подобные', color=VkKeyboardColor.POSITIVE)


xubuntu = VkKeyboard(one_time=False)
xubuntu.add_openlink_button(label='Оффициальный сайт', link='https://xubuntu.org')
xubuntu.add_line()
xubuntu.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
xubuntu.add_button('Ubuntu-подобные', color=VkKeyboardColor.POSITIVE)


lubuntu = VkKeyboard(one_time=False)
lubuntu.add_openlink_button(label='Оффициальный сайт', link='https://lubuntu.me')
lubuntu.add_line()
lubuntu.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
lubuntu.add_button('Ubuntu-подобные', color=VkKeyboardColor.POSITIVE)


ubs = VkKeyboard(one_time=False)
ubs.add_openlink_button(label='Оффициальный сайт', link='https://ubuntustudio.org')
ubs.add_line()
ubs.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
ubs.add_button('Ubuntu-подобные', color=VkKeyboardColor.POSITIVE)


pop = VkKeyboard(one_time=False)
pop.add_openlink_button(label='Оффициальный сайт', link='https://pop.system76.com')
pop.add_line()
pop.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
pop.add_button('Ubuntu-подобные', color=VkKeyboardColor.POSITIVE)


mint = VkKeyboard(one_time=False)
mint.add_openlink_button(label='Оффициальный сайт', link='https://linuxmint.com')
mint.add_line()
mint.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
mint.add_button('Ubuntu-подобные', color=VkKeyboardColor.POSITIVE)



arch = VkKeyboard(one_time=False)
arch.add_button('Manjaro', color=VkKeyboardColor.PRIMARY)
arch.add_line()
arch.add_button('Archman', color=VkKeyboardColor.PRIMARY)
arch.add_line()
arch.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
arch.add_button('Дистрибутивы', color=VkKeyboardColor.POSITIVE)


manjaro = VkKeyboard(one_time=False)
manjaro.add_openlink_button(label='Оффициальный сайт', link='https://manjaro.org')
manjaro.add_line()
manjaro.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
manjaro.add_button('Arch-подобные', color=VkKeyboardColor.POSITIVE)


archman = VkKeyboard(one_time=False)
archman.add_openlink_button(label='Оффициальный сайт', link='https://archman.org')
archman.add_line()
archman.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
archman.add_button('Arch-подобные', color=VkKeyboardColor.POSITIVE)


gentoo = VkKeyboard(one_time=False)
gentoo.add_openlink_button(label='Оффициальный сайт', link='https://www.gentoo.org')
gentoo.add_line()
gentoo.add_openlink_button(label='Gentoo Handbook', link='https://wiki.gentoo.org/wiki/Handbook:AMD64/ru')
gentoo.add_line()
gentoo.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
gentoo.add_button('Дистрибутивы', color=VkKeyboardColor.POSITIVE)


rufus = VkKeyboard(one_time=False)
rufus.add_openlink_button(label='Оффициальный сайт', link='https://rufus.ie/ru/')
rufus.add_line()
rufus.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
rufus.add_button('Создатели загрузочных флешек 💿', color=VkKeyboardColor.POSITIVE)


ventoy = VkKeyboard(one_time=False)
ventoy.add_openlink_button(label='Оффициальный сайт', link='https://www.ventoy.net/en/index.html')
ventoy.add_line()
ventoy.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
ventoy.add_button('Создатели загрузочных флешек 💿', color=VkKeyboardColor.POSITIVE)


bash = VkKeyboard(one_time=False)
bash.add_button('Файловые', color=VkKeyboardColor.PRIMARY)
bash.add_button('Архивация', color=VkKeyboardColor.PRIMARY)
bash.add_button('deb-пакеты', color=VkKeyboardColor.PRIMARY)
bash.add_line()
bash.add_button('Менеджер пакетов apt', color=VkKeyboardColor.PRIMARY)
bash.add_button('Текст', color=VkKeyboardColor.PRIMARY)
bash.add_button('Пользователь и система', color=VkKeyboardColor.PRIMARY)
bash.add_line()
bash.add_button('Права доступа', color=VkKeyboardColor.PRIMARY)
bash.add_button('SSH-подключение', color=VkKeyboardColor.PRIMARY)
bash.add_button('Дата и время', color=VkKeyboardColor.PRIMARY)
bash.add_line()
bash.add_button('На главную 🏠', color=VkKeyboardColor.NEGATIVE)
bash.add_button('Управление процессами', color=VkKeyboardColor.PRIMARY)
bash.add_button('Linux 🐧', color=VkKeyboardColor.POSITIVE)




for event in Lslongpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        vars1 = ['Начать']
        varsH = [ 'На главную 🏠']
        vars2 = ['Linux 🐧']
        vars3 = ['Windows 🪟']
        vars4 = ['Создатели загрузочных флешек 💿']
        vars5 =['Гайды 💁‍️']
        vars6 =['Ссылки']
        vars7 =['Дистрибутивы']
        vars8 =['Debian-подобные']
        vars9 = ['Deepin']
        vars10 = ['SteamOS']
        vars11 = ['Ubuntu-подобные']
        vars12 = ['Ubuntu']
        vars13= ['KUbuntu']
        vars14 = ['XUbuntu']
        vars15 = ['LUbuntu']
        vars16 = ['Ubuntu Studio']
        vars17 = ['PopOS!']
        vars18 = ['Linux Mint']
        vars19 = ['Arch-подобные']
        vars20 = ['Manjaro']
        vars21 = ['Archman']
        vars22 = ['Gentoo']
        vars23 = ['Для одного Файла']
        vars24 = ['Мультизагрузочная']
        vars25 = ['Консоль']




        if event.text in vars1:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    message = 'Я могу дать некоторые подсказки для програмного обеспечения, в соответствии с предпочтениями моего владельца 👋',
                    keyboard = keyboard.get_keyboard(),
                    random_id = get_random_id(),
                    )
        elif event.text in varsH:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    keyboard = keyboard.get_keyboard(),
                    message = 'Чух-чух\n🏡',
                    random_id = get_random_id()
                    )
        elif event.text in vars2:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Нужна информация по дистрибутивам, оболочкам или комманды консоли?',
                    keyboard = linux.get_keyboard()
                    )
        elif event.text in vars3:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Нужны ссылки для скачивания, или помощь с коммандной строкой?',
                    keyboard = windows.get_keyboard()
                    )
        elif event.text in vars4:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Нужна флешка для одной системы или для нескольких? Для нескольких систем рекомендуется носитель от 16 гигабайт.',
                    keyboard = iso.get_keyboard()
                    )
        elif event.text in vars5:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Какая именно помощь требуется?',
                    keyboard = guid.get_keyboard()
                    )
        elif event.text in vars6:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Есть Windows 10 с оффициального сайта, если перейти с windows, то скачается MediaCreationTool для создания загрузочной флешки.\nWindows 11 предварительная сборка на оффициальном сайте, но необходима учётная запить insider preview.',
                    keyboard = winurl.get_keyboard()
                    )
        elif event.text in vars7:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Здесь показан список дистрибутивов и семейств, про которые у меня имеется информация',
                    keyboard = distr.get_keyboard()
                )
        elif event.text in vars8:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Здесь показан список дистрибутивов, основанных на Debian.\n\nДанная ветка дистрибутивов наиболее стабильная и имеет удобный формат пакетов ПО .deb',
                    keyboard = deb.get_keyboard()
                )
        elif event.text in vars9:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Дистрибутив, основанный на Debian, разрабатывается в Китае. Имеет достаточно приятный внешний вид, многие называют его "самым красивым линуксом".\nМногие предустановленные программы разрабатываются, или форкаются, разработчиками дистрибутива. Имеет свой пакетный менеджер. Оболочка рабочего стола собственная (Deepin desktop enviroment).',
                    attachment ='photo-87865876_457239025',
                    keyboard = deepin.get_keyboard()
                )
        elif event.text in vars10:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Дистрибутив, основанный на Debian, разрабатываемый корпорацией Valve специально для сервиса Steam. SteamOS была ориентирована для запуска игр на экране телевизора.Используется оболочка Gnome 3.\n\nВ декабре 2021 года планируется переход на Arch и оболочку KDE plasma 5',
                    attachment='photo-87865876_457239026',
                    keyboard=steam.get_keyboard()
                )
        elif event.text in vars11:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Здесь показан список дистрибутивов, основанных на Ubuntu.\n\nДанная ветка дистрибутивов наиболее подходящая для использовования в качестве знакомства с Linux.',
                    keyboard=ubp.get_keyboard()
                )
        elif event.text in vars12:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Самый популярный дистрибутив линукс, разрабатывается компанией Canonical. Используется оболочка рабочего стола GNOME 3.',
                    attachment='photo-87865876_457239027',
                    keyboard=ubuntu.get_keyboard()
                )
        elif event.text in vars13:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Является частью проекта Ubuntu и использует его основу, но использует окружение рабочего стола KDE plasma.',
                    attachment='photo-87865876_457239028',
                    keyboard=kubuntu.get_keyboard()
                )
        elif event.text in vars14:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Легковесный дистрибутив, основанный на Ubuntu, использующий в качестве окружение Xfce (оболочка написана на GTK 3).\n\nПотребляет мало ресурсов, но остаётся актуальным.',
                    attachment='photo-87865876_457239029',
                    keyboard=xubuntu.get_keyboard()
                )
        elif event.text in vars15:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Легковесный дистрибутив, основанный на Ubuntu, использующий в качестве окружение LXQt (оболочка написана на Qt).\n\nПотребляет мало ресурсов, но остаётся актуальным.',
                    attachment='photo-87865876_457239030',
                    keyboard=lubuntu.get_keyboard()
                )
        elif event.text in vars16:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Дистрибутив Linux, основанный на Ubuntu, использует в качестве графической среды XFCE и KDE Plasma.\n\nЦель проекта — быстрое развёртывание готовой к использованию фото-, видео-, аудиостудии с минимальными затратами средств и максимальным комфортом.',
                    attachment='photo-87865876_457239031',
                    keyboard=ubs.get_keyboard()
                )
        elif event.text in vars17:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Дистрибутив, основанный на Ubuntu, использует окружение Gnome, позиционируется как дружелюбный к пользователю. Имеет нативную поддержку проприетарных драйверов для видеокарт Nvidia и AMD.',
                    attachment='photo-87865876_457239032',
                    keyboard=pop.get_keyboard()
                )
        elif event.text in vars18:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Дистрибутив Linux, основанный на Ubuntu, использует окружение Cinnamon (форк Gnome). Целью проекта является предоставление «современной, элегантной и удобной операционной системы, которая одновременно является мощной и простой в использовании».\n\nТак же существует версия не использующая Ubuntu, а основанная на чистом Debian – LMDE (Linux Mint Debian Edition).',
                    attachment='photo-87865876_457239033',
                    keyboard=mint.get_keyboard()
                )
        elif event.text in vars19:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Здесь показан список дистрибутивов, основанных на Arch.\n\nДанная ветка дистрибутивов наиболее гибкая и имеет меньше всего сложностей с драйверами',
                    keyboard=arch.get_keyboard()
                )
        elif event.text in vars20:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Дистрибутив, основанный на Arch Linux, имеет простой графический инсталлятор и «предустановленное» графическое окружение. Стабильный, быстрый и простой. Оффициально испльзует оболочки XFCE, KDE Plasma и GNOME.',
                    attachment='photo-87865876_457239034',
                    keyboard=manjaro.get_keyboard()
                )
        elif event.text in vars21:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Archman — дистрибутив, основанный на ArchLinux. Прост в установке. Устанавливается с готовой к работе средой рабочего стола. Полностью совместим с ArchLinux. Оффициально испльзует оболочки KDE Plasma, Xfce, MATE, GNOME, Deepin Desktop, LXQt',
                    attachment='photo-87865876_457239035',
                    keyboard=manjaro.get_keyboard()
                )
        elif event.text in vars22:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Дистрибутив с мощной и гибкой технологией Portage, совмещающей в себе возможности конфигурирования и настройки, а также автоматизированную систему управления пакетами.Отличительной особенностью Gentoo является возможность оптимизации под конкретное аппаратное обеспечение.\n\nЗаработает на любом калькуляторе, но для того, чтобы собрать и установить Gentoo, вооружитесь Gentoo Handbook и запритесь в комнате со своим компьютером на пару дней.',
                    attachment='photo-87865876_457239036',
                    keyboard=gentoo.get_keyboard()
                )
        elif event.text in vars23:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Rufus\n\nМаксимально понянтая и простая утилита, но написана только для Windows.',
                    keyboard = rufus.get_keyboard()
                )
        elif event.text in vars24:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Ventoy\n\nРаботает как в Windows, так и в Linux. Добавляет на флешку загрузчик Grub, после чего на неё надо лишь закинуть нужный ISO файл, даже не распаковывая, можно указать отдельный объём диска который будет использоваться для хранения данных.',
                    keyboard = ventoy.get_keyboard()
                )
        elif event.text in vars25:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Здесь показаны основные комманды подходящие как для zsh так и для bash.',
                    keyboard = bash.get_keyboard()
                )






        else:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    message = 'Я пока так не умею 🥺',
                    random_id = get_random_id()
                    )
