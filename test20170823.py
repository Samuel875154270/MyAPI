# class SchoolMember(object):    # 父类
#     def __init__(self, name, age):  # 对象建立时马上对此对象初始化
#         self.name = name
#         self.age = age
#         print('initialized SchoolMember is %s' % self.name)     # 注意格式
#
#     def tell(self):     # 又一个方法
#         print('name: "%s"  age:%s' % (self.name, self.age))     # 格式
#
#
# class Teacher(SchoolMember):  # 子类引用
#     def __init__(self, name, age, salary):          # 自己的方法添加额外元素
#         SchoolMember.__init__(self, name, age)      # 此方法里要加入父类方法的引用，很关键的一步
#         self.salary = salary    # 添加具体内容
#         print('initialized teacher is %s' % self.name)
#
#     def tell(self):
#         SchoolMember.tell(self)     # 同上很关键
#         print("salary:%d" % self.salary)
#
#
# teacher = Teacher("li", 23, 6000)      # 调用与验证
# teacher.tell()
from testClass import testClass
x = testClass()
js = x.ApiService()
print(js['Appid'])