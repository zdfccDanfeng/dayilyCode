# -*- encoding:utf-8 -*-

from __future__ import annotations

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
         给定一个以字符串表示的非负整数num，移除这个数中的 k 位数字，使得剩下的数字最小。
        注意:
        num 的长度小于 10002 且≥ k。
        num 不会包含任何前导零。
        示例 1 :

        输入: num = "1432219", k = 3
        输出: "1219"
        解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
        示例 2 :

        输入: num = "10200", k = 1
        输出: "200"
        解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
        示例 3 :

        输入: num = "10", k = 2
        输出: "0"
        解释: 从原数字移除所有的数字，剩余为空就是0。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/remove-k-digits
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        :param num:
        :param k:
        :return:
        """
        n = len(num)
        if n <= k:
            return "0"
        def findRemoveIndex(s):
            res = -1
            for i in range(len(s)-1):
                if s[i] > s[i+1]:
                    # 从高位向低位寻找第一个前面比后面大的字符
                    res = i
                    break
            return res if res != -1 else len(s)-1
        while k > 0 and num:
            removeIndex = findRemoveIndex(num)
            num = num[:removeIndex] + num[removeIndex+1:]
            k= k -1
        # print("num is :", num)
        c = 0
        if len(num) > 0:
            for i in range(len(num)):
                if num[i] != '0':
                    num = num[i:]
                    break
                else:
                    c += 1
        if c == len(num):
            return "0"
        # print("res is =====", num)
        return "0" if len(num) == 0 or not num else num








if __name__ == '__main__':
    c = Solution()
    nums = '12'
    k = 1
    res = c.removeKdigits(nums,k)
    print("res is : ", res)








