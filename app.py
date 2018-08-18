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
GOOGLE_API_KEY = app.config["GOOGLE_API_KEY"]


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

# photo template - some photo-icons in Lyon
@app.route("/photo01")
def photo01():
    google_api_key = GOOGLE_API_KEY
    list_photo_values_to_display = get_photo_values_for_display(PHOTO_FOLDER)

    # return render_template("photo01.html", mylist = list_photo_values_to_display)
    print_log(str(list_photo_values_to_display))
    return render_template('photo01.html', list_photo_values_to_display=list_photo_values_to_display,
                           google_api_key = google_api_key )

# photo template - a not-working structure CSS grid template (nav, header, footer, ....)
@app.route("/photo02")
def photo02():
    google_api_key = GOOGLE_API_KEY

    list_photo_values_to_display = get_photo_values_for_display(PHOTO_FOLDER)

    # return render_template("photo01.html", mylist = list_photo_values_to_display)
    print_log(str(list_photo_values_to_display))
    return render_template('photo02.html', list_photo_values_to_display=list_photo_values_to_display,
                           google_api_key = google_api_key )

# on-click - loading big photo
@app.route('/photo03')
def photo03():
    google_api_key = GOOGLE_API_KEY
    return render_template('photo03.html', google_api_key = google_api_key)

# some markers with listers, something is not working here...
@app.route('/photo04')
def photo04():
    google_api_key = GOOGLE_API_KEY
    return render_template('photo04.html', google_api_key = google_api_key)

# photo template - some photo-icons in Lyon
@app.route("/photo05")
def photo05():
    google_api_key = GOOGLE_API_KEY

    return render_template('photo05.html', list_photo_values_to_display=get_photo_values_for_display(PHOTO_FOLDER),
                           google_api_key = google_api_key )

# call of main
if __name__ == '__main__':
    app.run(debug=True)

