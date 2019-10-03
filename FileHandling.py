import json

with open('output.json', 'r', encoding='utf8', errors='ignore') as json_file:  
    data = json.load(json_file)
    for tweet in data:
      if "goal" in tweet["text"]:
        print("Created at:", tweet['created_at'])
        print("Tweet:", tweet['text'])
        print(tweet['user']['name'])
        print()

with open("Something.txt","r") as f:
 content = f.read()
 if "1234" in content:
   print ("True")
   
with open("Something.txt","r") as f:
for line in f:
  print(line)
  
  with open ("Week","w") as f:
  f.write("Days of the week")
