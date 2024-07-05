


x="merhaba"

def gg():
    
    x="doğum günü"
   

gg()
""" cümledeki harf , boşluk vs adetlerini gösterir """
print(len(x))
print(x)



tt=("at", "avrat", "silah")
print(tt)


x= 10
print(type(x))


v="tip"
print(type(v))


a=1
print(int(a))

b=1
print(complex(b))

c=1
print(float(c))

""" içinde bu kelime varmı diye kontrol etmek """
trxxx="merhaba bu gün hava bulutluu ve yağışlı"

print("doğru" is trxxx )


ii="hello    how are you"
print(ii[1:5])
print(ii[:10])

print(ii.upper())
print(ii.lower())

dd= """ boşlukları kaldırma """
illl="hell o  how  are  you merhaba"
print(illl.strip())

""" değiştirmek  """
print(ii.replace("h", "y"))
ğ="merhaba"
kl="günaydın"
cvc=ğ+" "+kl

print(cvc)

""" ssayıyla yazıyı birleştirmek  """
yaş=30
""" {yaş:.2f} . dan sonra 2 sıvır koyar """
yazı= f"merhaba yaşım {yaş}"

print(yazı)

tüğ=f"merhanva {yaş:.2f}"
print(tüğ)

öö="arabalar: bmw,audi,mercedes \"aaaaa\" alman arabalrı"
print(öö)

print(100<10)

print(bool(10>8))

""" türünü kontrol eder  int vs """

s=470
print(isinstance(s,int))

def  nbn():
    return True

if nbn():
    print("yes ")
else:
   print("no")

astt =["araba","elma","armut"]
print(astt)

print(type(astt))
print(astt[2])

if "üzüm" in astt:
    print("evet var")
else:
    print("hayır yok")

    if "mermi" in astt:
        print("evet burada")
    else:
        print("hayır burda yok")


        astt[1]="merhamet edin efendim"
        print(astt)

        thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

        thislist[0:2]= ["selam", "merhaba"]
        print(thislist)

        """ öge silmeden eklemek """
        yy=["apple", "banana", "cherry"]
        yy.insert(0, " wather")
        print(yy)

""" listenin sonuna ekler """
yy.append("car")
print(yy)

""" listeleri birbirine eklemek  """
cc=["para","altın","dollar","euro" ]
vv=["faiz","kredi"]

cc.extend(vv)
print(cc)
""" listeden kaldırmak remove """
cc.remove("altın")
print(cc)

""" sayı olarak kaldırmak  pop(3)  """
""" dizi belirtmes sen son ögeyi kaldırır pop()  """

cc.pop()
print(cc)
""" kaldırma """
odıı=["faiz","kredi","mezar"]
del odıı[1]
print(odıı)

""" listenin tamamını silmek 
çç=["faiz","kredi","mezar","sayı"]
del çç
print(çç)
"""
""" parentez kalır içindeki  diziler siler """
şş=["a","b","c","d","e","f"]
şş.clear()
print(şş)

""" döngü oluşturmak  """

adın=["aslan","şevket","polat","memati"]

for p in adın:
    print(p)

""" dizi numaraları arası döngü yene normal  döngü gibi dödürür """
for m in range(len(adın)):
 print(adın[m])

 dş=["d","ü","q","r"]
 i=0

 while i < len(dş):
     print(dş[i])
     i=i+1

""" fgü listesi  içinde a harfi olan kelimeleri ghb içine koyup yazdırır """
fgü=["aslan","kaplan","yılan","su","burun","öneri"]
ghb=[]

for ö in fgü:
    if "a" in ö:
        ghb.append(ö)
        print(ghb)

""" daha az satırlı hali """
fgü=["aslan","kaplan","yılan","su","burun","öneri"]
ghb=[ö for ö in fgü  if "a" in ö]
print(ghb)

""" kaç dışındakileri yazdır  """
bnb=["asıl","kaç","gel","git"]
nmb=[n for n in bnb if n != "kaç"]
print(nmb)

""" 10  kadar yazdır """
vfd=[c for c in range (10) ]
print(vfd)

ll=[h for h in range(10) if h < 5  ]
print(ll)

""" büyük harf yazdırmak  """
hh=["ali","veli","osman"]
bnd=[pp.upper() for pp in hh]
print(bnd)

""" listedekilerin hepsini aynı kelime yapmak """
oı=["apple", "banana", "cherry", "kiwi", "mango"]
ert=['hürme edin efendim' for t in oı ]
print(ert)

""" listedeki bir kelime yerine başka bir kelime yazdırma """
sd=["apple", "banana", "cherry", "kiwi", "mango"]
vnn=[yy if yy !="banana" else "yunanistan" for yy in sd ]

print(vnn)

""" düşükden yükseğe """
numberss=[100, 50, 65, 82, 23]
numberss.sort()

print(numberss)
""" alfabeye göre sırlama """
harff=["g","s","a","v","c"]
harff.sort()
print(harff)


"""  yüksekden düşüğe """

vdaa=[100, 50, 65, 82, 23,1000,7,56,22,1101]
vdaa.sort(reverse=True)

print(vdaa)

""" Listeyi sayının 50'ye ne kadar yakın olduğuna göre sıralar """
xcx=[100, 50, 65, 82, 23,1000,7,56,22,1101]


def aa(n):
    return abs(n- 50)
xcx.sort(key= aa)
print(xcx)
""" büyük harfle başlayan lar ilk sırada küçük harfle başlayanlar sonra sıralanır """
vvv=["banana", "Orange", "Kiwi", "Cherry"]

vvv.sort()
print(vvv)
""" büyük küçük harf ayrımı olmasın diyorsan """
vvv.sort(key= str.lower)
print(vvv)

""" listenin tersini yazdırmak istersen """
bbnn=["banana", "Orange", "Kiwi", "Cherry"]
bbnn.reverse()
print(bbnn)

""" liste kopyalama """

wae=["apple", "banana", "cherry"]
dff= wae.copy()
print(dff)
""" listeleri birleştirme """
aab=["a","b","c","d"]
abbc=[1,2,3,4]

brlşkk=aab+abbc

print(brlşkk)

""" listeleri birleştirmede başka bir yolu """
aab.extend(abbc)
print(aab)


""" tuple """
x = ("apple", "banana", "cherry")
""" tupleyi listeye çevirip değişiklik yapmak """
po=list(x)
""" yeni öge oluşturmak  """
po.append("blubery")
""" öge silmek çıkartmak  """
po.remove("apple")
""" değiştirmek  """
po[2]="lemon"
nn=tuple(po)
print(nn)
""" tamammını silmek istersen

del x 
print(x)
 """

""" tuple a tuple eklemek  """
frg=("a","b","c","d","e")
bvv=("f",)
frg += bvv
print(frg)

""" tupleyi  açmak  """
yaşam=("sağlık","yemek","huzur","para",)

(bırr,ıkıı,ucc,dortt)=yaşam
print(bırr)
print(ıkıı)
print(ucc)
print(dortt)

uits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(*rr,pp, tp)=uits

print(rr)
print(pp)
print(tp)

