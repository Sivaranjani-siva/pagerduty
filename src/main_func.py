from generator_for_div import generator_func_div_5_7
from interleaves_str import interleave_str


with open("C:\\Users\\sivaranjani\\project_demo\\input_files\\input.txt", 'r') as file:
    num = int(file.readline().strip())
    str_1 = file.readline().strip()
    str_2 = file.readline().strip()

def main():
    #num = 100
    res = generator_func_div_5_7(num)
    output = ",".join(map(str, res))
    #print(output)

    #str_1 = "AAAA"
    #str_2 = "1234567"
    interleaved_res = interleave_str(str_1, str_2)
    #print(interleaved_res)

if __name__ == "__main__":
    main()