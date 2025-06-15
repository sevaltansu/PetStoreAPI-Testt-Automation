import allure
import requests

from base.data import PetStoreURL


class UserAPI:
    BASE_URL=PetStoreURL.url

    def create_user(self,body,headers):
        with allure.step(f"{self.BASE_URL} POST İSTEĞİ GÖNDERİLİR"):
          return requests.post(f"{self.BASE_URL}/v2/user",json=body,headers=headers)

    def get_user(self):
        with allure.step(f"{self.BASE_URL} GET İSTEĞİ GÖNDERİLİR"):
          return requests.get(f"{self.BASE_URL}/v2/user/sevaltansu")

    def update_user(self,body,headers):
        with allure.step(f"{self.BASE_URL} PUT İSTEĞİ GÖNDERİLİR"):
         return requests.put(f"{self.BASE_URL}/v2/user/sevaltansu",json=body,headers=headers)

    def delete_user(self):
        with allure.step(f"{self.BASE_URL} DELETE İSTEĞİ GÖNDERİLİR"):
          return requests.delete(f"{self.BASE_URL}/v2/user/sevaltansuu")

    def login_user(self,params):
        with allure.step(f"{self.BASE_URL} GET İSTEĞİ GÖNDERİLİR"):
            return requests.get(f"{self.BASE_URL}/v2/user/login",params=params)

    def logout_user(self):
        with allure.step(f"{self.BASE_URL} GET İSTEĞİ GÖNDERİLİR"):
            return requests.get(f"{self.BASE_URL}/v2/user/logout")