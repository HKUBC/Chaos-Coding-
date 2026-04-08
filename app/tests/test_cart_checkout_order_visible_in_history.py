from fastapi.testclient import TestClient
from app.main import app
from app.services.order_service import repo as order_repo

client = TestClient(app)

def test_cart_checkout_order_visible_in_history():
    client.post("/cart/customer_hist/add", json={
        "item_id": "i1",
        "name": "Burger",
        "price": 9.99,
        "quantity": 1,
        "restaurant_id": "restaurant1"
    })
    checkout = client.post("/cart/customer_hist/checkout")
    assert checkout.status_code == 200
    order_id = checkout.json()["order_id"]

    # Verify the order landed in the shared session repo
    session_orders = order_repo.get_session_orders("customer_hist")
    ids = [o.order_id for o in session_orders]
    assert order_id in ids
