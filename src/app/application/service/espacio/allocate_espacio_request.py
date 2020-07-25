class AllocateEspacioRequest:

    def __init__(self, wh_id, space_name, max_volume, max_weight):
        self._wh_id = wh_id
        self._space_name = space_name
        self._max_volume = max_volume
        self._max_weight = max_weight

    def get_wh_id(self):
        return self._wh_id
    
    def get_space_name(self):
        return self._space_name
    
    def get_max_volume(self):
        return self._max_volume

    def get_max_weight(self):
        return self._max_weight
