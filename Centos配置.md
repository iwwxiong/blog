# Centos7 配置

### U盘安装Centos7出现无法找到镜像
>用UltraISO将DVD版的iso刻录到U盘后，删除packages文件夹（节省空间，不删除亦可），将iso文件复制进U盘根目录，开机之后出现`dracut:/#`, 表示为找到镜像所在地方，此时
输入命令
>
    $ cd dev
    $ ls
>找到U盘的盘符，比如sda3，然后重新开机，按方向键选择到第一项Install CentOS 7，按下Tab键，出现
>
    vmlinuz initrd=initrd.img inst.stage2=hd:LABEL=CentOS\x207\x20x86_64 quiet
>修改为
>
    vmlinuz initrd=initrd.img repo=hd:/dev/sda5:/ quiet
>然后重启即可（盘符可能很多，无法确定哪个是u盘的，最无奈的办法就是一个一个尝试。）

### 安装第三方源（EPEL和RPMForge）
> CentOS官方文档声称严重推荐EPEL，不推荐RPMForge，因为RPMForge已经不再被维护了，虽然曾经被CentOS推荐。
> [EPEL官方网站](http://fedoraproject.org/wiki/EPEL)
> [EL7下载地址](http://download.fedoraproject.org/pub/epel/7/x86_64/repoview/epel-release.html)
    $ rpm -ivh epel-release-7-5.noarch.rpm
> EPEL的repo文件已经在目录/etc/yum.repos.d/下。
> [RPMForge官方网站](http://repoforge.org/)
> [EL7下载地址](http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm)
    rpm -ivh rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm
> RPMForge的repo文件已经在目录/etc/yum.repos.d/下。

### 增加Window开机引导
>装完CentOS 7之后，以前装好的win7或是其它系统没有出现在启动项中的解决办法
>在/boot/grub2/grub.cfg中添加
    menuentry 'Windows 7 Professional' {
        set root=(hd0,1)
        chainloader +1
    }
>(hd0,1)代表第一个分区。

### 挂载NTFS文件系统
> CentOS本身不支持NTFS文件系统的，CentOS自身的源里没有支持NTFS的包，需要从EPEL或RPMForge（也叫RepoForge）源里安装。
    $ yum install ntfs-3g --enablerepo=epel
>或
    $ yum install fuse-ntfs-3g --enablerepo=rpmforge

### git配置
> centos7安装完成后默认就已经安装了git，我们只需要简单配置下即可使用。
>
    $ sudo git config --global user.email "huiquanxiong@gmail.com"
    $ sudo git config --global user.name "teddy"
    $ git config --list --global
    > user.email=huiquanxiong@gmail.com
    > user.name=teddy

### FLash Player
> 可以去adobe官网下载，然后使用rpm命令安装。不过也可使用yum简单安装：
    $ yum install flash-plugin --enablerepo=rpmforge

### Shadowsock配置
> Linux下没有shadowsock GUI工具，所以我们需要 Shadowsocks是一个轻量级的SOCK5代理软件，而Shadowsocks-libev是基于Shadowsocks的代理软件，他包括三部分：
1: ss-server：服务器端，部署在远程服务器，提供shadowsocks服务。
2: ss-local：客户端，提供本地socks5协议代理。
3: ss-redir：客户端，提供本地透明代理。
> 安装编辑包和shadowsocks-libev.git需要的包:
    $ yum -y install  wget curl curl-devel zlib-devel openssl-devel perl perl-devel cpio expat-devel gettext-devel
    $ yum -y install  autoconf libtool openssl-devel gcc swig python-devel
> git安装shadowsocks-livev
    $ cd /usr/local/src
    $ git clone  https://github.com/madeye/shadowsocks-libev.git
    $ cd /shadowsocks-libev
    $ ./configure
    $ make && make install
> 服务端我使用的是国外vps，这里不需要搭建本地shadowsock服务，所以我只需要简单配置使用ss-local即可。
