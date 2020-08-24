# 输入苹果单价
price_str=input("输入苹果单价")
# 输入购买数量
num_str=input("输入购买数量")
# 转换单价
price=float(price_str)
# 转换数量
num=float(num_str)
# 应付款值
money=price*num
#输出账单
print(money)
#-------------------------------------------------------------------#
# 推荐直接使用  price=float(input("输入苹果单价"))