
#Calculate GC content of different sequences in fasta file and output the header of the sequence with the highest content respective GC content in percent.

#store headers of single sequences as keys and sequences as relative values in dictionary
dict = {}
with open("Fasta.txt") as f:
    for line in f: #loop over single lines in file
        line = line.strip() #remove "\n" from linese       
        if line.startswith(">"):       #access only header line     
            header = line.replace(">","")   #remove ">" from header lines
            if header not in dict:      #for headers not already stored in dict
                dict[header] = []       #add header lines as keys to dict
        else:                           #sequence lines
            dict[header].append(line[:])  #add sequence lines as values to  dict


for value in dict:
    dict[value] = "".join(dict[value]) #join sequence lines to one value, which belong to one header


#calculate gc content

# determine length of sequences and parse them to list
length_list = [] 
for value in dict:
    length = len(dict[value]) #determine length of individual sequence and store temporarily in length variable
    length_list += [length] #add temporary length variable to length_list


# determine number of G and C in sequences and store them in list
gc_num_list = []
for value in dict:
    sequence = dict[value] #store different sequences temporarily in sequence variable
    occur_g = sequence.count("G") #count G in sequence
    occur_c = sequence.count("C") # count C in sequence
    occur_gc = int(occur_g) + int(occur_c) #add G and C occurences together   
    gc_num_list += [occur_gc] #add number of GC for each sequence to list
    
#calculate GC content in percent for each sequence
percent_gc_list = []
n = 0
for i in gc_num_list:
    percent = i / length_list[n] #divide GC number by total sequence length for each sequence
    n = n+1 #counter to specify which sequence length used for division based on index n
    percent_gc_list += [percent] #add different GC contents in percent to list
    

max_gc_index = percent_gc_list.index(max(percent_gc_list)) #determine list index with item with highest GC content to access respective header in dictionary


max_gc_val = max(percent_gc_list) #variable with Max GC content value
max_gc_val = max_gc_val *100 #calculate percent from decimal


max_gc_round = round(max_gc_val, 7) #round percent value with maximal GC content


key_list = list(dict) #store header keys from dictionary in list
highest_header = key_list[max_gc_index] #access header of sequence with highest GC content by index
print(highest_header) 
print(max_gc_round)


    
    
    




                 
    
            
            
            
                
            
            
            
            
            
            
                                 



            
            
            
            
        
        
        




        
