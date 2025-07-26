import time
import datetime
from ossapi import Ossapi
api = Ossapi('[redacted]','[redacted]') # how to set up https://github.com/tybug/ossapi
start_time = time.perf_counter()

Leaderboard_available = [1,2,3,4]
ranked_fine = [] #for checking if the map is DMCA'd in later days
approved_fine = []
loved_fine = []
qualified_fine = []
graved_fine = []
graved_dmca = []
dl_disabled = []
missing_content = []

def fetch_beatmapset(beatmap_id):
    try:
        return api.beatmapset(beatmap_id)
    except:
        pass
for i in range(1, 50): # change the range to whatever you want
    if i % 1000 == 0:
            print(f"the currrent ID is {i}")
    try:
        beatmapset = fetch_beatmapset(i)
        if not beatmapset:
            continue  # Skip if the beatmapset couldn't be fetched
            
        map_status = (api.beatmapset(i).ranked).value
        if beatmapset.availability.more_information:
            if map_status in Leaderboard_available:
                if beatmapset.availability.download_disabled:
                    dl_disabled.append(i)
                else:
                    missing_content.append(i)
            else:
                graved_dmca.append(i)
            
        elif map_status == 1:
            ranked_fine.append(i)
        elif map_status == 2:
            approved_fine.append(i)
        elif map_status == 3:
            qualified_fine.append(i)
        elif map_status == 4:
            loved_fine.append(i)
        else:
            graved_fine.append(i)

    except: # ctrl + C to interrupt the process in the cmd
        print(f"the currrent ID is {i}")
        break
    
print(f"Finished computing at {datetime.datetime.now()}")
with open('dmca.txt', 'w') as f:
    print('ranked \n', file = f)
    print(ranked_fine, file = f)
    print('\n approved \n', file = f)
    print(approved_fine, file = f)
    print('\n qualified \n', file = f)
    print(qualified_fine, file = f)
    print('\n loved \n', file = f)
    print(loved_fine, file = f)
    print('\n graved \n', file = f)
    print(graved_fine, file = f)
    print('\n graved dmca \n', file = f)
    print(graved_dmca, file = f)
    print('\n dl_disabled \n', file = f)
    print(dl_disabled, file = f)
    print('\n missing_content \n', file = f)
    print(missing_content, file = f)
    
end_time = time.perf_counter()
elapse_time = (end_time - start_time)/60
print(f'computation took {elapse_time:.2f} minutes')
