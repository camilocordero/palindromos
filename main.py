letras = {
  'A' : 'A',
  'E' : '3',
  'H' : 'H',
  'I' : 'I', 
  'J' : 'L',
  'L' : 'J',
  'M' : 'M',
  'O' : 'O',
  'S' : '2', 
  'T' : 'T',
  'U' : 'U',
  'V' : 'V',
  'W' : 'W',
  'X' : 'X', 
  'Y' : 'Y',
  'Z' : '5',
  '1' : '1',
  '2' : 'S',
  '3' : 'E', 
  '5' : 'Z',
  '8' : '8'
}

while True:
  try:
    string = input()

    es_palindromo = string == string[::-1]
    es_reflejo = string == "".join([letras.setdefault(ch, "") for ch in string[::-1]])

    outcome = "no es palindromo" if (not es_palindromo and not es_reflejo) else \
      "es un palindromo regular" if (not es_reflejo and es_palindromo) else \
      "es un string reflejado" if (not es_palindromo and es_reflejo) else \
      "es un palindromo refleajdo"
    
    print("{} -- {}.\n".format(string, outcome))

  except(EOFError):
    break