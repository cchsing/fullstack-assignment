# https://www.youtube.com/watch?v=sIOMDu6MXJQ

import requests
from bs4 import BeautifulSoup
import time


def main(*args, **kwargs):
    for i in range(1,3,1):
        url = "https://zuscoffee.com/category/store/melaka/page/" + str(i)
        print(url)

if __name__ == "__main__":
    main()