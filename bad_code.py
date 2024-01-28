def highly_complex_code(a, b, c, d):
    result = 0

    if a > 0:
        result += a
    elif a < 0:
        if b > 0:
            result -= b
        elif b < 0:
            if c > 0:
                result += c
            elif c < 0:
                if d > 0:
                    result -= d
                elif d < 0:
                    result += a * b * c * d
                else:
                    result -= a + b + c + d
            else:
                result += a - b - c - d
        else:
            result -= a * b * c * d
    else:
        result = 42

    return result

# 使用例
output = highly_complex_code(3, -2, 5, -4)
print(output)
