class Item:
    def __init__(self, item_id: int, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "id": self.item_id,
            "name": self.name,
            "price": self.price
        }
