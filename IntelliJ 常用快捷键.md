#IntelliJ 常用快捷键

Keymap：Mac OS X 10.5+。 参考[https://codingstyle.cn/topics/241](https://codingstyle.cn/topics/241)

##导航

`command + o`：打开类（输入类名）

`command + shift + o`：打开文件（输入文件名）

`command + e`：打开最近文件

`command + tab`：打开最近打开的文件

`command + shift + t`：打开测试文件

##代码编辑

`command + shift + up/down`：移动行

`command + d`：复制行

`command + x`：剪切行

`command + delete`：删除行

`alt + up/down`：扩展缩小选取（选中）

`control + up`：移动光标到方法签名（方法名称）

`command + shift + up/down`：移动方法（选中方法名，可和`control + up`配合使用）

##万能的 Alt + Enter

自动创建类和方法：在单元测试中，选中不存在的类或者方法时，然后使用`alt + enter`可直接创建该类和方法。

绑定构造器参数到字段：直接创建构造函数参数，并赋值。

##运行

`control + alt + r`：运行

##重构

`command + alt + v`：抽取变量（选中变量，然后使用命令）

`command + alt + c`：抽取常量

`command + alt + f`：抽取字段

`command + alt + p`：抽取参数

`command + alt + m`：抽取方法（选中返回的值，然后使用命令）

`command + alt + n`：内联（与上面方法作用相反）

`shift + f6`：重命名（类似`alt`选中多个）

`control + t`：打开重构菜单（部分重构高级用法）

##补全

内置`Live Templates`：在`Preferences --> Editor -- > Live Templates`可查看快捷模板，也可自定义个人喜欢的模板

`command + shift + enter`：智能补全（适用范围很多）

向后声明：比如

	"123".var --> String s = "123";
	
	words.for --> for(word in words){}
	
	words.fori --> for(var i=0; i<words.length; i++){}

##其它

`command + alt + l`：格式化代码

`control + alt + o`：优化`import`语句（去掉未使用的`import`语句）

`command + shift + a`：查找命令

