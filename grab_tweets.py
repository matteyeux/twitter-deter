"""Script used to grab all tweets from 2021-08-16 to 2021-08-19.
proudly written with vim."""

import configparser
import csv
import tweepy


def main():
    """main function."""
    # bring your own twitter API keys
    # https://developer.twitter.com/en/docs/apps/overview
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    # setup csv stuff, we'll write the
    # date, username and text to the CSV
    csv_file = open('tweets.csv', 'w')
    write_csv = csv.writer(csv_file)

    # loop through all pages
    for page in tweepy.Cursor(api.search,q="#PrimeVideoEvangelion",count=1000, since="2021-08-16", until="2021-08-19").pages():
        # write all tweets in pages to a csv file
        for tweet in page:
            print(f"{tweet.created_at} : {tweet.user.screen_name}   {tweet.text}")
            write_csv.writerow([tweet.created_at, tweet.user.screen_name, tweet.text.replace(',', ' ')])

    csv_file.close()
    print("done")

if __name__ == '__main__':
    main()
