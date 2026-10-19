import pytest
from app import app
from utils import calculate_discount, validate_item_data

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_get_items(client):
    response = client.get('/api/items')
    assert response.status_code == 200
    assert response.json['total'] == 2

def test_calculate_discount():
    assert calculate_discount(100, 20) == 80.0
    with pytest.raises(ValueError):
        calculate_discount(100, 150)

def test_validate_item_data():
    assert validate_item_data({"name": "Keyboard", "price": 500000}) is True
    assert validate_item_data({"name": "Keyboard"}) is False
