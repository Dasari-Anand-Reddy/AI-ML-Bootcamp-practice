text=input("Enter a string: ")
print("Reversed:",text[::-1])
vowels="aeiouAEIOU"
count=sum(1 for char in text if char in vowels)
print("Vowel count: ",count)