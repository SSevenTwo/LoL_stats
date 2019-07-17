import requests

print("**************************")
print("Solo Ranked Game Statistics of League of Legends (OCE)")
print("**************************")

while True:
    summoner = input("Who would you like to search? ('q' to quit) \n")
    if summoner.lower() == "q":
        print("Thank you for using the system.")
        break
    try:
        url_0 = "https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ summoner + "?api_key=RGAPI-57655c06-edcd-472c-8645-2480eee68dc5"
        r_0 = requests.get(url_0)
        api_dict = r_0.json()
    
        accountId = api_dict['id']
        accountId1 = api_dict['accountId']
    except:
        print("Summoner not found.\n")
        continue
    else:

        url_1 = "https://oc1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + accountId + "?api_key=RGAPI-57655c06-edcd-472c-8645-2480eee68dc5"
        r_1 = requests.get(url_1)
        ranked_stats = r_1.json()
    
        print("\n**************************")
        print("Statistics for " + summoner.title() )
        print("**************************")
        solo_queue = ranked_stats[1]
    
        print("Queue Type: ", solo_queue['queueType'])
        print("Rank: "+ solo_queue['tier'] + " "+ solo_queue['rank'])
        print("Wins: ", solo_queue['wins'])
        print("Losses: ", solo_queue['losses'])
        print("")
    
        print("Match History:\n")
        print("-To be implemented-\n")
    

    
    
