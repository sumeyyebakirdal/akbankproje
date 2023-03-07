import csv
import datetime

# Menu.txt dosyası oluşturuldu
with open('Menu.txt', 'w') as f:
    f.write('* Lütfen bir pizza tabani seçiniz:\n1: Classic fiyat:10 tl \n2: Margarita fiyat:12 tl\n3: Turk Pizzasi fiyat:15 tl\n4:Sade pizza fiyat:9 tl\n* Hangi sosu secersiniz?:\n11: Zeytin fiyat:1.5 tl\n12: Mantarlar fiyat:2.0 tl\n13: Keci Peyniri fiyat 2.5 tl:\n14: Et fiyat:4.0 tl\n15: Sogan fiyat:3.0 tl\n16: Misir fiyat:3.5 tl\n\n* Tesekkür ederiz!')

# Süper sınıf "pizza" oluşturuldu
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

# Alt sınıf "pizza" oluşturuldu
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__('Classic Pizza', 10)

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__('Margarita Pizza', 12)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__('Turk Pizza', 15)

class SadePizza(Pizza):
    def __init__(self):
        super().__init__('Sade Pizza', 9)

# "Dekoratör" üst sınıfını oluşturuldu
class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza
    
    def get_description(self):
        return self.pizza.get_description() + ', ' + super().get_description()
    
    def get_cost(self):
        return self.pizza.get_cost() + super().get_cost()

# Soslar için alt sınıflar oluşturuldu
class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = 'Zeytin'
        self.cost = 1.5

class Mantarlar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = 'Mantarlar'
        self.cost = 2.0

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = 'Keci peyniri'
        self.cost = 2.5
    
class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = 'Et'
        self.cost = 4.0

class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = 'Sogan'
        self.cost = 3.0

class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = 'Misir'
        self.cost = 3.5

def main():
    # Menü yazdırıldı 
    with open('Menu.txt', 'r') as f:
        print(f.read())
    
    ## Kullanıcı bir pizza ve sos seçer
    while True:
        pizza_choice = input('Lütfen pizzanizi seciniz (Classic pizza için 1, Margarita pizza için 2,Türk Pizzasi için 3,Sade Pizza için 4 tuslayiniz...): ')
        if pizza_choice in ('1', '2','3','4'):
            break
        else:
            print('Invalid choice.')
    
    pizza = None
    if pizza_choice == '1':
        pizza = ClassicPizza()
    elif pizza_choice == '2':
        pizza = MargaritaPizza()
    elif pizza_choice == '3':
        pizza = TurkPizza()
    elif pizza_choice == '4':
        pizza = SadePizza()
    
    
    while True:
        sauce_choice = input('Lütfen sos seciniz(Zeytin için 11, Mantarlar için 12  ,Keci Peyniri icin 13, Et icin 14, Sogan icin 15, Misir icin 16 tuslayiniz...): ')
        if sauce_choice in ('11', '12','13','14','15','16'):
            break
        else:
            print('geçersiz seçim.')
    
    if sauce_choice == '11':
        pizza = Zeytin(pizza)
    elif sauce_choice == '12':
        pizza = Mantarlar(pizza)
    elif sauce_choice == '13':
        pizza = KeciPeyniri(pizza)
    elif sauce_choice == '14':
        pizza = Et(pizza)
    elif sauce_choice == '15':
        pizza = Sogan(pizza)
    elif sauce_choice == '16':
        pizza = Misir(pizza)
    
    
    # Toplam fiyat hesaplanır
    total_cost = pizza.get_cost()
    print('Toplam Tutar:', total_cost)
    
   # Kullanıcı bilgileri istenir ve Orders_Database.csv dosyasına yazdırılır
    name = input('Lütfen isminizi girniz: ')
    tr_id = input('Lütfen TC kimlik no giriniz: ')
    credit_card = input('Lütfen kredi karti numaranii giriniz: ')
    password = input('Lütfen kredi karti sifrenizi giriniz: ')
    
    with open('Orders_Database.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([pizza.get_description(),name ,tr_id ,credit_card, datetime.datetime.now(), password])

if __name__ == '__main__':
    main()
    