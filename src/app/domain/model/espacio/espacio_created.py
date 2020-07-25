from dataclasses import dataclass
from src.app.domain.model.shared.event import Event

class EspacioCreated(Event):
    name:str