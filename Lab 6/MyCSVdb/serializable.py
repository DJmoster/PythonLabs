
class Serializable:

    @staticmethod
    def convert_single(obj_class, data: dict):
        obj = obj_class()
        obj.deserialize(data)

        return obj

    @staticmethod
    def convert(obj_class, data: list[dict]) -> list:
        res = []
        for i in data:
            obj = obj_class()
            obj.deserialize(i)
            res.append(obj)

        return res

    def serialize(self) -> dict:
        return self.__dict__

    def deserialize(self, data: dict):
        self.__dict__.update(data)
