
#phytonun çok satırlı yorum satırı yoktur bunun yerine 
"""
#phyton herhangi bir değişkene atanmamış dizileri yok sayacağı için çok satırlı stiring açarak yorum satırlarını belirtebilriz

"""

#casting döküm, kalıp demek veri kalıbını belirtebiliriz onun dışında direk yazılıyor değişkenler eğer belirtemek istiersek 
#belritebiliriz
x=str("hasan")

#değişkenin veri tipini görmek için type() kullanıyoruz
print(type(x))

#çoklu değişkenlere çoklu değer atayabiliyoruz buradaki önemli nokat 
#değişken sayısıyla değer sayısı eşit olmak zorunda yoksa hata alırız
x , y , z = 10 , -23 ,5

#koleyksiyondan paketten veri atama eğer bir dizi olarak elimizde varsa tüm bunları sadece dizi ismini belirterek
#sıraladığımız değişkenlere dizinin index sırasına göre atanır
yapilacaklar =["kriptoloji tekrari", "flutter","konu tekrari"]
pazartesi,sali,carsamba =yapilacaklar


#print komutunda birden fazla değişkeni virgülle ayırarak yazdırabiliriz
#ya da aralarına + koyarak yazdırıırız string ve int iki değikeni + ile yazdıramayız
#ancak virgülle yazdırabiliriz  
print(pazartesi,sali,carsamba)



#-------------------------------------------------------------------------------------------------------------------------------
# global veriable lar phyton da da geçerli
def fuckt():
    x=3
    print(x)
fuckt()

# bir fonksiyonun içinde global bir değişken oluştrumak için global anahtarını kullanıyoruz ve o değişken artık tüm dosyada 
# kullanılıyor.
print(x)

def fuckt():
    global x
    x=22
    print(x)
fuckt()

#-------------------------------------------------------------------------------------------------------------------------------
# float belirtirken bilimsel olarak gösterimde e harfide kullanılabiliriyor
# karmaşık sayılar ise j ile belirtiliyor  
x = 35e3
y = 12E4
z = -87.7e100
print(type(x)) 
print(type(y))
print(type(z))

# karmaşık sayılar ise j ile belirtiliyor  
karmasik=3+5j
print(type(karmasik)) 


#--------------------------------------------------- VERİ TİPİ DEĞİŞTİRME----------------------------------------------------------------------------
# veri tipi değişiminde olana bir değişkenin veri tipini başka bir değişkene atıyarak veri tipi değiştrilimiş bir şekilde
# atayabiliriz ama complej bir değişkeni başka bir veritipine dönüştüremeyiz ancak int bir değişkeni complej bir değişkene
# atayabiliriz

x = 35e3

a=int(x)
b=complex(x)
print(type(x)) 
print(type(y))

# random komutunu kütüphanesini oluşturarak oluşturabiliyoruz 1 ile 9 dahil rastgele sayılar oluşturabiliriz
import random
print(random.randrange(1, 10))


#-------------------------------------------------------------------------------------------------------------------------------
# her değiken istenilen veri tipine uygun olduğu sürece değiştirilebilir
x = int(1)   
y = int(2.8) 
z = int("3")
print(type(x)) 
print(type(y))
print(type(z))
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)
print(type(x)) 
print(type(y))
print(type(z))






#-------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------   FOR DÖNGÜSÜ    --------------------------------------------------------

# for döngüleri herhangi bir başlangıç ya da bitiş indexine ihtiyaç duymaz. 
# continue kullanırsak sadece döngü değişkeninin o indexini geçmiş olur eğer döngü değişkeni hala büyüyebiliyorsa 
# büyümeye devam eder her ettiğinde tekrardan döngü içine girer.
# 
# ama break kullanırsak belirtilen koşul sağlanır sağlanmaz tüm for döngüsü son bulur. 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
for x in fruits:
  if x == "banana":
    break
  print(x)

