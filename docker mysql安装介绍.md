# Docker Mysql

## Docker Mysql基本命令介绍

介绍docker创建`Mysql`镜像，并介绍如何挂载数据到本地、载入本地配置、端口映射等操作。

`docker run`命令
>
1. -d：(detach)后台运行
2. -p：端口映射 3306:3306
3. -v：(volume)映射host文件夹 /Users/mysql:/var/lib/mysql
4. -e：(environment)启动环境
5. --name：命名本地容器名称

启动本地镜像：

	docker run [IMAGE ID | REPOSITORY]
	
启动环境变量（environment）：

	-e MYSQL_ROOT_PASSWORD=dracarysX

数据挂载到本地：

	-v /db/mysql:/var/lib/mysql
	
加载本地配置(优先使用本地配置信息)

	-v /db/my.conf:/etc/mysql/my.cnf
	
日志挂在到本地:

	-v /db/log:/var/log/mysql
	
端口映射本地：
	
	-p 3306:3306

链接一个未运行的mysql容器，并启动：

	docker run -it [IMAGE_ID] bash
		
关闭容器
	
	docker stop [CONTAINER ID]
	
拷贝文件`docker cp`

	# 拷贝镜像文件之本地
	docker cp CONTAINER_ID:/etc/mysql/my.cnf /db/my.conf
		
链接一个运行中的mysql容器（docker exec）：
	
	docker exec -it [CONTAINER_ID | CONTAINER_NAME] bash
	
## 案例介绍

`docker`容器启动后，`mysql`产生的数据和日志都是保存在容器中的，当容器停止后我们的数据和日志也都销毁掉了。当然学习或者实验的情况下就无所谓了，不过生产环境下用户数据我们是需要保存的，此时我们就不能把数据直接放到容器中了，一般情况下需要挂在到本地服务器中了。

### 方案

个人认为比较好的方案是`mysql`的配置放到本地，可以使用一些版本管控工具管理，然后容器通过挂载本地配置来启动，这样的话当批量部署的时候我们的配置只需要变动一个地方就够了。其次，数据和日志也类似都挂载到本地来使用，保证数据的持久化。通过启动多容器的方案就可以实现比较好的性能了。

### 例子

下面是我本地开发使用的例子，`daocloud.io/mysql:5.7.14`是之前从`daocloud`上下载的`mysql`镜像，然后把数据和日志挂在到本地`/dev/Mysql`目录下面：

	docker run --name mysql5.7.14 -e MYSQL_ROOT_PASSWORD=password -d -p 3306:3306 -v $PWD/dev/Mysql/data/:/var/lib/mysql -v $PWD/dev/Mysql/log:/var/log/mysql/ daocloud.io/mysql:5.7.14
