import sys
def dec():
    print("this should decode base64 text")
    x = input("pls input the text: ")
    leng = len(x)
    count = 0
    for i in range (leng-(leng-2), leng, 1):
        y = x[i]
        if y == "=":
            count -= 1
    lett = leng + count
    result = ""
    l = 0
    for i in range (lett):
        string = ''
        string += x[i]
        string = string.encode('utf-8')
        string = ''.join(format(byte, '08b') for byte in string)
        var = int(string, 2)
        if var >= 65 and var <= 90:
            var -= 65
        elif var >= 97 and var <= 122:
            var -= 71
        elif var >= 48 and var <= 57:
            var += 4
        elif var == 43:
            var += 19
        elif var == 47:
            var += 16
        else:
            print("something went wrong")
        var = "{0:06b}".format(var)
        result += var
        l += 6
    length = len(result)
    length = int(length / 8)
    result2 = ""
    result3 = ""
    index = 0
    for i in range (0, length, 1):
        for j in range (0, 8, 1):
            result2 += result[j + index]
        index += 8
        result4 = int(result2, 2)
        result4 = bytes([result4])
        result4 = result4.decode("utf-8")
        result3 += result4
        result2 = ""
    print(result3)

def enc():
    print("this should convert text into base64")
    x = input("input pls right here: ")
    x = x.encode('utf-8')
    x = ''.join(format(byte, '08b') for byte in x)
    print(x)
    leng = len(x)
    print(len(x))
    mod = leng % 6
    if mod != 0:
        pad = leng % 6
        for _ in range (pad):
            x += "00"
    length = len(x)
    lett = int(length/6)
    result = ""
    l = 0
    for _ in range (lett):
        string = ''
        for i in range (l, l+6, 1):
            string += x[i]
        var = int(string, 2)
        if var >= 0 and var <= 25:
            var += 65
        elif var >= 26 and var <= 51:
            var += 71
        elif var >= 52 and var <= 61:
            var -= 4
        elif var == 62:
            var -= 19
        elif var == 63:
            var -= 16
        else:
            print("something went wrong")
        var = bytes([var])
        letter = var.decode()
        result += letter
        l += 6
    for _ in range (mod):
        result += "="
    print(result)
if __name__ == "__main__":
    print("1: encode, 2: decode")
    varname = input("enter choice: ")
    if varname == "1":
        enc()
    elif varname == "2":
        dec()
    else:
        print("please enter a real option mf >:(")
        sys.exit()