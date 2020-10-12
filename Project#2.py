#The function takes a DNA sequence string and a number that will determine the amount of
#indel copies. It then returns the sequence string with the indels added at the end.
def pad_with_indels(sequence,num):
    x = '-' * num
    return sequence + x
    
#The function takes a DNA sequence string and a number, in this case, being utilized as an
#index. It then returns a modified version of the string by inclusively slicing off both what #comes before as well as after the index, and placing an indel right in between.

def insert_indel(sequence, index):
   return sequence[:index] + '-' + sequence[index:]
#The function takes two DNA strings and compares each individual index to one another. It #identifies each match via a counter that increases by one each time an index from the #strings are identical.
#The function returns the amount of matches.
def count_matches(sequence1, sequence2):
    i = 0
    counter = 0
    for c in range(len(sequence1)):
        if sequence1[c] == sequence2[c] and (sequence1[c] != '-' and sequence2[c] != '-'):
            counter += 1
    return counter

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MILESTONE 2 STARTING FROM HERE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#The function displays the user’s options. Within this function it enables the user to see all 
#options that the user can choose from.

def print_menu():
    print("Main Menu")
    print("1. Insert an indel")
    print("2. Remove an indel")
    print("3. Score similarity")
    print("4. Suggest indel")
    print("5. Quit")
#After printing out the menu it is necessary that our user inputs the valid menu option. This 
#validates what integer value the user can input and keeps asking the user until a valid 
#number is given.

def get_menu_choice():
    menu_option = int(input("Please choose an option: \n"))
    while menu_option < 1 or menu_option > 5:
        menu_option = int(input("Please choose an option: \n"))
    return menu_option
#The function takes a DNA sequence number and validates it. If the number satisfies the #conditions, the function returns the given number. If the number does not satisfy the #condition, the function will repeatedly ask the user for a valid sequence number.   
def get_sequence_number():
    sequence_num = int(input("Sequence 1 or 2?\n"))   
    while sequence_num != 1 and sequence_num != 2:
        sequence_num = int(input("Sequence 1 or 2?\n"))
    return sequence_num

#In this function the user inputs a position, one greater than the index, to input an indel at a 
#position that is valid within the given sequence. This function does not return index but 
#rather where the indel will be placed.
    
def get_insert_position(sequence):
    position = int(input("Please choose a position:\n"))
    while position < 1 or position > len(sequence):
        position = int(input("Please choose a position:\n"))
    return position
#This function removes an indel by the given position of the user’s input. This returns the #position value.
def get_remove_position(sequence):
    position_of_indel = int(input("Please choose a position:\n"))
    while (position_of_indel < 1 or position_of_indel > len(sequence) or sequence[position_of_indel - 1] != '-'):
        position_of_indel = int(input("Please choose a position:\n"))
    return  position_of_indel
        
#The function takes a DNA sequence string and an index number.
#It then slices off both what comes before and then after the index, purposefully leaving the actual index out as if we are removing it.
#The function returns the two slices as the new DNA sequence string.
def remove_indel(sequence,index):
    removed_indel_string = sequence[0:index:] + sequence[index+1::]
    return removed_indel_string
#In this function, we calculate the optimal position by using brute force to get the highest percent of matches and returning the position of the best match. 
def find_optimal_indel_position(sequence, other_sequence):
    #Within my function I make an empty list where I input all the percentages of each time the indel is placed at a certain index.
    #After that I use the .append method to put all the percentages into a list and find the max value and then return the index of the max value.
    optimal_index = []
    i = 0
    other_sequence = pad_with_indels(other_sequence, 1)
    for n in range(len(sequence)):
        sequence_with_indel = insert_indel(sequence, i)
        percentage = count_matches(sequence_with_indel, other_sequence) / len(sequence_with_indel) * 100
        optimal_index.append(percentage)
        i += 1
    return optimal_index.index(max(optimal_index))
#The function takes two DNA sequence strings. It compares each individual index value to one another and determines if they’re identical. If they are identical, the function returns the letters in the indexes in lowercase and the letters that are not identical in uppercase.
def print_similar_sequences(dna_sequence1, dna_sequence2):
    new_sequence1 = ''
    new_sequence2 = ''
    for i in range(len(dna_sequence1)):
        if dna_sequence1[i] == dna_sequence2[i] and (dna_sequence1[i] != '-' and dna_sequence2[i] != '-'):
            if dna_sequence1[i] == 'A':
                new_sequence1 = new_sequence1 + 'a'
                new_sequence2 = new_sequence2 + 'a'
            elif dna_sequence1[i] == 'T':
                new_sequence1 = new_sequence1 + 't'
                new_sequence2 = new_sequence2 + 't'
            elif dna_sequence1[i] == 'C':
                new_sequence1 = new_sequence1 + 'c'
                new_sequence2 = new_sequence2 + 'c'
            else:
                new_sequence1 = new_sequence1 + 'g'
                new_sequence2 = new_sequence2 + 'g'
        else:
            new_sequence1 = new_sequence1 + dna_sequence1[i]
            new_sequence2 = new_sequence2 + dna_sequence2[i]
 
    print(f"Sequence 1: {new_sequence1}")
    print(f"Sequence 2: {new_sequence2}")
    

