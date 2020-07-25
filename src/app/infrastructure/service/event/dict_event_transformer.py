from src.app.domain.model.shared.event import Event
import json


class DictEventTransformer:

    def __init__(self, event:Event):
        self._event=event
        self._dict_event={}

    def toDict(self):
        self._dict_event["evento"]=self._event.event_name
        self._dict_event["body"]={
                "evento":self._event.event_name,
                "id":self._event.id,
                "timestamp":self._event.occurred_on
            }
        return self._dict_event

    def toJson(self):
        return json.dumps(self.toDict())
        
        