#----------  R A N G E    

# range fonksiyonu ise sayı dizisi dödürmemizi sağlar.

# mesela bu x değeri 0 dan 6 ya kadar (yani beş dahil altı değil) girmesini belirten şartı koyuyor 
for x in range(6):
  print(x) 

# iki parametreli range kullanırsak da bunların birincisi başlangıç değeri diğeri ise sınır değerine kadar olan sayıları kapsar
for x in range(2, 6):
  print(x) 

# üç parametreli olarak yazımda ise en son parametre defoult olarak gelen bir bir artma parametresini değiştirir belirlenen 
# değeri yapar 
for x in range(-2, -30, -3):
  print(x)

# -------- E L S E
# for döngüsünde else kullanımı döngü tamamlandığında çalışacak olan bloğu belirtir. Eğer döngüde bir break kullanıldıysa bu else
# kullanılamaz eğer break şartına girilmiş ve döngü kırıldıysa bu else bloğu hiç çalışmaz
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
#-------- N E S T E D     L O O P S
# her alt for döngüsü çalıştığında üst for da her defasında çalışacaktır
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#------- P A S S 
# hata alacağımız düşündüğüm durumlarda for döngülerinde pass kullanarak o durumu geçebilirz 

 





#-----------------------------------------------------   STRİNG İŞLEMLER    --------------------------------------------------------

# çok satırlı stringler """   """ olarak ta '''   ''' olarak da açılabilirler
# stringler dizilerdir dizi halindedirler istenilen karakter indexi çekilebilir
for x in "banana":
  print(x)

# string ifadenin uzunluğunu öğrenmek için len() kullanıyoruz
a = "Hello, World!"
print(len(a))

#--------- in anahtarı
# string bir metinde aranan ifadenin olmasını sorgulayan boolean bir ifade döndürür.
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

#--------- not in anahtarı
# bir ifadenin olmayışını sorgulayan boolean bir ifade döndürür.
txt = "The best things in life are free!"
print("expensive" not in txt)

# string ifadenin belli index aralığına ulaşmak istiyorsak değişkenin izmi köşeli parantez içinde aralığını yazıyoruz.
print(txt[2:10])
# başlangıç değerini belirtmezsek ilk karakterden başlayacaktır
print(txt[:10])
# bitiş değeri belirtilmezse ifadenin son indexine kadar gidecektir
print(txt[2:])
# negatif değerlerde belirtilebilir
print(b[-5:-2])

#------ modify kullanımları

# tüm string ifadeyi büyük ya da küçük harf yapar
a = "  Hello, World!  "
print(a.upper())
print(a.lower())

# string ifadedeki ilk dolu string ifadenin ve son ifade arasında kalanlar hariç tüm boşlulkları yok eder strip blok demek 
print(a.strip())

#replace değiştirmek demektir bir karakterden kaçtane olursa olsun istenen değerle değiştirir.
print(a.replace("H", "J"))

# split kullanarak da belirlenen karakterden arasında kalan tüm string ifadeleri birer dizi haline getirir.
print(a.split(","))

#stringler düz bir şekilde direk toplanabilir
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#------ FORMAT KULLANIMI
# iki farklı veri tipini birleştirken kullanıyoruz {} leri koydumuz her yere değişkenlerimizi sırasıyla yazıyor. Bunu formatını
# aldığımız sadece string işlemlerde yapabiliriz ne kadar fazla değikeni istersek istiyelim hepsini istediğimiz bölgelere koyarak
# string yapıyor. Eğer istersek bu yerine koyma sırasını değiştirebiliyoruz.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#------------- escape character
# kaçış karakteri \ ters slash dır bundan sonra istediğimiz karakteri yazarız
# mesela tırmak içinde tırnak yazacağız ama programlama dili buna izin vermiyor bunun için bu iki tırnağı da görmezden gelsin diye
# kaçış karakterini kullanıyoruz 
txt = "We are the so-called \"Vikings\" from the north."  
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# geriye kalan tüm string methotları yeni bir string değer döndürür orjinal dizeyi değiştirmez




