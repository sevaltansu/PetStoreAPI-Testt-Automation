from locust import task,HttpUser, between



class UserLoadTest(HttpUser):
    wait_time = between(1,2)

    @task
    def create_pet(self):
        body = dict()
        body["id"] = 1
        body["username"] = "sevaltansu"
        body["firstName"] = "seval"
        body["lastName"] = "tansu"
        body["email"] = "seval@gmail.com"
        body["password"] = "Deneme1"
        body["phone"] = "null"
        body["userStatus"] = 1
        headers = dict()
        headers["Content-Type"] = "application/json"
        headers["accept"] = "application/json"
        self.client.post("/v2/user",headers=headers,json=body)

    @task
    def get_user(self):
        self.client.get("/v2/user/sevaltansu")

    @task
    def update_user(self):
        body = dict()
        body["id"] = 123444468888
        body["username"] = "sevaltansuu"
        body["firstName"] = "sevall"
        body["lastName"] = "tansuu"
        body["email"] = "seval@gmail.com"
        body["password"] = "Deneme1"
        body["phone"] = "0555555"
        body["userStatus"] = 1
        headers=dict()
        headers["Content-Type"] = "application/json"
        headers["accept"] = "application/json"
        self.client.put("/v2/user/sevaltansu",headers=headers,json=body)

    @task
    def delete_user(self):
        self.client.delete("/v2/user/sevaltansu")

    @task
    def login_user(self):
        params = {
            "username": "sevaltansu",
            "password": "seval123"
        }
        self.client.get("/v2/user/login",params=params)

    @task
    def logout_user(self):
        self.client.get("/v2/user/logout")

