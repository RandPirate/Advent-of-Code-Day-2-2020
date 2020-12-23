filename = "day4inputs"
with open(filename, "r") as file:
    contents = file.read()

contents = contents.replace(" ", "\n")
lines = contents.splitlines()

results = [[]]
for line in lines:
    if not line:
        results.append([])
    else:
        results[-1].append(line)

def converting(x):  
    
    string = " "  
    joining = string.join(x)
    lines_ = joining.splitlines()
    return (lines_) 
        
final = []
for result in results:
    converted = (converting(result))
    for convert in converted:
        if all(["iyr" in convert, "pid" in convert, "ecl" in convert, "eyr" in convert, "byr" in convert, "hgt" in convert, "hcl" in convert]):
            final.append(results)
            # print(results)
end = len(final)
print(f"There are {end} valid passports!")