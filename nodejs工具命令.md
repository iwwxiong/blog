# Nodejs 各工具命令

### NPM命令
> npm是nodejs的包管理命令。
> npm i  (不加后面options的，默认安装当前路径下pacaage.json配置)
common options: [--save|--save-dev|--save-optional] [--save-exact]
>
    // save, save-dev, save-optional分别对应下面package.json里面的
    "devDependencies": {
        xxx
    }
    "dependencies": {
        xxx
    }
    "optDependencies": {
        xxx
    }
> npm i -g：默认全局安装（一些经常使用的模块可以使用）
> npm uninstall：卸载安装的包
> npm config：npm本地配置
> npm config set <key> <value>：设置config，例如设置代理
>
    npm config set http_proxy:127.0.0.1:1080
> npm config list：列出所有本地配置。

### Mocha(nodejs测试框架)
>Mocha（发音"摩卡"）诞生于2011年，是现在最流行的JavaScript测试框架之一，在浏览器和Node环境都可以使用。所谓"测试框架"，就是运行测试的工具。通过它，可以为JavaScript应用添加测试，从而保证代码的质量。
>通常，测试脚本与所要测试的源码脚本同名，但是后缀名为.test.js（表示测试）或者.spec.js（表示规格）。比如，`wwx.js`的测试脚本名字就是`wwx.test.js。`
>
    // 直接测试xxx.js文件
    $ mocha xxx.test.js
>
    // 测试多个js文件
    $ mocha xxx1.test.js xxx2.test.js xxx3.test.js
>
    // --recursive参数，test子目录下面所有的测试用例----不管在哪一层----都会执行。
    $ mocha --recursive
>
    //通配符
    $ mocha /test/*.js // 执行test目录下所有.js文件
    $ mocha /test/{wwx, teddy}.js // 执行test目录下wwx.js和teddy.js
>
    // --reporter参数用来指定测试报告的格式，默认是spec格式
    $ mocha --reporter spec
>
    // --watch参数用来监视指定的测试脚本。只要测试脚本有变化，就会自动运行Mocha。
    $ mocha -w
>
    // mocha --timeout 制定mocha每个测试用例执行的时间（默认2000ms）
    $ mocha -t 10000 wwx.test.js
>Mocha在describe块之中，提供测试用例的四个钩子：before()、after()、beforeEach()和afterEach()。它们会在指定时间执行。
>
    describe('hooks', function() {
      before(function() {
        // 在本区块的所有测试用例之前执行
      });
      after(function() {
        // 在本区块的所有测试用例之后执行
      });
      beforeEach(function() {
        // 在本区块的每个测试用例之前执行
      });
      afterEach(function() {
        // 在本区块的每个测试用例之后执行
      });
      // test cases
    });

>当然mocha还有更多有趣的用法，目前没有接触使用到，更多命令格式参考[mocha官网](http://mochajs.org/#reporters)。本文参考[阮一峰-测试框架 Mocha 实例教程](http://www.ruanyifeng.com/blog/2015/12/a-mocha-tutorial-of-examples.html)
