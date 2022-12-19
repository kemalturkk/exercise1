#metot 1#
def terimlerToplami (ilkTerim,sonTerim,artisMiktari):
    return ((sonTerim-ilkTerim)/artisMiktari+1)*(ilkTerim+sonTerim)/2
sonuc= terimlerToplami(19, 202, 3)
print (sonuc)
 
print("-----------ikinci yöntem-------------")
 

liste1 = range (19,203, 3)
print("elemanlar toplamı :" , sum(liste1))  