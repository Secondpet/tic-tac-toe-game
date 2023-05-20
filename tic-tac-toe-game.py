import random
a = '-'
b = '-'
c = '-'
d = '-'
e = '-'
f = '-'
g = '-'
h = '-'
lg = '-'
common_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
O_list = []
X_list = []
listwin = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
w = int
s = int
print("  0 1 2")
print(f"0 {a} {b} {c}")
print(f"1 {d} {e} {f}")
print(f"2 {g} {h} {lg}")


def kontrol_func(par):
    for i in listwin:
        X_list.sort()
        common = set(par).intersection(i)
        result = list(common)
        if i == result:
            bal = True
            break
        else:
            bal = False
    return bal


while (not kontrol_func(O_list)) or (not kontrol_func(X_list)):
    s = int(input("введите значение по горизонтали: "))
    w = int(input("введите значение по вертикали: "))
    if w == 0 and s == 0:
        if len(common_list) == 0:
            print('Ходы кончились - ничья!')
            break
        else:
            if 1 in common_list:
                common_list.remove(1)
                O_list.append(1)
                a = "O"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(O_list)
            else:
                print('Неверный ход, попробуйте заново')
                break
    elif w == 0 and s == 1:
        if len(common_list) == 0:
            print('Ходы кончились - ничья!')
            break
        else:
            if 2 in common_list:
                common_list.remove(2)
                O_list.append(2)
                b = "O"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(O_list)
            else:
                print('Неверный ход, попробуйте заново')
                break

    elif w == 0 and s == 2:
        if len(common_list) == 0:
            print('Ходы кончились - ничья!')
            break
        else:
            if 3 in common_list:
                common_list.remove(3)
                O_list.append(3)
                c = "O"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(O_list)
            else:
                print('Неверный ход, попробуйте заново')
                break
    elif w == 1 and s == 0:
        if len(common_list) == 0:
            print('Ходы кончились - ничья!')
            break
        else:
            if 4 in common_list:
                common_list.remove(4)
                O_list.append(4)
                d = "O"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(O_list)
            else:
                print('Неверный ход, попробуйте заново')
                break
    elif w == 1 and s == 1:
        if len(common_list) == 0:
            print('Ходы кончились - ничья!')
            break
        else:
            if 5 in common_list:
                common_list.remove(5)
                O_list.append(5)
                e = "O"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(O_list)
            else:
                print('Неверный ход, попробуйте заново')
                break
    elif w == 1 and s == 2:
        if len(common_list) == 0:
            print('Ходы кончились - ничья!')
            break
        else:
            if 6 in common_list:
                common_list.remove(6)
                O_list.append(6)
                f = "O"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(O_list)
            else:
                print('Неверный ход, попробуйте заново')
                break
    elif w == 2 and s == 0:
        if len(common_list) == 0:
            print('Ходы кончились - ничья!')
            break
        else:
            if 7 in common_list:
                common_list.remove(7)
                O_list.append(7)
                g = "O"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(O_list)
            else:
                print('Неверный ход, попробуйте заново')
                break
    elif w == 2 and s == 1:
        if len(common_list) == 0:
            print('Ходы кончились - ничья!')
            break
        else:
            if 8 in common_list:
                common_list.remove(8)
                O_list.append(8)
                h = "O"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(O_list)
            else:
                print('Неверный ход, попробуйте заново')
                break
    elif w == 2 and s == 2:
        if len(common_list) == 0:
            print('Ходы кончились - ничья!')
            break
        else:
            if 9 in common_list:
                common_list.remove(9)
                O_list.append(9)
                lg = "O"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(O_list)
            else:
                print('Неверный ход, попробуйте игру заново')
                break
    else:
        print('НЕверные поля попробуйте игру заново')
        break

    if kontrol_func(O_list):
        print("Вы победили")
        break
    else:
        ran_comp = int(random.choice(common_list))
        if ran_comp == 1:
            if len(common_list) == 0:
                print('Ходы кончились - ничья!')
                break
            else:
                common_list.remove(1)
                X_list.append(1)
                a = "X"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(X_list)
        elif ran_comp == 2:
            if len(common_list) == 0:
                print('Ходы кончились - ничья!')
                break
            else:
                common_list.remove(2)
                X_list.append(2)
                b = "X"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(X_list)
        elif ran_comp == 3:
            if len(common_list) == 0:
                print('Ходы кончились - ничья!')
                break
            else:
                common_list.remove(3)
                X_list.append(3)
                c = "X"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(X_list)
        elif ran_comp == 4:
            if len(common_list) == 0:
                print('Ходы кончились - ничья!')
                break
            else:
                common_list.remove(4)
                X_list.append(4)
                d = "X"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(X_list)
        elif ran_comp == 5:
            if len(common_list) == 0:
                print('Ходы кончились - ничья!')
                break
            else:
                common_list.remove(5)
                X_list.append(5)
                e = "X"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(X_list)
        elif ran_comp == 6:
            if len(common_list) == 0:
                print('Ходы кончились - ничья!')
                break
            else:
                common_list.remove(6)
                X_list.append(6)
                f = "X"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(X_list)
        elif ran_comp == 7:
            if len(common_list) == 0:
                print('Ходы кончились - ничья!')
                break
            else:
                common_list.remove(7)
                X_list.append(7)
                g = "X"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(X_list)
        elif ran_comp == 8:
            if len(common_list) == 0:
                print('Ходы кончились - ничья!')
                break
            else:
                common_list.remove(8)
                X_list.append(8)
                h = "X"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(X_list)
        elif ran_comp == 9:
            if len(common_list) == 0:
                print('Ходы кончились - ничья!')
                break
            else:
                common_list.remove(9)
                X_list.append(9)
                lg = "X"
                print("  0 1 2")
                print(f"0 {a} {b} {c}")
                print(f"1 {d} {e} {f}")
                print(f"2 {g} {h} {lg}")
                kontrol_func(X_list)
        else:
            print("Неверное поле")
        if kontrol_func(X_list):
            print("Компьютер победил")
            break
        else:
            continue