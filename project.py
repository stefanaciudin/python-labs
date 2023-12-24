import requests
import folium
import json


def get_photos(tag, count, output_file="outputdata.json"):
    url = 'https://api.flickr.com/services/rest/'
    params = {
        'method': 'flickr.photos.search',
        'api_key': 'a7d50a45916d6f2daaf0eaa86801addf',
        'tags': tag,
        'format': 'json',
        'nojsoncallback': 1,
        'sort': 'date-posted-desc',
        'per_page': 500,
        'extras': 'geo'
    }
    response = requests.get(url, params=params)
    data = response.json()
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(data, f)

    photos = data['photos']['photo']

    filtered_photos = [photo for photo in photos if 'latitude' in photo and 'longitude' in photo]
    placed = 0
    locations_map = folium.Map(location=[0, 0], zoom_start=2)

    coordinate_counter = {}
    for photo in filtered_photos:
        if placed == count:
            break
        coordinate = (photo['latitude'], photo['longitude'])
        if photo['latitude'] != 0 and photo['longitude'] != 0:
            if coordinate not in coordinate_counter:
                coordinate_counter[coordinate] = 1
            else:
                coordinate_counter[coordinate] += 1

            marker_popup = f"Coordinates: {coordinate}<br>Photo IDs: {', '.join(str(photo['id']) for photo in filtered_photos if (photo['latitude'], photo['longitude']) == coordinate)}"
            folium.Marker(
                location=[float(photo['latitude']), float(photo['longitude'])],
                popup=marker_popup
            ).add_to(locations_map)
            print(f"{placed}: Placed photo with id:{photo['id']}, coordinates: {coordinate}")
            placed += 1

    return locations_map


t = input("Enter the tag: ")
cnt = int(input("Enter the count: "))

generated_map = get_photos(t, cnt)
generated_map.save('map.html')
