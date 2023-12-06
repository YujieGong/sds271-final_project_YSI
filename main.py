import pandas as pd
class spotify_analysis:
    def __init__(self):
        self.spotify_data = pd.read_csv("spotify-2023.csv", encoding='latin-1')
    def clean_data(self):
        spotify_data_year = self.spotify_data["released_year"].value_counts()

    def extract_2023_data(self):
        year_mask = self.spotify_data["released_year"] == 2023
        self.year_df = self.spotify_data[year_mask]
        #print(year_df)
    def ranking_calculation(self):
        self.year_df.loc[:, "in_spotify_playlists"] = self.year_df["in_spotify_playlists"].astype(int)
        self.year_df.loc[:, "streams"] = self.year_df["streams"].astype(int)
        self.year_df.loc[:, "in_apple_playlists"] = self.year_df["in_apple_playlists"].astype(int)
        self.year_df["total_score"] = self.year_df["in_spotify_playlists"]+self.year_df["streams"]+self.year_df["in_apple_playlists"]
        self.year_df["ranking"] = self.year_df["total_score"].rank()
        print(self.year_df)


analysis = spotify_analysis()
analysis.clean_data()
analysis.extract_2023_data()
analysis.ranking_calculation()