#-----------------------------------------------------    BOOLEANS    --------------------------------------------------------
# Eğer bir değer içeriğe sahipse doğrudur. Bir dize boş değilse doğrudur. 0 dışında her sayıda doğrudur. Boş olanlar hariç tüm listeler
# tuple lar kümeler ve sözlükler de doğrudur.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# yanlış olanlar ise bunlardır
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# sıfır döndüren fonksiyonlar, ya da kendini defoult olarak sıfır döndüren objeler de yanlış olarak kabul edilir
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
 
# doğru ya da yanlış değer döndüren fonksiyonlar da oluşturulabilir
def myFunction() :
  return True
print(myFunction())


def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")


#------------------  isinstance()
# kullanarak belirtilen değerin istenen değerde mi olup olmadığını boolean olarak döndürür
x = 200
print(isinstance(x, int))

#------------------  Floor division
# Kat bölme, sonucu normal bölme sonucundan küçük veya ona eşit olan en yakın tam sayıya veya tam sayıya yuvarlayan
# bir bölme işlemidir. Kat fonksiyonu matematiksel olarak bu ⌊ ⌋ sembolüyle gösterilir.  

#-----------------------------------------------------    OPERATÖRLER    --------------------------------------------------------
# +  	Addition	x + y	
# -	  Subtraction	x - y	
# * 	Multiplication	x * y	
# /  	Division	x / y	
# %  	Modulus	x % y	
# **	Exponentiation(üs alma)	x ** y	
# //	Floor division(katlı bölme)	x // y

#------------------  " &= "  operatörü

# &= operatörü, bir değişkenin mevcut değerini başka bir değerle "ve" (bit düzeyinde) işlem yaparak günceller.
x = 5          # Örnek bir sayı (binary: 0101)
y = 3          # Başka bir sayı (binary: 0011)
x &= y         # x'i y ile "ve" işlemine tabi tut
print(x)       # Sonuç: 1 (binary: 0001)

#------------------  " |= "  operatörü
# |= operatörü, bir değişkenin mevcut değerini başka bir değerle "veya" (bit düzeyinde) işlem yaparak günceller.
x = 5  # Örnek bir sayı (binary: 0101)
y = 3  # Başka bir sayı (binary: 0011)
x |= y  # x'i y ile "veya" işlemine tabi tut
print(x)  # Sonuç: 7 (binary: 0111)

#------------------  " ^= "  operatörü
# ^= operatörü, bir değişkenin mevcut değerini başka bir değerle "XOR" (bit düzeyinde) işlem yaparak günceller. 
x = 5  # Örnek bir sayı (binary: 0101)
y = 3  # Başka bir sayı (binary: 0011)
x ^= y  # x'i y ile XOR işlemine tabi tut
print(x)  # Sonuç: 6 (binary: 0110)

#------------------  " >>= "  operatörü
# >>= operatörü, bir değişkenin mevcut değerini belirtilen bir sayı kadar sağa kaydırmak için kullanılır.
x = 16  # Örnek bir sayı (binary: 10000)
x >>= 2  # x'i 2 bit sağa kaydır
print(x)  # Sonuç: 4 (binary: 0001)

#------------------ " <<= " operatörü
# >>= operatörü, bir değişkenin mevcut değerini belirtilen bir sayı kadar sağa kaydırmak için kullanılır. 
x = 16  # Örnek bir sayı (binary: 10000)
x >>= 2  # x'i 2 bit sağa kaydır
print(x)  # Sonuç: 4 (binary: 0001)


# Kimlik operatörleri, nesneleri eşit olup olmadıklarını değil, gerçekte aynı nesne olup olmadıklarını
# ve aynı bellek konumuna sahip olup olmadıklarını karşılaştırmak için kullanılır

