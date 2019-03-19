print("Pounds \t Kilograms")
print("-----------------")

pounds = 100

for x in range(100, 301, 10):
    kg =  pounds / 2.2046
    print(pounds,"\t",format(kg, "4.2f"))
    pounds += 10
    
   
        
