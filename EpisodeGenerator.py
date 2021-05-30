import random
import ShowsData

Shows = ShowsData.Data

def getEpisode(episodes):
    season = random.randint(0, len(episodes['Seasons']) - 1)
    episode = random.randint(1, episodes['Seasons'][season])            
    print("Watching {} season {} episode {}".format(episodes['Name'], season + 1, episode))

if __name__ == '__main__':
    query = "What show do you want to watch? (enter number)\n"
    for index in range(len(Shows)):
        query = query + "{}. {}\n".format(index + 1, Shows[str(index + 1)]['Name'])
    query = query + "{}. Any\n".format(len(Shows) + 1)
    num = input(query)
    
    if len(num) == 0 or num == str(len(Shows) + 1):
        num = str(random.randint(1, len(Shows)))
    else: 
        try: 
            int(num)
        except ValueError:
            num = str(random.randint(1, len(Shows)))

    show = Shows[num]
    showName = show['Name']        
    getEpisode(show)