#----- is
# Her iki değişken de aynı nesne ise True değerini döndürür 
x is y
#----- is not
# her iki değişken aynı değilse true değerini döndürü
x is not y

#Üyelik operatörleri bir nesnede bir dizinin sunulup sunulmadığını test etmek için kullanılır
# ------------  in 
# Nesnede belirtilen değere sahip bir dizi mevcutsa True değerini döndürür
x in y
# ------------  not in 
# Nesnede belirtilen değere sahip bir sıra mevcut değilse True değerini döndürür
x not in y	

# ------------  BİTSEL OPERATÖRLER
# & 	AND	
# |	  OR	
# ^	  XOR	
# ~	  NOT	
# <<	Zero fill left shift	
# >>	Signed right shift	 







#--------------------------------------------             Lists                ----------------------------------------------------

#    Listeler köşeli parantezlerle gösterilir. Listelerde öğeler index mantığıyla çalışırlar ve bu index sıralaması değiştirilemez
# yani biz yeni bir öğe eklersek eğer bu listeye en son indexe yerleşir.
#
# listeler değiştirilebilirdir yani olan bir öğeyi silebilir ya da yerine yeni bir öğe atayabiliriz. listeler
# değiştirilebilirdir yani olan bir öğeyi silebilir ya da yerine yeni bir öğe atayabiliriz.
# 
# aynı değere sahip birden fazla öğe oluşturabiliriz
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# Bir listenin kaç öğeye sahip olduğunu belirlemek için len() işlevini kullanırız.  
print(len(thislist))

#---------------   listelerin veri türleri

# listeler herhangi bir veri türünde olabilirler
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False] 

# bir liste farklı farklı veri türlerini de barındırabilir. Phyton zaten listeleri ayrı bir veri tipi olarak görür
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

# list() Constructor kullanarak da listeleri belirtebiliriz fakat burada çift yuvarlak parantez açmamız gerektiğine dikkat edelim
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Python programlama dilinde dört koleksiyon veri türü vardır:
# Liste sıralı ve değiştirilebilir bir koleksiyondur. Yinelenen üyelere izin verir.
# Tuple, sıralı ve değiştirilemez bir koleksiyondur. Yinelenen üyelere izin verir.
# Set, sırasız, değiştirilemez* ve indekslenmemiş bir koleksiyondur. Yinelenen üye yok.
# Sözlük, sıralı ** ve değiştirilebilir bir koleksiyondur. Yinelenen üye yok.



#---------  [ Access List Items  ]

# listelere erişim indexini verekek olur negatif index verilirse sondan başlayacağı karakteri belirtir
print(thislist[1])
# istersek aralıklı index de verebiliriz. Bu aralıklı indexleri verirken yine tüm aralık belirtme kuralları burada da geçerli
# başlangıçı belirtmezsek bitişi belirtmezsek negatif değerler verirsek gibi gibi
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# listenin içinde bir öğenin olup olmadığını kontrol check etmek için yine in anahtarını kullanıyoruz
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



#---------------  [  Change List Items   ]
thislist[1] = "blackcurrant"

# bir öğe aralığını değiştirebiliriz bunu yaparken eğer belirtilen değer aralığından daha fazla ya da daha az ise bütün listenin
# o değer aralığndan sonraki tüm öğelerinin indexi değişecektir
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#-------------------------   [   ÖĞE EKLEME   ]   -----------------
#------------  append() komutu
# listeye yeni bir öğe ekleriz en sonuna eklenir bu öğe.
thislist.append("orange")

#-------------------  Insert komutu

# mevcut değerlerden herhangi birini değiştirmeden belirtilen indexe yeni bir liste öğesi eklemek için insert() kullanıyoruz
# ilk parametre olarak koyulmasını istediğimiz indexi ikinci olarak öğeyi yazıyoruz.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#---------- liste genişletme extend etmek

