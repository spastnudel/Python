largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done":
        break
    
    try: 
        num == int(num)
                
        #check for smallest  AND  for largest        
        if smallest is None and largest is None:
            smallest = num
            largest = num
        
        elif smallest > num :
            smallest = num
                        
        elif largest < num :
            largest = num
        
    except:
        print "Invalid input"
		
print "Maximum is", largest
print "Minimum is", smallest