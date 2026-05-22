## input we need from the user 
# Total Rent 
# Total food ordered for snacking 
# Electricity units spend 
# Charge per unit 
# Persoons living in flat 

## Output 
## total amount you have to pay is 

Rent = int(input("enter your flat rent ="))
Food = int(input("Enter amount of food ordered ="))
Electricity_Spend = int(input("Enter total electricity spend ="))
Charge_per_unit = int(input("Enter charge per unit = "))
Persons = int(input("Enter the number of person living in the room = "))

total_bill = Electricity_Spend * Charge_per_unit
Output = ( Food + Rent + total_bill) // Persons 
print ("Each person will pay = ", Output )