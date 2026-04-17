username = input("Isi username : ")
password = input("Isi password : ")

data = [
    {
        "username" : "guntur123",
        "password" : "123"
    },
    
    {
        "username" : "fadel123",
        "password" : "123"
    }
    
]

bool = False

for i in data :
    if (i["username"] == username) & (i["password"] == password) :
        bool = True
        print("Akun ada")
        break

if not bool :
    print("Akun tidak ada")
        
    