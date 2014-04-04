# -*- coding: cp1251 -*-
import re
#def routeId()
def routeId(trType, trDir, info):
    route = info[0][1]
    p = re.compile('\d+')
    r_int = p.findall(route)
    zero_num = 4 - len(r_int[0])
    rout_name = str(trType) + '0'*zero_num + r_int[0]
    p = re.compile('[^\d]')
    r_let = p.findall(route)
    if len(r_let)>1:
        print 'warning!'
    if r_let[0] == 'А':
        n = '1'
    else:
        n = str((ord(r_let[0]) - ord('А')) + 1)
    zero_num = 2 - len(n)
    rout_name = rout_name + '0'*zero_num + n + str(trDir)
    return rout_name
    
info = (('\xca/\xd2 &quot;\xcf\xc5\xd0\xc2\xce\xcc\xc0\xc9\xd1\xca\xc8\xc9&quot;', '15Рc', '&quot;\xd1\xd2. \xd0\xc5\xd3\xd2\xce\xc2\xce&quot;', '\xc1\xd3\xc4\xcd\xc8'), ['5:30', '5:58', '6:26'])
trType = 1
trDir = 0
routNum = routeId(trType, trDir, info)
print routNum


