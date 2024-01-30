class PocketMoneyCalculator:
    def __init__(self, total_monthly_balance, rent_fee, other_necessary_costs, daily_costs):
        self.total_monthly_balance = total_monthly_balance
        self.rent_fee = rent_fee
        self.other_necessary_costs = other_necessary_costs
        self.daily_costs = daily_costs

    def calculate_pocket_money(self):
        total_costs = self.rent_fee + self.other_necessary_costs + self.daily_costs * 30
        pocket_money = self.total_monthly_balance - total_costs

        if pocket_money >= 0:
            daily_pocket_money = pocket_money / 30
            return f"You can use {pocket_money:.2f} THB for pocket money.\nYou can use {daily_pocket_money:.2f} THB daily for pocket money."
        else:
            return "You do not have enough money for pocket money after paying all the costs."

if __name__ == "__main__":
    total_monthly_balance = float(input("Enter the total monthly balance: "))
    rent_fee = float(input("Enter the rent fee: "))
    other_necessary_costs = float(input("Enter the other necessary costs: "))
    daily_costs = float(input("Enter the daily costs: "))

    calculator = PocketMoneyCalculator(total_monthly_balance, rent_fee, other_necessary_costs, daily_costs)
    result = calculator.calculate_pocket_money()
    print(result)

