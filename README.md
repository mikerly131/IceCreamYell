# IceCreamYell
a mystery dataset. what does it tell you?

The point of this lab is to examine a dataset (ice_cream.csv) and figure out what you can discover about it. 
You may have to research what terms are used in its description. (what's a dependent variable? predictor?)

Read the files presented here in the repo, esp the Ice_cream_data_description.rtf
What can you learn about the terms in the RTF. What do they mean.

Examine this data set. Load it into a python script and try to run some stat measures against it.

What interesting things can you discover about this data?

Things to Consider before starting
- How would you read it into memory using python?
  - with open csv file (file handler) and read in I think, ill start there
- What data structure would you use to handle the data?
  - Idea 1: Dictionary, Key: Row 0 values, Values: All rows of column as items in a DS, column is key
  - Idea 2: Dictionary, Keys: Each Row Value from Column 1, Values: Dictionary, Keys: Row 0 Column 2-5, Values: 
- What statistical measures might be helpful in understanding what the data is?
  - Find if there is a correlation between video game scores, gender, and favorite ice cream flavor
    - Look at average score in game by flavor, gender
    - Look at normal distribution and standard deviation for the flavor, gender combos
  - There is nothing causal to explore or prove
  - There is a significant sample data gap, around 4 years between collections.
  - Mess with dependent(?) variables - compare preferred flavor scores no gender, compare gender scores no flavor
- Can you see any relationships between the various columns?
  - See above, but probably will discover more.
- Do test scores and gender indicate anything about what kind of ice cream a person favors?
  - No, with only 200 people sample size, the confidence interval will be too wide to use it as a basis for the entire US or world population.

*Finally*: What can you do to present / communicate what you discovered about this dataset?

You might wish to use some functions from https://docs.python.org/3/library/statistics.html
