# Q7. python program to count the number of each vowel

vowels = 'aeiou'
p_str = 'Hello, i am priyanshu kumar'
p_str = p_str.casefold()
count = {}.fromkeys(vowels,0)
for char in p_str:
   if char in count:
       count[char] += 1

print(count)