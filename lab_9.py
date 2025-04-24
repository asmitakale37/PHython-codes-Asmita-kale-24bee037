import string

# 1. Count uppercase and lowercase letters
def count_lower_upper(s):
    result = {'upper': 0, 'lower': 0}
    for char in s:
        if char.isupper():
            result['upper'] += 1
        elif char.islower():
            result['lower'] += 1
    return result

print(count_lower_upper("Hello World! PYTHON is Fun"))

# 2. Compute n + nn + nnn + nnnn
def compute(n):
    n = str(n)
    return int(n) + int(n*2) + int(n*3) + int(n*4)

for i in range(4, 8):
    print(f"compute({i}) =", compute(i))

# 3. Create a 3D array
def create_array(x, y, z, value):
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

print("3D Array Example:", create_array(2, 2, 2, 7))

# 4. Sum and average of 5 subjects
def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

print("Sum & Average:", sum_avg([75, 80, 85, 90, 95]))

# 5. Check for Pangram
def ispangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

print("Is Pangram:", ispangram("The quick brown fox jumps over the lazy dog"))

# 6. List of (x, x^2, x^3)
def power_list(n):
    return [(x, x**2, x**3) for x in range(1, n+1)]

print("Power List:", power_list(5))

# 7. Palindrome check
def ispalindrome(s):
    s = ''.join(s.lower().split())
    return s == s[::-1]

print("Is Palindrome:", ispalindrome("A man a plan a canal Panama"))

# 8. Remove duplicates and sort
def convert(s):
    return ' '.join(sorted(set(s.split())))

print("Converted String:", convert("apple banana apple orange banana"))

# 9. Count alphabets and digits
def count_alpha_digits(s):
    result = {'alphabets': 0, 'digits': 0}
    for char in s:
        if char.isalpha():
            result['alphabets'] += 1
        elif char.isdigit():
            result['digits'] += 1
    return result

print("Alphabets & Digits Count:", count_alpha_digits("abc123xyz456"))

# 10. Word frequency sorted
def frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items()))

print("Word Frequency:", frequency("apple banana apple orange banana"))

# 11. List intersection
def create_list(list1, list2):
    return list(set(list1) & set(list2))

print("List Intersection:", create_list([1, 2, 3], [2, 3, 4]))

# --- Recursive Functions ---

# 1. Recursive prime factorization
def prime_factors(n, i=2):
    if n == 1:
        return []
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    return prime_factors(n, i + 1)

print("Prime Factors of 60:", prime_factors(60))

# 2. Binary equivalent
def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)

print("Binary of 13:", to_binary(13))

# 3. Count vowels recursively
def count_vowels(s):
    if not s:
        return 0
    return (s[0].lower() in 'aeiou') + count_vowels(s[1:])

print("Vowel Count:", count_vowels("Recursion is powerful"))

# 4. Reverse list recursively
def reverse_list(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

print("Reversed List:", reverse_list([1, 2, 3, 4]))

# 5. Recursive exponentiation
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print("2^5 =", power(2, 5))

# 6. Sanitize list (replace negatives with 0)
def sanitize(lst):
    if not lst:
        return []
    return [max(0, lst[0])] + sanitize(lst[1:])

print("Sanitized List:", sanitize([4, -3, 0, -2, 5]))

# 7. Average of list recursively
def recursive_avg(lst):
    def helper(lst, total=0, count=0):
        if not lst:
            return total / count if count else 0
        return helper(lst[1:], total + lst[0], count + 1)
    return helper(lst)

print("Recursive Average:", recursive_avg([5, 10, 15]))

# 8. Length of string recursively
def string_length(s):
    if not s:
        return 0
    return 1 + string_length(s[1:])

print("String Length:", string_length("Hello world!"))
