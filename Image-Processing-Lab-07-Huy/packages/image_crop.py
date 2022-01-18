def crop(img, w, h, wr, hr):
    ls = []
    coordinate = []
    for x in range(0, w, wr):
        for y in range(0, h, hr):
            if x + wr > w:
                x = w - wr
            elif y + hr > h:
                y = h - hr
            coordinate.append((x, y, x+wr, y+hr))
            roi = img[x:x+wr, y:y+hr]
            ls.append(roi)
    return ls, coordinate