# Python MRO C3算法详解

一直以来，对`Python`的多继承方法解析顺序（MRO）还停留在：经典类是子节点从左到右，深度优先搜索方式；新式类是子节点从左到右，广度优先搜索方式。然而经过查询文档后发现事实并非如此。下面就是一些自己对`Python MRO C3`算法理解的记录。

## MRO（Method resolution order）

`MRO`方法解析顺序，主要是用于在多继承时判断属性的路径问题。

## 历史问题

`Python`的多继承`MRO`经历了3个版本的变更，分别是`Python2.2`之前的经典类（`classic class`）, `Python2.2`的新式类（`new-style class`）和`Python2.3`之后的采用`MRO C3`算法的新式类。

### Python2.2之前，经典类(classic class)

在`Python2.2`以前的版本中，类的定义是无继承的（`class A:`）,实例化的类型也是`type`类型。`MRO`采用DFS（`depth-first-search`）算法，子节点从左到右（`left-to-right`）。

    > class A:
    >     def foo(self):
    >         print 'class: A'

    > class B(A):
    >     pass

    > class C(A):
    >     def foo(self):
    >         print 'class C'

    > class D(B, C):
    >     pass

    > d = D()
    > d.foo()
    class: A
    > import inspect
    > inspect.getmro(D)
    (<class __main__.D at 0x7f56cd399940>, <class __main__.B at 0x7f56cd3998d8>, <class __main__.A at 0x7f56cd399808>, <class __main__.C at 0x7f56cd399870>)

从上面例子的结果看来，完全不是我们想要的输出（`class: C`），也就是说如果基本`A`和子类`C`中有同名方法，那么我们的实例化自`D`类实例就永远无法调用到`C`类的方法了，违背了多继承的本地优先级的定义。

### Python2.2，新式类(new-style class)

为了解决经典类的问题，在`Python2.2`的版本中引入了新式类的定义。新式类的每个类都继承于一个基类，默认是`object`。新式类`MRO`采用了BFS（`breadth-first-search`）算法，子节点从左到右（`left-to-right`）。此时我们用新式类来看上面的例子：

    > class A(object):
    >     def foo(self):
    >         print 'class: A'

    > class B(A):
    >     pass

    > class C(A):
    >     def foo(self):
    >         print 'class C'

    > class D(B, C):
    >     pass

    > d = D()
    > d.foo()
    class: C
    > import inspect
    > inspect.getmro(D)
    (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)

从结果看来，完全符合我们的预期。但是也有些不合理的问题存在，从常理来看`D`类继承`B`类，那么方法查找应该从`B`类的父类`A`类中查找，然而偏偏查找了`C`类，这不符合多继承的单调性问题。比如我们从下面的例子来看看这个问题：

    >>> O = object
    >>> class F(O): pass
    >>> class E(O): pass
    >>> class D(O): pass
    >>> class C(D, F): pass
    >>> class B(D, E): pass
    >>> class A(B, C): pass

继承关系图 ![](http://7xrszf.com1.z0.glb.clouddn.com/class_a.png)

从图中中我们可以看出，按照BFS算法来看，方法的查找路线路为`A-->B-->C-->D-->E-->F--object`。这样一看问题就出来了，完全违背了多继承的单调性问题。所以之后的`Python`版本采用了`C3`算法来替代`BFS`算法来解决这一问题。

## Python2.3之后

看`C3`算法前我们先介绍下下面的概念问题：

1. 本地优先级：指声明时父类的顺序，比如C(A,B)，如果访问C类对象属性时，应该根据声明顺序，优先查找A类，然后再查找B类。
2. 单调性：如果在C的解析顺序中，A排在B的前面，那么在C的所有子类里，也必须满足这个顺序。

### C3算法

`C3`算法最早被提出是用于Lisp的，应用在Python中是为了解决原来基于深度优先搜索算法不满足本地优先级，和单调性的问题。下面我们通过例子来解释`C3`算法的原理，还是上面的那个例子：

    >>> O = object
    >>> class F(O): pass
    >>> class E(O): pass
    >>> class D(O): pass
    >>> class C(D, F): pass
    >>> class B(D, E): pass
    >>> class A(B, C): pass

我们先来看看E, F, D的继承：

    LO = O
    LD = [D O]
    LE = [E O]
    LF = [F O]

然后我们来看B的继承：

    L[B] = B + merge(DO, EO, DE)

从左到右看D位于第一个，没有被继承，那么第一次合并后就是`BD + merge(O, EO, E)`，再次观察发现O被E继承了，那么我们跳过第一个，从EO中查找合并后就是`BDE + merge(O, O)`，那么再次合并后的顺序就是`BDEO`。

同理我们看C的继承：

    L[C] = C + merge(DO, FO, DF)

得到的结果就是`CDFO`。然后我们看下完整的顺序：

    L[A] = A + merge(BDEO, CDFO, BC)
     = A + B + merge(DEO, CDFO, C)
     = A + B + C + merge(DEO, DFO)
     = A + B + C + D + merge(EO, FO)
     = A + B + C + D + E + merge(O, FO)
     = A + B + C + D + E + F + merge(O, O)
     = A B C D E F O

那么我们对比下程序运行结果：

    >>> A.__mro__
    (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <type 'object'>)

符合推测结果。如果我们稍微调整下B类的继承顺序（`class B(E, D)`）,如图![](http://7xrszf.com1.z0.glb.clouddn.com/class_a.png)。从图中我们可以推测出顺序应该是`ABECDFO`。来看看程序运行结果：

    >>> O = object
    >>> class F(O): pass
    >>> class E(O): pass
    >>> class D(O): pass
    >>> class C(D, F): pass
    >>> class B(E, D): pass
    >>> class A(B, C): pass
    >>> A.__mro__
    (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <type 'object'>)

推测完全正确。从上面例子看来`C3`算法完全结果了之前`DFS`和`BFS`算法所带来的问题，符合多继承本地优先级和单调性原则。所以`Python3`之后`C3`就一统天下了。

## 参考

类历史主要参考[https://www.python.org/download/releases/2.2.2/bugs/](https://www.python.org/download/releases/2.2.2/bugs/), C3算法主要参考官网的[https://www.python.org/download/releases/2.3/mro/](https://www.python.org/download/releases/2.3/mro/)。
