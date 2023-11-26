import os, requests, sqlite3, re
from bs4 import BeautifulSoup

path = __file__
parentDir = os.path.abspath(os.path.join(path, os.pardir, os.pardir))



def main(*args, **kwargs):
    conn = sqlite3.connect("zuscoffee.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stores (
                   name TEXT NOT NULL UNIQUE,
                   address TEXT NOT NULL UNIQUE,
                   googlemap_url TEXT NOT NULL UNIQUE,
                   gps_lattitude FLOAT,
                   gps_longitude FLOAT);
    """)

    count = 0
    for i in range(1,3,1):
        url = "https://zuscoffee.com/category/store/melaka/page/" + str(i)

        r = requests.get(url=url)
        soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.find_all("article", {"class":["elementor-post","elementor-grid-item","ecs-post-loop"]})
        
        for article in articles:
            
            googlemap = article.find('a','premium-button')
            if googlemap is None:
                continue
            else:
                count+=1

            title = article.find('p', 'elementor-heading-title')
            address = article.select('p:not(.elementor-heading-title)')

            store_name = title.text
            store_address = re.search(pattern=r"^<p>(.+?)</p>$", string=str(address[0])).groups()[0]
            googlemap_url = googlemap['href']

            print("#"*10+" "*3+str(count)+" "*3+"#"*10)
            print(store_name)
            print(store_address)
            print(googlemap_url)
            print("-"*50)

            sqlite_insert = """INSERT INTO stores (name, address, googlemap_url)
                           VALUES(?,?,?);"""
            data_tuple = (store_name, store_address, googlemap_url)
            cursor.execute(sqlite_insert, data_tuple)

    conn.commit()
    conn.close()

    
if __name__ == "__main__":
    main()