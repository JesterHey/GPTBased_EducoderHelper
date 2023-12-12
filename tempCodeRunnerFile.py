class Solution:
    def maxArea(self, height) -> int:
        # 设x,y是某两根柱子的索引
        # 要找的是表达式 abs(x-y) * min(height[x],height[y]) 之最大值
        # 初始化两个指针，分别指向数组头和尾的索引 
        # 若向内移动长板,min()函数的值不变或变小，s必然变小
        # 若向内移动短板,min()函数的值可能变大，s可能变大
        i,j = 0,len(height) - 1
        cur_max = (j-i) * min(height[i],height[j])
        while i<j:
            dis = j - i
            cur_v = dis * min(height[i],height[j])
            if cur_v > cur_max:
                cur_max = cur_v
            else:
                pass
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return cur_max