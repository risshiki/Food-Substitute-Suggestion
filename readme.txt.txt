Code to effectively group items that had similar macronutrient ratios per 100g of weight.


Introduction :

S.Q.U.A.T.S, an online health service portal based out of Pune recently released a dataset of over 10,000 food items. Of this, I used a 3000 + food datasheet with a standardized weight of 100g and extracted that into Dataset.csv

An effective way to picture this problem is to visualize the items in three dimensions. Labeling Protein in the X axis, Carbs in the Y axis and Fats in the Z axis, you can plot the points on the co-ordinate axis and then group the items into rectangular subsets. However, since Fats are higher in caloric value than protein and carbs, it needs to be scaled accordingly.

In this case the threshold for fats was 4 whilst the threshold for carbs and 
protein was 9. This was to standardise the threshold for caloric content (36) when traversing through each box. A box of 9x9x4 can be visualized for each group.

The highest difference possible in each box is 108 calories [(0,0,0) and (9,9,4)]. However, most items fall well below that threshold.



