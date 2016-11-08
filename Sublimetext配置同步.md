# Sublimetext配置，插件同步

Sublimetext的优势在于可以安装各类插件，进行个性配置，但是如果你有多台电脑，逐个配置的话，不仅麻烦，而且不可持续（因为插件和配置是经常变化的）。目前也没有比较合适的三方插件，大多借助云盘或者git仓库来同步。本文主要介绍通过git仓库来同步配置。

## 原理

同步的原理主要是同步本地使用Sublimetext配置文件夹来实现的。

### 用户数据文件夹

Windows: %APPDATA%Sublime Text 3

Linux: ~/.config/sublime-text-3

OS X: ~/Library/Application Support/Sublime Text 3

### 同步文件夹

1. 不要同步 `Packages` 和 `Installed Packages`，不同平台内容不同；
2. 同步 `Packages/User/` 即可，该文件夹里面有 `Package Control.sublime-settings` 文件，它会帮你做好未装插件的安装工作；

## 步骤

### 初始化仓库

    > cd /Users
    > git init

添加`.gitignore`文件，忽略掉下列文件：

    > Package Control.last-run
    > Package Control.ca-list
    > Package Control.ca-bundle
    > Package Control.system-ca-bundle
    > Package Control.cache/
    > Package Control.ca-certs/
    > encoding_cache.json

### 提交到远程仓库

远程仓库大多使用公用仓库，比如github。不过由于国内网络环境，github速度相对较慢，本文使用的git仓库是coding.net。

    > git add --all
    > git commit -m ""
    > git remote add origin https://git.coding.net/xxxxxx.git
    > git pull
    > git push origin master

### 其它设备同步配置

    > cd /Users
    # 这里可备份之前配置
    > git clone https://git.coding.net/xxxxxx.git

至此配置同步完成。
