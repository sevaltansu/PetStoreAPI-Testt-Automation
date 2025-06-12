import allure

from base.api.store_api import StoreAPI

store_api=StoreAPI()

@allure.title("POST- /v2/store/order- Create Order")
def test_create_order():
    body=  {
        "id": 1,
        "petId": 1,
        "quantity": 10,
        "shipDate": "2025-05-30T13:58:54.647Z",
        "status": "available",
        "complete": "true"
    }
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response=store_api.create_order(headers,body)
    assert response.status_code==200

@allure.title("GET- /v2/store/order/1- GET Order")
def test_get_order_id():
    response=store_api.get_order_id()
    assert response.status_code==200
    data=response.json()
    assert data["id"]==1
    assert data["petId"]== 1
    assert data["status"]=="available"

@allure.title("DELETE- /v2/store/order/1- DELETE Order")
def test_delete_order():
    response=store_api.delete_order()
    assert response.status_code==200

@allure.title("GET- /v2/store/order/1- Control Order")
@allure.description("Silinen order hala duruyorsa yazdır")
def test_order_id_control():
    response=store_api.get_order_id()
    data=response.json()
    print(data)
    assert response.status_code==404

@allure.title("GET- /v2/store/inventory- GET Inventory")
def test_get_inventory():
    response=store_api.get_inventory()
    assert response.status_code==200
