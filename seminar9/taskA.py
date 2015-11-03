
def IsAscending(A):
    while A[1] > A[0] or len(A) == 1:
        A = A[1:]
    return len(A)
if IsAscending(input().split() == 1):
    print('YES')
else:
    print('NO')
