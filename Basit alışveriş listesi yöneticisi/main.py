def menu():
    print("\n*** Alışveriş Listesi ***")
    print("1. Listeyi Görüntüle")
    print("2. Ürün Ekle")
    print("3. Ürün Sil")
    print("4. Çıkış")

def listeyi_goruntule(liste):
    if not liste:
        print("Alışveriş listeniz boş.")
    else:
        print("\nAlışveriş Listeniz:")
        for i, urun in enumerate(liste, start=1):
            print(f"{i}. {urun}")

def urun_ekle(liste):
    urun = input("Eklemek istediğiniz ürünü girin: ")
    liste.append(urun)
    print(f"'{urun}' listeye eklendi.")

def urun_sil(liste):
    listeyi_goruntule(liste)
    if liste:
        try:
            secim = int(input("Silmek istediğiniz ürünün numarasını girin: "))
            if 1 <= secim <= len(liste):
                silinen = liste.pop(secim - 1)
                print(f"'{silinen}' listeden silindi.")
            else:
                print("Geçersiz numara.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

def main():
    alisveris_listesi = []
    while True:
        menu()
        secim = input("Seçiminiz: ")
        if secim == "1":
            listeyi_goruntule(alisveris_listesi)
        elif secim == "2":
            urun_ekle(alisveris_listesi)
        elif secim == "3":
            urun_sil(alisveris_listesi)
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()