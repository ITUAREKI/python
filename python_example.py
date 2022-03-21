#Listing a list in multiples of 5 with Python.

List1=[12,34,543,223,67,54,55,25,12,10]
counter=0
for i in List1:
    if(i % 5 == 0):
        print(str(i)+ (" is a multiple of 5."))
        counter=counter+1
    else:
        print("The loop is over.")
print("number of multiples of 5",str(counter))
