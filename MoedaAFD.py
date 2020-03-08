class DFA:
  def __init__(self):
    self.accepted = [10, 25]
    self.states = [1, 2, 3]
    self.state = 1

  def set_state(self, index):
    self.state = self.states[index]

  def get_state(self):
    return self.state

  def verify(self, data, result):
    self.state = self.get_state()

    if data in self.accepted:
      self.set_state(1)
      
      if result >= 45:
        self.set_state(2)

      return True
    
    else:
      return False

def main():
  dfa = DFA()
  total = 0

  while(True):
    value = int(input("Digite um valor: "))
    total += value
    status = dfa.verify(value, total)

    if status == True:
      if dfa.get_state() == 3:
        print("Aprovado! Valor final: {}".format(total))
        break

    else:
      print("Rejeitado!")

if __name__ == "__main__":
  main()
