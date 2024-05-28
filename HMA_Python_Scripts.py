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
      output[speciesname]['evs'] = {}
      output[speciesname]['evs']['hp'] = mon.evs.hp
      output[speciesname]['evs']['atk'] = mon.evs.atk
      output[speciesname]['evs']['def'] = mon.evs.defense
      output[speciesname]['evs']['spa'] = mon.evs.spa
      output[speciesname]['evs']['spd'] = mon.evs.spd
      output[speciesname]['evs']['spe'] = mon.evs.spd
      output[speciesname]['graphics'] = {}
      output[speciesname]['graphics']['bodycolor'] = mon.graphics.bodycolor
      output[speciesname]['graphics']['noflip'] = mon.graphics.noflip
      output[speciesname]['iconpal'] = {}
      output[speciesname]['iconpal']['index'] = mon.iconpal.index
      output[speciesname]['iconpal']['indexfem'] = mon.iconpal.indexfemale
      output[speciesname]['flags'] = {}
      output[speciesname]['flags']['legendary'] = mon.flags.legendary
      output[speciesname]['flags']['mythical'] = mon.flags.mythical
      output[speciesname]['flags']['ultrabeast'] = mon.flags.ultrabeast
      output[speciesname]['flags']['totem'] = mon.flags.totem
      output[speciesname]['flags']['paradox'] = mon.flags.paradox
      output[speciesname]['flags']['mega'] = mon.flags.megaevolution
      output[speciesname]['flags']['primal'] = mon.flags.primalreversion
      output[speciesname]['flags']['ultraburst'] = mon.flags.ultraburst
      output[speciesname]['flags']['gigantamax'] = mon.flags.gigantamax
      output[speciesname]['flags']['alolan'] = mon.flags.alolan
      output[speciesname]['flags']['galarian'] = mon.flags.galarian
      output[speciesname]['flags']['hisuian'] = mon.flags.hisuian
      output[speciesname]['flags']['paldean'] = mon.flags.paldean
      output[speciesname]['flags']['trade'] = mon.flags.trade
      output[speciesname]['flags']['perfectivs'] = mon.flags.perfectivs
      output[speciesname]['flags']['dexforce'] = mon.flags.dexforce
      output[speciesname]['flags2'] = {}
      output[speciesname]['flags2']['tmilliterate'] = mon.flags2.tmilliterate
      output[speciesname]['leveluplearnset'] = {}
      if type(mon.leveluplearnset) is not int:
        for pair in mon.leveluplearnset:
          output[speciesname]['leveluplearnset'][pair.move] = pair.level
      output[speciesname]['teachablelearnset'] = []
      if type(mon.teachablelearnset) is not int:
        for move in mon.teachablelearnset:
          output[speciesname]['teachablelearnset'].append(move.move)
      output[speciesname]['evolutions'] = {}
      if type(mon.evolutions) is not int:
        for keys_ in mon.evolutions:
          output[speciesname]['evolutions'][keys_.targetspecies] = {keys_.method: str(keys_.param)}
      output[speciesname]['formchangetable'] = {}
      if type(mon.formchangetable) is not int:
        for keys_ in mon.formchangetable:
          output[speciesname]['formchangetable'][keys_.targetspecies] = {keys_.method: [str(keys_.param1), str(keys_.param2), str(keys_.param3)]}
  else:
    output[speciesname + str(mons.count(speciesname) + 1)] = {}
    for key in keys:
      output[speciesname + str(mons.count(speciesname) + 1)][key] = mon[key]
  mons.append(speciesname)
output = json.dumps(output, indent=4)
with open("output.json", "w") as outfile:
    outfile.write(output)