# python3

def read_input():
    input_type = input()

    if "I" in input_type:
        pattern = input().rstrip()
        text = input().rstrip()

    elif "F" in input_type:
        file_name = "06"

        if "test/" in file_name:
            file_name.replace("test/", "tests/")

        if "tests/" not in file_name:
            file_name = "tests/" + file_name

        with open(file_name, 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

    return(pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    n = len(text)
    m = len(pattern)
    p = 31
    modulus = 10**9 + 9

    pattern_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % modulus

    substr_hash = [0] * (n - m + 1)
    substr_hash[0] = 0
    for i in range(m):
        substr_hash[0] = (substr_hash[0] * p + ord(text[i])) % modulus
    for i in range(1, n - m + 1):
        substr_hash[i] = ((substr_hash[i-1] - ord(text[i-1]) * pow(p, m-1, modulus)) * p + ord(text[i+m-1])) % modulus

    occurrences = []
    for i in range(n - m + 1):
        if substr_hash[i] == pattern_hash:
            if text[i:i+m] == pattern:
                occurrences.append(i)
    
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))