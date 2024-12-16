import time


class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"User: {self.nickname}, Password: {self.password}, Age: {self.age}"


class Video:
    def __init__(self, title: str, duration: int):
        self.title = title           # заголовок, строка
        self.duration = duration     # продолжительность, секунды
        self.time_now = 0            # секунда остановки
        self.adult_mode = False      # ограничение по возрасту

    def __str__(self):
        return f'Video: {self.title}, duration: {self.duration}'


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
        for user in self.users:
            if nickname in self.users:
                print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User.__str__())
            self.current_user = self.users
            print(f'Пользователь {nickname} зарегистрирован. Выполнен вход.')

    def log_out(self):
        self.current_user = None

    def add(self, *args: Video):
        for arg in args:
            if arg.title in self.videos:
                continue
            else:
                self.videos.append(arg)

    def get_videos(self, search_term):
        list_on_request = []
        for i in self.videos:
            if search_term.lower() in 'i'.lower():
                list_on_request.append(i)
        return list_on_request

    def watch_video(self, video_title):
        self.register()
        if self.current_user:
            if video_title in self.videos:
                if video_title.adult_mode and User(age) >= 18 or self.video.adult_mode is False:
                    print(Video.duration)
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу.')
            else:
                print('Видео не найдено. Попробуйте повторить запрос.')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео.')
        print('Конец видео.')


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