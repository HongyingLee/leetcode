#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2019/8/29
# @Name: add_two_numbers

# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 链接：https://leetcode-cn.com/problems/add-two-numbers


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add_two_num(l1, l2):
        a1 = []
        while (l1):
            a1.append(l1.val)
            l1 = l1.next

        a2 = []
        while (l2):
            a2.append(l2.val)
            l2 = l2.next
        s1 = ""
        for i in range(len(a1) - 1, -1, -1):
            s1 += str(a1[i])

        s2 = ""
        for j in range(len(a2) - 1, -1, -1):
            s2 += str(a2[j])

        num = str(int(s1) + int(s2))

        tmp_node = ListNode(None)
        # node = ListNode(None)

        for x in num[::-1]:
            if not tmp_node.val:
                tmp_node.val = x
            #     node = tmp_node
            # else:
            #     tmp_node.next = ListNode(x)
            #     tmp_node = tmp_node.next
        return tmp_node


