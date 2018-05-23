# Web开发中问题

webk开发中我们经常会遇到一些奇怪的问题，有时候是浏览器差异造成的，有时候是函数版本问题。下面是个人的一些简单记录。

## 中文名文件下载乱码

下面是网上找的关于content-dispositoin显示中文问题的唯一正确的总结... 浏览器能正确识别的编码格式，只要按照这样的编码来设置对应的Content-Disposition，那么应该就不会出现中文文件名的乱码问题了。  

1. IE浏览器，采用URLEncoder编码  
2. Opera浏览器，采用filename方式  
3. Safari浏览器，采用ISO编码的中文输出  
4. Chrome浏览器，采用Base64编码或ISO编码的中文输出  
5. FireFox浏览器，采用Base64或filename或ISO编码的中文输出 

## 修改placeholder样式

有时候因为一些奇葩的UI设计，我们需要修改input框的placeholder样式，但是我们正常修改css无法实现，所以我们可以借用下面代码来处理（各个浏览器内核处理方式不一样，所以每个都要写。ps：placeholder只支持IE10+浏览器。）

```css
::-webkit-input-placeholder { /* WebKit browsers */
  color: #616161;
  font-family: "microsoft yahei",simsun;
}
:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
  color: #616161;
  font-family: "microsoft yahei",simsun;
}
::-moz-placeholder { /* Mozilla Firefox 19+ */
  color: #616161;
  font-family: "microsoft yahei",simsun;
}
:-ms-input-placeholder { /* Internet Explorer 10+ */
  color: #616161;
  font-family: "microsoft yahei",simsun;
}
```
