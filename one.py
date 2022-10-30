import os
import time
import requests
import sys

print("hello")


def retrieve_html():
    for year in range(2013, 2022):
        for month in range(1, 13):
            url = f'https://en.tutiempo.net/climate/{month:02d}-{year}/ws-432950.html'

        texts = requests.get(url)
        text_utf = texts.text.encode('utf-8')

        if not os.path.exists("./Data/Html_Data/{}".format(year)):
            os.makedirs("./Data/Html_Data/{}".format(year))
        with open("./Data/Html_Data/{}/{}.html".format(year, month), "wb") as output:
            output.write(text_utf)

        sys.stdout.flush()


if __name__ == "__main__":
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print("time taken {}".format(stop_time-start_time))
