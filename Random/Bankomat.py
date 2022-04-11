amount = int(input("Hur mycket vill du ta ut? ")) # Få input från användare

number_of_500 = amount // 500 # Räkna ut antal fem hundra lappar
amount_left_after_500 = amount % 500 # Räkna ut resterande mängd

number_of_200 = amount_left_after_500 // 200 # Räkna ut antal två hundra lappar
amount_left_after_200 = amount_left_after_500 % 200 # Räkna ut resterande mängd

number_of_100 = amount_left_after_200 // 100 # Räkna ut antal hundra lappar
extra = amount_left_after_200 % 100 # Räkna ut resterande mängd

print("Antal femhundra lappar: " + str(number_of_500) + "\nAntal tvåhundra lappar: " + str(number_of_200)
 + "\nAntal hundra lappar: " + str(number_of_100) + "\nMed en resterande mängd på: " + str(extra) + "kr...") 
