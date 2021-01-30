import requests, re
url = input("url>> ")
text = requests.get(url).text
url_pattern = r'\"fb://(.*?)\" />'
urls = re.findall(url_pattern, text) 
print("ID:", urls[0].replace("profile/", ""))