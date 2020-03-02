def read_coin():
  x = float(input("Digite o valor da moeda: "))

  return x

def check_coin():
  t = 0
  allowed = [0.10, 0.25]

  while(t <= 0.45):
    coin = read_coin()

    if coin not in allowed:
      print("Moeda inválida!")

    t += coin

    if t >= 0.45:
        return 1

res = check_coin()

if res == 0:
  print("Rejeitado!")

elif res == 1:
  print("Toma sua Coca!")

