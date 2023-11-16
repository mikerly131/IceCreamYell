import pandas as pd

# For beginners purpose, assume/use clean, whole dataset
csv_file = pd.read_csv('ice_cream.csv')
headers = pd.DataFrame(csv_file.columns)

student_ids = csv_file['id']
genders = csv_file['female']
favorite_ice_cream = csv_file['ice_cream']
video_game_scores = csv_file['video']
puzzle_scores = csv_file['puzzle']

mean_vgs = video_game_scores.mean()
mean_puzzle_scores = puzzle_scores

avg_vgs_by_ice_cream = csv_file.groupby('ice_cream').video.mean()
avg_vgs_by_gender = csv_file.groupby('female').video.mean()
avg_puzzle_by_ice_cream = csv_file.groupby('ice_cream').puzzle.mean()
avg_puzzle_by_gender = csv_file.groupby('female').puzzle.mean()


print(avg_vgs_by_ice_cream)
print(avg_vgs_by_gender)
print(avg_puzzle_by_ice_cream)
print(avg_puzzle_by_gender)
