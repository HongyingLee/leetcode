# 某气象观测程序在一个文件记录了每30分钟的天气情况，给定两种天气情况，找出两种天气(不限出现的前后顺序)变化相隔最小的时间间隔。
# PS:若两种天气相邻出现，则最小时间间隔即为30分钟
# 例如
# 输入:
# 输入:[["sunny","sunny","overcast","overcast","light rain","sunny"],overcast,sunny]
# 输出:30

def findX(weathers, weather1, weather2):
    n = len(weathers)
    res = 0
    # 0,1,5
    w1 = []
    # 2,3
    w2 = []

    for i in range(n):
        if weathers[i] == weather1:
            w1.append(i)
        elif weathers[i] == weather2:
            w2.append(i)
        else:
            pass

    if len(w1) == 0 or len(w2) == 0:
        return 0
    else:
        x = []
        for i in w1:
            for j in w2:
                x.append(abs(j - i))
        res = min(x) * 30

    return res


if __name__ == '__main__':
    print(findX(["sunny", "sunny", "overcast", "overcast", "light rain", "overcast", "overcast", "sunny"], "light rain", "sunny"))

    # 表：Visits
    # +-------------+---------+
    # | Column Name | Type    |
    # +-------------+---------+
    # | visit_id    | int     |
    # | customer_id | int     |
    # +-------------+---------+
    # visit_id 是该表的主键。
    # 该表包含有关光临过购物中心的顾客的信息。
    #  
    # 表：Transactions
    # +----------------+---------+
    # | Column Name    | Type    |
    # +----------------+---------+
    # | transaction_id | int     |
    # | visit_id       | int     |
    # | amount         | int     |
    # +----------------+---------+
    # transaction_id 是此表的主键。
    # 此表包含 visit_id 期间进行的交易的信息。
    #  
    # 有一些顾客可能光顾了购物中心但没有进行交易。请你编写一个 SQL 查询，来查找这些顾客的 ID ，以及他们只光顾不交易的次数。
    # 返回以 任何顺序 排序的结果表。

# select Visits.customer_id,count(*) as num from Visits join Transactions on Visits.visit_id = Transactions.visit_id where Transactions.amount = 0 group by Visits.customer_id;

# 课件、管理老师、学生、拉新、增长、技术项目；
#