def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = int(input("Enter a number: "))
    if  in_num <= 21:
        difference = 21 - in_num
        return f"result: {difference}"
    else:
        difference_2 = (in_num - 21) * 2
        return f"result: {difference_2}"
        


    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
