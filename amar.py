Giant Numbers
a,b =map(int,input().split())
y=(a*b)
print(y)

ww3

def impact(a):
    curr_stack = list()
    max_area = 0
    ind = 0
    while ind < len(a):
        if (not curr_stack) or (a[curr_stack[-1]] <= a[ind]):
            curr_stack.append(ind)
            ind += 1
        else:
            top = curr_stack.pop()
            area = (a[top] * ((ind - curr_stack[-1] - 1)  if curr_stack else ind))
            max_area = max(max_area, area)
    while curr_stack:
        top = curr_stack.pop()
        area = (a[top] * ((ind - curr_stack[-1] - 1)  if curr_stack else ind))
        max_area = max(max_area, area)
    return max_area * 600


arr = list(map(int, input().split()))
print(impact(arr))

spaceship

def min_swaps(total_damage, string):
    min_damage = string.count('S')
    if min_damage > total_damage:
        return 'IMPOSSIBLE'

    max_damage = 0
    pwr = 1
    for e in string:
        if e == 'S':
            max_damage += pwr
        else:
            pwr *= 2

    if max_damage <= total_damage:
        return 0

    s_so_far = 0
    swaps = 0

    for e in reversed(string):
        if e == 'S':
            s_so_far += 1
        else:
            pwr //= 2
            tmp = s_so_far*pwr
            if max_damage - tmp > total_damage:
                swaps += s_so_far
                max_damage -= tmp
            else:
                swaps += abs(-(max_damage-total_damage)//pwr)
                break
    return swaps


if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        td, s = input().strip().split()
        td = int(td)
        ans = min_swaps(td, s)
        print(ans)