import folium
import os



if __name__ == "__main__":
    m_path = 'map1.htm'
    map_location=[26.171838, 91.768723]
    test_map = folium.Map(map_location, zoom_start=14.14, zoom_control=False,scroll_wheel_zoom=False)
    test_map.save(m_path)

# # Create a map
# map = folium.Map(location=[26.171838, 91.768723], zoom_start=15, zoom_control=False)

# # Specify the full path where you want to save the HTML file
# path = 'map1.html'

# try:
#     # Save the map to the HTML file
#     map.save(path)
#     print("Map HTML file saved successfully.")
# except Exception as e:
#     print("Error occurred while saving the map HTML file:", e)
