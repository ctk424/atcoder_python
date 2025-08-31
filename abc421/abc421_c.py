n = int(input())
s = input()
"""
考えられるゴール
ababa...
babab...
になるには何回移動が必要か ==> 何マス離れているか
"""
a_pos = [] # sに含まれるAの座標
for i in range(n + n):
    if s[i] == 'A':
        a_pos.append(i)
odd = [] # Aが偶数番目の時の座標
even = [] # Aが奇数番目の時の座標
for i in range(0, n + n, 2):
    odd.append(i)
for i in range(1, n + n, 2):
    even.append(i)
# print(a_pos)
# print(odd)
# print(even)
"""
a_posがoddとevenからいくつ離れているか計算
少ないほうが最小移動回数
"""
cost_odd, cost_even = 0, 0
for i in range(n):
    cost_odd += abs(a_pos[i] - odd[i])
for i in range(n):
    cost_even += abs(a_pos[i] - even[i])
print(min(cost_odd, cost_even))
