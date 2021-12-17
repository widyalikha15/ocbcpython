numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507,725, 547, 544, 615, 83, 165, 141, 501,
  263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418,907, 344, 236, 375,
  823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
  626, 949
  ]
print('angka belum diurut: {}'.format(numbers))
numbers.sort() 
print(' ')
print('angka sesudah diurut: {}'.format(numbers))

ganjil = []
genap = []

for urut in numbers: 
    if urut % 2 == 0:
        genap.append(urut)
    else :
        ganjil.append(urut)
print(' ')
print('genap: {}'.format(', '.join([str(urut) for urut in genap])))
print(' ')
print('ganjil: {}'.format(', '.join([str(urut) for urut in ganjil])))

for x in genap:
  if x <= 100:
    print(x)
  else:
    print('done')
    break