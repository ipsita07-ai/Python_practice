
##in kgs
items_tobe_purchased= { "potatoes": 3,                    
                 "onions": 2,
                 "tomatoes": 5,
                 "cucumbers": 1,
                 "bananas": 0.5,
                 "paneer": 1.5}


#price in INR per kg
items_available_instore= { "potatoes": 60,
                 "onions": 100,              
                 "tomatoes": 120,
                 "cucumbers": 75,
                 "bananas": 48,
                 "paneer": 92,
                 "meat": 10,
                 "fish": 30,
                 "dates": 25}

#Find total money spent if man bought bananas, tomatoes and paneer



print ([y*b  for x,y in items_available_instore.items() for a,b in items_tobe_purchased.items() if x==a ])  


print ([[y,b]  for x,y in items_available_instore.items() for a,b in items_tobe_purchased.items() if x==a ])  



for items,quantity in items_tobe_purchased.items():
    if items in items_available_instore:
        print("amount to be spent on each item:", quantity*items_available_instore[items])
        total_cost= [quantity*items_available_instore[items]]

        

        print("total amount to be spent on grocery listt :",  )

        
    




