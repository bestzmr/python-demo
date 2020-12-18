# python知识点整理

python是一种动态语言（变量本身类型不固定的语言）

**注：**

python代码**采用缩进方式**，按照约定俗成的惯例，采用4个空格的缩进，在文本编辑器中，需要设置把Tab自动转换为4个空格，确保不混用Tab和空格；当语句以**冒号：**结尾时，缩进的语句视为代码块

**以#开头的语句是注释**。

Python程序是**大小写敏感**的，如果写错了大小写，程序会报错

## 输入和输出

`print()`在括号中加上字符串，就可以向屏幕上输出指定的文字,`print()`函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出,遇到逗号“,”会输出一个空格

如果字符串内部有很多换行，用`\n`写在一行里不好阅读，为了简化，Python允许用`'''...'''`的格式表示多行内容，可以自己试试：

```python
>>> print('''line1
... line2
... line3''')
line1
line2
line3
```



`input()`可以让用户输入字符串，并存放到一个变量里,**`str`不能直接和整数比较，`input()`返回的数据类型是str，必须先把`str`转换成整数，Python提供了`int()`函数**

## 数据类型

* 数字(number)

  * 整数

    用科学计数法表示，把10用e替代，1.23x109就是`1.23e9`，或者`12.3e8`，0.000012可以写成`1.2e-5`，Python的浮点数也没有大小限制，但是超出一定范围就直接表示为`inf`（无限大）

  * 浮点数

    对于很大的数，例如`10000000000`，很难数清楚0的个数。Python允许在数字中间以`_`分隔，因此，写成`10_000_000_000`和`10000000000`是完全一样的。十六进制数也可以写成`0xa1b2_c3d4`。

