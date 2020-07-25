from src.app.adapters.repository import AbstractRepository
from src.app.domain.model import Space


class FakeSpaceRepository(AbstractRepository):

    def __init__(self):
        self.spaces = []

    def add(self, space: Space):
        self.spaces.append(space)

    def get(self, reference: str):
        for sp in self.spaces:
            if reference == sp.ref:
                return sp

    def get_all(self):
        return self.spaces