import datetime

today = datetime.datetime.now()

filename_prefix = today.strftime("%m-%d-%Y")

new_leaflet_filename = f"{filename_prefix}-leaflet.html"

new_links = open("link-list.html", "r")

template = open("leaflet.html", "r")