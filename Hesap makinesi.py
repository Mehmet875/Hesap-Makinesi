print("Lütfen Doğru Bilgileri Giriniz")
defkullanici="1"
defparola="123"
while(True):
    kullanici = input("Kulllanıcı Adınız:")
    parola = input("Parolanız:")
    if ((defparola == parola) and (defkullanici == kullanici)):
        print("""
    ========================================================
    ========================================================


    SÜPER HESAP MAKİNESİ'NE HOŞGELDİN KULLANICI


    =========================================================
    =========================================================
    """)
        while (True):
            cevap = input("""
a:Parola Değiştirme
b:Kullanıcı Adı Değiştirme
1:Toplama
2:Çıkarma 
3:Çarpma 
4:Bölme
5:Üssünü Alma
6:Dikdörtgenin Alanını Bulma            
7:Dikdörtgenin Çevresi Bulma
8:Daire Alanı
9:Daire Çevresi
10:Karne Notu Hesaplama
11:Havuz Problemi
12:Faktoriyel Sorgulama
13:Kütle İndeksi Sorgulama
Lütfen Yapacağınız İşlemi Seçiniz:""")
            if((cevap=="a")or(cevap=="A")):
                mevcutpar=input("Mevcut Parolanız:")
                if(mevcutpar==defparola):
                    yenipar=input("Yeni parolanız:")
                    print("Parolanız Değiştiriliyor...")
                    yenipar=defparola
                    print("Parolanız Başarıyla Değiştirildi.")
                else:
                    print("Lütfen Mevcut Parolanızı Kontrol Ediniz.")
            elif((cevap=="b")or(cevap=="B")):
                mevcutkull=input("Mevcut Kullanıcı Adınız:")
                if(mevcutkull==defkullanici):
                    yenikull=input("Yeni Kullanıcı Adınız:")
                    print("Kullanıcı Adınız Değiştiriliyor...")
                    yenikull=defkullanici
                    print("Kullanıcı Adınız Başarıyla Değiştirildi.")
                else:
                    print("Lütfen Mevcut Kullanıcı Adınız Kontrol Ediniz.")
            elif (cevap == "1"):
                a = input("Birinci Sayıyı Giriniz:")
                b = input("İkinci Sayıyı Giriniz: ")
                sonuç = (int(a) + int(b))
                print("İşleminizin Sonucu", sonuç)
                input("Devam Etmek İçin Bi tuşa Basınız")
            elif (cevap == "2"):
                a = input("Çıkan Sayıyı Girin:")
                b = input("Çıkarılan Sayıyı Girin:")
                sonuç = (int(a) - int(b))
                print("İşleminizin Sonucu", sonuç)
                input("Devam Etmek İçin Bi tuşa Basınız")
            elif (cevap == "3"):
                a = input("Birinci Sayıyı Giriniz:")
                b = input("İkinci Sayıyı Giriniz: ")
                sonuç = (int(a) * int(b))
                print("İşleminizin Sonucu", sonuç)
                input("Devam Etmek İçin Bi tuşa Basınız")
            elif (cevap == "4"):
                a = input("Bölünen Sayıyı Giriniz:")
                b = input("Bölen Sayıyı Giriniz: ")
                sonuç = (int(a) / int(b))
                print("İşleminizin Sonucu", sonuç)
                input("Devam Etmek İçin Bi tuşa Basınız")
            elif (cevap == "5"):
                a = input("Tabanı Giriniz:")
                b = input("Üssü Giriniz: ")
                sonuç = (int(a) ** int(b))
                print("İşleminizin Sonucu", sonuç)
                input("Devam Etmek İçin Bi tuşa Basınız")
            elif (cevap == "6"):
                kisa = input('Kısa Kenar : ')
                uzun = input('Uzun Kenar : ')
                alan = int(kisa) * int(uzun)
                print("Alan : {0}".format(alan))
                input("Devam Etmek İçin Bi tuşa Basınız")
            elif (cevap == "7"):
                kisa = input('Kısa Kenar : ')
                uzun = input('Uzun Kenar : ')
                cevre = 2 * (int(kisa) + int(uzun))
                print("Çevre : {0}".format(cevre))
                input("Devam Etmek İçin Bi tuşa Basınız")
            elif (cevap == "8"):
                while (True):
                    yaricap = input("Yarıçapı Giriniz:")
                    pi = input("Pi değerini giriniz:")
                    if (pi == "3"):
                        cevap = (2 * int(pi) * int(yaricap))
                        print("Çemberinizin Çevresi:", cevap)
                        input("Devam Etmek İçin Bi tuşa Basınız")
                        break
                    elif (pi == "3,14"):
                        cevap = (2 * int(pi) * int(yaricap))
                        print("Çemberinizin Çevresi:", cevap)
                        input("Devam Etmek İçin Bi tuşa Basınız")
                        break
                    else:
                        print("Lütfen Doğru Bir Değer Giriniz:")
            elif (cevap == "9"):
                while (True):
                    yaricap = input("Yarıçapı Giriniz:")
                    pi = input("Pi değerini giriniz:")
                    if (pi == 3):
                        cevap = (2 * int(pi) * int(yaricap) * int(yaricap))
                        print("Çemberinizin Alanı:", cevap)
                        input("Devam Etmek İçin Bi tuşa Basınız")
                        break
                    elif (pi == 3, 14):
                        cevap = (2 * int(pi) * int(yaricap) * int(yaricap))
                        print("Çemberinizin Alanı:", cevap)
                        input("Devam Etmek İçin Bi tuşa Basınız")
                        break
                    else:
                        print("Lütfen Doğru Bir Değer Giriniz:")
            elif (cevap == "10"):
                t1 = input("Türkçe 1. Yazılıyı giriniz:")
                t2 = input("Türkçe 2. Yazılıyı giriniz:")
                to = (int(t1 + t2) / 2)
                m1 = input("Matematik 1. Yazılıyı giriniz:")
                m2 = input("Matematik 2. Yazılıyı giriniz:")
                mo = (int(m1 + m2) / 2)
                s1 = input("Sosyal 1. Yazılıyı giriniz:")
                s2 = input("Sosyal 2. Yazılıyı giriniz:")
                so = (int(s1 + s2) / 2)
                i1 = input("İngilizce 1. Yazılıyı giriniz:")
                i2 = input("İngilizce 2. Yazılıyı giriniz:")
                io = (int(i1 + i2) / 2)
                b1 = input("Beden Eğitimi 1. Yazılıyı giriniz:")
                b2 = input("Beden Eğitimi 2. Yazılıyı giriniz:")
                bo = (int(b1 + b2) / 2)
                M1 = input("Müzik 1. Yazılıyı giriniz:")
                M2 = input("Müzik 2. Yazılıyı giriniz:")
                Mo = (int(M1 + M2) / 2)
                d1 = input("Din Kültürü ve Ahlak Bilgisi 1. Yazılıyı giriniz:")
                d2 = input("Din Kültürü ve Ahlak Bilgisi 2. Yazılıyı giriniz:")
                do = (int(d1 + d2) / 2)
                f1 = input("Fen ve Teknoloji 1. Yazılıyı giriniz:")
                f2 = input("Fen ve Teknoloji 2. Yazılıyı giriniz:")
                fo = (int(f1 + f2) / 2)
                B1 = input("Bilim Uygulamaları 1. Yazılıyı giriniz:")
                B2 = input("Bilim uygulamaları 2. Yazılıyı giriniz:")
                Bo = (int(B1 + B2) / 2)
                T1 = input("Teknoloji Tasarım 1. Yazılıyı giriniz:")
                T2 = input("Teknoloji Tasarım 2. Yazılıyı giriniz:")
                To = (int(T1 + T2) / 2)
                ko = (int(to + Bo + bo + fo + do + Mo + mo + io + so + To) / 10)
                ko=ğ
                if (ğ >= 85):
                    t = "Takdir"
                elif (ğ >= 65):
                    t = "Teşekkür"
                else:
                    t = "Düz"
                print("Karne Notunuz:" + ko + "" + "Karne Belgeniz" + t)
                ort = ko
                if (int(ort) >= 50):
                    print("Geçtiniz")
                else:
                    print("Kaldınız")
            elif (cevap == "11"):
                musluksay = input("Musluk Sayısı:")
                saat = input("Bir Musluk Bir Havuzu Kaç Saatde Dolduruyor:")
                cevap = (1 * int(saat) / int(musluksay))
                print("İşleminizin Sonucu", cevap)
                input("Devam Etmek İçin Bi tuşa Basınız")
            elif (cevap=="12"):
                faktoriyel = 1
                while (True):
                    sayi = int(input("Faktöriyelini Öğrenmek İstediğiniz Sayıyı Giriniz:"))
                    if (sayi <= 0):
                        print("Lütfen Pozitif Bir Sayı Giriniz")
                    else:
                        for i in range(1, sayi + 1):
                            faktoriyel *= i
                        print("Faktoriyeliniz:", faktoriyel)
                        input("Devam Etmek İçin Bi tuşa Basınız")
                        break
            elif(cevap=="13"):
                boy=int(input("Boyunuzu giriniz(cm cinsinden): "))
                kilo=float(input("kilonuzu giriniz: "))
                vki=kilo/((boy/100)**2)
                print("Vücut kitle index'iniz {}".format(round(vki,2)))
                print("Durumunuz: ")
                if vki <=18.5:
                    print("Zayıf")
                    print("{} kilogram almanız gerekiyor".format(round(18.5*((boy/100)**2)-kilo,2)))
                    input("Devam Etmek İçin Bi tuşa Basınız")
                elif vki <=24.9:
                    print("Normal")
                elif vki<=29.9:
                    print("Fazla kilolu")
                    print("{} kilogram vermeniz gerekiyor".format(round(kilo-24.9*((boy / 100) ** 2)),2))
                    input("Devam Etmek İçin Bi tuşa Basınız")
                elif vki<=39.9:
                    print("Obez")
                    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
                    input("Devam Etmek İçin Bi tuşa Basınız")
                else:
                    print("Aşırı obez")
                    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
                    input("Devam Etmek İçin Bi tuşa Basınız")
            else:
                print("Lütfen Doğru Sayıyı Giriniz")
    elif ((defparola != parola) and (defkullanici == kullanici)):
        print("Parolanız yanlış ")
        devam=input("Değiştirmek istermisinz? (E/H)")
        if((devam=="e")or(devam=="E")):
            yenipar=input("Yeni parolanız:")
            print("Parolanız Değiştiriliyor...")
            yenipar=defparola
            print("Parolanız Başarıyla Değiştirildi.")
        elif((devam=="h")or(devam=="H")):
            break
    elif ((defparola == parola) and (defkullanici != kullanici)):
        print("Kulllanıcı Adınız yanlış ")
        devam=input("Değiştirmek istermisinz? (E/H)")
        if((devam=="e")or(devam=="E")):
            yenikull=input("Yeni KUllanıcı Adınız:")
            print("Kullanıcı Adınız Değiştiriliyor...")
            yenikull=defkullanici
            print("Kullanıcı Adınız Başarıyla Değiştirildi.")
        elif((devam=="h")or(devam=="H")):
            break
    else:
        print("Lütfen girdiniz bilgileri kontrol ediniz")