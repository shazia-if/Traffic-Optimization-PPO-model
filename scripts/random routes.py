import random
import xml.etree.ElementTree as ET
from numpy.random import choice
import numpy as np


edges = {
    "top0": "A3",
    "top1": "B3",
    "top2": "C3",
    "top3": "D3",
    "bottom0": "A0",
    "bottom1": "B0",
    "bottom2": "C0",
    "bottom3": "D0",
    "left0": "A0",
    "left1": "A1",
    "left2": "A2",
    "left3": "A3",
    "right0": "D0",
    "right1": "D1",
    "right2": "D2",
    "right3": "D3"
}

adjacent = {
    "A0": ["A1", "B0", "left0", "bottom0"],
    "A1": ["A0", "A2", "B1", "left1"],
    "A2": ["A1", "A3", "B2", "left2"],
    "A3": ["A2", "B3", "left3", "top0"],
    "B0": ["A0", "B1", "C0", "bottom1"],
    "B1": ["A1", "B0", "B2", "C1"],
    "B2": ["A2", "B1", "B3", "C2"],
    "B3": ["A3", "B2", "C3", "top1"],
    "C0": ["B0", "C1", "D0", "bottom2"],
    "C1": ["B1", "C0", "C2", "D1"],
    "C2": ["B2", "C1", "C3", "D2"],
    "C3": ["B3", "C2", "D3", "top2"],
    "D0": ["C0", "D1", "right0", "bottom3"],
    "D1": ["C1", "D0", "D2", "right1"],
    "D2": ["C2", "D1", "D3", "right2"],
    "D3": ["C3", "D2", "right3", "top3"]
}


def generate_route():
    start_edge = random.choice(list(edges.keys()))
    point1 = start_edge
    point2 = edges[start_edge]
    old_point = None
    route = [f"{point1}{point2}"]

    while point2 not in edges.keys():
        old_point = point1
        point1 = point2
        next_points = [p for p in adjacent[point1] if p != old_point]
        point2 = random.choice(next_points)
        route.append(f"{point1}{point2}")
    return " ".join(route)

def generate_biased_route():
    Biased_Routes_1= ["left0A0 A0A1 A1A2 A2A3 A3top0", "bottom0A0 A0A1 A1A2 A2A3 A3top0",
                       "left2A2 A2B2 B2C2 C2C3 C3D3 D3right3",
                       "left2A2 A2B2 B2C2 C2C3 C3top2", "left2A2 A2A3 A3top0", 
                      "bottom0A0 A0A1 A1A2 A2B2 B2C2 C2C3 C3top2", 
                      "bottom0A0 A0A1 A1A2 A2B2 B2C2 C2C3 C3D3 D3right3"]
    #75% chance of picking 1st 3 routes
    #25% chance of picking last routes

    #chosen_route = random.choice(Biased_Routes_1, weights= ())
    chosen_route = choice(Biased_Routes_1, p=[0.25, 0.25, 0.25, 0.0625, 0.0625, 0.0625, 0.0625])

    return chosen_route



routes = ET.Element("routes", {
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xsi:noNamespaceSchemaLocation": "http://sumo.dlr.de/xsd/routes_file.xsd"
})


current_depart_time = 0.0
for vehicle_id in range(1, 120000):
    
    # route_edges = generate_route() 
    Bias =  random.choice([True, False]) # Set False for even traffic representation leave as it is for bias
    if Bias:
        route_edges = generate_biased_route()
    else:
        route_edges = generate_route()

    vehicle = ET.SubElement(routes, "vehicle", {
        "id": str(vehicle_id),
        "depart": f"{current_depart_time:.2f}"
    })
    
    route = ET.SubElement(vehicle, "route", {
        "edges": route_edges
    })
    
    current_depart_time += random.randint(2, 10) 
    # Set to 2, 10 for low traffic, set to 2,4 for heavy traffic, set to 1,3 for extra heavy traffic
    print(f"vehicle num {vehicle_id} generated")

random_int = random.random()
tree = ET.ElementTree(routes)
with open(f"routes120klowTraffic_Biased{random_int}.rou.xml", "wb") as f:
    tree.write(f, encoding='utf-8', xml_declaration=True)