class QBETError(Exception):
    def __init__(self, message, line=None):
        self.message = message
        self.line = line
        super().__init__(self.message)

    def __str__(self):
        if self.line:
            return f"Line {self.line}: {self.message}"
        return self.message
class NameError(QBETError):
    def __init__(self, name, line=None):
        super().__init__(f"Name '{name}' is not manifested in this reality.", line)
