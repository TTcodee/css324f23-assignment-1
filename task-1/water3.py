def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4;

def successors(s):
    x, y, z = s
    # Try empty
    if x > 0:
        yield ((0, y, z), 8);
    if y > 0:
        yield ((x, 0, z), 8);
    if z > 0:
        yield ((x, y, 0), 8);
    # Try fill others with 8 litres cup
    t = 5 - y;
    if x > 0 and t > 0:
        if (x >= t):
            yield ((x - t, y + t, z), t);
        else:
            yield ((0, y + x, z), x);
    t = 3 - z;
    if x > 0 and t > 0:
        if (x >= t):
            yield ((x - t, y, z + t), t);
        else:
            yield ((0, y, z + x), x);
    # Try fill others with 5 litres cup
    t = 8 - x;
    if y > 0 and t > 0:
        if (y >= t):
            yield ((x + t, y - t, z), t);
        else:
            yield ((x + y, 0, z), y);
    t = 3 - z;
    if y > 0 and t > 0:
        if (y >= t):
            yield ((x, y - t, z + t), t);
        else:
            yield ((x, 0, z + y), y);
    # Try fill others with 3 litres cup
    t = 8 - x;
    if z > 0 and t > 0:
        if (z >= t):
            yield ((x + t, y, z - t), t);
        else:
            yield ((x + z, y, 0), z);
    t = 5 - y;
    if z > 0 and t > 0:
        if (z >= t):
            yield ((x, y + t, z - t), t);
        else:
            yield ((x, y + z, 0), z);

    # Try full
    if x < 8:
        yield ((8, y, z), 8 -x);
    if y < 5:
        yield ((x, 5, z), 5 - y);
    if z < 3:
        yield ((x, y, 3), 3 - z);
    return []
