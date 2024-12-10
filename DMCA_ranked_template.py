from ossapi import Ossapi
api = Ossapi("[redacted]","[redacted]")

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
            continue  # Skip if the beatmapset couldn't be fetched
        if (api.beatmapset(i).ranked).value in Leaderboard_available:
            if beatmapset.availability.more_information:
                if beatmapset.availability.download_disabled:
                    print(f"DL_disabled : https://osu.ppy.sh/beatmapsets/{beatmapset.id}/  ")
                else:
                    print(f"Missing_content : https://osu.ppy.sh/beatmapsets/{beatmapset.id}/")
            elif (api.beatmapset(i).ranked).value == 1 or 3:
                ranked_fine.append(beatmapset.id)
            elif (api.beatmapset(i).ranked).value == 2:
                approved_fine.append(beatmapset.id)
            elif (api.beatmapset(i).ranked).value == 4:
                loved_fine.append(beatmapset.id)
    except: # ctrl + C to interrupt the process in the cmd
        print(f"the currrent ID is {i}")
        break
    
print("Finished")
print(ranked_fine)
print()
print(approved_fine)
print()
print(loved_fine)
