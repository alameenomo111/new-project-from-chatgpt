print("===== SIMPLE SHOPPING CART =====")

products = ["rice", "beans", "bread", "yam"] 
prices = [2000, 1500, 1000, 2500]

print("Available products:")
print("1. rice - ₦2000") 
print("2. beans - ₦1500")
print("3. bread - ₦1000")
print("4. yam - ₦2500") 

product = input("Enter the product you want: ").lower() 

if product in products:
    quantity = int(input("Enter quantity: ")) 
    
    index = products.index(product) 
    price = prices[index] 
    
    total = price * quantity
    
    print("Product:", product) 
    print("Price:", price)
    print("Quantity:", quantity) 
    print("Total: ₦", total) 
    
else: print("Sorry, that product is not available.")

print("====== GAME SHOP ======")
games=["minecraft","fifa","gta","dls"]
prices=[2700,3000,4000,3500]

print("Available games: ")

print("1.minecraft - ₦2700") 
print("2. fif - ₦3000")
print("3. gta - ₦4000")
print("4. dls - ₦3500") 
games=input("ENTER GAME: ")
    
    
if game in games:
    quantity= int(input("ENTER TIME: "))
    index=games.index(games)
    price=prices[index]
    
    total=price*quantity
    
    print("Product:", product) 
    print("Price:", price)
    print("Quantity:", quantity) 
    print("Total: ₦",total) 
        
else: print("Sorry, that product is not available.")