try:
    file_object = open('DamianHutchinson.txt','r')
    for lines in file_object:
        print(lines)
except FileNotFoundError:
    print("use the corretct path of your file")
