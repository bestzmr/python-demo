# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min_num = max_num = L[0]
        for i in L:
            if min_num > i:
                min_num = i
            elif max_num < i:
                max_num = i
    return (min_num, max_num)

    # Press the green button in the gutter to run the script.


def triangles():
    listL = [[1]]
    yield listL[0]
    for i in range(1, 10):
        L = []
        for j in range(0, i + 1):
            if j == 0 or i == j:
                L.append(1)
            else:
                L.append(listL[i - 1][j - 1] + listL[i - 1][j])
        listL.append(L)
        yield listL[i]
    return listL


if __name__ == '__main__':
    print_hi('PyCharm')
    # print(findMinAndMax([1, 4, 5]))
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
