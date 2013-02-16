def put_chars_array(win, array, x, y, fgcolor=None, bgcolor=None):
    for i in range(len(array)):
        win.putchars(array[i], x, y + i, fgcolor=fgcolor, bgcolor=bgcolor)
