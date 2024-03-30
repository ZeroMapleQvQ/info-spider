import pandas as pd

global shape


def read_info(file_path):
    return_list = []

    sheet = pd.read_excel(file_path, sheet_name=0)
    shape = sheet.shape[0]

    name = sheet["学生姓名"]
    username = sheet["登录账号"]
    password = sheet["初始化密码"]

    name = name.values.tolist()
    username = username.values.tolist()
    password = password.values.tolist()

    # return_dict["name"] = name
    # return_dict["username"] = username

    for j in range(shape):
        return_dict = {}
        return_dict["name"] = name[j]
        return_dict["username"] = username[j]
        return_dict["password"] = password[j]
        return_list.append(return_dict)

    # print(return_list)

    # print(f"共有{shape}行")

    return return_list


if __name__ == '__main__':
    # file_path = "./8.1账号.xlsx"
    # sheet = pd.read_excel(file_path, sheet_name=0)

    # name = sheet["学生姓名"]
    # username = sheet["登录账号"]
    # password = sheet["初始化密码"]

    # name = name.values.tolist()
    # username = username.values.tolist()
    # password = password.values.tolist()

    # shape = sheet.shape[0]
    # print(f"共有{shape}行")

    # # print(sheet)
    # # print(sheet.index.values)
    # print(name)
    # print(username)
    # print(password)
    print(read_info("./8.1账号.xlsx"))
