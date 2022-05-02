from numpy import interp

def ranInt(min, max, table):
    # change table to a string of numbers
    tab_str = ''
    for n in table:
        tab_str += str(n)
        
    # jump around the table
    fir_i = int(tab_str[0])
    sec_i = int(tab_str[fir_i])
    
    # read 4 random digits in the table to a string
    pm_str = ''
    for n in range(sec_i, sec_i + 4):
        pm_str += str(tab_str[n])
        
    # convert that string to a number between 1 and 0
    pm = float(pm_str)
    m = pm / 10000
    
    print(fir_i, sec_i, m)
    
    # remap the 1 to 0 number to a min to max value
    return int(interp(m, [0, 1], [min, max]))


ran = input ("Input random integer between 1 and 999")
ran_int = int(ran)

# initialize variables for the equation
a = 237
b = 764
m = 10000
ran_num_tab = [divmod(ran_int * a + b, m)[1]]

# create table
for n in range(0, 9):
    new_ran = ran_num_tab[n] * a + b
    mod_ran = divmod(new_ran, m)[1]
    ran_num_tab.append(mod_ran)

print("Random Number Table:")

# format the table for reading
table = []
for n in range(0, divmod(len(ran_num_tab), 5)[0] + 1):
    table.append('')

for n in range(0, len(ran_num_tab)):
    table[divmod(n, 5)[0]] += (str(ran_num_tab[n]) + '\t')
    
# pring table
for s in table:
    print(s)
    
print("Random Number: " + str(ranInt(50, 100, ran_num_tab)))

