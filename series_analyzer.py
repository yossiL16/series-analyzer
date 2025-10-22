

def input_series():

    print("""                       Welcome 
    
         please enter your number atntion:
         
        # You must enter at least 3 numbers.
        
        # All numbers must be positive (> 0).
        
        # Separate the numbers using spaces""")

    while True:
        series = []
        x = input("please enter series of numbers: ")

        list_split = x.split(" ")

        try:
            for i in list_split:
                i = float(i)

                if i < 0:

                    print("the number is less then 0, try again...")
                    series = []
                    continue
                series.append(i)

                continue

        except:
            print("please don't put a word, only numbers.")
            continue
        print(len(series))
        if len(series) < 3:
            print("Enter at least 3 numbers.")
            continue

        break

    return series





