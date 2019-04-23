# import requests 
# url = ’https://54qhf521ze.execute -api.eu-north -1.amazon aws.com/weather/stockholm/’ 
# r = requests.get(url) 
# response_dictionary = r.json() 
# # Nu inneh˚aller response_dictionary objektet vi # h¨amtade fr˚an API:et. 
# print(response_dictionary)

# print("Ange ett positivt heltal")
# användarenstal=input()
# användarenstal=int(användarenstal)
# if användarenstal % 2== 0:
#     print(användarenstal)
import requests
url = ’https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm’ 
r = requests.get(url)
response_dictionary = r.json() 
# Nu inneh˚aller response_dictionary objektet vi # h¨amtade fr˚an API:et. 
print(response_dictionary)