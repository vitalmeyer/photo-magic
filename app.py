import glob
import vitalsModules
from pyhtml import *
import ntpath
from pathlib import Path

# Global var
PHOTO_FOLDER = Path("static/photos/")

# from flask import Flask
from flask import Flask, render_template, send_file

# set the project root directory as the static folder, you can set others.
# app = Flask(__name__, static_url_path='')
app = Flask(__name__, static_url_path='/static')
app.jinja_env.filters['zip'] = zip



#######
# web commands
#######

# default command
@app.route('/')
def hello_world():
    return "Hello World!"


# test pyhtml
@app.route('/pyhtml')
def hello_pyhtml():
    return get_pyhtml_dummypage()

# test yattag
@app.route('/yattag')
def hello_yattag():
    return get_yattag_dummypage()


# foo command
@app.route('/foo')
def hello_foo():
    photo_list = glob.glob("photos/*")
    print_log(photo_list)
    output_text = 'Hello World FOO!'
    for photo_name in photo_list:
        print_log(photo_name)
        output_text = output_text + photo_name
    return output_text


# bar command
@app.route('/bar')
def hello_bar():
    return 'Hello World BAR99!'

# photo template
@app.route("/photo")
def photo():

    list_photo_values_to_display = get_photo_values_for_display()

    # return render_template("photo.html", mylist = list_photo_values_to_display)
    print_log(str(list_photo_values_to_display))
    return render_template('photo.html', data=list_photo_values_to_display )



#######
# HELPER FUNCTIONS
#######
import glob


# simple logging routine
def print_log(text):
    print(">>> ", text)



# get one list with all photo names
def get_list_photo_names():
    photo_names = []
    for el in PHOTO_FOLDER.glob("*.jpg"): photo_names.append(el.name)
    return photo_names

def get_list_photo_urls():
    urls= []
    for el in PHOTO_FOLDER.glob("*.jpg"):
        filename = el.name
        url = PHOTO_FOLDER / filename
        urls.append(url)
    return urls

# get one list with all image_meta_data objects
def get_list_image_meta_data(list_photo_names):
    res_list = []
    for el in list_photo_names:
        path = PHOTO_FOLDER / el
        res_list.append(vitalsModules.ImageMetaData(el))
    return res_list



# list of photos and lag lng data...
def get_photo_list_lag_lng(photo_list):
    photo_list_lag_lng = []
    for el in photo_list:
        photo_list_lag_lng.append(el)
        photo_list_lag_lng.append (get_lat_lng_from_photo(el))
    return photo_list_lag_lng


# sollte JSON -formatiert sein (https://de.wikipedia.org/wiki/JavaScript_Object_Notation#Beispiel)
pics = """
{
    {Filename : <filename>
        {Lag: "33.2"}
        {Lng: "44.4"}
        {XXX: "foobar" }
    }
}
"""
# was ich brauche: URL, lag, lng in JSON,
# zusätzlich CENTER (mittelwert lag / lng),
# für jedes listenelement einen Icon / Marker...
# zoom-Wert ???
# ..
# json_input = '{"photos": [{"src": "static/foo.jpg", "lag": "3.4", lng: "5.5"},
#                           {"src": "static/bar.jpg", "lag": "3.5", lng: "5.6"}] }'
# --> unnötig hier...
# Dictionaries are built with curly brackets:
#
# d = {"a":1, "b":2}
# dic = {"src": {src}, "lag:": {lag}, "lng": {lng}}
# --> geht nicht gut...
# multidim arrays
# photosData = [[static/foo.jpg, 3.4, 5.5], [static/bar.jpg, 3.5, 5.6]]
# einfache lösung für mich!

# ALTERNATIVE
# Object welches Liste mit URLs, Liste mit LAG's und Liste mit LNG's etc enthält
# Lösung:
# Liste von "photo-objekten"
#