# başka bir listedeki öğeleri belli bir listeye eklemek için kullanılıyor
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# extend illa liste ekleyecek diye birşey yoktur tekrarlanabilir herhangi bir şeyi listenin içine alarak genişletebiliriz
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#--------------- [   REMOVE etmek kaldırmak listeden veri silmek   ]

# remove belirtilen öğeyi kaldırır. Eğer belirtilen öğeden birden fazla varsa bunlardan index numarasına göre ilk olanı kaldırır
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#------------- pop() methodu

# belirtilen numaradaki veriyi silmemize yarıyor index değil numara yani 1 den başlıyor
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# eğer numara belirtmezsek dizindeki en son öğeyi kaldırır
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



#------------  del()

# del ile belirtilen indexteki veriyi silebiliriz
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) 

# aynı zamanda belirtilen listenin hepsini silebilir
del thislist


#---------  clear()
# clear ile tüm listeyi temizleyebiliriz içinde hiçbir öğe kalmaz
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)




#------------------------------------------------     Listeleri Anlamak         -------------------------------------------

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# listenin index parametresindeymiş gibi gösterip tüm listeyi for döngüsüyle yazdırıyor
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#---------  bir listenin değerlerine dayalı olarak başka bir liste oluşturmak istersek yazmamız gerekenler

# şu alttaki örnek x değeriyle fonksiyon oluşturmuş ve içinde a geçen her öğeyi yeni listeye append ediyor ekliyor.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# list comprehension denen kavramla şu yukarıdaki tüm işlemleri tek bir satırda yapabiliyoruz
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
# dönen değer bir yeni liste eski listeyi değiştirmeden tutmaya devam eder.


#   newlist = [expression for item in iterable if condition == True]

#------- condition
# yani koşul demek. Mesela aşağıdaki koşul x in apple olmadığı tüm durumları istiyor 
newlist = [x for x in fruits if x != "apple"]

#-------- iterable
# yinelenen tekrar edebilen herhangi bir veri tipi liste tuple set gibi. Bunun için range de kullanabiliriz
newlist = [x for x in range(10)]
# koşul eklersek
newlist = [x for x in range(10) if x < 5]

#-------------- Expression
# ifade demektir ve yinelemede kullanılacak olan asıl değerdir. Aynı zamanda atanacak olan depoya eklemeden önce 
# değiştirebileceğimiz sonuçtur.

# mesela bu örnek listedeki öğeleri büyük harfe çevirerek atıyor.
newlist = [x.upper() for x in fruits]

# sonucu istediğimiz gibi ayaralayabiliriz 
newlist = ['hello' for x in fruits]

# expresion sadece yapılacak olan flitere ya da işlem değil aynı zamanda sonucu etkileyecek olan koşulları da içerebilir
newlist = [x if x != "banana" else "orange" for x in fruits]




#-------------------------------------------             SHORT LİST            ---------------------------------------------

# short yöntemi ile nesneleri artan biçimde sıralayabiliyoruz. Eğer nesneler kelime ise baş harfleri büyükten küçüğe eğer sayı
# lardan oluşuyorlarsa küçükten büyüğe sıralıyor
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# eğer azalan şekilde sıralanmasını istersek de revers değişkenini aktif durma getirerek yapabiliriz.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#---------------- kişiselleştirilmiş short fonksiyonu 
# short fonksiyonunun içine anahtar değişkenini bizim istediğimiz gibi çalışan fonksiyonu belirterek istediğimiz şekilde 
# sıralanmasın sağlayabiliriz

# bu örnekteki gibi.
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# short varsayılan olararak büyük harfleri küçük harflerden önce sıralar büyük küçük harfe duyarsız sıralamak içinde lower
# anahtarını kullanabiliriz 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# alfabe sırasına bakılmaksızın sırayı tersine çevirmek istersek revers fonksiyonunu kullanıyoruz. Bir fonksiyon herhangi 
# bir nesneye ihtiyaç duymaz ve bağımsızdır, metot ise herhangi bir nesneyle bağlantılı bir işlevdir.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#--------------------------------------------       LİSTE KOPYALAMAK       ----------------------------------------------------

