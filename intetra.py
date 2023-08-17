class Product:
    def __init__(self, name):
        self.name = name
        self.ingredients = {}

    def add_ingredient(self, ingredient, quantity):
        self.ingredients[ingredient] = quantity

    def display_recipe(self):
        print(f"Ürün: {self.name}")
        print("Malzemeler:")
        for ingredient, quantity in self.ingredients.items():
            print(f"{ingredient}: {quantity} birim")
vms_hazır_modul= Product("vms modul")
vms_hazır_modul.add_ingredient("HAZIR MODÜL PANEL VMS ALM (P10) DÜZ 1972X844mm", 87)
vms_hazır_modul.add_ingredient("VİDA INOX A2 YSB  M4 L10", 31320)
vms_hazır_modul.add_ingredient("HPUL INOX A2  M4", 31320)
vms_hazır_modul.add_ingredient("YAYLI RONDELA INOX A2  M4", 31320)
vms_hazır_modul.add_ingredient("ÇAKMA SOMUN BSOS M5 L20", 870)


vms_sag_kapi = Product("vms sağ kapı")

vms_sag_kapi.add_ingredient("KAPI VMS ALM SAĞ 830X935mm"	, 87) 
vms_sag_kapi.add_ingredient("FAN YUVASI ALM 214X200mm"	, 87)  	 
vms_sag_kapi.add_ingredient("FİLTRE YUVASI ALM 214X200mm"	, 87)
vms_sag_kapi.add_ingredient("SİLİNDİRLİ KİLİT METAL 063-1-1-01-47"	, 87)
vms_sag_kapi.add_ingredient("ÇEYREK DÖNÜŞLÜ YAYLI KİLİT (MEKANİK) METAL Q30 060-1-1-15-47"	, 174) 	 
vms_sag_kapi.add_ingredient("ÇAKMA CIVATA FAST M5 L15"	, 2001) 	 
vms_sag_kapi.add_ingredient("ÇAKMA CIVATA FAST M6 L15"	, 261) 	 
vms_sag_kapi.add_ingredient("ÇAKMA CIVATA FAST M6 L25"	, 522) 	 
vms_sag_kapi.add_ingredient("SOMUN AKB INOX A2 M5"	, 1566) 	 
vms_sag_kapi.add_ingredient("YAYLI RONDELA INOX A2  M5"	, 1566) 	 
vms_sag_kapi.add_ingredient("PUL INOX A2  M5"	, 1566) 	
vms_sag_kapi.add_ingredient("sOMUN PERÇİN INOX ALTIGEN GÖVDE, SIFIR KAFA M4 ARKASI AÇIK"	, 696) 	 



def main():
    products = [vms_hazır_modul, vms_sag_kapi]

    while True:
        print("1. Ürün Ekle")
        print("2. Ürün Reçetesi Ekle")
        print("3. Reçeteyi Görüntüle")
        print("4. Çıkış")
        choice = int(input("Seçim yapınız: "))

        if choice == 1:
            product_name = input("Ürün adı: ")
            product = Product(product_name)
            products.append(product)
            print(f"{product_name} ürünü eklendi.")
        elif choice == 2:
            product_name = input("Ürün adı: ")
            product = next((p for p in products if p.name == product_name), None)
            if product:
                ingredient = input("Malzeme adı: ")
                quantity = int(input("Miktar: "))
                product.add_ingredient(ingredient, quantity)
                print(f"{ingredient} malzemesi {product_name} ürün reçetesine eklendi.")
            else:
                print(f"{product_name} ürünü bulunamadı.")
        elif choice == 3:
            product_name = input("Ürün adı: ")
            product = next((p for p in products if p.name == product_name), None)
            if product:
                product.display_recipe()
            else:
                print(f"{product_name} ürünü bulunamadı.")
        elif choice == 4:
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
