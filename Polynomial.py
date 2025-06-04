class Polynomial:

    def __init__(self, **kwargs):
        self.p = {}
        for exp, coef in kwargs.items():
            self.p[int(exp[1:])] = coef
        self.max_deg = max(self.p.keys()) if self.p else 0

    def __str__(self):
        if not self.p:
            return "0"
        terms = []
        for exp, coef in sorted(self.p.items(), reverse=True):
            if coef == 0:
                continue
            if exp == 0:
                terms.append(f"{coef}")
            elif exp == 1:
                terms.append(f"{coef}x")
            else:
                terms.append(f"{coef}x^{exp}")
        return " + ".join(terms) if terms else "0"

    def __add__(self, other):
        sum_p = {}
        unique_expos = set(self.p) | set(other.p)
        for expo in unique_expos:
            coef = self.p.get(expo, 0) + other.p.get(expo, 0)
            sum_p[f"x{expo}"] = coef

        return Polynomial(**sum_p)


my_polynomial = Polynomial(x2=3, x1=2, x0=1)
my_other_polynomial = Polynomial(x1=5, x0=1)

print(my_polynomial)
print(my_other_polynomial)

sum_polynomial = my_polynomial + my_other_polynomial
print(sum_polynomial)