# liste2=liste1 yaparak listeyi kopyalayamayız bu durumda liste1 liste2 ye referans olacaktır, liste1 de yapılan her ne varsa
# liste ikide de aynıları olacaktır.
# 
# kopyalamanın bir yöntemi copy fonksiyonun kullanmak
# thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# diğer bir yöntem ise list methodunda listeyi blirterek ilişkilendirmeden direk kopyalamak
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#-------------------------------------------           LİSTE BİRLEŞTİRMEK         --------------------------------------

# En kolayı + ile ayrı bir listeye eklemek
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# tek tek for ile liste2 nin elemanlarını liste1  e de appand yaparak ekleyebiliriz
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

# ya da extend kullanarak 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)










#--------------------------------------------------------      TUPLES    -------------------------------------------------------

# Tuple birden fazla öğeyi tek bir değişkende tutan değiştirilemeyen veri türüdür.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# tuple lar index numaraları değiştirilemez. Bir tuple ın içindeki hiçbir veri değiştirilemez.
# tuple lar index mantığıyla çalıştıkları için bir tuple içinde tekrar eden birden fazla değer olabilir
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# len() methodu ile tuple ın uzunluğu öğrenilebilir
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# tek öğeli bir tuple oluşturmak istediğimiz zaman öğeyi yazdıktan sonra virgül koymamız gerekir aksi halde tuple olarak
# kabul etmeyecektir
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 

# tuple lar birçok veri tipindeki öğeleri barındırabilirler
tuple1 = ("abc", 34, True, 40, "male")

# tuple constructor ını kullanarak yazmak istersek de çift parntez koymaya dikkat edelim.
tuple_list=tuple(("ahmet",85))




#--------------------------------------------------    Sets      --------------------------------------------------------------

# setler sırasız değiştirilemez dizin mantığıyla çalışazlar. Atanan öğeler değiştirilemez ama silinip yeni bir öğe atanabilir.
# kümeler süslü parantezeler ile yazılır.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# setlerin sıralanmamış olmaları tanımlanmamış bir sıraya sahip oldukları anlamına gelir. Eğer bu setlere bir sıra tanımlarsak
# bu sıra her biz seti kullandığımızda farklı bir sırada görüncecektir index veya anahtarla başvurulamaz

# aynı öğenin tekrar etmesine izin verilmez
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# setlerde true ve 1 değerleri aynı kabul edilir ve bu yüzden kopya sayarak ilk olanı döndürür
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
# false ve sıfırda aynı şekilde
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# len() ile uzunluğunu öğrenebiliriz
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# set lerde tutulacak veriler her türlü veri tipine sahip olabilirler. set() constractoru kullanarak belirtilebilir. type() 
# kullabiliyoruz.
# Diğer koleksyiyon verileri ile hemen hemen aynı özelliklere sahip







#-----------------------------------------         M  A  T  R  İ  S  L  E  R          -------------------------------------------  

# Gözlem sayısını yani satırları n belirtir. Değişken yani sütun sayısını ise p matris boyutu ise nxp olarak gösterilir.
# Matrisleri istersek çok boyutlu listeler olarak tanımlayıp kullanbliliriz istersek de daha çok matris özelliğine sahip NumPy
# paketiyle kullanabiliriz. 
A =[[7,-12,5],[78,45,-30]]
print(A[0][1])

