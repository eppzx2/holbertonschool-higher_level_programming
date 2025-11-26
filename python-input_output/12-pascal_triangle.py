#!/usr/bin/python3
"""
Function that returns the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """some documentation"""

    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
