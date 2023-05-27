from pyrosm import OSM, get_data
import geopandas as gpd
import pandas as pd
from sklearn.neighbors import BallTree
import numpy as np
import mapclassify as mc
import matplotlib.pyplot as plt
import time
import networkx as nx
import igraph as ig
import osmnx as ox
import folium
import json

if name == "main":
    hospitals = json.loads("hospitals.json") # read from api hospitals list
    source_loc = (34.018255, -118.313290) # just for test you must get it from gps
    nearest_hospitals = []
    for hospital in hospitals:
        hospital_loc = (hospital['lat'], hospital['long'])
        hospital_score = hospital['score'] # this is score of hospital in api just for rating
        route, route_lenght, route_time = get_route(source_loc, hospital_loc)
        # route_lenght -> distance between us and hospital in meter
        # route_time   -> duration of startpoint to hospital in minutes
        # route        -> array of point by point to hospital 
        hospital_score -= (route_time * 5) # dec 5 score per minute to arrive at the hospital
        nearest_hospitals.append({'id':hospital['id'],'score': hospital_score})
    newlist = sorted(nearest_hospitals, key=lambda d: d['score'], reverse=True) 
    print(newlist)
    # new list is most populer and nearst hospital from start point