import folium

# Create a Folium map centered around CU Boulder
cu_boulder_map = folium.Map(location=[40.0076, -105.2659], zoom_start=15)

# Allow users to add markers by double-clicking on the map
folium.ClickForMarker(popup='Add a Marker').add_to(cu_boulder_map)

# Save the map to an HTML file
cu_boulder_map.save("cu_boulder_map.html")

# Define a custom JavaScript callback
callback = ('''
            function (e) {
                var markerId = e.target._leaflet_id;
                removeMarker(markerId);
            }
            ''')

# Add the JavaScript callback to the map
#folium.map.Marker([40.0076, -105.2659], popup='Remove this marker by double-clicking').add_to(cu_boulder_map)
cu_boulder_map.get_root().add_child(folium.Element(callback))

# Save the map again with the added JavaScript callback
cu_boulder_map.save("cu_boulder_map.html")
