# My function
def Calculate_Grade_Ore(Weight_Metal, Weight_Ore):
    Grade = (Weight_Metal / Weight_Ore) * 1000000
    print(f"The grade of the ore is equal to {Grade} ppm")

def Calculate_Mineral_Reserve(LengthOre, WidthOre, HeightOre, Ore_Grade):
    VolumeOre = LengthOre * WidthOre * HeightOre
    Mineral_Reserve = VolumeOre*(Ore_Grade/1000000)
    print(f"The Mineral reserve is equal to {Mineral_Reserve} cubic meters")
    
def Calculate_Extracted_Tonnage(weight_ore, grade, recovery_rate ):
    tonnage = ( grade*weight_ore*recovery_rate) / 1000000
    print(f"The tonnage of extracted mineral is equal to {tonnage} tons")
   
def Calculate_Mining_Rate(Total_Tonnage, Working_Day):  
    Mining_Rate = Total_Tonnage / Working_Day
    print(f"the rate of mining is equal to {Mining_Rate} tons per day")

def Calculate_Mining_Cost(Mining_Rate, Operational_Cost, Initial_Investment):
    Annual_Tonnage = Mining_Rate*365
    Annual_Operational_Cost = Annual_Tonnage * Operational_Cost
    Total_Cost = Annual_Operational_Cost + Initial_Investment
    print(f"The total annual mining cost is equal to $ {Total_Cost}")
    
def Calculate_Mining_Profit(Selling_Price, Total_Tonnage, Mining_Cost):
    Total_Revenue = Selling_Price * Total_Tonnage
    Profit = Total_Revenue - Mining_Cost
    print(f"Total profit is equal to $ {Profit}")