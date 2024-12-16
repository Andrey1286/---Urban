import time


class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"User: {self.nickname}, Password: {self.password}, Age: {self.age}"


class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title           # заголовок, строка
        self.duration = duration     # продолжительность, секунды
        self.time_now = 0            # секунда остановки
        self.adult_mode = adult_mode  # ограничение по возрасту

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title


class UrTube:
    def __init__(self, current_user=None):
        self.users = []               # список объектов User
        self.videos = []              # список объектов Video
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user and user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Добро пожаловать, {nickname}')
            else:
                print('Неверный логин или пароль')

    def register(self, nickname, password, age):
        nick_not_search = True
        for user in self.users:
            if user.nickname == nickname:
                nick_not_search = False
        if nick_not_search:
            self.users.append(User(nickname, password, age))
            print(f'Пользователь {nickname} зарегистрирован. Выполнен вход.')
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video in self.videos:
                print(f'Видео с названием: {video.title} существует')
            else:
                self.videos.append(video)

    def get_videos(self, search_term):
        list_on_request = []
        for video in self.videos:
            if search_term.lower() in video.title.lower():
                list_on_request.append(video.title)
        return list_on_request

    def watch_video(self, video_title):
        for video in self.videos:
            if video_title == video.title:
                if self.current_user != None:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет. Просмотр запрещен')
                    else:
                        current_time = 1
                        while current_time <= video.duration:
                            print(f'Проигрывание видео "{video.title}" ({current_time} секунда из {video.duration})')
                            time.sleep(1)
                            current_time += 1
                        print('Видео закончилось')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



# Добавление видео

ur.add(v1, v2)



# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')