import json


def signup_data_get():
    result = []
    with open("E:/testpro/MeetHere/python-autoTest/src/data/signup_data.json", "r", encoding="utf-8") as f:
        datas = json.load(f)
        for data in datas.values():
            result.append((data['username'], data['email'], data['phone'],
                           data['userid'], data['password'],data['expect']))
    return result


def login_data_get():
    result = []
    with open("E:/testpro/MeetHere/python-autoTest/src/data/login_data.json", "r", encoding="utf-8") as f:
        datas = json.load(f)
        for data in datas.values():
            result.append((data['userid'], data['password'], data['expect']))
    return result


if __name__ == '__main__':
    print(signup_data_get())
