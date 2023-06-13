from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''
def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
#test
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # print(line.rstrip())
            data = line.rstrip()
            usr, passw  = data.split(", ")
            print("user: ", usr, ", Password: ", fer.decrypt(passw.encode()).decode())
def add():
    name = input('Account name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write("{ Account: " + name + ", " + "Password: " + fer.encrypt(pwd.encode()).decode() + " }\n")

while True:
    mode = input("Do you want to view or add password? [q to quite] [view, add]: ").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode..!")
        continue