# Mining_Calculator
 This program performs some calculations related to mining and extraction. These calculations were written very simply. Here, the user selects the desired calculation and sets the necessary inputs, then the output is calculated and displayed by the program.
 1. In the first part, the grade of an ore is calculated on the ppm scale, based on the weight of the metal and the weight of the rock. The formula used to calculate the grade is equal to:
		
		Grade = (Weight of Metal / Weight of Ore) * 1000000

2. In the second part, the volume of the mineral reserve is calculated based on its length, width, height, and grade. Here, two formulas are used, one to calculate the volume and the other to calculate the volume of mineral reserves, which are equal to:

		Volume of Ore = Length of Ore * Width of Ore * Height of Ore

		Mineral Reserve = Volume of Ore*(Ore Grade/1000000)

3. In the third part, the tonnage extracted from the mine is calculated based on the grade of the ore, the weight of the extracted rock, and the recovery factor. The following formula is used here:

		tonnage = (grade*weight ore*recovery rate) / 1000000

4. In the fourth section, the mining rate is calculated based on the extracted tonnage and the number of working days per year. Formula used:

		Mining Rate = Total Tonnage / Working Day

5. The fifth item is the mining cost, calculated and displayed based on the mining rate, operating costs, and initial investment. To perform this calculation, the following three formulas are used:

		Annual Tonnage = Mining Rate*365

		Annual Operational Cost = Annual Tonnage * Operational Cost

		Total Cost = Annual Operational Cost + Initial Investment

6. The last item is mine profitability, calculated based on the selling price of minerals, the cost of extraction, and the extracted tonnage, and the result is displayed. For this case, the following two formulas are used:

			Total Revenue = Selling Price * Total Tonnage

			Profit = Total Revenue - Mining Cost

A function has been designed for each section and to prevent errors during execution, input control commands have been used because in each section it was necessary to enter a number or decimal number, and if the wrong data was entered, the calculations would not be performed correctly.


