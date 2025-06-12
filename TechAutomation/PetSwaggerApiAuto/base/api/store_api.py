import allure
import requests

from base.data import PetStoreURL


class StoreAPI:
    BASE_URL=PetStoreURL.url

    def create_order(self,headers,body):
        with allure.step(f"{self.BASE_URL} POST İSTEĞİ GÖNDERİLİR"):
         return requests.post(f"{self.BASE_URL}/v2/store/order",headers=headers,json=body)

    def get_order_id(self):
        with allure.step(f"{self.BASE_URL} GET İSTEĞİ GÖNDERİLİR"):
         return requests.get(f"{self.BASE_URL}/v2/store/order/1")

    def delete_order(self):
        with allure.step(f"{self.BASE_URL} DELETE İSTEĞİ GÖNDERİLİR"):
         return requests.delete(f"{self.BASE_URL}/v2/store/order/1")

    def get_inventory(self):
        with allure.step(f"{self.BASE_URL} GET İSTEĞİ GÖNDERİLİR"):
         return requests.get(f"{self.BASE_URL}/v2/store/inventory")
