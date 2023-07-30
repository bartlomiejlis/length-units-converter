def forKilometers(x, y):
  return x * y
def forMiles(x, y):
  return x / y
print('Witaj w przeliczniku jednostek długości.')
print('Wybierz właściwą operację:')
print('1. Mile (mi) -> kilometry (km)')
print('2. Kilometry (km) -> mile (mi)')
choice = input('Którą operację chcesz wykonać? Wybierz numer: ')
if choice == '1':
  num1 = float(input('Podaj wartość: '))
  print(num1, 'mi *', 1.609344, '=', forKilometers(num1, 1.609344), 'km')
elif choice == '2':
  num1 = float(input('Podaj wartość: '))
  print(num1, 'km /', 1.609344, '=', forMiles(num1, 1.609344), 'mi')
else:
  print('Niepoprawna wartość')