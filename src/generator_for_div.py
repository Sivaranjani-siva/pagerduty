with open("C:\\Users\\sivaranjani\\project_demo\\input_files\\input.txt", 'r') as file:
    input = int(file.readline().strip())
   

def generator_func_div_5_7(num):
    for i in range(num + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

#input = 100
res = list(generator_func_div_5_7(input))
output = ",".join(map(str, res))
print(output)