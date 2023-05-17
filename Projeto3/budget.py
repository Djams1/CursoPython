class Category:
    def __init__(self,description):
        self.description = description
        self.ledger = []
        self.__saldo = 0

    def deposit(self,amount,description = ""):
        self.ledger.append({'amount':amount,'description':description})
        self.__saldo += amount

        
    def withdraw(self,amount,description = ""):
        if self.__saldo - amount >= 0:
            self.ledger.append({'amount':amount*-1,'description':description})
            self.__saldo -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.__saldo

    def transfer(self,amount,description):
        if self.withdraw(amount, f"Transfer to {description.description}"):
            description.deposit(amount, f"Transfer from {self.description}")
            return True
        else:
            return False

    def __repr__(self):
        topo = self.description.center(30, '*') + '\n'
        lista = ""
        for i in self.ledger:
            linha = f'{i["description"][:23]:<23}{i["amount"]:>7.2f}'
            lista += linha + "\n"
        total = "Total: " + f'{self.__saldo:.2f}'
        return topo + lista + total

    def check_funds(self,amount):
        if self.__saldo >= amount:
            return True
        else:
            return False

def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

  
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")
  