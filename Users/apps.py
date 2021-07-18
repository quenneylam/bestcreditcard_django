from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'User_bcc '

    def ready(self):
        import Users.signals