# ndarray.shape : Dizi boyutunu verir. a X b matrisi (a,b) olarak döner.
# ndarray.size : Dizideki eleman sayısını verir. Yani a*b işleminin sonucudur.
# ndarray.dtype : Dizideki eleman türünü döndürür.
# ndarray.full() : elemanları aynı olan dizi oluşturur. Örneğin; 2 satır 3 sutunu olan matrisin elemanları 8’dir. np.full((2,3),8)
# np.eye((a)) : axa değerinde birim matris oluşturur.
# np.linspace(a,b,x): a’dan b’ye kadar (b dahil) x adet sayı üretmek için kullanılır.

# çok boyutlu bir listeyi istersek direk numpy dizinine dönüştürebiliriz
import numpy as nmp
arr = nmp.array( [ [1, 0], [6, 4] ] )
print(arr)

# tüm değerlerin 0’a ayarlandığı, verilen şeklin ve veri türünün bir Numpy dizisini döndürür.
zero_array = nmp.zeros( (3, 2) )

# tüm değerlerin 1'e ayarlandığı, verilen şeklin ve veri türünün bir Numpy dizisini döndürür.
one_array = nmp.ones( (3, 2) )

# Elemanları 0’dan 9’a kadar olan bir array oluşturmamızı sağlar.
X = nmp.arange(9).reshape(3, 3)

# Matrislerin satırını sütun, sütunlarını satır yapmaya transpoz alma işlemi denir.Bir array’in transpozu .T ile bulunur.
print( X.transpose())

#------------------------ Matris birleştirme

# iki veya daha fazla dizeyi tek bir dizeye koyuyoruz. Matrislerde birleştirmeyi axes ler ile yapıyoruz. Birleştirmek için
# concatenate() methodunu eksen bilgisi belirterek kullanıyoruz. Eğer eksen bilgisi vermemişsek ekseni varsayılan olarak 0 kabul
# edilir
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)  

# Dikkat edilmesi gereken en önemli nokta mesela yukarıdaki iki dizinde tek boyutlu bu yüzden 0 dan başka bir ekseni olamaz
# belirtemeyizde. Ancak çok boyutlu matrislerde belirtebiliriz.
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr) 

# numpyarray.mean() : aritmetik ortalamayı bulur.
# numpyarray.median() : geometrik ortayı verir.
# numpyarray.var() : var yans bulur.
# numpyarray.std() : standart sapmasını bulur.
# numpyarray.sum() : elemanların toplamını verir.
# numpyarray.min() : en küçük elemanı verir.
# numpyarray.max() : en büyük elemanı verir.



# math.fabs() yöntemi, bir sayının mutlak değerini kayan nokta olarak döndürür. 


# abs() işlevi belirtilen sayının mutlak değerini döndürür.

#------------------- NumPy random üretimi

#Rastgele sayı her seferinde farklı bir sayı anlamına gelmez. Rastgele, mantıksal olarak tahmin edilemeyen şey anlamına gelir.

# Rastgele modülün Rand() yöntemi, 0 ile 1 arasında rastgele bir kayan nokta döndürür.
from numpy import random
x = random.rand()
print(x)

# Randint() constractorunda size parametresi ile üretilecek rastgele sayının kaçtane olduğunu belirtebiliriz zaten ilk 
# verdiğimiz sayıyı 0 ile ilk parametredeki sayı mesela 100 arasında üretmek istediğimizi belirtiyoruz.
import numpy as np
dizi=np.random.randint(100,size=6)
print(dizi)
# size parametresine ikinci bir değer girersek bize matris oluşturur
x = random.randint(100, size=(3, 5))
print(x)


#-------------------round()
# belirtilen sayıda ondalık sayıyla yuvarlatılmış versiyonu olan kayan noktalı bir sayı döndürür. 
x = round(5.76543, 2)
print(x)
# Varsayılan ondalık sayı sayısı 0'dır; bu, işlevin en yakın tam sayıyı döndüreceği anlamına gelir.
x = round(5.76543)
print(x)

#---------------------shape()
# numpy kütüphanesinde bir constractordur belirtilen matrisin ilk boyutun kaç öğeden oluştuğunu ikinci boyutun kaw
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) 
