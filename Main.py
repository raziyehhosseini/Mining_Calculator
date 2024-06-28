from Functions import (Calculate_Grade_Ore, Calculate_Mineral_Reserve, 
                       Calculate_Extracted_Tonnage, Calculate_Mining_Rate, 
                       Calculate_Mining_Cost, Calculate_Mining_Profit)

def main():
    
    print("Hello. This program performs a number of calculations for mining related tasks.\nPlease enter your desired task number:\n 1. Calculate grade of ore\n 2. Calculate mineral reserve\n 3. Calculate Extracted tonnage\n 4. Calculate Mining rate\n 5. Calculate Mining cost\n 6. Calculate Mining profitability\n 7. Exit")
    while True:
        try:
            User_Selection = int(input("Your choice (1 to 7): "))
            if User_Selection in range(1,8):
                break
            else:
               print("Invalid input, Choose again from 1 to 7")
        except ValueError:
            print("The input is invalid. Please try again.")
            
    while True:
        try:
            if User_Selection == 1: # grade of ore
                print("this part of the program is going to calculate the grade of ore. \nplease enter the parameters that are needed.")
                Weight_Metal = float(input("Enter the weight of the metal in grams:"))
                Weight_Ore = float(input("Enter the weight of the ore in grams:"))
                Calculate_Grade_Ore(Weight_Metal, Weight_Ore)
                break
                
            elif User_Selection == 2: # mineral reserve
                print("This part of the program is going to calculate the mineral reserve. \nPlease enter the parameters that are needed.")
                LengthOre = float(input("Enter the length of the ore in meters: "))
                WidthOre = float(input("Enter the width of the ore in meters: "))
                HeightOre = float(input("Enter the height of the ore in meters: "))
                Ore_Grade = float(input("Enter the grade of the ore in ppm: "))
                Calculate_Mineral_Reserve(LengthOre, WidthOre, HeightOre, Ore_Grade)
                break
                
            elif User_Selection == 3: # Extracted tonnage
                print("This part of the program is going to calculate the Extracted tonnage. \nPlease enter the parameters that are needed.")
                Grade = float(input("Enter the grade of the ore in ppm:"))
                Weight_Ore = float(input("Enter the weight of the extracted ore in tons:"))
                Recovery_Rate = float(input("Enter the recovery rate in percentage: ")) / 100
                Calculate_Extracted_Tonnage(Grade,Weight_Ore,Recovery_Rate)
                break

            elif User_Selection == 4: # Mining rate
                print("This part of the program is going to calculate the Mining rate. \nPlease enter the parameters that are needed.")
                Total_Tonnage =float(input("Enter the total tonnage extracted in a year: "))
                Working_Day =float(input("Enter the Number of working days in a year: "))
                Calculate_Mining_Rate(Total_Tonnage, Working_Day)
                break

            elif User_Selection == 5: # Mining cost
                print("This part of the program is going to calculate the total Mining cost. \nPlease enter the parameters that are needed.")
                Mining_Rate =float(input("Enter the mining_rate in tons per day: "))
                Operational_Cost =float(input("Enter the operational_cost in dollars: "))
                Initial_Investment =float(input("Enter the initial_investment in dollars: "))
                Calculate_Mining_Cost(Mining_Rate, Operational_Cost, Initial_Investment)
                break
                
            elif User_Selection == 6: # Mining profitability 
                print("This part of the program is going to Calculate the profitability of the mine. \nPlease enter the parameters that are needed.")
                Selling_Price = float(input("Enter the selling price per ton (in dollars): "))
                Total_Tonnage = float(input("Enter the total tonnage extracted (in tons): "))
                Mining_Cost = float(input("Enter the total mining cost (in dollars): "))
                Calculate_Mining_Profit(Selling_Price, Total_Tonnage, Mining_Cost)
                break
            
            elif User_Selection == 7: # Exit
                print("***The END Of the Program***")
                break

        except ValueError:
            print("   !!! Sorry !!!, The input is invalid. >>> try again <<<")
    
if __name__ == "__main__":
    main()