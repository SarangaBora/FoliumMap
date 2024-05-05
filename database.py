import mysql.connector

mydb= mysql.connector.connect(host='localhost',user='root',password='password',database='bus_info')
print(mydb.connection_id)

cur = mydb.cursor() # We need this to access or excute any DB SQL queries
cur.execute("CREATE  DATABASE IF NOT EXISTS bus_info")


# cur.execute("SELECT PickUp, Bus_name, Dropping FROM buses")
#  bus_stops = {}
#     for PickUp, Bus_name, Dropping in cur.fetchall():
#         if PickUp not in bus_stops:
#             bus_stops[PickUp] = {}
#         bus_stops [PickUp][Bus_name] = Dropping
    
#     # Close cursor and database connection
#     cur.close()
#     mydb.close()
#     return bus_stops



# # Add markers for bus stops
#     for stop, buses in bus_stops.items():
#         # Create popup content for bus stop
#         popup_content = f"<b>{stop}</b><br>"
#         for bus, destination_stop in buses.items():
#             popup_content += f"Bus: {bus}, Destination: {destination_stop}<br>"
        
#         # Add marker with popup
#         folium.Marker(location=(latitude, longitude), popup=popup_content).add_to(test_map)  # Replace latitude and longitude with actual coordinates
        

