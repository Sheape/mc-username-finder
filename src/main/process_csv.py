import pandas as pd
import requests
import time

CSV_PATH = "~/Documents/data/csv/unigram_freq.csv"
MOJANG_API_URL = "https://api.mojang.com/users/profiles/minecraft/"
AMOUNT = 5000  # Amount of usernames that you want to check

import_words = pd.read_csv(CSV_PATH)
words_df = pd.DataFrame(import_words, columns=["word"]).head(AMOUNT)

valid_usernames = []

# Infinite Loop
i = 0
while i <= 10:
    for index, row in words_df.iterrows():
        r = requests.get(MOJANG_API_URL + row["word"])

        if r.status_code == 200 or len(row["word"]) <= 2:
            pass
        elif r.status_code == 204:
            print("Username is valid!!")
            print("Adding " + row["word"] + " to the list!!")
            valid_usernames.append(row["word"])
            print(valid_usernames)
        time.sleep(1)  # To comply with 600 Request per 10 min
