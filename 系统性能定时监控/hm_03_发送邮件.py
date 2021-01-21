#导入第三方模块yagmail
import yagmail
#使用SMTP类创建对象，（发件人，发件授权码，发件服务器）
ya_obj = yagmail.SMTP(user="d572372838@163.com",password="JNAWCLMYBLKNUTWJ",host="smtp.163.com")
#发件内容
content = "hello你好"
#对象发送（收件人，主题，内容）
ya_obj.send("572372838@qq.com","test",content)