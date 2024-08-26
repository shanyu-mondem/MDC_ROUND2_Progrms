# At odd positions if positional count start from 0
s = input("Enter your string: ")
chars = list(s)
for i,char in enumerate(chars):
    if (i%2!=0) and (ord(char) in range(97,123) or ord(char) in range(65,91)):
        chars[i] = chr(ord(char)-3)
orig_str=''.join(chars)
rev_str = orig_str[::-1]
print('Original String: ',orig_str)
print("Resultant String: ",rev_str)