# class Base:
#     counter = 10
#
# class Derived(Base):
#     def get_counter(self):
#         return self.counter
#
"""
实现上面的类
"""
Base = type('Base', (object,), {'counter': 10})
Derived = type('Derived', (Base,), dict(get_counter=lambda self: self.counter))

x = Derived()
print(x.get_counter())

class Meta(type):
    def __new__(cls, name, bases, attrs):
        # Modify the attributes of the class being created
        attrs['additional_attr'] = 'Added by metaclass'
        return super().__new__(cls, name, bases, attrs)
class Me(type):
    def __new__(cls, name, bases, attrs):
        attrs['name'] = 'fick'
        return super().__new__(cls, name, bases, attrs)
# Define a class with the metaclass
class MyClass(metaclass=Me):
    pass

# Create an instance of the class
obj = MyClass()

# Access the additional attribute added by the metaclass
print(obj.name)  # Output: Added by metaclass
