#1.显示系统界面
def print_menu():
    systom = "名片管理系统"
    print("="*50)
    print(systom.center(50))
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查询名片")
    print("5.显示所有")
    print("6.保存文件")
    print("7.退出系统")
    print("="*50)
def add_new_card_infor():
#获取名片信息
    new_name = input("请输入新的姓名:")
    new_addr = input("请输入新的地址:")
    new_qq = input("请输入新的qq:")
    #名片信息导入列表
    #先定义一个字典，把名片信导入字典
    infors = {}
    infors["name"] = new_name
    infors["addr"] = new_addr
    infors["qq"] = new_qq
    #字典添加到列表中
    card_infors.append(infors)
    print(card_infors)#for test
def del_card_infor():    
    remove_name = input("请输入要删除的姓名:")
    card_infors = list(filter(lambda x:x['name']!=remove_name,card_infors))
    print(card_infors)
def change_card_infor():
    change_name = input("请输入要修改的名字:")
    changed_name = input("请输入修改后的名字:")
    for temp in card_infors:
        if temp['name']==change_name:
            temp["name"] = changed_name
            print(card_infors)
            break
    else:
        print("您的输入有误")
def find_card_infor():
    find_name = input("请输入查询的名字:")
    for temp in card_infors:
        if temp['name']==find_name:
            print("%s\t%s\t%s"%(temp["name"],temp["addr"],temp["qq"]))
            break
    else:
        print("没找到")
def show_all_infor():
    print("姓名\t地址\tqq")
    for temp in card_infors:
        print("%s\t%s\t%s"%(temp["name"],temp["addr"],temp["qq"]))
def save_2_file():

    f = open("backup.data","w")
    f.write(str(card_infors))
    f.close()
 

def load_file():
    """导入原文件"""
    global card_infors
    try:
        f = open("backup.data")           
        card_infors = eval(f.read())
        f.close()
    except Exception:
        pass


def main():
    load_file()
    print_menu()  
    #2.获取用户选择
    while True:
        num = int(input("请输入操作序号:"))
        #3.根据用户选择完成操作
        if num==1:
            add_new_card_infor()
        elif num==2:
            del_card_infor()
        elif num==3:
            change_card_infor()
        elif num==4:
            find_card_infor()
        elif num==5:
            show_all_infor()
        elif num==6:
            save_2_file()
        elif num==7:
            break
        else:
            print("您的输入有误，请重新输入")
        print("")#选择操作前空格让界面更好看
#定义名片列表
card_infors = []
if __name__ == "__main__":
    main()