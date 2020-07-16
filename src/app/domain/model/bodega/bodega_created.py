from dataclasses import dataclass
from src.app.domain.model.shared.event import Event

@dataclass
class BodegaCreated(Event):
    id:str