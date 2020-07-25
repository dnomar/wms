import uuid

class BodegaId:

    @staticmethod
    def next_identity():
        return str(uuid.uuid1())


