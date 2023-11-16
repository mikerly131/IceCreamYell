import pandas as pd

# For beginners purpose, assume/use clean, whole dataset
csv_file = pd.read_csv('ice_cream.csv')

# Headers - Column names from CSV
# headers = pd.DataFrame(csv_file.columns)
headers = ['Student ID', 'Gender', 'Favorite Ice Cream', 'Video Game Score', 'Puzzle Score']

# Each column is now a pandas series
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
