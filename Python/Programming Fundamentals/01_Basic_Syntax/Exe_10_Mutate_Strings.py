string1 = input()
string2 = input()

for i in range(0, len(string1)):
    if string2[i] != string1[i]:
        print(string2[:i+1] + string1[i+1:])