def read_coin():
  x = float(input("Digite o valor da moeda: "))

  return x

def check_coin():
  total = 0
  allowed = [0.10, 0.25]

  while(total <= 0.45):
    coin = read_coin()

    if coin not in allowed:
      print("Moeda inválida!")

    total += coin

    if total == 0.45:
      return 1

    if total >= 0.45:
        print("Toma sua coca! Perdeu {0:.0f} centavos!".format((total - 0.45) * 100))

res = check_coin()

if res == 0:
  print("Rejeitado!")

elif res == 1:
  print("Toma sua Coca!")

