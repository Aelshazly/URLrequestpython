import urllib.request

webUrl = urllib.request.urlopen('https://www.watch2gether.com/')

print("result code: " + str(webUrl.getcode()))

data = webUrl.read()
print(data)
