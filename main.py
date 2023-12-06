import pandas as pd
class spotify_analysis:
    def __init__(self):
        """
        initialize the spotify_analysis class and imports the data into the class
        """
        self.spotify_data = pd.read_csv("spotify-2023.csv", encoding='latin-1')
    def clean_data(self):
        """
        Count the number of row for each year in the spotify dataset
        """
        spotify_data_year = self.spotify_data["released_year"].value_counts()

    def extract_2023_data(self):
        """
        create a mask and extract only the songs that are released in 2023
        """
        # Create a mask to filter songs released in 2023
        year_mask = self.spotify_data["released_year"] == 2023
        # Extract the songs for the year 2023
        self.year_df = self.spotify_data[year_mask]
        #print(year_df)
    def ranking_calculation(self):
        """
        calculate the ranking of the songs and ranked them based their scores
        """
        # Convert relevant columns to integers for calculations
        self.year_df.loc[:, "in_spotify_playlists"] = self.year_df["in_spotify_playlists"].astype(int)
        self.year_df.loc[:, "streams"] = self.year_df["streams"].astype(int)
        self.year_df.loc[:, "in_apple_playlists"] = self.year_df["in_apple_playlists"].astype(int)
        # Calculate the total score for each song
        self.year_df["total_score"] = self.year_df["in_spotify_playlists"]+self.year_df["streams"]+self.year_df["in_apple_playlists"]
        # Rank the songs based on their total score
        self.year_df["ranking"] = self.year_df["total_score"].rank()
        print(self.year_df)

# Example of how to use the class
analysis = spotify_analysis()
# Clean the data (counting songs for each release year)
analysis.clean_data()
# Extract songs released in 2023
analysis.extract_2023_data()
# Calculate rankings of songs for the extracted songs
analysis.ranking_calculation()

