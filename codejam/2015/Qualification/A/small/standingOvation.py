infile = "A-small-attempt0.in"
outfile = "A-small-attempt0.out"
f = open(infile, "r")
o = open(outfile, "w")

loops = int(f.readline())
for i in range(1,loops+1):
  case = f.readline().split()
  maxShyness = int(case[0])
  people = case[1]
  currentSum = 0
  addedPeople = 0
  o.write("Case #" + str(i) + ": ")
  for j in range(0,maxShyness+1):
    if (currentSum >= j):
      currentSum += int(people[j])
    else:
      addedPeople += j - currentSum
      currentSum = j + int(people[j])
  o.write(str(addedPeople) + "\n")
