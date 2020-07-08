class FakeSession:

    def __init__(self):
        self._commited = False

    def commit(self):
        self._commited = True
        return self._commited

    def rollback(self):
        pass