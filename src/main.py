import folium

from data import coordinates_of_city, locations


def generate_map():
    # generate map of city
    city = folium.Map(location=coordinates_of_city, zoom_start=12)

    # generate group of markers
    markers = folium.FeatureGroup(name='Show markers', show=True).add_to(city)

    # create markers of locations
    for location in locations:
        folium.Marker(location=location["coordinates"], popup=location["descriptions"]).add_to(markers)
    folium.LayerControl().add_to(city)

    # create map of Nizhny_Novgorod in html file
    city.save('Nizhny_Novgorod.html')


if __name__ == "__main__":
    generate_map()
