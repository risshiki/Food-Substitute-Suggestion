# Food-Substitute-Suggestion
A co-ordinate geometrical approach to suggesting alternatives for food sources


Challenge associated with issue:
Simply suggesting food alternatives within a certain caloric range doesn’t work as calories can be obtained in multiple ways.

Approach 1 (Naïve) :

Set manual limits for the threshold of protein, carbs and fats. Process the entire list and insert values that fit all our parameters. Append values to entry if an entry already exists.
For any new entry, repeat the same process by parsing through the entire table.

First time complexity : O(N^2)
Insertion complexity : O(N)

Approach 2 (Uses 3-D Co-ordinate space) :

Project the values onto a 3-D Co-ordinate space using three arrays. Index the values by separating values into boxes of sizes X x Y x Z, where X,Y,Z represent thresholds for fat, protein and carbs respectively.
I would recommend to set the fat co-ordinate with a smaller threshold as it has a higher caloric value.

The first part of the equation would then look like

Cluster_id = Fat//X + Protein//Y + Carbs//Z
(Values used in code for X,Y,Z = 4:9:9 ; // signifies integer division)
This was done with the rationale that 4g of fat has the same value of calories as 9g of protein or 9g of carbs.)

However, this approach is still not complete as an object with say 4F,0C,0P can end up in the same group as an object with 0F,9P,0C.

That's where indexing comes in. By choosing a multiplier that exceeds the threshold for the maximum number of units in any given axis, you ensure that there's no overlap between groups.

So for instance, if a threshold size of 9 is selected for say, the carb axis, and the maximum value associated with that axis is 100, 100/9 is the theoretical max. Since this number is < 12, we will choose this as our indexing value.
When you apply the same principle again, we end up with a co-efficient of 144 for the final axis to differentiate between the 12x12 grid.
However, in practice, you can get away with any value beyond 100 for the final co-efficient.

The final equation in the code looks like this

Group_id = 144*Fat//X + 12*Protein//Y + Carbs//Z

Food groups are indexed on that basis.

While this approach works well with most inputs and inserts in O(1) time, a second alternative is being looked for as the code doesn't hold true 
if an item with a value greater than the largest macronutrient value of our food item is encountred.
