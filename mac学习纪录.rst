.. _Mac学习纪录:

Mac学习纪录
===========

本文主要是纪录Mac下的学习经历。

Homebrew
----------

Homebrew是Mac下的套件管理工具，非常好用。`Homebrew官网 <http://brew.sh/>`_ ,Homebrew安装软件默认在 ``/usr/local`` 下。

**安装方法**

直接使用如下命令安装即可::

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

安装完成后可以使用 brew doctor 来检查是否安装正确。如果需要升级可以使用下列命令::

    $ brew update
    $ brew upgrade

launchctl学习
--------------

``launchctl`` 是Mac OS下用于初始化系统环境的关键进程，它是内核装载成功之后在OS环境下启动的第一个进程。采用这种方式来配置自启动项或者定时任务就很简单，只需要一个plist文件，该plist文件存在的目录有::

    ~/Library/LaunchAgents
    /Library/LaunchAgents
    /System/Library/LaunchAgents

标准plist文件格式如下::

    <?xml version="1.0" encoding="UTF-8"?>  
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">  
    <plist version="1.0">  
      <dict>
        
        <key>Label</key>
        <!-- 名称，要全局唯一 -->
        <string>dracarysX</string> 

        <!-- 要运行的程序， 如果省略这个选项，会把ProgramArguments的第一个
        元素作为要运行的程序 -->
        <key>Program</key>
        <string>/Users/hanks/run.sh</string>

        <!-- 命令， 第一个为命令，其它为参数-->
        <key>ProgramArguments</key>
        <array>
          <string>/Users/hanks/run.sh</string>
        </array>

        <!-- 运行时间 -->
        <key>StartCalendarInterval</key>
        <dict>

          <key>Minute</key>
          <integer>30</integer>

          <key>Hour</key>
          <integer>9</integer>

          <key>Day</key>
          <integer>1</integer>

          <key>Month</key>
          <integer>5</integer>

          <!-- 0和7都指星期天 -->
          <key>Weekday</key>
          <integer>0</integer>

        </dict>
        <!-- 开机自启动设置 -->
        <key>RunAtLoad</key>
        <true/>

        <!-- 命令运行目录 -->
        <key>WorkingDirectory</key>
        <string>/usr/local/var</string>

        <!-- 运行间隔，与StartCalenderInterval使用其一，单位为秒 -->
        <key>StartInterval</key>
        <integer>30</integer>

        <!-- 标准输入文件 -->
        <key>StandardInPath</key>
        <string>/Users/hanks/run-in.log</string>

        <!-- 标准输出文件 -->
        <key>StandardOutPath</key>
        <string>/Users/hanks/run-out.log</string>

        <!-- 标准错误输出文件 -->
        <key>StandardErrorPath</key>
        <string>/Users/hanks/run-err.log</string>
      </dict>  
    </plist>

launchctl常用命令如下::

    # 加载dracarysX.plist
    launchctl load dracarysX.plist
    # 查看launchctl列表
    launchctl list
    ＃ 移除plist
    launchctl remove dracarysX.plist

Mysql安装
-----------

使用 `Brew` 命令安装::

    $ brew install mysql

安装完成之后可以使用下列命令控制服务::

    $ mysql.server start
    $ mysql.server stop

Redis安装
----------

使用 ``Brew`` 命令安装::

    $ brew install redis

服务启动::

    $ redis-server /usr/local/etc/redis.conf

测试redis服务::

    $ redis-cli
    127.0.0.1:6379> 

然后可以使用如下命令设置 ``Redis`` 开机启动::

    $ ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents
    $ launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist

Mac下redis客户端没看到什么合适的，暂时使用 `medis <https://github.com/luin/medis>`_ 。