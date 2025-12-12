# 初始化数据：座位信息（键为座位号，值为预约状态和预约人）
seats = {
    "A01": {"status": "空闲", "user": None},
    "A02": {"status": "空闲", "user": None},
    "A03": {"status": "空闲", "user": None},
    "B01": {"status": "空闲", "user": None},
    "B02": {"status": "空闲", "user": None}
}
# 存储用户预约记录
user_reservations = {}


def display_menu():
    """显示功能菜单"""
    print("\n===== 图书馆座位预约系统 =====")
    print("1. 查询可用座位")
    print("2. 预约座位")
    print("3. 取消预约")
    print("4. 查看我的预约")
    print("5. 管理员添加座位")
    print("6. 退出系统")
    print("==============================")


def query_seats():
    """查询可用座位"""
    print("\n【当前座位状态】")
    for seat_num, info in seats.items():
        print(f"座位{seat_num}: {info['status']}（预约人：{info['user'] or '无'}）")


def reserve_seat():
    """预约座位"""
    user_name = input("\n请输入你的姓名：")
    seat_num = input("请输入要预约的座位号（如A01）：")

    if seat_num not in seats:
        print("错误：该座位不存在！")
        return
    if seats[seat_num]["status"] == "已预约":
        print("错误：该座位已被预约！")
        return

    # 执行预约
    seats[seat_num]["status"] = "已预约"
    seats[seat_num]["user"] = user_name
    # 记录用户预约
    if user_name not in user_reservations:
        user_reservations[user_name] = []
    user_reservations[user_name].append(seat_num)
    print(f"成功预约座位{seat_num}！")


def cancel_reservation():
    """取消预约"""
    user_name = input("\n请输入你的姓名：")
    if user_name not in user_reservations or not user_reservations[user_name]:
        print("你暂无预约记录！")
        return

    print(f"你的预约座位：{user_reservations[user_name]}")
    seat_num = input("请输入要取消预约的座位号：")

    if seat_num not in user_reservations[user_name]:
        print("错误：你未预约该座位！")
        return

    # 执行取消
    seats[seat_num]["status"] = "空闲"
    seats[seat_num]["user"] = None
    user_reservations[user_name].remove(seat_num)
    if not user_reservations[user_name]:
        del user_reservations[user_name]
    print(f"成功取消座位{seat_num}的预约！")


def view_my_reservations():
    """查看我的预约"""
    user_name = input("\n请输入你的姓名：")
    if user_name not in user_reservations or not user_reservations[user_name]:
        print("你暂无预约记录！")
        return
    print(f"你的预约座位：{user_reservations[user_name]}")


def add_seat():
    """管理员添加座位"""
    admin_pwd = input("\n请输入管理员密码：")
    if admin_pwd != "admin123":  # 简单的管理员密码验证
        print("密码错误，无权限操作！")
        return

    new_seat = input("请输入要添加的座位号（如C01）：")
    if new_seat in seats:
        print("错误：该座位已存在！")
        return

    seats[new_seat] = {"status": "空闲", "user": None}
    print(f"成功添加座位{new_seat}！")


# 主程序循环
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("请输入功能编号（1-6）：")

        if choice == "1":
            query_seats()
        elif choice == "2":
            reserve_seat()
        elif choice == "3":
            cancel_reservation()
        elif choice == "4":
            view_my_reservations()
        elif choice == "5":
            add_seat()
        elif choice == "6":
            print("感谢使用图书馆座位预约系统，再见！")
            break
        else:
            print("输入错误，请输入1-6之间的数字！")