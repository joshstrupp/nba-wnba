## Method

**Below is a brief description of how I identified similarities and created stat match scores**

The method starts with the .py script available in this repository. It first looks at player A's stats and standardizes them against every player in player A's league. The process is then repeated for player B for player B's league. Now, you have - relative to their respective leagues - 22 standardized stats for player A and 22 standardized stats for player B. Note that this factors in not how closely the numbers themselves align (e.g. player A with 20 points and player B with 20 points would be closely matched), but how their number align relative to their league (if a player A was the #1 scorer in their league with 20 points per game, and player B was the #1 scorer in their league with 35 points per game, they'd be closely matched).

The scores are generated then by taking the absolute value of player A's standardized minus player B's standardized stats. So if player A has a value of 2 for "PTS" and player B has a value of 3 in the same stat, the correlation number is 1. The closer to 0 a stat value is, the more similar they are. 

Numbers were converted into percentages for readability within Excel.
