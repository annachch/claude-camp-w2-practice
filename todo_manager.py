import json
from pathlib import Path

#将todos.json放在Python程序所在的文件夹
todo_file = Path(__file__).parent / "todos.json"
print("待办文件保存位置:",todo_file.resolve())

#create a dictionary of todo
todo ={}

def load_todo():
    #程序启动时，加载之前保存的数据
    try:
        with open(todo_file, "r", encoding="utf-8") as file:
            data=json.load(file)

        todo.update(data)
        return True
    except FileNotFoundError:
        print ("未找到todos.json文件，将创建新的待办事项列表。")
        return True
    except (json.JSONDecodeError, UnicodeDecodeError):
        print ("无法读取待办文件内容，请检查todos.json。")
        return False
    except OSError as error:
        print(f"读取文件时发生错误：{error}")
        return False

def save_todo():
    try:
        with open(todo_file, "w", encoding="utf-8") as file:
            json.dump(todo, file, ensure_ascii=False, indent=4)
        return True
    except OSError as error:
        print(f"保存文件时发生错误：{error}")
        print("本次修改仅保留在内存中，退出后可能丢失。")
        return False
#Define a function to add a todo item
def add_todo():
    task=input("请输入待办事项：")
    if not task:
        print("待办事项不能为空，请重新输入。")
        return
    deadline=input("请输入截止日期（格式：YYYY-MM-DD）：")
    if not deadline:
        print("截止日期不能为空，请重新输入。")
        return
    done = input("是否已完成？（y/n）：")
    if done.lower() == "y":
        todo[task] = {"task": task,"deadline": deadline, "completed": True}
    else:
        todo[task] = {"task": task, "deadline": deadline, "completed": False}

    if save_todo():
        print(f"已添加待办事项：{task}")
def view_todo():
    if not todo:
        print("当前没有待办事项。")
        return
    print("\n待办事项列表：")
    for task in todo:
        print(f"- {todo[task]['task']} - 截止日期：{todo[task]['deadline']} - 已完成：{'是' if todo[task]['completed'] else '否'}")
def mark_completed():
    task = input("请输入要标记为已完成的待办事项：")
    if task in todo:
        todo[task]["completed"] = True

        if save_todo():
            print(f"已将待办事项“{task}”标记为已完成。")
    else:
        print(f"未找到待办事项“{task}”。")
def delete_todo():
    task = input("请输入要删除的待办事项：")
    if task in todo:
        del todo[task]
        if save_todo():
            print(f"已删除待办事项“{task}”。")
    else:
        print(f"未找到待办事项“{task}”。")
def main():
    if not load_todo():
        return

    while True:
        print("\n待办事项管理系统")
        print("1. 添加待办事项")
        print("2. 查看待办事项")
        print("3. 完成待办事项")
        print("4. 退出")

        choice = input("请选择操作（1-4）：")

        if choice == "1":
            add_todo()
        elif choice == "2":
            view_todo()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print ("退出程序。")
            break
        else:
            print("无效的选择，请重新输入。")
if __name__ == "__main__":
    main()
