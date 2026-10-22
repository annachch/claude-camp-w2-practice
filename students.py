from argparse import Action


students={}
def addstudents():
    name=input("请输入学员姓名").strip()
    if not name:
        print ("姓名不能为空")
        return
    else: 
        print (f"""Welcome {name}""")
    if name in students:
        print ("姓名已存在")
        return
    email=input("请输入学员邮箱").strip()
    if not email:
        print ("邮箱不能为空")
        return
    date=input("请输入加入时间 YYYY-MM-DD").strip()     
    if not date:
        print ("加入时间不能为空")
        return
    students[name]={
        "姓名":name,
        "邮箱":email,
        "加入日期":date,
    }
    print ("添加成功")
def querystudents():
    name=input("请输入要查询的姓名").strip()
    if not name:
        print("姓名不能为空")
        return
    student=students.get(name)
    if student is None:
        print("未找到该学员")
    else: 
        print("姓名：",student["姓名"])
        print("邮箱：",student["邮箱"])
        print("加入日期",student["加入日期"])
def deletestudents():
    name=input("要删去的学生姓名").strip()
    if not name:
        print ("姓名不能为空")
        return
    if name not in students:
        print ("未找到该学员信息")
    else: del students[name]
    print ("删除成功")
def main():
    actions={
        "1":addstudents,
        "2":querystudents,
        "3":deletestudents,
    }
    while True:
        print ("请输入所需要的操作编号")
        print("1:加入学生")
        print("2:查询学生")
        print("3:删除学生")
        print ("0: 退出")
        choice=input("请选择操作").strip()
        if choice=="0":
            print("程序退出中，再见")
            break

        action=actions.get(choice)
        if action is None:
            print ("输入无效，重新选择")
        else: 
            action()
if __name__ == "__main__":    
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序退出中，再见")
        
               

               
               



               
