import random
import ShowsData

Shows = ShowsData.Data

# Preparing query to send to the user
query = "What show do you want to watch? (enter number)\n"
for index in range(len(Shows)):
    query = query + "{}. {}\n".format(index + 1, Shows[str(index + 1)]['Name'])
query = query + "{}. Any\n".format(len(Shows) + 1)

# Get the episode based off the show
def getEpisode(episodes):
    season = random.randint(0, len(episodes['Seasons']) - 1)
    episode = random.randint(1, episodes['Seasons'][season])            
    print("Watching {} season {} episode {}".format(episodes['Name'], season + 1, episode))

def getShow():
    num = input(query)
    
    if len(num) == 0 or num == str(len(Shows) + 1):
        num = str(random.randint(1, len(Shows)))
    else: 
        try: 
            int(num)
        except ValueError:
            num = str(random.randint(1, len(Shows)))

    return Shows[num]

if __name__ == '__main__':
    getEpisode(getShow())
    while input("Input R to pick another show or enter to exit ...\n").upper() == "R":
        getEpisode(getShow())
