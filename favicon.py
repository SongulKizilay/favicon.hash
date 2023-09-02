import mmh3
import requests
import codecs

# Kullanıcıdan URL alınması
url = input("Lütfen bir URL girin: ")

try:
    # URL'den içerik çekilmesi
    response = requests.get(url)

    if response.status_code == 200:
        # İçeriğin base64'e kodlanması
        favicon = codecs.encode(response.content, "base64")
        # Favicon hash hesaplanması
        hash_value = mmh3.hash(favicon)
        print("Favicon Hash Değeri:", hash_value)
    else:
        print("URL'ye erişim sağlanamadı. HTTP kodu:", response.status_code)

except requests.exceptions.MissingSchema:
    print("Geçersiz URL formatı. Lütfen URL'yi doğru şekilde girin.")
except Exception as e:
    print("Bir hata oluştu:", str(e))
