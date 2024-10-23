#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:     
#Student Name:  Mathew Akunyili

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Program Title
    print("Erewhon Mobile Data Plans")
    print("")

    # Ask user for data usage
    dataUsage = float(input("Enter data usage (Mb): "))
                      
    # Calculations
    if dataUsage <= 200: #This ,meams if the data usage is lower or is also equal to 200 That is would hava a chare of 20 dollars
        totalCharge = 20
    elif dataUsage <= 500:
        roc = 0.105 # This would be multiplied to the data usage the user enters to give the total charge
        totalCharge = roc * dataUsage
    elif dataUsage <= 1000:
        roc = 0.110
        totalCharge = roc * dataUsage
    else:
        totalCharge = 118
    
     

    # Print total charge
    print(f"Total charge is: ${totalCharge:.2f}")









    # YOUR CODE ENDS HERE

main()