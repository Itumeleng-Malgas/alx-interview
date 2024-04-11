def pascal_triangle(n):
    """
    a function that returns a list
    of integers representing the
    pascal triangle of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """
    if n <= 0:
        return []

    pascal_tri = [[1]]

    for i in range(1, n):
        prev_row = pascal_tri[-1]
        cur_row = [1]

        for j in range(1, i):
            cur_row.append(prev_row[j - 1] + prev_row[j])

        cur_row.append(1)
        pascal_tri.append(cur_row)

    return pascal_tri
