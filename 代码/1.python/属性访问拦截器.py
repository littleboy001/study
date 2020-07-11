class Person(object):
        def __getattribute__(self,obj):
            print("---test---")
            if obj.startswith("a"):
                return "hahha"
            else:
                return self.test#调用这个会产生死循环


        def test(self):
            print("heihei")

t = Person()

print(t.a) #返回hahha

#t.b #会让程序死掉