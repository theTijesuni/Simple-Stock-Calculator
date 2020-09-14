#features coming soon
# go back
# quit
# add GUI

def stock_diff():
    print("a. Calculate price difference")
    print("b. Increase by x percent\n")
    user_input = input("A or B:\n>..")

    while (user_input != "q"):
        if (user_input.lower() == "a" ):
            print("Press to \"go back\"\n")
            price1 = input("Price 1\n>..")
            price2 = input("Price 2\n>..") 
            price1, price2 = float(price1), float(price2)
            output = ((price2 - price1)/ price1) * 100
            message = ("Difference = %{}").format(output)
            print(message,"\n")

        elif(user_input.lower() == "b"):
            num = input("Increase what no?%:\n >..")
            margin = input("By how many percent?%:\n >..")
            num, margin = float(num), float(margin)
            output = margin/100 * num + num
            message = ("Value = %{}").format(output)
            print(message,"\n")

        else:
            print("Please choose A or B")
            stock_diff()
        
stock_diff()
