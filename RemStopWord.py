import pdb
import sys

#take the input file name , and output generated by the model-file

#check stop words
#sw_file =open("stopWords.txt")
#stopWords=sw_file.readlines()

#check pos output
pos_file = open("pos_output.txt")
pos_file_lines = pos_file.readlines()
posIndex =0 #to skip forward lines
posSkip = 0

inp_file = open(sys.argv[1],"r")
arg  = sys.argv[2]
if(arg == 'test'):
    index = -1
    posSkip = 2
else:
    index =-2
    posSkip =3


#dump the contents into the file int_input.txt

result = open("int_input.txt","w")

inp_file_lines = inp_file.readlines()

#for each line prepend features

for i in range(len(inp_file_lines)):

    if inp_file_lines[i]=='\n':
        result.write("\n") #might need to change this for POS tagging
        continue

    item_toks = inp_file_lines[i].strip().split(" ")
    pos_tokens = pos_file_lines[posIndex].strip().split("\t")

    #extract previous word as feature 
    if i > 0 : 
        p_item_toks = inp_file_lines[i-1].strip().split(" ")
    else :
        p_item_toks = item_toks

    if p_item_toks == ['']:#if the previous word was new line then its a new sentence
        p_item_toks = item_toks

    prev_word = p_item_toks[index]
   
    #extract previous POS tokens as features
    if posIndex - posSkip >= 0:
        p_pos_tokens = pos_file_lines[posIndex-posSkip].strip().split("\t")
    else:
        p_pos_tokens = pos_tokens

    #check stop words
    #if item_toks[index].lower() in stopWords: #might be -1 for test input
    #    item_toks = ['STOPWORD']+item_toks

    #check for uppercase and include
    if item_toks[index][0].isupper():
        item_toks = ['CAPITAL']+item_toks

    #check for POS and include previous POS as well
    if item_toks[index] == pos_tokens[-2] :
       item_toks = [pos_tokens[-1]]+item_toks #current pos tags
       #item_toks = [p_pos_tokens[-1]]+item_toks #previous pos tags

    #include previous word 
    item_toks = [prev_word]+item_toks

    #check POS feature W-1 = IN , W0 = JJ
    #if 'JJ' in pos_tokens and 'IN' in p_pos_tokens :
    #    item_toks = ['INJJ']+item_toks


    #include previous POS features
    #if 'JJ' in pos_tokens and 'IN' in p_pos_tokens :
    #    item_toks = ['INJJ']+item_toks

    posIndex = posIndex + posSkip
    result_str = " ".join(item_toks)
    result_str = result_str+"\n"
    result.write(result_str)

inp_file.close()
result.close()
