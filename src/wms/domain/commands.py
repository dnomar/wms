from dataclasses import dataclass
import datetime, time


class Command:
    pass


@dataclass
class CreateWarehouse(Command):
    reference: str






