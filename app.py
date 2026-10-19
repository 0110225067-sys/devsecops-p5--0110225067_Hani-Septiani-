import os
from flask import Flask, jsonify, request
from config import Config
from models import Item
from utils import calculate_discount, validate_item_data

app = Flask(__name__)
app.config.from_object(Config)

items_db = [
    Item(1, "Laptop", 15000000.0).to_dict(),
    Item(2, "Mouse", 250000.0).to_dict()
]

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "DevSecOps Demo API"}), 200

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({"data": items_db, "total": len(items_db)}), 200

@app.route('/api/items/discount', methods=['POST'])
def get_discounted_price():
    data = request.get_json()
    if not data or 'price' not in data or 'discount' not in data:
        return jsonify({"error": "Data tidak valid"}), 400
    
    try:
        final_price = calculate_discount(data['price'], data['discount'])
        return jsonify({"original_price": data['price'], "final_price": final_price}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Membaca host dan port dari environment, dengan default localhost (127.0.0.1)
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
