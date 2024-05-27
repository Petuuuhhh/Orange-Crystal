# output = open("output.txt", "w") 
#for mon in data.pokemon.stats:
  # output.write('+"' + mon.speciesname + '"\n')
# for item in data.items.info:
  # output.write('+"' + item.name + '"\n')
import json
output = {}
mons = []
keys = [
    'hp',
    'attack',
    'defense',
    'speed',
    'spatk',
    'spdef',
    'type1',
    'type2',
    'catchrate',
    'padding',
    'expyield',
    # 'evs',
    'itemcommon',
    'itemrare',
    'genderratio',
    'eggcycles',
    'friendship',
    'growthrate',
    'egggroup1',
    'egggroup2',
    'ability1',
    'ability2',
    'hiddenability',
    'safarizonefleerate',
    'cryid',
    'natdexnum',
    'height',
    'weight',
    'pokemonscale',
    'pokemonoffset',
    'trainerscale',
    'traineroffset',
    'padding',
    'description',
    # 'graphics',
    'frontanimdelay',
    'frontanimid',
    'backanimid',
    'frontpicsize',
    'frontpicsizefemale',
    'frontpicyoffset',
    'backpicsize',
    'backpicsizefemale',
    'backpicyoffset',
    # 'iconpal',
    'enemymonelevation',
    # 'flags',
    # 'flags2',
    # 'leveluplearnset',
    # 'teachablelearnset',
    # 'evolutions',
    # 'formchangetable',
]

for mon in data.pokemon.info:
  speciesname = mon.speciesname
  if speciesname not in mons:
    output[speciesname] = {}
    for key in keys:
      output[speciesname][key] = mon[key]
  else:
    output[speciesname + str(mons.count(speciesname) + 1)] = {}
    for key in keys:
      output[speciesname + str(mons.count(speciesname) + 1)][key] = mon[key]
  mons.append(speciesname)
output = json.dumps(output, indent=4)
with open("output.json", "w") as outfile:
    outfile.write(output)