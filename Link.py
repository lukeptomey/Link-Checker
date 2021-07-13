import requests
ccfile = open("List.txt", "r")

for aline in ccfile:
    try:
        request = requests.get(aline, timeout=30)
        
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error.\n Link: ", aline)        
        continue
    except requests.Timeout as e:
        print("OOPS!! Timeout Error. \n Link: ",aline)
        continue
    except requests.RequestException as e:
        print("OOPS!! Not Link.\n Link: ",aline)
        continue
    except KeyboardInterrupt:
        print("Someone closed the program")

ccfile.close()