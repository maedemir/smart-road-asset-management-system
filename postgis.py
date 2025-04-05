import os
import pandas as pd
from exif import Image

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


def image_coordinates(image_path):
    with open(image_path, 'rb') as src:
        img = Image(src)
        if img.has_exif:
            try:
                coords = (decimal_coords(img.gps_latitude,
                          img.gps_latitude_ref),
                          decimal_coords(img.gps_longitude,
                          img.gps_longitude_ref))
            except AttributeError:
                print('No Coordinates')
        else:
            print('The Image has no EXIF information')
            print(f"Image {src.name}, OS Version:{img.get('software', 'Not Known')} ------")
    return coords


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import psycopg2
    conn = psycopg2.connect(database="B.sc db",
                            host="localhost",
                            user="postgres",
                            password="ur pass",
                            port="1478")
    cursor = conn.cursor()
    image_path = "/Users/maedehmirzazadeh/Downloads/final_dataset_merged/images"
    csv_files = "/Users/maedehmirzazadeh/Downloads/detection_results_csv"
    for file in os.listdir(csv_files):
        data = pd.read_csv(os.path.join(csv_files, file))
        for index, row in data.iterrows():
            img_name = row['ref-img'].split('/')[-1]
            print(img_name)
            ref_img = os.path.join(image_path, img_name)
            asset_location = image_coordinates(ref_img)
            asset_class = row['class']
            query = """  INSERT INTO assets_info(asset_ref_img, asset_class, geom)
                         VALUES(%s, %s, ST_GeomFromText('POINT(%s %s)', 4326));
                    """
            cursor.execute(query, (ref_img, asset_class, asset_location[1], asset_location[0]))
            conn.commit()
    conn.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
