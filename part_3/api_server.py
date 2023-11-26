import os, sqlite3
from fastapi import FastAPI

app = FastAPI()
path = __file__
parentDir = os.path.abspath(os.path.join(path, os.pardir, os.pardir))

@app.get('/stores')
def get_all_stores():
    conn = sqlite3.connect(os.path.join(parentDir,"zuscoffee.db"))
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM stores;")
    data = {'data': cursor.fetchall()}

    conn.commit()
    conn.close()
    return data

@app.get('/store/{name}')
def get_store_with_name(name):
    print(name)
    conn = sqlite3.connect(os.path.join(parentDir,"zuscoffee.db"))
    cursor = conn.cursor()

    sqlite_select = """SELECT *
                    FROM stores
                    WHERE
                        name = ?;
    """
    cursor.execute(sqlite_select, (name,))
    data = {'data': cursor.fetchall()}

    conn.commit()
    conn.close()
    return data

@app.get('/store/{name}/coordinate')
def get_coordinate_of_store_with_name(name):
    print(name)
    conn = sqlite3.connect(os.path.join(parentDir,"zuscoffee.db"))
    cursor = conn.cursor()

    sqlite_select = """SELECT gps_lattitude, gps_longitude
                    FROM stores
                    WHERE
                        name = ?;
    """
    cursor.execute(sqlite_select, (name,))
    data = {'data': cursor.fetchall()}

    conn.commit()
    conn.close()
    return data


def main(*args, **kwargs):
    pass

if __name__ == "__main__":
    main()