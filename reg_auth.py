#-*- coding:utf-8 -*-
import hashlib
import dbaccess

db = dbaccess.load()


def islogin(login):
    return bool(db.get(login))
islogin('vasya')

def add_user(login, password):
    if islogin(login):
        return False
    password = hashlib.sha512(password.encode('utf-8')).hexdigest()
    db[login] = {'password':password}
    dbaccess.save(db)
    return True





def front():
    print("Введите логин")
    login1 = input()
    for i in db.keys():
        if i == login1:
            print('Такой логин уже есть')
            continue                      #тут должно просить ввести логин заново, если он есть в базе
    print("ВВедите пароль")
    password1 = input()
    add_user(login1,password1)

front()
print(db.keys())