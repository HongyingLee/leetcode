# 反转链表
class ListNode:
    def __init__(self,val,next):
        self.val = val
        self.next = next

def reverseL(head):
    occ = []
    while head:
        occ.append(head.val)
        head = head.next
    occReverse = occ[::-1]

    dummy = tmp = ListNode(0)

    for i in range(len(occReverse)):
        tmp.next = ListNode(occReverse[i])
        tmp = tmp.next

    return dummy.next



# 有序数组，找target，如果target存在，则返回下标值，否则返回-1
def findT(nums,target):
    n = len(nums)
    if n == 0:
        return -1
    l = 0
    r = n - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


print(findT([2,3,4,10,40],10))


"""
ls、pwd、cd
vim i ：wq
du、df、free、top
cat、less、more、tail
grep
chown、chmod

tail -f 10 文件

git pull
git status
git add
git commit
git push
git revert
git checkout -b 分支

后端测试开发
交易所的核心业务：订单、清算、账户、MGT、运营后台；


"""
