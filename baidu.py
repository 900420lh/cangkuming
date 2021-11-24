
import xlrd

# 工作簿对象
wb = xlrd.open_workbook(R"C:\Users\86159\Desktop\python自动化测试（）\python\百度python\百度合作单位-人员管理-二期.xls")


st = wb.sheet_by_index(0)

rows = st.nrows
cols =  st.ncols


#sum_age = 0
#sum_sal = 0
#男女
a = 0
b = 0
#年龄
c = 0
#工资
d = 0
e = 0
#手机号
f = 0
g = 0
h = 0
#地区
i = 0
k = 0
l = 0
m = 0
#公司
n = 0
for j  in range(1,rows):
    data = st.row_values(j)
    if data[8] == "男":
        a = a + 1
    elif data[8] =='女' :
        b = b + 1 
    if data[7] > 45 :
        c = c + 1
    if data[11] > 8000:
        d = d + 1
    elif data[11] < 3000:
        e = e + 1
    if data[5] .startswith('14' or '17'):
        f = f + 1
    elif data[5].startswith('13'):
        g = g + 1
    elif data[5].startswith('15'):
        h = h + 1
    if data[9] .startswith('黑龙江'):
        i = i + 1
    elif data[9].startswith('北京'):
        k = k + 1
    elif data[9].startswith('福建'):
        l = h + 1
    elif data[9].startswith('四川'):
        m = m + 1
    if data[13] .endswith('传媒有限公司'):
        n = n + 1
    #sum_age = sum_age + data[2]
    #sum_sal = sum_sal +  data[4]

print("男生人数：",a)
print('女生人数：',b)
print('45岁以上的人数：',c)
print('工资8000以上的人数：',d)
print('工资3000以下的人数：',e)
print('电信人数：',f)
print('移动人数：',g)
print('联通人数：',h)
print("黑龙江",i)
print('北京',k)
print('福建',l)
print('四川',m)
print('传媒有限公司',n)




























