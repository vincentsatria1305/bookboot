def get_book_text(path_to_file) :
    message_contents=""
    with open(path_to_file) as f:
        file_contents = f.read().strip("\n");
        message_contents = message_contents + file_contents;
    #print(message_contents)    
    return message_contents


def number_of_words(path_to_file):
    message_contents=""
    count = 0
    with open(path_to_file) as f:
        file_contents = f.read();
    
        for word in file_contents.split():
        
            count+=1
        #print(f"{count} words found in the document")
    return f"Found {count} total words"

def count_word(path_to_file):
    message_contents=get_book_text(path_to_file)
    dictcount={}
    for char in message_contents:
        char = char.lower()
        if dictcount.get(char)==None:
            dictcount[char]=1
        else:
            dictcount[char]+=1
    return dictcount
def sort_on(dict):
    return dict["num"]


def count_word_report(path_to_file):
    message_contents=get_book_text(path_to_file)
    dictcount={}
    for char in message_contents:
        char = char.lower()
        if char.isalpha():
            #print("alphanum")  
            if dictcount.get(char)==None:
                
                dictcount[char]=1
            else:
                dictcount[char]+=1
    sorted_dict = dict(sorted(dictcount.items(), key=lambda item: item[1], reverse=False))
    result = f"Analyzing book found at {path_to_file} \n "
    result = result + number_of_words(path_to_file) + "\n"
    for record in sorted_dict:
        #print(record)
        result = result + record + ": " + str(sorted_dict[record]) +"\n"
    print(result)
    #return result