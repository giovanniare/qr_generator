class NoUrl(Exception):
    def __init__(self, message="Por favor introduce una url para poder generar el codigo QR") -> None:
        self.message = message
        super().__init__(self.message)


class NoName(Exception):
    def __init__(self, message="Por favor introduce una nombre para guradar el codigo QR como img") -> None:
        self.message = message
        super().__init__(self.message)


class NoLogo(Exception):
    def __init__(self, message="Por favor introduce tu logo.") -> None:
        self.message = message
        super().__init__(self.message)
