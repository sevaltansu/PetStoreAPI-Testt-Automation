import allure
import requests

from base.data import PetStoreURL


class PetAPI:
    BASE_URL=PetStoreURL.url

    def create_pet(self,body,headers):
        with allure.step(f"{self.BASE_URL} POST İSTEĞİ GÖNDERİLİR"):
          return requests.post(f"{self.BASE_URL}/v2/pet",json=body,headers=headers)

    def get_id(self):
        with allure.step(f"{self.BASE_URL} GET İSTEĞİ GÖNDERİLİR"):
          return requests.get(f"{self.BASE_URL}/v2/pet/10")

    def find_pets_by_status(self,status):
        with allure.step(f"{self.BASE_URL} GET İSTEĞİ GÖNDERİLİR"):
         return requests.get(f"{self.BASE_URL}/v2/pet/findByStatus", params={"status": status})

    def update_pet(self,headers,body):
        with allure.step(f"{self.BASE_URL} PUT İSTEĞİ GÖNDERİLİR"):
         return requests.put(f"{self.BASE_URL}/v2/pet",headers=headers,json=body)

    def delete_pet(self):
        with allure.step(f"{self.BASE_URL} DELETE İSTEĞİ GÖNDERİLİR"):
         return requests.delete(f"{self.BASE_URL}/v2/pet/10")