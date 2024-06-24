


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

   
 