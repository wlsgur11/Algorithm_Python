def solution(id_pw, db):
    for i in db:
        if i[0] == id_pw[0]:
            print(i)
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"