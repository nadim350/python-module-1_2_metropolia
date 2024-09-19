pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot = 13.3

talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))

total_lots = talents * pounds_per_talent * lots_per_pound + pounds * lots_per_pound + lots
total_grams = total_lots * grams_per_lot

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"\nThe weight in modern units:\n{kilograms} kilograms and {grams:.2f} grams.")
