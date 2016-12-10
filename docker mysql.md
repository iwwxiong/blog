# Docker Mysql

介绍docker创建`Mysql`镜像，并介绍如何挂载数据到本地、载入本地配置、端口映射等操作。

`docker run`命令
>
1. -d：(detach)后台运行
2. -p：端口映射 3306:3306
3. -v：(volume)映射host文件夹 /Users/mysql:/var/lib/mysql
4. -e：(environment)启动环境

启动本地镜像：

	docker run [IMAGE ID]
	
启动环境变量（environment）：

	-e MYSQL_ROOT_PASSWORD=dracarysX

数据挂载到本地：

	-v /db/mysql:/var/lib/mysql
	
加载本地配置(优先使用本地配置信息)

	-v /db/my.conf:/etc/mysql/my.cnf
	
端口映射本地：
	
	-p 3306:3306

下面命令是为我们创建一个名称为`dracarysX_mysql`镜像，共享本地3306端口，并且挂在数据文件到本地。数据库创建时候设置root密码为`dracarysX`。（因本地无此镜像，设置镜像仓库为`daocloud.io/mysql:5.7.14`）

	docker run --name dracyarsX_mysql -e MYSQL_ROOT_PASSWORD=dracarysX -d -p 3306:3306 -v /Users/dracarysX/Document/mysql:/var/lib/mysql daocloud.io/mysql:5.7.14
	
拷贝文件`docker cp`

	# 拷贝镜像文件之本地
	docker cp CONTAINER_ID:/etc/mysql/my.cnf /db/my.conf
		
链接一个运行中的mysql容器（docker exec）：
	
	docker exec -it [CONTAINER_ID | CONTAINER_NAME] bash

> 例如
> 
	> docker exec -it dracarys_mysql bash
	> root@a2b843caebcd:/#	
	> root@a2b843caebcd:/# mysql -u root -p
	Enter password: 	
	mysql> 
	
链接一个未运行的mysql容器，并启动：

	docker run -it [IMAGE_ID] bash
		
关闭容器
	
	docker stop [CONTAINER ID]
	
