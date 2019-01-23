# Yandex Translate API - Python - Console Uygulaması

Yandex Translate Api kullanılarak, internet bağlantısı aracılığıyla 
Türkçe - İngilizce çeviri yapan bir konsol uygulamasıdır. 

Python 3 kullanılarak yazılmıştır.

Temel olarak Kullanıcının istediği kelimeyle Yandex Translate Api'ye
uygun url oluşturulmuş. Çevirisi "request" modülü kullanarak, 
Yandex Translate Api'ye get request gönderilmiştir.
 Dönen bilgi json verisi verisi olarak işlenmiştir.

Programın bir bölümünde kullanılan "os" modülü; oluşacak son aramalar
dosyasının boyutuna göre boş olup olmadığını kontrol için kullanılmıştır.

Program çalıştırıldığı dizinde "last_searchs.txt" isimli bir dosya oluşturur. Son arananları
bu dosyaya kaydeder ve bu dosyadan okur. 

## Uygulamadan fotoğraflar

![Imgur](https://i.imgur.com/7tkJ2sj.png?1)    ![Imgur](https://i.imgur.com/LRuBYND.png?1)

![Imgur](https://i.imgur.com/FTVJgkf.png?1)    ![Imgur](https://i.imgur.com/2pSHNcY.png?1)

### Gereklilikler

Python 3 kurulu olması gerekli.

```
Python 3
```

### Yükleme

Eklentileri Yüklemek için.
```
pip install -r requirements.txt
```

Çalıştırmak için
```
python yta_c_prj.py
```

## Test Pyinstaller
Pyinstaller ile Windows 10 - 64 bit için derlediğim dosya
[https://github.com/demirtaserdem/yandex-translate-api-python-console/releases](https://github.com/demirtaserdem/yandex-translate-api-python-console/releases)
adresindedir.

Derleme işlemi   
```
pyinstaller.exe --onefile --icon=icon1.ico yta_c_prj.py
```
komutu kullanılarak yapılmıştır.

Derleme yapmak isteyenler.
```
pip install pyinstaller 
```
komutuyla pyinstaleri kurmalılar.

## Yandex Api Dökümantasyonu

[https://tech.yandex.com/translate/](https://tech.yandex.com/translate/)


