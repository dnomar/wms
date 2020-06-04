class singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print(f"Dentre a la instancia {self._instance}")




if __name__=="__main__":
    a = singleton()
    print(a)
    b = singleton()
    print(b)