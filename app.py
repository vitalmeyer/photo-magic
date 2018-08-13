from pathlib import Path
import logging

from helpers import get_photo_values_for_display, print_log
from simpletests import get_pyhtml_dummypage
from flask import Flask, render_template


# set the project root directory as the static folder, you can set others.
# app = Flask(__name__, static_url_path='')
app = Flask(__name__, static_url_path='/static')
# config file
app.config.from_object('config')
# logging
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
# Global var
PHOTO_FOLDER = Path(app.config["PHOTO_FOLDER_PATH"])


#######
# web commands
#######
@app.route('/loggertest', methods=['GET'])
def loggertest():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')
    return "check your logs\n"

# default command
@app.route('/')
def hello_world():
    return "Hello World!"
# bar command
@app.route('/bar')
def hello_bar():
    return 'Hello World BAR99!'
# test pyhtml
@app.route('/pyhtml')
def hello_pyhtml():
    return get_pyhtml_dummypage()


# photo template
@app.route("/photo")
def photo():

    list_photo_values_to_display = get_photo_values_for_display(PHOTO_FOLDER)

    # return render_template("photo.html", mylist = list_photo_values_to_display)
    print_log(str(list_photo_values_to_display))
    return render_template('photo.html', data=list_photo_values_to_display )

# photo template
@app.route("/photo2")
def photo2():

    list_photo_values_to_display = get_photo_values_for_display(PHOTO_FOLDER)

    # return render_template("photo.html", mylist = list_photo_values_to_display)
    print_log(str(list_photo_values_to_display))
    return render_template('photo2.html', data=list_photo_values_to_display )


# call of main
if __name__ == '__main__':
    app.run(debug=True)

