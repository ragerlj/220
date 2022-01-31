import math
numer_of_vals = eval(input("Enter number of terms: "))
terms = 0
rms_terms = 0
harmonic_terms = 0
geometric_terms = 1
for i in range(numer_of_vals):
   value = eval(input("What is term? "))
   terms = terms + value
   rms_terms = rms_terms + math.pow(value, 2)
   harmonic_terms = (1 / value) + harmonic_terms
   geometric_terms = geometric_terms * value


Arithmetic_mean = terms / numer_of_vals
print("Arithmetic mean: ", Arithmetic_mean)

rms_average = math.sqrt(rms_terms / numer_of_vals)
print("rms average: ", rms_average)

harmonic_mean = numer_of_vals / harmonic_terms
print("harmonic mean: ", harmonic_mean)

geometric_mean = math.pow(geometric_terms, 1/numer_of_vals)
print("geometric mean: ", geometric_mean)