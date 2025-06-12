
import allure
import pytest
import requests
from base.api.pet_api import PetAPI
from base.data import PetStoreURL

pet_api=PetAPI()

@allure.title("POST-/v2/pet-Create PetID")
def test_create_pet():
    body = {
        "id": 10,
        "category": {"id": 10, "name": "deneme"},
        "name": "deneme",
        "photoUrls": ["string"],
        "tags": [{"id": 10, "name": "deneme"}],
        "status": "available"
    }
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response= pet_api.create_pet(body,headers)
    with allure.step("status kod doğrulanıyor"):
     assert response.status_code==200

@allure.title("GET-/v2/pet/- Pet ID")
def test_get_id():
    response=pet_api.get_id()
    assert response.status_code==200

@allure.title("GET - /v2/pet/findByStatus- Pets by All Status ")
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets_by_status(status):
        response = pet_api.find_pets_by_status(status)
        with allure.step("status kod doğrulanıyor"):
         assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)
        assert len(pets) > 0
        for pet in pets:
            assert pet.get("status") == status

@allure.title("PUT- /v2/pet- Update")
def test_update_pet():
    body = {
        "id": 10,
        "category": {"id": 10, "name": "update1"},
        "name": "update1",
        "photoUrls": ["string"],
        "tags": [{"id": 10, "name": "update1"}],
        "status": "placed"
    }
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response= pet_api.update_pet(headers,body)
    with allure.step("status kod doğrulanıyor"):
     assert response.status_code==200

@allure.title("GET- Pet Control")
def test_pet_control():
    response=pet_api.get_id()
    with allure.step("status kod doğrulanıyor"):
     assert response.status_code==200
    data = response.json()
    assert data["name"] == "update1"
    assert data["status"] == "placed"

@allure.title("DELETE -/v2/pet/1-Delete Pet ID ")
def test_delete_id():
    response=pet_api.delete_pet()
    with allure.step("status kod doğrulanıyor"):
     assert response.status_code==200



