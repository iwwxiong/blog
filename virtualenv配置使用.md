# Python virtualenv搭建使用

`virtualenv`通过创建独立Python开发环境的工具, 来解决依赖、版本以及间接权限问题。官方介绍（virtualenv is a tool to create isolated Python environments.）。文章参考[廖雪峰Python教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)

## 安装

通过Python包管理器pip安装：

    > pip install virtualenv
    # python3
    > pip3 install virtualenv

## 使用

创建个人项目`dracarysX`，然后创建独立的Python环境，命名为`venv`：

    > mkdir dracarysX
    > cd dracarysX
    > virtualenv --no-site-packages venv

进入项目，切换到`venv`环境中：

    # windows方式
    > venv\Scripts\activate
    (venv) D:\dracarysX>
    # mac or linux
    > source venv/bin/activate
    (venv) dracarysX$

使用`pip`安装各种第三方包就会被安装在该环境下，系统Python环境不受任何影响。也就是说`venv`是我们的项目`dracarysX`独立环境了。

> 如果在命令行中运行virtualenv --system-site-packages venv, 会继承/usr/lib/python2.7/site-packages下的所有库, 最新版本virtualenv把把访问全局site-packages作为默认行为。

## 退出

使用命令`deactivate`可直接退出当前环境，此时再次使用`pip`等命令就等于直接操作Python全局环境了。

##　virtualenv-wrapper介绍

`virtualenv-wrapper`是virtualenv的扩展包，用于更方便管理虚拟环境，它可以做：

1. 将所有虚拟环境整合在一个目录下；
2. 管理（新增，删除，复制）虚拟环境；
3. 快速切换虚拟环境；

### 命令列表

    lsvirtualenv：列出虚拟环境列表
    mkvirtualenv：新建虚拟环境
    workon [虚拟环境名称]：切换虚拟环境
    rmvirtualenv：删除虚拟环境
    deactivate：离开虚拟环境

## 多版本环境

有时候工作中需要使用`Python2.x`或者`3.x`版本的环境，共同环境下容易产生包冲突问题。这时候我们就需要用`virtualenv`搭建虚拟且独立的多个版本 python 环境，使每个项目特有环境与其他项目独立开来。

    > mkdir python3_env
    > cd python3_env
    > virtualenv --no-site-packages --python=/usr/local/bin/python3 venv  # 指定python版本即可。


