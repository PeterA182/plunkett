import os
import sys
import folium as fl
import datetime as dt
import pandas as pd

# --- --- ---
# Run Params
projDir = "/Users/peteraltamura/Documents/fun/plunkett/location/"
fname = "locations.csv"
outpath = "/Users/peteraltamura/Documents/fun/output/"


# --- --- ---
# Run
df_coords = pd.read_csv(projDir+fname)
print(df_coords.head())

# Instantiate Map
map = fl.Map()

# Begin Iterating over coordinates dataframe
locs = []
for i in range(df_coords.shape[0]):
    print(df_coords[['Lat', 'Lon']].iloc[i])    
    
    # Unpack Coordinates
    convLat = float(df_coords['Lat'].iloc[i].split("-")[0]) + \
            (float(df_coords['Lat'].iloc[i].split("-")[1][:2])/60)
    if df_coords['Lat'].iloc[i][-1:]=='S':
        convLat *= -1
    convLon = float(df_coords['Lon'].iloc[i].split("-")[0]) + \
            (float(df_coords['Lon'].iloc[i].split("-")[1][:2])/60)
    if df_coords['Lon'].iloc[i][-1:]=='W':
        convLon *= -1
    # add to locs
    locs.append((convLat, convLon))

    # Unpack Date
    date_ = df_coords['Date'].iloc[i]
    
    # Unpack time
    time_ = df_coords['Time'].iloc[i]

    # Unpack Notes
    notes = df_coords['Notes'].iloc[i] if str(df_coords['Notes'].iloc[i]) \
            != 'nan' else ''
    print(convLat, convLon, notes)

    html_ = """
        <div class="header">
        <h1>{}-{} USS Plunkett Log Notes</h1>
        </div>
    """.format(date_, time_)
    popup_ = fl.Popup(fl.IFrame(html=html_+notes, width=400, height=250), max_width=2650)

    # Make Marker
    currMarker = fl.Marker(
            [convLat, convLon],
            icon=fl.Icon(color='red', icon='hospital-symbol', prefix='fa'),
            popup=popup_
    ).add_to(map)

# Add Line

journey = fl.PolyLine(locs, color='red', weight=8, opacity=0.6).add_to(map)
    
if not os.path.exists(outpath):
    os.makedirs(outpath)
map.save(outpath+"PlunkettChart.html")
