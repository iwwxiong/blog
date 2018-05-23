# Python MRO C3算法详解

一直以来，对`Python`的多继承方法解析顺序（MRO）还停留在：经典类是子节点从左到右，深度优先搜索方式；新式类(继承自object)是子节点从左到右，广度优先搜索方式。然而经过仔细阅读文档后发现事实并非如此，下面就是一些自己对`Python`新式类`MRO C3`算法理解。

## MRO（Method Resolution Order）

`MRO`：方法解析顺序，主要是用于在多继承时判断属性的路径问题。

## 历史问题

`Python`的多继承`MRO`经历了3个版本的变更，分别是`Python2.2`之前的经典类（`classic class`）, `Python2.2`的新式类（`new-style class`）和`Python2.3`之后的采用`MRO C3`算法的新式类。

### Python2.2之前，经典类(classic class)

在`Python2.2`以前的版本中，类的定义是无继承的（`class A:`）,实例化的类型也是`type`类型。`MRO`采用深度优先DFS（`depth-first-search`）算法，子节点从左到右（`left-to-right`）。

```python
class A:
    def foo(self):
        print 'Class A'

class B(A):
    pass

class C(A):
    def foo(self):
        print 'Class C'

class D(B, C):
    pass

import inspect
inspect.getmro(D)
D > B > A > C
```

基于深度优先算法，上面的例子结果是：`Class A`，不是我们期望的`class C`，违背了多继承的本地优先的原则。

### Python2.2，新式类(new-style class)

为了解决经典类的问题，在`Python2.2`的版本中引入了新式类的定义。新式类的每个类都继承于一个基类，默认是`object`。新式类`MRO`采用了广度优先BFS（`breadth-first-search`）算法，子节点从左到右（`left-to-right`）。此时我们用新式类来看上面的例子：

```python
class A(object):
    def foo(self):
        print 'Class A'

class B(A):
    pass

class C(A):
    def foo(self):
        print 'Class C'

class D(B, C):
    pass

import inspect
inspect.getmro(D)
D > B > C > A
```

从结果看来，完全符合我们的预期。但是也有些不合理的问题存在，从常理来看`D`类继承`B`类，那么方法查找应该从`B`类的父类`A`类中查找，然而偏偏查找了`C`类，这不符合多继承的单调性原则。比如我们从下面的例子来看看这个问题：

```python
class A: pass
class B: pass
class C: pass
class D: pass
class E: pass
class K1(A,B,C): pass
class K2(D,B,E): pass
class K3(D,A):   pass
class Z(K1,K2,K3): pass
```

继承关系图 ![](http://7xrszf.com1.z0.glb.clouddn.com/mro.png)

* 按照DFS算法，线路为：`Z > K1 > A > B > C > K2 > D > E > K3`。
* 按照BFS算法， 路线为：`Z > K1 >  K3 > A > K2 > D > B > C > E`。

这样一看问题就出来了，不管是`DFS`还是`BFS`算法都违背了多继承的单调性或单一继承原则。所以之后的`Python`版本采用了`C3`算法来解决这一问题。

## Python2.3之后

看`C3`算法前我们先介绍下下面的概念问题：

1. 本地优先级：指声明时父类的顺序，比如C(A,B)，如果访问C类对象属性时，应该根据声明顺序，优先查找A类，然后再查找B类。
2. 单调性：如果在C的解析顺序中，A排在B的前面，那么在C的所有子类里，也必须满足这个顺序。

### C3算法

`C3`算法最早被提出是用于Lisp的，应用在Python中是为了解决原来基于深度优先搜索算法不满足本地优先级，和单调性的问题。下面我们通过例子来解释`C3`算法的原理，还是上面的那个例子：

```python
class A(object): pass
class B(object): pass
class C(object): pass
class D(object): pass
class E(object): pass
class K1(A,B,C): pass
class K2(D,B,E): pass
class K3(D,A):   pass
class Z(K1,K2,K3): pass
```

我们先来看看K1, K2, K3的继承：

```python
K1 = [A, B, C]
K2 = [D, B, E]
K3 = [D, A]
```

然后我们来看Z线性化计算

```python
L[Z] = Z + merge(K1, K2, K3)
# 也就是
L[Z] = Z + K1 + K2 + K3 + merge(ABC, DBE, DA)
```

如上可以看出，下个个继承的D的权重比A高，所以经过下一次计算后

```python
L[Z] = Z + K1 + K2 + K3 + D + merge(ABC, BE, A)
```

然后我们看下完整的顺序：

```python
L[Z] = Z + merge(K1, K2, K3)
     = Z + K1 + K2 + K3 + merge(ABC, DBE, DA)
     = Z + K1 + K2 + K3 + D + merge(ABC, BE, A)
     = Z + K1 + K2 + K3 + D + A + merge(BC, BE)
     = Z + K1 + K2 + K3 + D + A + B + merge(C, E)
     = Z + K1 + K2 + K3 + D + A + B + C + merge(E)
     = Z + K1 + K2 + K3 + D + A + B + C + E
```

继承顺序为`Z > K1 > K2 > K3 > D > A > B > C > E`，那么我们对比下程序运行结果：

```python
>>> Z.__mro__
(<class '__main__.Z'>, <class '__main__.K1'>, <class '__main__.K2'>, <class '__main__.K3'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.E'>, <type 'object'>)
```

推测结果完全符合预期。从上面例子看来`C3`算法完全结果了之前`DFS`和`BFS`算法所带来的问题，符合多继承本地优先级和单调性原则。所以`Python3`之后`C3`就一统天下了。

## 参考

类历史主要参考[https://www.python.org/download/releases/2.2.2/bugs/](https://www.python.org/download/releases/2.2.2/bugs/), C3算法主要参考官网的[https://www.python.org/download/releases/2.3/mro/](https://www.python.org/download/releases/2.3/mro/)。
