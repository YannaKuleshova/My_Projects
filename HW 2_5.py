kilometers=12.25
miles=7.38
miles_kilo=1.61
kilometers_t=round(miles*miles_kilo)
miles_t=round(kilometers/miles_kilo)
print(miles, "miles is", miles_t, "kilometers", sep=" ", end="\n")
print(kilometers,"kilometers is",kilometers_t, "miles", sep=" ")