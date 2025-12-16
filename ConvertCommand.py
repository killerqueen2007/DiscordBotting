import json

def convert_interaction(json_input):
    original = json.loads(json_input)

    def stringify_options(options):
        new_options = []
        for opt in options:
            new_opt = opt.copy()
            if isinstance(new_opt.get("value"), bool):
                new_opt["value"] = str(new_opt["value"]).lower()
            new_options.append(new_opt)
        return new_options

    options = stringify_options(original["data"].get("options", []))

    NeededJson = {
        "type": original["type"],
        "application_id": original["application_id"],
        "guild_id": original["guild_id"],
        "channel_id": original["channel_id"],
        "session_id": original["session_id"],
        "data": {
            "id": original["data"]["id"],
            "version": original["data"]["version"],
            "name": original["data"]["name"],
            "options": options if options else []
        },
        "nonce": "str(random.randint(1111111111111, 9999999999999))",
        "analytics_location": original.get("analytics_location", "slash_ui")
    }

    print("\n\npayload = {")
    for k, v in NeededJson.items():
        if isinstance(v, dict):
            print(f'    "{k}": {json.dumps(v, indent=8)},')
        elif isinstance(v, str) and v.startswith("str(random"):
            print(f'    "{k}": {v},')
        else:
            print(f'    "{k}": "{v}",')
    print("}\n")

# The Json you got from discord interaction value
raw_json = input("value\n\n\n")

convert_interaction(raw_json)