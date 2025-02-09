def solution(wallpaper):
    lux, luy, rdx, rdy = 0, 0, len(wallpaper), len(wallpaper[0])
    rev_wallpaper = []
    for i in range(len(wallpaper[0])):
        a = ""
        for j in range(len(wallpaper)):
            a += wallpaper[j][i]
        rev_wallpaper.append(a)
    for i in wallpaper:
        if "#" in i:
            break
        lux += 1
    for i in rev_wallpaper:
        if "#" in i:
            break
        luy += 1
    for i in wallpaper[::-1]:
        if "#" in i:
            break
        rdx -= 1
    for i in rev_wallpaper[::-1]:
        if "#" in i:
            break
        rdy -= 1
    return lux, luy, rdx, rdy