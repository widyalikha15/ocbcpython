import time
numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507,725, 547, 544, 615, 83, 165, 141, 501,
  263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418,907, 344, 236, 375,
  823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
  626, 949
  ]

#proses ganjil genap
genap = []
ganjil = []
for number in numbers: 
    if number % 2 == 0:
        genap.append(number)
    else :
        ganjil.append(number)

#proses looping
nomor = 918
i = 0
while i < len(genap):
  if genap[i] == nomor:
      # Processing for item found
      print(genap[i])
      print('done')
      break
  # Processing for item
  print(genap[i])
  time.sleep(0.5) 
  i += 1
else:
  # Processing for item not found
  print(nomor, 'not found in list.')

