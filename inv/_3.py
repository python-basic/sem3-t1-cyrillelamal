def heron(a, b, c):
    """Return area of triangle taht posses passed dimensions"""
    p = 1/2 * (a + b + c)
    s = (p * (p-a) * (p - b) * (p - c))**(1/2)
    return s
