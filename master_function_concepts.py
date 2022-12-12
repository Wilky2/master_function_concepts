import string,random

#egzeis 3
def generate_code_with_alphabetical_char(code_length):
    select_list = list(string.ascii_lowercase)
    return "".join(random.sample(select_list,code_length))

print("egzesis 3")
print("Code de longueur 6")
print(f"Code : {generate_code_with_alphabetical_char(6)}\n")

#egzesis 4
def generate_code_with_alphanumeric_char(code_length):
    select_list = list(string.ascii_lowercase) + [f"{i}" for i in range(10)]
    return "".join(random.sample(select_list,code_length))

print("egzesis 4")
print("Code de longueur 7")
print(f"Code : {generate_code_with_alphanumeric_char(7)}\n")

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

slug =  generate_slug("!Cl&rvil Wilky")
print("egzesis 5")
print("slug de la chaine : !Cl&rvil Wilky")
print(f"SLUG : {slug}\n")  
 

#egzesis 6
def separate_char_with_comma(word):
    list_of_char = list(word)
    return ",".join(list_of_char)

result = separate_char_with_comma("Wilky")
print("egzesis 6")
print("Mot choisi : Wilky")
print(f"resultat : {result}\n")

#egzesis 7
def crypt_word_with_alphabet_index(word):
    word_crypt= "-".join([str(ord(char)-97) for char in word.lower()])
    return word_crypt

crypt = crypt_word_with_alphabet_index("ALO")
print("egzesis 7")
print("Mot a decrypter : ALO")
print(f"cryptage : {crypt}\n")

#egzesis 8
def decrypt_word_with_alphabet_index(word_crypt):
    list_of_index = word_crypt.split("-")
    word="".join([chr(int(index)+97) for index in list_of_index])
    return word

decrypt = decrypt_word_with_alphabet_index("0-11-14")
print("egzesis 8")
print("Code : 0-11-14")
print(f"Mot : {decrypt}\n")

#egzesis 9
def swap(parameter1,parameter2):
    temp=parameter1
    parameter1=parameter2
    parameter2=temp
    return (parameter1,parameter2)

swp = swap("Wilky","Clervil")
print("egzesis 9")
print("valeur : Wilky,Clervil")
print(f"resultat : {swp}\n")

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

init_name = initial_name("Jean-Baptiste Jean")
print("egzesis 10")
print("Nom : Jean-Baptiste Jean")
print(f"initial name : {init_name}")
