import random as rd


def octet_mass():
    a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    c = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    d = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    e = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    f = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    g = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    h = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    i = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    j = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    k = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    ll = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    m = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    n = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    o = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    p = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    q = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    r = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    s = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    t = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    u = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    v = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    w = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    y = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    z = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "@", ".", ":", ",", "_", "=", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    sel = [a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j,
           k, ll, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    direct = rd.choice(sel)
    password = []
    for x in range(8):
        pas = rd.choice(direct)
        password.append(pas)

    for x in range(rd.randint(1, 16)):
        num = rd.randint(1, 7)
        password[num] = rd.choice(direct)
        num = rd.randint(1, 7)
        password[num] = rd.choice(direct)
        num = rd.randint(1, 7)
        password[num] = rd.choice(direct)

    passca = ""
    for x in range(0, 8):
        y = rd.choice(password)
        case = [y.lower(), y.upper()]
        case1 = rd.choice(case)
        passca = passca + case1
    return passca

