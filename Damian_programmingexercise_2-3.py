tractSize = 0.0
acres = 0.0

SQ_FEET_PER_ACRE = 43560

tractSize = float(input("Enter the number of square feet in the tract."))

acres = tractSize * float(input("Enter the number of acres"))

print("The size of that tract is", format(acres, '.2f'), "acres.")
