import math

xa, ya, xb, yb, xc, yc = map(int, input().split())

ab = math.sqrt(math.pow(xa-xb, 2) + math.pow(ya-yb, 2))
bc = math.sqrt(math.pow(xb-xc, 2) + math.pow(yb-yc, 2))
ca = math.sqrt(math.pow(xc-xa, 2) + math.pow(yc-ya, 2))

if xa-xb != 0:
    _ab = abs((ya-yb)/(xa-xb))
else:
    _ab = 0
### Silver 5 ###

# 1차: 210116
# 2차: 210917

'''
평행사변형
- 수학
- 기하학
'''

if xb-xc != 0:
    _bc = abs((yb-yc)/(xb-xc))
else:
    _bc = 0

if math.isclose(_ab, _bc):
    print(-1.0)
#if ((ab+bc == ca) or (bc+ca == ab) or (ab+ca == bc)): print(-1.0)
#if (math.fabs(ab+bc-ca), math.fabs(bc+ca-ab), math.fabs(ab+ca-bc) <= sys.float_info.epsilon): print(-1.0)
#if math.isclose(ab+bc, ca) or math.isclose(bc+ca, ab) or math.isclose(ab+ca,bc): print(-1)
else:
    print(max(abs(ab-bc), abs(bc-ca), abs(ca-ab))*2)
