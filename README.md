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
### Test Senaryoları

- ✔️ `POST /v2/user` - Kullanıcı oluşturma
- ✔️ `GET /v2/user/{username}` - Kullanıcıyı görüntüleme
- ✔️ `PUT /v2/user/{username}` - Kullanıcı güncelleme
- ✔️ `DELETE /v2/user/{username}` - Kullanıcı silme
- ✔️ `GET /v2/user/login?` - Kullanıcı giriş
-  ✔️ `GET /v2/user/logout` - Kullanıcı çıkış
- ✔️ `POST /v2/pet` - Pet oluşturma
- ✔️ `GET /v2/pet/{id}` - Pet görüntüleme
- ✔️ `PUT /v2/pet` - Pet güncelleme
- ✔️ `DELETE /v2/pet/{id}` - Pet silme

---

###Load Testleri (Locust)
 Test Kapsamı
- ✔️ `POST /v2/pet` - Pet oluşturma
- ✔️ `GET /v2/pet/{id}` - Pet görüntüleme
- ✔️ `PUT /v2/pet` - Pet güncelleme
- ✔️ `DELETE /v2/pet/{id}` - Pet silme


Yük testlerine ait belge locust-report/ klasörü altında sunulmuştur.
Bu belge, test süresince elde edilen performans verilerini detaylı bir şekilde göstermektedir.
