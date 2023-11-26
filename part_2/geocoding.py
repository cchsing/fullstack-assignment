import os, sqlite3
from geocoder import osm

path = __file__
parentDir = os.path.abspath(os.path.join(path, os.pardir, os.pardir))

def main(*args, **kwargs):
    conn = sqlite3.connect("zuscoffee.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM stores;")
    data = cursor.fetchall()
    
    for store in data:
        print(store)
        geocode_result = osm(store[1])
        if geocode_result.osm is None:
            continue
        longitude = geocode_result.osm['x']
        lattitude = geocode_result.osm['y']
        data_tuple = (lattitude, longitude, store[0])
        print(data_tuple)

        sqlite_update = """UPDATE stores
                        SET gps_lattitude = ?,
                            gps_longitude = ?
                        WHERE 
                            name = ?;
                        """
        cursor.execute(sqlite_update, data_tuple)

    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    main()