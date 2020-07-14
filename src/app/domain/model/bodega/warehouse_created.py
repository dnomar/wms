from dataclasses import dataclass
from src.app.domain.model.shared.event import Event

@dataclass
class WarehouseCreated(Event):
    id:str