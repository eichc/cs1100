# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:27:41 2022

@author: Cam Eich

Given two documents, analyze and compare them. Things to analyze include
average word length, ratio of distinct words to total words, sets of words for
each word length, and discinct word pairs given a maximum separation distance.
"""

def parse_file(fname):
    '''
    Given a file, separate it into a list of strings with non-whitespace
    characters. Then remove all non-letters from the list and convert all of
    the words to lowercase. Return the list of words.
    '''
    file = open(fname, 'r', encoding = "ISO-8859-1")
    file_str = file.read()
    L = file_str.split()
    word_list = []
    
    for word in L:
        word = word.lower()
        letters = list(word)
        #remove every character that isn't a letter
        for i in range(len(letters)-1, -1, -1): #index backwards to avoid skipping characters
            if not 'a' <= letters[i] <= 'z':
                letters.remove(letters[i])
        new_word = ''.join(letters)
        #add the word to the final list, as long as it has letters in it
        if len(new_word) > 0:
            word_list.append(new_word)
    file.close()
    return word_list

def avg_len(words):
    '''
    Given a list of words, calculate and return the average word length.
    '''
    num_words = len(words)
    total_len = 0
    for word in words:
        total_len += len(word)
    avg = total_len / num_words
    return avg

def distinct(words):
    '''
    Given a list of words, calculate and return the ratio of distinct words to
    total words.
    '''
    num_words = len(words)
    distinct = set(words)
    num_distinct = len(distinct)
    ratio = num_distinct / num_words
    return ratio

def word_lengths(words):
    '''
    Given a list of words, create a list of sets. Each set contains only words
    of a specific length. For example, the set at index 2 contains only the
    words of length 2.
    **Note: with this indexing system, the first set will always be empty 
    because no word has length 0.
    '''
    #find longest word length
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    #create and initialize the list of sets
    L = []
    for i in range(max_len + 1):
        L.append(set())
    #add each word to its appropriate set
    for word in words:
        word_len = len(word)
        L[word_len].add(word)
    return L

def word_pairs(words, max_sep):
    '''
    Given a list of words and a max steparation distance, find all pairs of 
    words that are max_sep or fewer words apart. Put each pair in a tuple, 
    and return a list containing all of the tuples.
    '''
    pairs = []
    for i in range(len(words) - 1):
        current = words[i]
        for j in range(i + 1, min((i + max_sep + 1), len(words))): #use min to avoid out of bounds error
            pair = sorted((current, words[j]))
            pair = tuple(pair)
            pairs.append(pair)
    pairs.sort()
    return pairs

def distinct_pairs(pairs):
    '''
    Given a list of word pairs, return a list containing only the distinct pairs.
    '''
    distincts = set(pairs)
    L = sorted(distincts)
    return L
    
def jaccard(s1, s2):
    '''
    Given 2 lists or sets, calculate and return the Jaccard similarity between
    them.
    '''
    set1 = set(s1)
    set2 = set(s2)
    if len(set1) == 0 or len(set2) == 0:
        return 0
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    return len(intersection) / len(union)


if __name__ == "__main__":
    #all inputs
    file1 = input("Enter the first file to analyze and compare ==> ").strip()
    print(file1)
    
    file2 = input("Enter the second file to analyze and compare ==> ").strip()
    print(file2)
    
    max_sep = input("Enter the maximum separation between words in a pair ==> ").strip()
    print(max_sep)
    max_sep = int(max_sep)
    
    #parse the three files
    words1 = parse_file(file1)
    words2 = parse_file(file2)
    stop_words = parse_file("stop.txt")
    stop_words = set(stop_words)
    
    #remove stop words
    for i in range(len(words1)-1, -1, -1):
        if words1[i] in stop_words:
            words1.remove(words1[i])
    for i in range(len(words2)-1, -1, -1):
        if words2[i] in stop_words:
            words2.remove(words2[i])
    
    
    #analyze the first document
    avg1 = avg_len(words1)
    distinct1 = distinct(words1)
    lengths1 = word_lengths(words1)
    pairs1 = word_pairs(words1, max_sep)
    distinct_pairs1 = distinct_pairs(pairs1)
    pair_ratio1 = len(distinct_pairs1) / len(pairs1)
    
    #print analysis of the first document
    print("\nEvaluating document {}".format(file1))
    
    print("1. Average word length: {:.2f}".format(avg1))
    
    print("2. Ratio of distinct words to total words: {:.3f}".format(distinct1))
    
    print("3. Word sets for document {}:".format(file1))
    for i in range(1, len(lengths1)):
        if len(lengths1[i]) == 0:
            print("{:4d}:   0:".format(i))
        elif len(lengths1[i]) <= 6:
            print("{:4d}:{:4d}:".format(i, len(lengths1[i])), end='')
            words = sorted(lengths1[i])
            for word in words:
                print(" " + word, end='')
            print("")
        else:
            print("{:4d}:{:4d}:".format(i, len(lengths1[i])), end='')
            words = sorted(lengths1[i])
            for i in range(3):
                print(" " + words[i], end='')
            print(" ...", end='')
            for i in range(-3,0):
                print(" " + words[i], end='')
            print("")
            
    print("4. Word pairs for document {}".format(file1))
    print("  {} distinct pairs".format(len(distinct_pairs1)))
    if len(distinct_pairs1) <= 5:
        for i in range(len(distinct_pairs1)):
            print("  {} {}".format(distinct_pairs1[i][0], distinct_pairs1[i][1]))
    else:
        for i in range(5):
            print("  {} {}".format(distinct_pairs1[i][0], distinct_pairs1[i][1]))
        print("  ...")
        for i in range(-5, 0):
            print("  {} {}".format(distinct_pairs1[i][0], distinct_pairs1[i][1]))
        
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(pair_ratio1))
    
    
    #analyze the second document
    avg2 = avg_len(words2)
    distinct2 = distinct(words2)
    lengths2 = word_lengths(words2)
    pairs2 = word_pairs(words2, max_sep)
    distinct_pairs2 = distinct_pairs(pairs2)
    pair_ratio2 = len(distinct_pairs2) / len(pairs2)
    
    #print analysis of the second document
    print("\nEvaluating document {}".format(file2))
    
    print("1. Average word length: {:.2f}".format(avg2))
    
    print("2. Ratio of distinct words to total words: {:.3f}".format(distinct2))
    
    print("3. Word sets for document {}:".format(file2))
    for i in range(1, len(lengths2)):
        if len(lengths2[i]) == 0:
            print("{:4d}:   0:".format(i))
        elif len(lengths2[i]) <= 6:
            print("{:4d}:{:4d}:".format(i, len(lengths2[i])), end='')
            words = sorted(lengths2[i])
            for word in words:
                print(" " + word, end='')
            print("")
        else:
            print("{:4d}:{:4d}:".format(i, len(lengths2[i])), end='')
            words = sorted(lengths2[i])
            for i in range(3):
                print(" " + words[i], end='')
            print(" ...", end='')
            for i in range(-3,0):
                print(" " + words[i], end='')
            print("")
            
    print("4. Word pairs for document {}".format(file2))
    print("  {} distinct pairs".format(len(distinct_pairs2)))
    if len(distinct_pairs2) <= 5:
        for i in range(len(distinct_pairs2)):
            print("  {} {}".format(distinct_pairs2[i][0], distinct_pairs2[i][1]))
    else:
        for i in range(5):
            print("  {} {}".format(distinct_pairs2[i][0], distinct_pairs2[i][1]))
        print("  ...")
        for i in range(-5, 0):
            print("  {} {}".format(distinct_pairs2[i][0], distinct_pairs2[i][1]))
        
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(pair_ratio2))
    
    
    #compare the two documents
    print("\nSummary comparison")
    if avg1 > avg2:
        print("1. {} on average uses longer words than {}".format(file1, file2))
    else:
        print("1. {} on average uses longer words than {}".format(file2, file1))
    
    overall_jac = jaccard(words1, words2)
    print("2. Overall word use similarity: {:.3f}".format(overall_jac))
    
    print("3. Word use similarity by length:")
    #only compute the similarity for as many times as the length of the smaller
    #of the two lists, to avoid an out of bounds error
    for i in range(1, min(len(lengths1), len(lengths2))):
        jac = jaccard(lengths1[i], lengths2[i])
        print("{:4d}: {:.4f}".format(i, jac))
    #print a 0 for the similarity of the remaining lengths
    for i in range(min(len(lengths1), len(lengths2)), max(len(lengths1), len(lengths2))):
        print("{:4d}: 0.0000".format(i))
    
    pair_jac = jaccard(pairs1, pairs2)
    print("4. Word pair similarity: {:.4f}".format(pair_jac))