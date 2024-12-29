bentuk_goa =["|_|"]
goa = [bentuk_goa] * 4

goa_kosong = goa.copy()
goa_kosong[2] = "Glen"


print(goa) # data asli tidak terpengaruh 
print(goa_kosong) # sedangkan salinannya aja terpengaruh 

