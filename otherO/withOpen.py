def op(file):
    f = open(file,"r+")
    f.write("Hello World")
    print("文件的内容是：{0}".format(f.readlines()))
    f.close()


def withOp(file):
    with open(file,"r+") as f:
        f.write("with open Hello world")
        print("文件的内容是：{0}".format(f.readlines()))


if __name__ == '__main__':
    op("/score.txt")
    withOp("/score.txt")

    tu = tuple((1, 1, 2, 2))
    tu.count(1)
    print(tu)