# ---------------------------------------------------------------------------------------------- #


if __name__ == "__main__": 

    dna_sequence1 = input("Please enter DNA Sequence 1:\n")
    dna_sequence2 = input("Please enter DNA Sequence 2:\n")
    print()
    if len(dna_sequence1) < len(dna_sequence2):
        dna_sequence1 = pad_with_indels(dna_sequence1,(len(dna_sequence2) - len(dna_sequence1)))
    elif len(dna_sequence2) < len(dna_sequence1):
        dna_sequence2 = pad_with_indels(dna_sequence2,(len(dna_sequence1) - len(dna_sequence2)))


    print_similar_sequences(dna_sequence1, dna_sequence2)
    print()
    print_menu()
    print()
    option = get_menu_choice()

    while option < 5:
        if option == 1:
            sequence_num = get_sequence_number()
            if sequence_num == 1:   
                get_position = get_insert_position(dna_sequence1)
                dna_sequence1 = insert_indel(dna_sequence1, get_position - 1)
                dna_sequence2 = pad_with_indels(dna_sequence2, 1)
                
            else:
                get_position = get_insert_position(dna_sequence2)
                dna_sequence2 = insert_indel(dna_sequence2, get_position - 1 )
                dna_sequence1 = pad_with_indels(dna_sequence1, 1)
                   
        elif option == 2:    
            sequence_num = get_sequence_number()      
            if sequence_num == 1:
                actual_index_indel = get_remove_position(dna_sequence1)
                dna_sequence1 = remove_indel(dna_sequence1, actual_index_indel)
                dna_sequence2 = remove_indel(dna_sequence2, len(dna_sequence2) -1)
            else:
                actual_index_indel = get_remove_position(dna_sequence2)
                dna_sequence2 = remove_indel(dna_sequence2, actual_index_indel)
                dna_sequence1 = remove_indel(dna_sequence1, len(dna_sequence1) -1)
                
        elif option == 3:
            mismatching_position = (len(dna_sequence1)) - count_matches(dna_sequence1, dna_sequence2)
            percentage = (count_matches(dna_sequence1, dna_sequence2) / len(dna_sequence1)) * 100
    
            print(f"Similarity: {count_matches(dna_sequence1, dna_sequence2)} matches, {mismatching_position} mismatches. {percentage:0.1f}% match rate.")
            
            
        elif option == 4:
            sequence_num = get_sequence_number()
            if sequence_num == 1:
                i = find_optimal_indel_position(dna_sequence1, dna_sequence2)
                new_dna_suggested_indel = insert_indel(dna_sequence1, i)
                new_dna2 = pad_with_indels(dna_sequence2, 1)
                print(f"Insert an indel into Sequence 1 at position {i+1}.")
                mismatching_position2 = len(new_dna_suggested_indel) - count_matches(new_dna_suggested_indel, new_dna2)
                percentage2 = (count_matches(new_dna_suggested_indel, new_dna2) / len(new_dna_suggested_indel)) * 100
                print(f"Similarity: {count_matches(new_dna_suggested_indel, new_dna2)} matches, {mismatching_position2} mismatches. {percentage2:0.1f}% match rate.")
            else:
                i = find_optimal_indel_position(dna_sequence2, dna_sequence1)
                new_dna_suggested_indel = insert_indel(dna_sequence2, i)
                new_dna1 = pad_with_indels(dna_sequence1, 1)
                print(f"Insert an indel into Sequence 2 at position {i+1}.")
                mismatching_position2 = len(new_dna_suggested_indel) - count_matches(new_dna_suggested_indel, new_dna1)
                percentage2 = (count_matches(new_dna_suggested_indel, new_dna1) / len(new_dna_suggested_indel)) * 100
                print(f"Similarity: {count_matches(new_dna_suggested_indel, new_dna2)} matches, {mismatching_position2} mismatches. {percentage2:0.1f}% match rate.")
        print()      
        print_similar_sequences(dna_sequence1, dna_sequence2)            
        print()
        print_menu()
        print()
        option = get_menu_choice()
        print()
        
        
            

    
