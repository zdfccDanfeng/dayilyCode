# -*- coding:utf-8 -*-

from __future__ import annotations


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        给定三个字符s1、s2、s3，请你帮忙验s3是否是由s1和s2 交错 组成的。
        两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
        s = s1 + s2 + ... + sn
        t = t1 + t2 + ... + tm
        |n - m| <= 1
        交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
        提示：a + b 意味着字符串 a 和 b 连接。
          思考：
             首先得一个前提是: len(s1) + len(s2) == len(s3).否则两者之间不存在匹配的可能性。当满足匹配的可能性之后，进一步思考下面的问题场景：
            假定 S1的前i个字符,和S2的前j个字符可以进行交错组成s3的前i+j个字符。
             迭代式思考：
               1. 当s1[i] 和 s3[i+j] 相等，如果需要保证前面的结论【s1的前i个字符和s2的前j个字符可以组成s3的前i+j个字符，那么就需要保证 ：s1[:i-1]和s2[:j]可以交错组成s3的前i+j-1个字符串】
               2. 反之，如果s[j]和s3[j+i]相等，如果需要保证前面的结论成立。那么久需要保证s1[:i]和s2[j:]可以组成s3的前i+j-1个字符
               dp[i,j] = dp[i-1,j] && s1[i] == s3[i+j] ||  dp[i,j-1] && s2[j] == s3[i+j]

         最简单的情况分析：
          s1 = 'a', s2 = 'b', s3='ab'
          dp[1,1] = dp[1,0]

          s1 = 'a' s2 = 'bc' s3 = 'abc'

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/interleaving-string
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        n, m, k  = len(s1), len(s2), len(s3)
        if n +m != k :
            return False
        dp = [[False for j in range(m+1)] for i in range(n+1)]

        #边界情况分析处理
        #print("dp is :", dp)
        dp[0][0] = True

        for i in range(0,n+1):
            for j in range(0,m+1):
                if i > 0:
                    if s1[i - 1] == s3[i + j - 1]:
                        dp[i][j] |= dp[i - 1][j]
                if j > 0:
                    if s2[j - 1] == s3[i + j - 1]:
                        dp[i][j] |= dp[i][j - 1]
        print("dp is : ", dp)
        return dp[n][m]

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        """

        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        n,m,k = len(s1),len(s2),len(s3)
        if n+m != k:
            return False
        memo = [[-2 for j in range(m+1)] for i in range(n+1)]
        def dfs(p1:int,p2:int,p3:int)->bool:
            """

            :param p1:
            :param p2:
            :param p3:
            :return:
            """
            if p3 == len(s3):
                return True
            if memo[p1][p2] != -2:
                return memo[p1][p2]
            curr = s3[p3]
            res = False
            if p1 < len(s1) and curr == s1[p1]:
                res = dfs(p1+1,p2,p3+1)
            if res:
                return True
            if p2 < len(s2) and curr == s2[p2]:
                res = dfs(p1,p2+1,p3+1)
            memo[p1][p2] = res
            return res
        return dfs(0,0,0)

if __name__ == '__main__':
    c = Solution()
    s1,s2,s3 = "","",''
    res = c.isInterleave2(s1,s2,s3)
    print("res is : ", res)
