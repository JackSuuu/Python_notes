

def hanoi(n, x, y, z):
    if n == 1:
        print(f'{x} --> {z}')
    else:
        hanoi(n-1, x, z, y)  # 将n-1个盘子从x移动到y上
        print(f'{x} --> {z}')  # 将最底下的最后一个盘子从x移动到y上
        hanoi(n-1, y, x, z)  # 将y上的n-1个盘子移动到z上


n = int(input('请输入汉诺塔的层数: '))

hanoi(n, 'x', 'y', 'z')

