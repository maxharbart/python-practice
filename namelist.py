def namelist(names):
    
    nms = []
    for item in names:
        arr = list(item.values())
        for x in arr:
            nms.append(x)
        
    if len(nms) == 1:
        print(nms[0])
    elif len(nms) == 2:
        print(nms[0] + ' & ' + nms[1])
    else:
        res = ''
        for item in range(0, len(nms) - 2):
            res += nms[item]
            res += ', '
        res += nms[-2]
        res += ' & '
        res += nms[-1]
        print(res)
        
namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])