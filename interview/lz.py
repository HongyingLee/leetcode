# txt文件，英文文章，统计词频
import random


def wordsNum(file):
    with open(file, "rb") as f:
        data = f.read().split(" ").strip()
        dict_num = {}
        for i in range(data):
            if data[i] not in dict_num:
                dict_num[i] = 1
            else:
                dict_num[i] += 1
    return dict_num


# 两个倒序列表，合并成一个倒序列表

def mergeList(l1, l2):
    res = l1.extend(l2)
    n = len(res)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if res[i] < res[j]:
                res[i], res[j] = res[j], res[i]
    return res

# 彩票36选7

def seven(nums,target):
    total = []
    i = nums
    while i > 0:
        if random.randint(0,100) not in total:
            total.append(random.randint(0,100))
            i -= 1
    print(total)


    res = []
    j = target
    while j > 0:
        if total[random.randint(0,nums)] not in res:
            res.append(total[random.randint(0,nums)])
            j -= 1

    return res

print(seven(36,7))



# update 表名 set (key1,key2) values (value1,value2);
# 订单表、用户表 ，用户id
# select 用户表.用户id,sum(order.money) as totalMoney from order join user on user.id = order.userId group by order.userId having sum(order.money) > 100;

#cipan  du/df

#free

# top

# lsof

# ps

"""
1、业务逻辑；
2、业务模块内部
3、移动端：网络、设备性能
    PC 
4、兼容性
5、性能测试：接口、页面、APP
6、安全：
"""

"""
1、
"""