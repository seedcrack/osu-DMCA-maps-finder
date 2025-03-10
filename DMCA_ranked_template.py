from ossapi import Ossapi
api = Ossapi("[redacted]","[redacted]") # how to set up https://github.com/tybug/ossapi

Leaderboard_available = [1,2,3,4]
ranked_fine = [] # for checking if the map is DMCA'd in later days
approved_fine = []
loved_fine = []

def fetch_beatmapset(beatmap_id):
    try:
        return api.beatmapset(beatmap_id)
    except:
        pass
        
for i in range(0, 0): # change the range to whatever you want
    try:
        beatmapset = fetch_beatmapset(i)
        if not beatmapset:
            continue  # skip if the beatmapset couldn't be fetched  
        map_status = (api.beatmapset(i).ranked).value
        
        if map_status in Leaderboard_available:
            if beatmapset.availability.more_information:
                if beatmapset.availability.download_disabled:
                    print(f"DL_disabled : https://osu.ppy.sh/beatmapsets/{beatmapset.id}/  ")
                else:
                    print(f"Missing_content : https://osu.ppy.sh/beatmapsets/{beatmapset.id}/")
                    
            elif map_status == 1 or map_status == 3:
                ranked_fine.append(beatmapset.id)
            elif map_status == 2:
                approved_fine.append(beatmapset.id)
            elif map_status == 4:
                loved_fine.append(beatmapset.id)
        else:
            continue # skip if the map has no leaderboard
    except: # ctrl + C to interrupt the process in the cmd
        print(f"the currrent ID is {i}")
        break
    
print("Finished")
print(ranked_fine)
print()
print(approved_fine)
print()
print(loved_fine)
