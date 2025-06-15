# Petstore API Test Otomasyonu Projesi

Bu proje, [Swagger Petstore API](https://petstore.swagger.io/) üzerinde temel CRUD işlemleri için otomatik test senaryoları oluşturarak gerçekleştirilmiştir.  
Ayrıca aynı API'ye yönelik **yük testleri** de yapılmıştır.

---

##  Kullanılan Teknolojiler ve Araçlar

- ✅ Python
- ✅ Pytest
- ✅ Allure Reporting
- ✅ Locust (Load Testing)
- ✅ Postman

---

##  Test Senaryoları

-POST /v2/user → Yeni kullanıcı oluşturma
-GET /v2/user/{username} → Kullanıcı bilgilerini getirme
-PUT /v2/user/{username} → Kullanıcı bilgilerini güncelleme
-DELETE /v2/user/{username} → Kullanıcı silme
-GET /v2/user/login → Kullanıcı girişi
-GET /v2/user/logout → Kullanıcı çıkışı
-POST /v2/pet → Pet oluşturma
-GET /v2/pet/{id} → Pet bilgisi görüntüleme
-PUT /v2/pet → Pet güncelleme
-DELETE /v2/pet/{id} → Pet silme
 ---

 Allure raporları, allure-report/ klasörü altında HTML formatında sunulmuştur. Her test adımı ve sonucu detaylı biçimde yer almaktadır.

## Load Testleri (Locust)
 Test Kapsamı
- ✔️ `POST /v2/pet` - Pet oluşturma
- ✔️ `GET /v2/pet/{id}` - Pet görüntüleme
- ✔️ `PUT /v2/pet` - Pet güncelleme
- ✔️ `DELETE /v2/pet/{id}` - Pet silme


Yük testlerine ait belge locust-report/ klasörü altında sunulmuştur.
Bu belge, test süresince elde edilen performans verilerini detaylı bir şekilde göstermektedir.
