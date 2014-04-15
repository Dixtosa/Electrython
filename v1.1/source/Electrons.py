#import About
import math
k=9*10**9
Point_List=[]
Point_List_Dzalwir=[]

"""Point_List=[
    [[400,100],2],
    [[400,200],2],
    [[400,400],-5]
    ]
"""


def addp(x):
    Point_List.append(x)

def remp(x):
    Point_List.remove(x)
def lenP():
    return len(Point_List)
def CLRp():
    global Point_List,Point_List_Dzalwir
    Point_List=[]
    Point_List_Dzalwir=[]
def ret():
    return Point_List

def addp_dzalw(XY):
    x,y=XY[0]
    Point_List_Dzalwir=Point_List
    Point_List_Dzalwir.append(XY)
    
    managed_dz=convert(Point_List_Dzalwir)
    added_dz=Vec_Add_All(managed_dz)
    Point_List_Dzalwir.remove(XY)
    for i in added_dz:
    	if i[0]==[x,y]: return i[1]


def convert(Point_List,zoom=40):
   Point_managed=[]
   for i in Point_List:
      [x,y],q=i
      tmp=[]
      for j in Point_List:
         if i!=j:
            [_x,_y],_q=j
            dx=(_x-x)/(100.0*zoom)
            dy=(_y-y)/(100.0*zoom)
            r=math.sqrt(dx**2+dy**2)
            f=-(k*q*_q)/(float(r)**2)
            f/=50000
            COS=dx/r
            SIN=dy/r
            tmp.append([j,[x+int(f*COS),y+int(f*SIN)]])
      Point_managed.append([i,tmp])
   return Point_managed




def Vec_Add_All(Point_managed):
    VECz=[]
    #print "Point_managed=",Point_managed
    for i in Point_managed:
        main=i[0][0]
        otherz=i[1]#tmp
        others=[]
        for tmp in otherz: others.append(tmp[1])
        #print "main,others=", main,others
        addEd=Vec_Add(main,others)
        VECz.append(addEd)
    #print "VECz",VECz
    return VECz



def Vec_Add(main,others):
    while True:
        if len(others)>=2:
            f=others[0]
            s=others[1]
            tmp_X=s[0]-main[0]
            tmp_Y=f[1]-main[1]
            tmp=[f[0]+tmp_X,s[1]+tmp_Y]
            others.remove(f)
            others.remove(s)
            others.insert(0,tmp)
        else:
            break
    return [main,others[0]]



#managed_=convert()
#added_=Vec_Add_All(managed_)

#print Vec_Add((100,100),[[123,123],[150,1]])
