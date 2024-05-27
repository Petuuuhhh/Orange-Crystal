output = open("output.txt", "w") 
#for mon in data.pokemon.stats:
  # output.write('+"' + mon.speciesname + '"\n')
for item in data.items.info:
  output.write('+"' + item.name + '"\n')
output.close()