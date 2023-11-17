import pandas as pd
from tabulate import tabulate


"""
EDA on data set of students who selected a favorite ice cream and were scored on a puzzle and video game test
Using pandas (DataFrames & Series for data analysis) and tabulate (output formatting)
There will be heavy commenting throughout, spreading this out over a few days and need to keep continuity
The rtf supplied provides the key info for what columns, values and types are in the data set
"""

# For beginners purpose, assume/use clean, whole dataset
csv_file = pd.read_csv('ice_cream.csv')
csv_file2 = pd.read_csv('ice_cream.csv')

# Helpful methods
# csv_file.info() -> either that or print will print out all the values
# csv_file.head() -> can put an integer in there, or defaults 5 - gets top X columns/rows of data

# I can make each column of data a Series object, analysis/manipulation methods provided by pandas
# This might be useful...but I paused this idea to start simple with the DataFrame object
student_ids = csv_file['id']
genders = csv_file['female']
favorite_ice_cream = csv_file['ice_cream']
video_game_scores = csv_file['video']
puzzle_scores = csv_file['puzzle']

# Headers - 0th Column from CSV file
# I want to give them more meaningful names, a list might work, but pandas has some methods as well
# headers = pd.DataFrame(csv_file.columns)
# headers = ['Student ID', 'Gender', 'Favorite Ice Cream', 'Video Game Score', 'Puzzle Score']

# headers.rename() -> This will modify the same original series or dataframe, not make it a new list.
# The below function .columns grabs row 0th from csv_file and assigns new values.
csv_file.columns = ['Student_ID', 'Gender', 'Favorite_Ice_Cream', 'Video_Game_Score', 'Puzzle_Score']

# DataFrame - Reassigning data values, providing better context for humans
# Replace the values in gender ('female' column) with 0 = Male and 1 = Female
# csv_file["Gender"] = csv_file["Gender"].replace({0: "male", 1: "female"})

# Replace the values in Favorite_Ice_Cream ('ice_cream' column) with vanilla, chocolate and strawberry
# csv_file["Favorite_Ice_Cream"] = csv_file["Favorite_Ice_Cream"].replace({3: "Strawberry", 2: "Chocolate", 1: "Vanilla"})

# For tabulate, set changed DataFrame to a fresh variable
# This is one way, but uses another variable: for_tabulate_csv_file = pd.DataFrame(csv_file)

# For tabulate, make a method to call to print it out,  it to a function
def print_tabulate_table(df, format):

    print(tabulate(df, headers="keys", tablefmt=format))


# Print out DataFrame of CSV file with renamed keys (column 0) and values
# print_tabulate_table(csv_file, "simple")

# Variables, Dependent: Favorite_Ice_Cream, Independent: Gender, Puzzle_Score, Game_Score
# A dependent variable would be one that should not change...narrows what I should cacluate
# An independent variable is the one that varies...which can be done with favorite ice cream

# Try one mean comparison for favorite ice cream and mean score..
# This means: Can a students favorite ice cream predict a better average video game score
avg_ic_video_score = csv_file.groupby("Favorite_Ice_Cream").Video_Game_Score.mean().reset_index()
print_tabulate_table(avg_ic_video_score, "simple")
print('*' * 20)

avg_ic_puzzle_score = csv_file.groupby("Favorite_Ice_Cream").Puzzle_Score.mean().reset_index()
print_tabulate_table(avg_ic_puzzle_score, "simple")
print('*' * 20)

avg_ic_gender = csv_file.groupby("Favorite_Ice_Cream").Gender.mean().reset_index()
print_tabulate_table(avg_ic_gender, "simple")
print('*' * 20)

# What other statistics should I check?  Std dev? norm dist?


"""
Example from Imir white boarding
# Avg video game score for each gender by flavor
avg_gender_video_score = csv_file.groupby(["Gender", "Favorite_Ice_Cream"]).Video_Game_Score.mean().reset_index()
print(avg_gender_video_score)
"""


"""
Probably don't need this - we aren't after score by gender.
# Avg video game score for each gender
avg_gender_video_score = csv_file.groupby("Gender").Video_Game_Score.mean().reset_index()
print(avg_gender_video_score)
"""

"""
# TO USE - change the names to the renamed column name if declaring after changing columns...duh Mike
student_ids = csv_file['id']
genders = csv_file['female']
favorite_ice_cream = csv_file['ice_cream']
video_game_scores = csv_file['video']
puzzle_scores = csv_file['puzzle']

# Multi-column operation
male_vanilla = csv_file[(csv_file.female == 0) & (csv_file.ice_cream == 1)]
mean_vgs_male_vanilla = male_vanilla.video.mean()
mean_ps_male_vanilla = male_vanilla.puzzle.mean()
print(mean_vgs_male_vanilla)
print(mean_ps_male_vanilla)
"""


"""
# Not Sure - Series or DataFrame of mean score for each game
mean_vgs = video_game_scores.mean()
mean_puzzle_scores = puzzle_scores
"""

"""
# Mean Score for Each Game by Gender DataFrames
avg_vgs_by_ice_cream = csv_file.groupby('ice_cream').video.mean()
avg_vgs_by_gender = csv_file.groupby('female').video.mean()
avg_puzzle_by_ice_cream = csv_file.groupby('ice_cream').puzzle.mean()
avg_puzzle_by_gender = csv_file.groupby('female').puzzle.mean()
"""


"""
# Get the mean score by gender for video games
find_mgs_by_gender_df = csv_file[['id', 'female', 'video']]
print(find_mgs_by_gender_df)
mgs_by_gender_df = find_mgs_by_gender_df.groupby(csv_file.female == 0).video.mean()
print(mgs_by_gender_df)
"""

"""
# Get the mean score by gender for video games by ice cream
find_mgs_by_gender_df = csv_file[['id', 'female', 'video', 'ice_cream']]
print(find_mgs_by_gender_df)

mgs_by_gender_df = find_mgs_by_gender_df.groupby(csv_file.female == 0).video.mean()
print(mgs_by_gender_df)

mgs_by_gender_by_ice_cream_df = mgs_by_gender_df.groupby(csv_file.ice_cream).video.mean()
print(mgs_by_gender_by_ice_cream_df)
"""
