import json

with open("export.geojson", "r", encoding="utf8") as file:
    data = json.loads(file.read())

for obj in data['features']:
    if 'name' not in obj['properties']:
         obj['properties']['name'] = obj['id']

    
with open("map_data.geojson", "w", encoding="utf8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

