import math

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Bölme işleminde payda sıfır olamaz!"
    return a / b

def karekok(a):
    return math.sqrt(a)

def us_alma(a, b):
    return math.pow(a, b)

def faktoriyel(a):
    return math.factorial(a)

def trigonometrik_fonksiyonlar():
    print("1. Sinüs")
    print("2. Kosinüs")
    print("3. Tanjant")
    secim = input("Bir seçenek girin (1/2/3): ")
    aci = float(input("Açıyı derece cinsinden girin: "))
    aci_radyan = math.radians(aci)
    
    if secim == '1':
        return math.sin(aci_radyan)
    elif secim == '2':
        return math.cos(aci_radyan)
    elif secim == '3':
        return math.tan(aci_radyan)
    else:
        return "Geçersiz seçenek!"

def hesap_makinesi():
    print("Gelişmiş Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Kare Kök")
    print("6. Üs Alma")
    print("7. Faktöriyel")
    print("8. Trigonometrik Fonksiyonlar")
    
    while True:
        secim = input("Bir seçenek girin (1/2/3/4/5/6/7/8) veya çıkmak için 'q': ")
        
        if secim == 'q':
            print("Hesap makinesi kapatılıyor...")
            break
        
        if secim in ['1', '2', '3', '4', '6']:
            num1 = float(input("Birinci sayıyı girin: "))
            num2 = float(input("İkinci sayıyı girin: "))
        
        if secim == '1':
            print(f"Sonuç: {toplama(num1, num2)}")
        elif secim == '2':
            print(f"Sonuç: {cikarma(num1, num2)}")
        elif secim == '3':
            print(f"Sonuç: {carpma(num1, num2)}")
        elif secim == '4':
            print(f"Sonuç: {bolme(num1, num2)}")
        elif secim == '5':
            num = float(input("Sayiyi girin: "))
            print(f"Sonuç: {karekok(num)}")
        elif secim == '6':
            print(f"Sonuç: {us_alma(num1, num2)}")
        elif secim == '7':
            num = int(input("Sayiyi girin: "))
            print(f"Sonuç: {faktoriyel(num)}")
        elif secim == '8':
            print(f"Sonuç: {trigonometrik_fonksiyonlar()}")
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

hesap_makinesi()
