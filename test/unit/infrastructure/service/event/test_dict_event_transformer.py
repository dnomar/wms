from src.app.infrastructure.service.event.dict_event_transformer import DictEventTransformer
from src.app.domain.model.bodega.warehouse_created import WarehouseCreated
import json

def test_dict_event_transformer_return_the_right_dto_structure():

    #setup
    test_event=WarehouseCreated(id="id-1")

    #testing_case
    dict_event=DictEventTransformer(test_event).toDict()

    #expexted data
    expected_data={
        "evento":test_event.event_name,
        "body":{
            "evento":test_event.event_name,
            "timestamp":test_event.occurred_on,
            "id":"id-1"
        }
    }

    assert dict_event==expected_data

def test_dict_event_transformer_return_the_right_json_structure():

    #setup
    test_event=WarehouseCreated(id="id-1")

    #testing_case
    json_event=DictEventTransformer(test_event).toJson()

    #expexted data
    expected_data={
        "evento":test_event.event_name,
        "body":{
            "evento":test_event.event_name,
            "id":"id-1",
            "timestamp":test_event.occurred_on

        }
    }

    assert json_event == json.dumps(expected_data)
