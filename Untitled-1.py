


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
ill="hello  how  are  you "
print(ill.strip())

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

   
 