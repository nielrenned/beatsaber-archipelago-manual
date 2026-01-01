import json

with open('album_data.json') as f:
    album_data = json.load(f)

categories = {}
items = [
    {
		"name": "Bloq",
		"count": "30",
		"category": [
			"Bloqs"
		],
		"progression": True
	}
]
locations = [
	{
		"name": "Done!",
		"victory": True,
		"category": ["Victory"],
		"requires": "|Bloq:20|"
	}
]

for album_info in album_data:
    album_name = album_info['name']
    categories[album_name] = {'yaml_option': [album_name.replace('.', '').replace(' ', '_')]}
    for song_name in album_info['songs']:
        song_item_name = f'"{song_name}" Unlock'
        items.append({
            'name': song_item_name,
            'count': '1',
            'category': [
                'Song Unlocks',
                album_name
            ],
            'progression': True,
            'useful': True
        })
        locations.append({
            'name': f"{song_name} (Pass)",
            'category': [album_name],
            'requires': f"|{song_item_name}|"
        })
        locations.append({
            'name': f"{song_name} (A+ Ranking)",
            'category': [album_name],
            'requires': f"|{song_item_name}|"
        })

with open('categories.json', 'w') as f:
    json.dump(categories, f, indent=2)

with open('items.json', 'w') as f:
    json.dump(items, f, indent=2)

with open('locations.json', 'w') as f:
    json.dump(locations, f, indent=2)