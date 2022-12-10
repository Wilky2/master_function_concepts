import string,random

def generate_code_without_char_repeat(code_length,select_list):
    code = ""
    select_list_copy = select_list.copy()
    for i in range(code_length):
        char = random.choice(select_list_copy)
        select_list_copy.remove(char)
        code+=str(char)
    return code

#egzeis 3
def generate_code_with_alphabetical_char(code_length):
    select_list = list(string.ascii_lowercase)
    return generate_code_without_char_repeat(code_length,select_list)
    
print(generate_code_with_alphabetical_char(6))

#egzesis 4
def generate_code_with_alphanumeric_char(code_length):
    select_list = list(string.ascii_lowercase) + list(range(10))
    return generate_code_without_char_repeat(code_length,select_list)

print(generate_code_with_alphanumeric_char(6))

#egzesis 5
def replace_all_special_char(string):
    special_chars = "!#$%^*(),_+=`~./\|"
    string_without_special_char = string
    for char in special_chars:
        string_without_special_char=string_without_special_char.replace(char,"")
    string_without_special_char=string_without_special_char.replace("@","a")
    string_without_special_char=string_without_special_char.replace("&","e")
    return string_without_special_char

def generate_slug(string):
    string_without_special_char = replace_all_special_char(string)
    return string_without_special_char.replace(" ","-")

print(generate_slug("Clervil Wilky"))    
 

#egzesis 6
def separate_char_with_comma(word):
    list_of_char = list(word)
    return ",".join(list_of_char)

print(separate_char_with_comma("Wilky"))

#egzesis 7
def crypt_word_with_alphabet_index(word):
    alphabet = list(string.ascii_lowercase)
    word_lower = word.lower()
    word_crypt=""
    for char in word_lower:
        word_crypt+=str(alphabet.index(char)) + "-"
    return word_crypt[0:len(word_crypt)-1]

print(crypt_word_with_alphabet_index("ALO"))

#egzesis 8
def decrypt_word_with_alphabet_index(word_crypt):
    alphabet = list(string.ascii_lowercase)
    list_of_index = word_crypt.split("-")
    word=""
    for index in list_of_index:
        word+=alphabet[int(index)]
    return word

print(decrypt_word_with_alphabet_index("0-11-14"))

#egzesis 9
def swap(parameter1,parameter2):
    temp=parameter1
    parameter1=parameter2
    parameter2=temp
    return (parameter1,parameter2)

print(swap("Wilky","Clervil"))

#egzesis 10
def list_of_name_component(name):
    list_of_name_component = name.split()
    list_of_name_component_without_hyphen=[]
    for name_component in list_of_name_component:
        list_of_name_component_without_hyphen += name_component.split("-")
    return list_of_name_component_without_hyphen
    
def initial_name(name):
    name_component = list_of_name_component(name)
    initial = ""
    for component in name_component:
        initial+=component[0]
    return initial

print(initial_name("Jean-Baptiste Jean"))
