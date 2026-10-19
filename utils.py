def calculate_discount(price: float, discount_percent: float) -> float:
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Diskon harus di antara 0 dan 100")
    return price * (1 - discount_percent / 100)

def validate_item_data(data: dict) -> bool:
    return bool(data and "name" in data and "price" in data)
