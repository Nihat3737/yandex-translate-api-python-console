
#Yandex Apiden çeviri bilgilerini alabilmek için eklendi.
import requests

# Son arananlar dosyasının (last_searchs.txt) boyutuna bakarak boş
# olup olmadığını kontol için  eklendi.
import os		

#Yandex Apide Çeviri Url İsteğni oluşturmak için kısımlara ayrıldı.
#"https://tech.yandex.com/translate/doc/dg/reference/
# translate-docpage/JSON"
#temel alınarak oluşturulmuştur.
#Url'nin ilk değişmeeyen kısmı
base_url ="https://translate.yandex.net/api/v1.5/tr.json/translate"
# Api key yandex translate tarafından alınacak.
# "https://translate.yandex.com/developers/keys"
key = "?key=trnsl.1.1.20190121T100542Z.4befbb4bba198843.b6081dd6370342a5c61258dbb83fb7b9a58dd523"
#arama yapacağımız kelime - metindir. ilk url oluşturulurken amaçsız
#"Merhaba" yazılmıştır, text = Str() oluşturulabilir.
text = "Merhaba"
#url'nin devamı kullanılan bir sabit
base_text = "&text="
#Çevirilmesi istenen dil değişkeni
lang = "en" 
#tr- kısmı çevrinmesi istenen dilin otomatik algılamasını kapatıp
#türkçeden çeviri yapılmasını sağlıyor. örn. "&lang=tr-eng" ya da
# otomatik: "&lang=eng" olarak yazılabilir.
base_lang = "&lang=tr-"
#oluşan temel url
translate_url = base_url + key+base_lang + lang + base_text + text  
#####-----#####

def clean_Last_Searched():
	"""last_searchs.txt dosyasının temizlenmesinde ve oluşturulmasını
	sağlar
	"""
	open("last_searchs.txt","w",encoding = "utf-8").close()
	
def selections_list():
	"""Seçim Listesidir
	"""
	print(
	"""
	*************************
	Çeviri Uygulaması

	1. Çeviri Yap. 

	2. Son Arananları göster.

	3. Son Arananları temizle.

	Çıkmak İçin 'q' ya basın
	*************************
	
	"""
	)  

def translateFunc(translate_url):
	"""Oluşturulan url'ye istek gönderir, alır, json objesine çevirir
	json objesinin içinden ilgili kısmı dataya yazar. Çevriyi Str 
	olarak döndürür.
	"""
	data_get = requests.get(translate_url)
	data_json = data_get.json()
	data = data_json["text"][0]
	return data


def writeLastSearch(text,translated_word):
	"""Çevrilen ve çeviri kelimeyi str olarak alır,
	last_searchs.txt dosyasına yazar konsola yazabiliyorsa yazar, 
	utf-8 hatasından - çince vs hata olursa hata mesajı verir.
	"""
	with open("last_searchs.txt","a",encoding = "utf-8") as file:
		file.write(text +" --->>> "+ translated_word + "\n")
	try:
		print(text + " --->>> " + translated_word + "\n")
	except:
		print("""Konsola yazdırırken hata oluştu... txt dosyasını 
			kontrol edebilirsiniz. \n""")

def printLastSearch():
	"""Son Arananların listesini
	last_searchs.txt den alır. yazdırır
	"""
	with open("last_searchs.txt","r",encoding = "utf-8") as file:
		print("*"*25)
		print(file.read())
		print("*"*25)

def clean_sure_question():
	"""Son Arananlar silinsin mi evet hayır seçeneği istiyor.
	girdiyi küçültüp temizleyip kontrol ediyor true veya false 
	dönüyor
	"""
	while True:
		intext = "Son arananlar silinecek emin misiniz? [Y/n]: "
		inputtemp = input(intext).lower().strip()
		if inputtemp == "y" or inputtemp == "yes":
			return True
		elif inputtemp == "n" or inputtemp == "no":
			return False
		else:
			print("Geçerli bir seçenek giriniz: ")



#Program Başlangıcı
#listeyi Ekrana bastırıyor.
selections_list()
#last_search dosyası oluşturuyor. ya da oluşmuş varsa siliyor.
clean_Last_Searched()

while True:
#Ana Döngü Seçeneklerden oluşuyor
	selection = input("Seçeneği Giriniz: ")
		
	if selection == "1":
		print("Çıkmak için 'q' tuşuna basınız. \n")
		while True:
		#q tuşuna basıncaya kadar sürekli kelime istiyor.
			#kelimeyi aldık küçülttük
			word = str(input("Kelimeyi Giriniz: ")).lower()
			try:
				#kelime q ise döngüden çıkıp listeyi tekrar yazdırdık.
				if word == "q":
					selections_list()
					break
				else:
					#kelime tam geldiyse urlyi oluşturduk
					text = word
					translate_url = (base_url + key + base_lang + lang
						+ base_text + text)
					#çeviriyi yaptık
					translated_word = translateFunc(translate_url)
					#Yazdırma kısmını çalıştırdık.
					writeLastSearch(word,translated_word)
			except:
				print("Hatalı kelime girişi - tekrar giriniz... \n")

	elif selection == "2":
			if os.stat("last_searchs.txt").st_size == 0:
				print("Son Aranan Kemlime Bulunmamaktadır. \n")
			else: 
				printLastSearch()    

	elif selection == "3":
		if clean_sure_question():
			clean_Last_Searched()
			print("Son aramalar temizlendi.\n")
		else:
			print("Son aramalar temizlenemedi!!!.\n")
		
	elif selection == "q":
		break

