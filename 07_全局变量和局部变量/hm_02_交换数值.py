a = 1000
c = 99

# 交换ac的数值
# （1）
q = a
a = c
c = q
# （2）
q = a + c
c = q - a
a = q - c
# （3）
a,c = c,a   # 此处右边实际为（c，a）元组分别给左边赋值
