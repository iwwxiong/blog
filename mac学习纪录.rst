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

MPV安装
--------

MPV是一款免费，开源的视频播放器，mpv fork 自 Mplayer 和 Mplayer2，是现在唯一仍在活跃开发的 Mplayer 系的播放器，大部分原 Mplayer 社区的开发者都已经转到 mpv 的开发上了。mpv 以 ffmpeg 为解码器，可以调用 OS X 平台的硬件加速解码，支持 ass 字幕，有高级 OpenGL scale 算法，还支持 lua 扩展脚本。

安装
>>>>

.. code::

    brew install mpv --with-bundle
    brew linkapps mpv

这样 Homebrew 会自动在 /Applications 下创建一个到 mpv.app 的软链。

指定默认打开脚本::

    EXTS=( 3GP ASF AVI FLV M4V MKV MOV MP4 MPEG MPG MPG2 MPG4 RMVB WMV MTS )

    brew install duti

    for ext in ${EXTS[@]}
    do
        lower=$(echo $ext | awk '{print tolower($0)}')
        duti -s io.mpv $ext all
        duti -s io.mpv $lower all
    done

配置
>>>>>

mpv 的配置文件在 ``~/.config/mpv/`` 里。``mpv.conf`` 是一些基本的配置，``input.conf`` 是播放过程中一些操作快捷键的设置，``lua-settings/osc.conf`` ，是播放器控制 UI 自定义设置。

另外，可以使用下面命令将 ``rmvb`` 格式视频转换成 ``mp4`` 格式::

    ffmpeg -i input.rmvb -c:v libx264 -preset veryfast -crf 18 -c:a copy output.mp4