* 字符串(str)

  如果字符串里面有很多字符都需要转义，就需要加很多`\`，为了简化，Python还允许用`r''`表示`''`内部的字符串默认不转义

  在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

  对于单个字符的编码，Python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符

  ```python
  >>> ord('A')
  65
  >>> ord('中')
  20013
  >>> chr(66)
  'B'
  >>> chr(25991)
  '文'
  ```

  **格式化字符串：**

  | 占位符 | 替换内容     |
  | :----- | :----------- |
  | %d     | 整数         |
  | %f     | 浮点数       |
  | %s     | 字符串       |
  | %x     | 十六进制整数 |

  ```python
  >>> 'Hello, %s' % 'world'
  'Hello, world'
  >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
  'Hi, Michael, you have $1000000.'
  ```

  字符串里面的`%`是一个普通字符怎么办？这个时候就需要转义，用`%%`来表示一个`%`：

  ```python
  >>> 'growth rate: %d %%' % 7
  'growth rate: 7 %'
  ```

  **format()格式化**

  另一种格式化字符串的方法是使用字符串的`format()`方法，它会用传入的参数依次替换字符串内的占位符`{0}`、`{1}`……，不过这种方式写起来比%要麻烦得多：

  ```python
  >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
  'Hello, 小明, 成绩提升了 17.1%'
  ```

  **f-string格式化**

  字符串如果包含`{xxx}`，就会以对应的变量替换：

  ```python
  >>> r = 2.5
  >>> s = 3.14 * r ** 2
  >>> print(f'The area of a circle with radius {r} is {s:.2f}')
  The area of a circle with radius 2.5 is 19.62
  ```

* 布尔值(bool)

  True 和 False

* 空值(none)

  空值是Python里一个特殊的值，用`None`表示。`None`不能理解为`0`，因为`0`是有意义的，而`None`是一个特殊的空值。

* 列表（list）

  Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

  `len()`函数可以获得list元素的个数

  `append()`函数可以往list中追加元素到末尾

  `insert(index,param)`函数可以把指定元素插入到指定位置

  `pop()`删除list末尾的元素

  `pop(index)`删除指定位置的元素

* 元组(tuple)

  另一种有序列表叫**元组**：tuple。tuple和list非常类似，但是**tuple一旦初始化就不能修改**，它没有append()，insert()这样的方法。其他获取元素的方法和list是一样的

  ```python
  >>> t = (1, 2) #定义元组
  >>> t
  (1, 2)
  >>> t = () #定义空元组
  >>> t
  ()
  # 容易踩到的坑，如下
  >>> t = (1)
  >>> t
  1
  # 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，Python规定，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
  >>> t = (1,)
  >>> t
  (1,)
  ```

  

* 字典(dict)

  Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

  创建一个字典，如下：

  ```python
  >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
  >>> d['Michael']
  95
  >>> d['Adam'] = 67 #把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
  >>> d['Adam']
  67
  ```

  如果key不存在，dict就会报错：

  ```python
  >>> d['Thomas']
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  KeyError: 'Thomas'
  ```

  要避免key不存在的错误，有两种办法，一是通过`in`判断key是否存在：

  ```python
  >>> 'Thomas' in d
  False
  ```

  二是通过dict提供的`get()`方法，如果key不存在，可以返回`None`，或者自己指定的value：

  ```python
  >>> d.get('Thomas') # 注意：返回None的时候Python的交互环境不显示结果。
  >>> d.get('Thomas', -1)
  -1
  ```

  要删除一个key，用`pop(key)`方法，对应的value也会从dict中删除：

  ```python
  >>> d.pop('Bob')
  75
  >>> d
  {'Michael': 95, 'Tracy': 85}
  ```

* 集合(set)

  set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，**没有重复的key且无序**。

  要创建一个set，需要提供一个list作为输入集合：

  ```python
  >>> s = set([1, 2, 3])
  >>> s
  {1, 2, 3}
  ```

  通过`add(key)`方法可以添加元素到set中，可以重复添加，但不会有效果：

  ```python
  >>> s.add(4)
  >>> s
  {1, 2, 3, 4}
  >>> s.add(4)
  >>> s
  {1, 2, 3, 4}
  ```

  通过`remove(key)`方法可以删除元素：

  ```python
  >>> s.remove(4)
  >>> s
  {1, 2, 3}
  ```

## 条件判断

`if`语句的完整形式：

```python
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```



## 循环

* `for x in ...`

  ```python
  sum = 0
  for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
      sum = sum + x
  print(sum)
  ```

  `range()`函数，可以生成一个整数序列，e.g. range(5)生成的序列是**从0开始小于5的整数，range函数生成的数的范围是左闭右开**

* `while`循环

  ```python
  sum = 0
  n = 99
  while n > 0:
      sum = sum + n
      n = n - 2
  print(sum)
  ```

**break**

在循环中，`break`语句可以提前退出循环

**continue**

通过`continue`语句，跳过当前的这次循环，直接开始下一次循环



## 函数

### 定义函数

* 定义一个函数要使用`def`语句，依次写出函数名、括号、括号中的参数和冒号`:`，然后，在缩进块中编写函数体，函数的返回值用`return`语句返回

* 请注意，函数体内部的语句在执行时，一旦执行到`return`时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

* 如果没有`return`语句，函数执行完毕后也会返回结果，只是结果为`None`。`return None`可以简写为`return`。

* 函数可以同时返回多个值，但其实就是一个tuple。

### 函数的参数

* 位置参数  

* 默认参数

  置默认参数时，有几点要注意：

  一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

  二是如何设置默认参数。

  当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

   **定义默认参数要牢记一点：默认参数必须指向不变对象！**

* 可变参数

  把函数的参数改为可变参数：

  ```python
  def calc(*numbers):
      sum = 0
      for n in numbers:
          sum = sum + n * n
      return sum
  ```

  定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个`*`号。在函数内部，参数`numbers`接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数

  如果已经有一个list或者tuple，要调用一个可变参数怎么办？

  ```python
  >>> nums = [1, 2, 3]
  >>> calc(*nums)  #  *nums表示把nums这个list的所有元素作为可变参数传进去。
  14
  ```

  

* 关键字参数

  关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

  ```python
  def person(name, age, **kw):
      print('name:', name, 'age:', age, 'other:', kw)
      
  >>> person('Bob', 35, city='Beijing')
  name: Bob age: 35 other: {'city': 'Beijing'}
  >>> person('Adam', 45, gender='M', job='Engineer')
  name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
  
  >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
  >>> person('Jack', 24, **extra)  #    **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
  name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
  ```

  

* 命名关键字参数

  如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收`city`和`job`作为关键字参数。这种方式定义的函数如下：

  ```python
  def person(name, age, *, city, job):
      print(name, age, city, job)
  ```

  和关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数。

  如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了：

  ```python
  def person(name, age, *args, city, job):
      print(name, age, args, city, job)
  ```

  

* 参数组合

  在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：**必选参数、默认参数、可变参数、命名关键字参数和关键字参数**。

**注意定义可变参数和关键字参数的语法**：

`*args`是可变参数，args接收的是一个tuple；

`**kw`是关键字参数，kw接收的是一个dict。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符`*`，否则定义的将是位置参数。

## 高级特性

