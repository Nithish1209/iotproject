def count_words(line):
    words = line.split()  
    return len(words)  

line_number = 1  

with open('sam.txt', 'r') as file:  
    for line in file:  
        word_count = count_words(line)  
        print(f"Line {line_number}: Word Count - {word_count}")  
        line_number += 1 
