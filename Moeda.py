def read_coin():
  x = int(input("Digite o valor da moeda: "))

  return x

def check_coin():
  total = 0
  allowed = [10, 25]

  while(total <= 45):
    coin = read_coin()

    if coin not in allowed:
      print("Moeda inválida!")
      return 0

    total += coin

    if total == 45:
      return 1

    if total > 45:
        print("Toma sua coca! Perdeu {} centavos!".format(total - 45))

res = check_coin()

if res == 0:
  print("Rejeitado!")

elif res == 1:
  print("Toma sua Coca!")
