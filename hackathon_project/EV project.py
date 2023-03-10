#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import haversine as hs
import webbrowser

ev_dict=[*csv.DictReader(open(r"EV_location.csv"))]
#fuction to sort two of the nearsest EV charging stations from your current location
def top_two_ev(flat, flong):
    
    loc1 = (float(flat), float(flong))
    rows, cols = (len(ev_dict),2)
    arr = []    
    i = 0
    for j in range(len(ev_dict)):           
        loc2 = (float(ev_dict[i]['lat']),float(ev_dict[i]['long']) )
        dist = hs.haversine(loc1,loc2)*1.2
        arr.insert(j,[i,dist])
        i=i+1
    arr.sort(key=lambda arr:arr[1])

    return arr[0], arr[1]
# function to change the car battery percentage into distance
def bat_dist(fbat):
    b_dist = float(fbat) * 4

    return b_dist

with open(r"current_location.csv") as current_location:
   csv_reader = csv.reader(current_location)
   for index, row in enumerate(csv_reader):   
        lat = row[1]
        long = row[2]
        bat = row[3]
        evs = top_two_ev(lat, long)
        car_dist = bat_dist(bat)

            
        if (evs[0][1])>car_dist:
            print("The car's current location is " + lat+ ", "+ long)
            print("Car cannot reach the nearsest authorized EV station. Use your mobile charging Kit")
            print("\n\n")
        elif (evs[1][1]> car_dist):
            ev_index = evs[0][0]
            maps = "https://www.google.com/maps?q=" + ev_dict[ev_index]['lat'] + ','+ev_dict[ev_index]['long']
            print("The car's current location is " + lat+ ", "+ long)
            print("Go to " + ev_dict[ev_index]['cs']+ " for charging.")
            print("This charging station is " + str(int(evs[0][1])) + " km away from your current location" )
            print("Coordinates of charging station are "+ ev_dict[ev_index]['lat'] + ', '+ev_dict[ev_index]['long'])
            print("\n\n")
            #It will open the live locations of the EV charging stations
            webbrowser.open(maps)
            
        else:
            print(" ")
                    


# In[ ]:




