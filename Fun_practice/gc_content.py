#GC Content Calculator
#Susan Puckett
#Sept. 25, 2017
#Determines the percentage of a DNA sequence that is G or C vs. A or T

DNA = input("Enter DNA here: ")
bases = ["g","c","a","t"]

DNA = DNA.lower()

for character in DNA:
  if character not in bases:
    print("Sequence is not all DNA. Try again.")
    break

base_count_list = [] 
for base in bases:
  base_count = DNA.count(base)
  print(base + ": " + str(base_count))
  base_count_list.append(base_count)

GC = base_count_list[0] + base_count_list[1]
AT = base_count_list[2] + base_count_list[3]
print ("% GC content: " + str(GC/(GC+AT)*100))

