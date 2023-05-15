# INHERITANCE

Encapsulation is one of the fundamental concepts of object-oriented programming (OOP) that involves hiding the internal details of an object and exposing only the necessary interface or public methods. It's a way to restrict direct access to the object's properties and methods from outside the object and provide controlled access through well-defined interfaces. 

In OOP, encapsulation is achieved through the use of access modifiers, such as public, private, and protected. 

- Public methods and properties are accessible from anywhere, including outside the class.
- Private methods and properties are only accessible within the class and are not visible from outside the class.
- Protected methods and properties are only accessible within the class and its subclasses.

By encapsulating the internal details of an object and exposing only the necessary interface, you can prevent unauthorized modification of the object's state and ensure that the object is used correctly. Encapsulation also allows you to change the implementation details of the object without affecting the code that uses the object.

Here's an example of encapsulation in Python:

```python
class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number   # Private attribute
        self.__balance = balance                 # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance
```

In this example, we define a `BankAccount` class with two private attributes (`__account_number` and `__balance`) and three public methods (`deposit`, `withdraw`, and `get_balance`). The private attributes are not visible from outside the class, but the public methods provide a controlled interface to access and modify the object's state.

The `deposit` method allows you to deposit money into the account by adding the specified amount to the balance. The `withdraw` method allows you to withdraw money from the account by subtracting the specified amount from the balance, but only if the balance is sufficient. The `get_balance` method allows you to retrieve the current balance of the account.

By encapsulating the `account_number` and `balance` attributes and providing controlled access through public methods, we ensure that the object's state is not modified in unauthorized ways and that the object is used correctly.

## Private methods/properties
In Python, there is no true concept of private methods or properties, but there is a convention to denote a property or method as private. A private method or property is one that is intended to be used only within the class and not by the code outside of the class.

In Python, you can denote a property or method as private by adding a double underscore prefix before the property or method name. This is known as name mangling. Python will automatically prepend the name of the class to the property or method name to avoid name clashes with properties or methods in subclasses. 

For example, consider the following class:

```python
class MyClass:

    def __init__(self):
        self.__private_property = 42

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()
        print(f"The private property value is {self.__private_property}.")
```

In this example, the `__private_property` and `__private_method` are denoted as private using the double underscore prefix. The `public_method` is a public method that can be accessed from outside the class.

However, despite the use of name mangling to make the property and method private, it is still possible to access them from outside the class by using the mangled name. For example, you can access the private property and method of the `MyClass` object as follows:

```python
obj = MyClass()
print(obj._MyClass__private_property)   # Output: 42
obj._MyClass__private_method()          # Output: "This is a private method."
```

Note that accessing private properties or methods of a class from outside the class is generally discouraged because it can break encapsulation and lead to code that is difficult to maintain. Instead, it is better to rely on the public interface of the class to interact with its properties and methods.

## Protected methods/properties

In Python, protected methods and properties are denoted with a single underscore prefix before the method or property name. The use of a single underscore prefix is a convention to indicate that a method or property is intended for internal use within the class and its subclasses.

Protected methods and properties can be accessed from within the class and its subclasses but not from outside the class.

Here's an example of a class with a protected property and method:

```python
class MyClass:
    def __init__(self):
        self._protected_property = 42

    def _protected_method(self):
        print("This is a protected method.")

    def public_method(self):
        print("This is a public method.")
        self._protected_method()
        print(f"The protected property value is {self._protected_property}.")
```

In this example, the `_protected_property` and `_protected_method` are denoted as protected using the single underscore prefix. The `public_method` is a public method that can be accessed from outside the class.

However, it is generally recommended to avoid accessing protected methods or properties from outside the class or its subclasses. Instead, you should rely on the public interface of the class to interact with its properties and methods.

It's worth noting that the use of single or double underscores to denote private or protected members in Python is just a convention. In Python, there is no true concept of private or protected members, and it is still possible to access them from outside the class if you know their names. The convention is intended to discourage direct access to these members and encourage the use of the public interface of the class instead.

## Public methods/properties

In Python, public methods and properties are those that do not have any prefix before their name. They are accessible from within the class, its subclasses, and from outside the class.

Here's an example of a class with a public property and method:

```python
class MyClass:
    def __init__(self):
        self.public_property = 42

    def public_method(self):
        print("This is a public method.")
        print(f"The public property value is {self.public_property}.")
```

In this example, the `public_property` and `public_method` are denoted as public without any prefix. The `public_method` can be accessed from outside the class as well.

Public methods and properties are the primary way to interact with an object from outside the class. They are the interface to the object and allow you to get or set the object's state, call its behavior, and interact with its data.

It's important to note that while public methods and properties are accessible from outside the class, it is still important to design them carefully. You should ensure that they provide a safe and consistent interface for interacting with the object and that they do not expose any implementation details that could break encapsulation.