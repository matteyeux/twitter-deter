# twitter-deter

scripts pour le concours de rebeu deter sur Twitter

### grab_tweets.py

Script qui recupère tous les tweets qui contiennent le hashtag `#PrimeVideoEvangelion` entre les dates 2021-08-16 et 2021-08-18 (à 23:57:32).

Pour recupérer les tweets on utilise [tweepy](https://docs.tweepy.org/en/stable/).

Pensez à fournir vos access token pour l'API de Twitter.


### chose_winner.py

Script qui fais un random entre 0 et le nombre de lignes du CSV et qui affiche le gagnant (date, username, text)


---

Tous les tweets récuperés sont dans `tweets.csv`.
