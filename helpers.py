from pathlib import Path

from models import ImageMetaData


def get_photo_values_for_display(photo_folder):
    list_photo_name = get_list_photo_urls(photo_folder)
    list_image_meta_data = get_list_image_meta_data(list_photo_name)

    #return z    ip(list_photo_name, list_image_meta_data)
    lat_lng = []
    for image_meta_data in list_image_meta_data:
        lat_lng.append(image_meta_data.get_lat_lng())
    print_log("list_photo_name" + str(list_photo_name))
    print_log("lat_lng" + str(lat_lng))

    return zip(list_photo_name,lat_lng)


def print_log(text):
    print(">>> ", text)


def get_list_photo_urls(photo_folder):
    urls= []
    for el in photo_folder.glob("*.jpg"):
        filename = el.name
        url = photo_folder / filename
        urls.append(url)
    return urls


def get_list_photo_names(photo_folder):
    photo_names = []
    for el in photo_folder.glob("*.jpg"): photo_names.append(el.name)
    return photo_names


def get_list_image_meta_data(list_photo_names):
    res_list = []
    for el in list_photo_names:
        res_list.append(ImageMetaData(el))
    return res_list


def get_photo_list_lag_lng(photo_list):
    photo_list_lag_lng = []
    for el in photo_list:
        photo_list_lag_lng.append(el)
        photo_list_lag_lng.append (get_lat_lng_from_photo(el))
    return photo_list_lag_lng





def get_lat_lng_from_photo(photo_name):
    meta_data = ImageMetaData(photo_name)
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