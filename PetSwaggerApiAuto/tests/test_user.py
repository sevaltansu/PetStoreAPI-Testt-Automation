import allure
from base.api.user_api import UserAPI

user_api=UserAPI()

@allure.title("POST -/v2/user- Create User")
def test_create_user():
    body = dict()
    body["id"] = 1
    body["username"] = "sevaltansu"
    body["firstName"] = "seval"
    body["lastName"] = "tansu"
    body["email"] = "seval@gmail.com"
    body["password"] = "Deneme1"
    body["phone"] = "null"
    body["userStatus"] = 1

    headers=dict()
    headers["Content-Type"] = "application/json"
    headers["accept"]= "application/json"
    response=user_api.create_user(body,headers)
    with allure.step("status kod doğrulanıyor"):
        assert response.status_code == 200

@allure.title("GET -/v2/user/sevaltansu- Get User")
def test_get_user():
    response =user_api.get_user()
    assert response.status_code==200
    data=response.json()
    assert data["username"]=="sevaltansu"


@allure.title("PUT -/v2/user/sevaltansu- Update User")
@allure.description("Var olan bir kullanıcı güncelleniyor ")
def test_update_user():
    body = dict()
    body["id"] = 123444468888
    body["username"] = "sevaltansuu"
    body["firstName"] = "sevall"
    body["lastName"] = "tansuu"
    body["email"] = "seval@gmail.com"
    body["password"] = "Deneme1"
    body["phone"] = "0555555"
    body["userStatus"] = 1

    headers = dict()
    headers["Content-Type"] = "application/json"
    headers["accept"] = "application/json"
    response=user_api.update_user(body,headers)
    with allure.step("status kod doğrulanıyor"):
     assert response.status_code == 200

@allure.title("DELETE-/v2/user/sevaltansuu -Delete User ")
def test_delete_user():
    response=user_api.delete_user()
    with allure.step("status kod doğrulanıyor"):
     assert response.status_code == 200

@allure.title("GET -/v2/user/login- Login")
def test_login():
    params={
        "username":"sevaltansu",
        "password":"seval123"
    }
    response = user_api.login_user(params)
    with allure.step("status kod doğrulanıyor"):
     assert response.status_code==200

@allure.title("GET -/v2/user/logout- Logout")
def test_logout():
    response = user_api.logout_user()
    with allure.step("status kod doğrulanıyor"):
      assert response.status_code == 200

