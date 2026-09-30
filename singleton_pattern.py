class DatabaseConnection:
    _instance = None
    _connected = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def connect(self):
        if not self._connected:
            print("Connected to database")
            self._connected = True

a = DatabaseConnection()
b = DatabaseConnection()
a.connect()
b.connect()  # should NOT print again
print(a is b)  # True