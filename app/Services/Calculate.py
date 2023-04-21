class Calculate:
    def __init__(self, kg_weight: float, weight: float, additional_per_kg=None, express=False):
        self.kg_weight = kg_weight
        self.weight = weight
        self.additional_per_kg = additional_per_kg
        self.express = express
        self.FINAL_STANDARD_WEIGHT = 1000
        self.FINAL_PREMIUM_WEIGHT = 10000
        self.final_calculation = self.calculate()

    def calculate(self):
        if self.express:
            if self.weight <= self.FINAL_STANDARD_WEIGHT:
                final_calculation = self.kg_weight * (self.weight / self.FINAL_STANDARD_WEIGHT)
            elif self.FINAL_STANDARD_WEIGHT <= self.weight <= self.FINAL_PREMIUM_WEIGHT:
                final_calculation = self.kg_weight + ((
                                                              self.weight - self.FINAL_STANDARD_WEIGHT) / self.FINAL_STANDARD_WEIGHT) * self.additional_per_kg
            else:
                final_calculation = self.kg_weight * (self.weight / self.FINAL_STANDARD_WEIGHT)
        else:
            if self.weight <= self.FINAL_STANDARD_WEIGHT:
                final_calculation = self.kg_weight * (self.weight / self.FINAL_STANDARD_WEIGHT)
            elif self.FINAL_STANDARD_WEIGHT <= self.weight <= self.FINAL_PREMIUM_WEIGHT:
                final_calculation = self.kg_weight + ((
                                                              self.weight - self.FINAL_STANDARD_WEIGHT) / self.FINAL_STANDARD_WEIGHT) * self.additional_per_kg
            else:
                final_calculation = self.kg_weight * (self.weight / self.FINAL_STANDARD_WEIGHT)

        print(final_calculation)
        return final_calculation