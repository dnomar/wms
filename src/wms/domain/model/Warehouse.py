from src.wms.domain.model import Space
from src.wms.domain.model.Exeptions import NotEmpty, EmptyWarehouseReference


class Warehouse:

    def __init__(self, wh_reference: str):
        self._wh_ref = wh_reference
        self.allocated_spaces = []

    def add_space(self, space: Space):
        space.space_assigned()
        self.allocated_spaces.append(space)

    def get_space(self, space_reference: str) -> Space:
        for space in self.allocated_spaces:
            if space_reference == space.ref:
                return space

    def delete_space(self, space_reference: str):
        for space in self.allocated_spaces:
            if not space.list_prod():
                self.allocated_spaces.remove(space_reference)
            else:
                raise NotEmpty(f"Espacio {space.ref} no esta vacio")

    def list_allocated_spaces(self):
        return self.allocated_spaces

    def get_warehouse_ref(self):
        return self._wh_ref

    def change_warehouse_ref(self, new_reference_str: str):
        if not new_reference_str.strip():
            raise EmptyWarehouseReference()
        self._wh_ref = new_reference_str