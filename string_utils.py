def split_before_each_uppercases(formula):
    start = 0 
    end = 0
    i = 0
    split_formula = []
    if not formula:
        return []
    for i in range(1,len(formula)):
      end = i
      if formula[i].isupper() : 
       split_formula.append(formula[start:end])
       start = end
    split_formula.append(formula[start:])
    return split_formula
    

def split_at_first_digit(formula):
   digit_location = 1
   new_formula = ()
   for char in formula[1:]:
      if char.isdigit():
          break
      digit_location += 1

   if digit_location == len(formula):
       return formula,1
   else :
      figure = int(formula[digit_location:])
      return formula[:digit_location],figure

   
       