# howto get metadata from photo
def get_lat_lng_from_photo(photo_name):
    meta_data = vitalsModules.ImageMetaData(photo_name)
    # return "lat + lng = " + str(meta_data.get_lat_lng()) + " (...from " + photo_name + ")"
    # DateTime, ExifImageWidth, ExifImageHeight
    #
    # meta_data.get_exif_data()
    # {'GPSInfo': {'GPSLatitudeRef': 'N', 'GPSLatitude': ((45, 1), (44, 1), (251, 100)),
    # 'GPSLongitudeRef': 'E', 'GPSLongitude': ((4, 1), (51, 1), (4684, 100)),
    # 'GPSAltitudeRef': b'\x00', 'GPSAltitude': (30871, 178), 'GPSTimeStamp': ((12, 1), (45, 1), (1700, 100)),
    # 'GPSSpeedRef': 'K', 'GPSSpeed': (0, 1), 'GPSImgDirectionRef': 'T', 'GPSImgDirection': (469780, 1489),
    # 'GPSDestBearingRef': 'T', 'GPSDestBearing': (469780, 1489), 'GPSDateStamp': '2018:08:03',
    # 'GPSHPositioningError': (10, 1)}, 'ResolutionUnit': 2, 'ExifOffset': 208, 'Make': 'Apple',
    # 'Model': 'iPhone 6 Plus', 'Software': '11.4', 'Orientation': 6, 'DateTime': '2018:08:03 14:45:18',
    # 'YCbCrPositioning': 1, 'XResolution': (72, 1), 'YResolution': (72, 1), 'ExifVersion': b'0221',
    # 'ComponentsConfiguration': b'\x01\x02\x03\x00', 'ShutterSpeedValue': (26090, 2517),
    # 'DateTimeOriginal': '2018:08:03 14:45:18', 'DateTimeDigitized': '2018:08:03 14:45:18',
    # 'ApertureValue': (7983, 3509), 'BrightnessValue': (9311, 904), 'ExposureBiasValue': (0, 1), 'MeteringMode': 5,
    # 'Flash': 16, 'FocalLength': (83, 20), 'ColorSpace': 1, 'ExifImageWidth': 3264, 'DigitalZoomRatio': (72, 35),
    # 'FocalLengthIn35mmFilm': 59, 'SceneCaptureType': 0, 'ExifImageHeight': 2448, 'SubsecTimeOriginal': '242',
    # 'SubsecTimeDigitized': '242', 'SubjectLocation': (1626, 1220, 1790, 1076), 'SensingMethod': 2,
    # 'ExposureTime': (1, 1319), 'FNumber': (11, 5), 'SceneType': b'\x01', 'ExposureProgram': 2,
    # 'ISOSpeedRatings': 32, 'ExposureMode': 0, 'FlashPixVersion': b'0100', 'WhiteBalance': 0,
    # 'LensSpecification': ((83, 20), (83, 20), (11, 5), (11, 5)), 'LensMake': 'Apple', 'LensModel':
    # 'iPhone 6 Plus back camera 4.15mm f/2.2',
    # 'MakerNote': b'Apple iOS\x00\x00\x01MM\x00\x11\x00\x01\x00\t\x00\x00\x00\x01\x00\x00\x00\t\x00\x02\x00\
    # x07\x00\x00\x02.\x00\x00\x00\xe0\x00\x03\x00\x07\x00\x00\x00h\x00\x00\x03\x0e\x00\x04\x00\t\x00\x00\x00\x01\x00
    # ....

    return str(meta_data.get_lat_lng())

# key-value list, key = "photo name", val = "lat / lng tuple"
def get_photo_values_for_display():
    list_photo_name = get_list_photo_urls()
    list_image_meta_data = get_list_image_meta_data(list_photo_name)

    #return zip(list_photo_name,list_image_meta_data)
    lat_lng = []
    for image_meta_data in list_image_meta_data:
        lat_lng.append(image_meta_data.get_lat_lng())
    print_log("list_photo_name" + str(list_photo_name))
    print_log("lat_lng" + str(lat_lng))

    return zip(list_photo_name,lat_lng)

def test_list_access():
    data = get_photo_values_for_display()
    for n,v in zip(data[0::2], data[1::2]):
        print(  "n=", n, "v=", v, "v0=", v[0])


# test yattag
def get_yattag_dummypage():
    return "i don't like it...."


# test pyhtml
def get_pyhtml_dummypage():
    t = html(
        head(
            title('Awesome website'),
        ),
        body(
            header(

            ),
            div(
                'Content here'
            ),
            footer(
                hr,
                'Copyright 2013'
            )
        )
    )
    return t.render()

# logging

import logging
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/loggertest', methods=['GET'])
def loggertest():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')
    return "check your logs\n"


# call of main
if __name__ == '__main__':
    app.run(debug=True)

