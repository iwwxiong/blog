# Dockerfile语法

`Dockerfile`是由一系列命令和参数构成的脚本，这些命令应用于基础镜像并最终创建一个新的镜像。它们简化了从头到尾的流程并极大的简化了部署工作。`Dockerfile`从`FROM`命令开始，紧接着跟随者各种方法，命令和参数。其产出为一个新的可以用于创建容器的镜像。

## 语法示例

`Dockerfile`语法由两部分组成，注释和命令+参数

    # 注释
    命令 参数1 参数2 ...

## 命令

`Dockerfile`大概有十几条命令用于构建镜像，下面是命令介绍

### FROM

第一条指令必须是`FROM`。如果同一个`Dockerfile`文件中创建多个镜像时，可以用多个`FROM`命令，不过每个镜像只能有一条。

    FROM <image> || FROM <image>:<tag>

### MAINTAINER

该命令用于生成作者姓名的，建议放在`FROM`之后。

    MAINTAINER <name>

### RUN

`RUN`命令是`Dockerfile`执行命令的核心部分。它接受命令作为参数并用于创建镜像。每条`RUN` 指令将在当前镜像基础上执行指定命令，并提交为新的镜像。当命令较长时可以使用`\`来换行。

    RUN <command>
    > RUN apt-get install python

### CMD

指定启动容器时执行的命令，每个Dockerfile只能有一条`CMD`命令。如果指定了多条命令，只有最后一条会被执行。和RUN命令相似，`CMD`可以用于执行特定的命令。和`RUN`不同的是，这些命令不是在镜像构建的过程中执行的，而是在用镜像构建容器后被调用。

    CMD command param1 param2
    > CMD "echo" "hello world."
    CMD ["executable","param1","param2"]
    > RUN ["/bin/bash", "echo", "hello world."]

### ADD

`ADD`命令有两个参数，源和目标。它的基本作用是从源系统的文件系统上复制文件到目标容器的文件系统。如果源是一个`URL`，那该`URL`的内容将被下载并复制到容器中；还可以是一个`tar`文件（自动解压为目录）。

    ADD <src> <dest>

### ENTRYPOINT

配置容器启动后执行的命令，并且不可被`docker run`提供的参数覆盖。每个`Dockerfile`中只能有一个`ENTRYPOINT`，当指定多个时，只有最后一个起效。

    ENTRYPOINT ["executable", "param1", "param2"]

### COPY

复制本地主机的`<src>`为Dockerfile所在目录的相对路径）到容器中的`<dest>`。当使用本地目录为源目录时，推荐使用`COPY`。

    COPY <src> <dest>

### EXPOSE

暴露容器端口，供相互连接使用。

    EXPOST <port> [port.]

###ENV

格式为`ENV <key> <value>`。 指定一个环境变量，会被后续`RUN`指令使用，并在容器运行时保持。

    ENV <key> <value>
    > ENV SERVER_WORKERS 5

### VOLUME

创建一个可以从本地主机或其他容器挂载的挂载点，一般用来存放数据库和需要保持的数据等。

    VOLUME ["/dir_1", "/dir_2" ..]

### WORKDIR

`WORKDIR`命令用于设置CMD指明的命令的运行目录。为后续的`RUN`、`CMD`、`ENTRYPOINT`指令配置工作目录。

    WORKDIR ~/

### USER

指定运行容器时的用户名或UID。

    USER <uid>
    > USER 751

