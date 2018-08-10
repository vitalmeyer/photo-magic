import glob
import vitalsModules
from pyhtml import *

# from flask import Flask
from flask import Flask, render_template, send_file

# set the project root directory as the static folder, you can set others.
# app = Flask(__name__, static_url_path='')
app = Flask(__name__, static_url_path='/static')


#######
# web commands
#######


# default command
@app.route('/')
def hello_world():
    photo_name = 'static\\photos\\2018-08-03 14.45.18.jpg'
    return get_lat_lng_from_photo(photo_name)


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
    return render_template("photo.html")


#######
# HELPER FUNCTIONS
#######


# simple logging routine
def print_log(text):
    print(">>> ", text)

# one list with all photo names
photo_list = glob.glob('static/photos/*.jpg')

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

# howto get metadata from photo
def get_lat_lng_from_photo(photo_name):
    meta_data = vitalsModules.ImageMetaData(photo_name)
    # return "lat + lng = " + str(meta_data.get_lat_lng()) + " (...from " + photo_name + ")"
    return str(meta_data.get_lat_lng())


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

