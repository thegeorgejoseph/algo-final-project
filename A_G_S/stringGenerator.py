import sys

def stringGenerator():
    input_filename="input.txt"
    if len(sys.argv) >1:
        input_filename=sys.argv[1]
    results = []
    flag = False
    with open(input_filename) as file:
        for line in file:
            line = line.strip('\n')
            if line.isdigit() is False:
                if flag is True:
                    results.append(string)
                string = line
                flag = False
            else:
                flag = True
                result = string[:int(line)+1] + string + string[int(line)+1:]
                string = result
                # print(string)
                
        if flag is True:
            results.append(string)
            
    file.close()
    return results[0],results[1]