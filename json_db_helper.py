import json
from datetime import datetime, timedelta

# Load the JSON file
with open(r'C:\Users\Kamila\OneDrive\Desktop\project-chores\data\chores.json', 'r') as f: 
    chores = json.load(f)

# Access chore "0"
chore0 = chores["18"]


together="{"
for key, item in chore0.items():
    if isinstance(item, str):
        line = '"'+str(key)+'":'+'{"S": "'+str(item)+'"},'
    else:
        line = '"'+str(key)+'":'+'{"N": "'+str(item)+'"},'

    together = together + line

together = together[:-1]+'}'
print(together)

