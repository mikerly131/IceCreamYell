import pandas as pd
from tabulate import tabulate


# get tabulate module -> has a bunch of format for outputting final data

# For beginners purpose, assume/use clean, whole dataset
csv_file = pd.read_csv('ice_cream.csv')

# csv_file.info() -> either that or print will print out all the values
# ic.head() -> can put an integer in there, or default 5 - gets top X columns/rows of data

student_ids = csv_file['id']
genders = csv_file['female']
favorite_ice_cream = csv_file['ice_cream']
video_game_scores = csv_file['video']
puzzle_scores = csv_file['puzzle']

# Headers - Column names from CSV
# Grabs heading column and renames it, changes it to list
headers = pd.DataFrame(csv_file.columns)
headers = ['Student ID', 'Gender', 'Favorite Ice Cream', 'Video Game Score', 'Puzzle Score']
# headers.rename() -> use this to modify the same original series or dataframe
csv_file.columns = ['Student_ID', 'Gender', 'Favorite_Ice_Cream', 'Video_Game_Score', 'Puzzle_Score']
print(csv_file.columns)

# Renaming data in data frame
# Replace the values in gender ('female' column) with 0 = Male and 1 = Female
csv_file["Gender"] = csv_file["Gender"].replace({0: "male", 1: "female"})

# Renaming is for presenting data in understandable way
# Replace the values in gender ('female' column) with 0 = Male and 1 = Female
csv_file["Favorite_Ice_Cream"] = csv_file["Favorite_Ice_Cream"].replace({3: "Strawberry", 2: "Chocolate", 1: "Vanilla"})

# For tabulate, set changed DataFrame to a fresh variable
for_tabulate_csv_file = pd.DataFrame(csv_file)

# For tabulate, make a method to call to print it out,  it to a function
def print_tabulate_table(df, format):
    print(tabulate(df, headers="Keys", tablefmt=format))


# Avg video game score for each gender
avg_gender_video_score = csv_file.groupby("Gender").Video_Game_Score.mean().reset_index()
print(avg_gender_video_score)

# Avg video game score for each gender by flavor
avg_gender_video_score = csv_file.groupby(["Gender", "Favorite_Ice_Cream"]).Video_Game_Score.mean().reset_index()
print(avg_gender_video_score)




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
