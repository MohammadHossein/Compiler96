from tabnanny import errprint


class ErrorHandler:
    def __init__(self):
        pass

    @staticmethod
    def error(self, message):
        errprint(message)
