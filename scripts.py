from pip._vendor import tomli
with open("pokeemerald_.toml", "rb") as f:
    data = tomli.load(f)
    named_anchors = data.get("NamedAnchors")
    for named_anchor in named_anchors:
        name = named_anchor.get("Name")
        if name == 'data.pokemon.info':
            format = named_anchor.get("Format")
            formats = format.split()
            for format_ in formats:
                if ':' in format_:
                    print(format_.split(':')[0])
                if '.' in format_:
                    print(format_.split('.')[0])