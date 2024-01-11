# XXUST-Web-Authenticate
某高校网络自动认证

## 使用方法

使用浏览器打开认证页面

![](imgs/web-auth-page.png)

按 `F12`，打开 `网络` 选项卡

![](imgs/f12.png)

弹出的界面右上角，点击网络设置（齿轮图标），勾选 `持续记录`

![](imgs/f12-keep-record.png)

输入用户名和密码，登录

![](imgs/login.png)

选择文件为 `do` 的项目

在 `消息头` 中的 `请求头` 栏中打开 `原始` 选项，复制全文，粘贴至 `headers.txt` 中

复制第一行 POST 后面的内容，粘贴至 `config.json` 中 `url` 字段

![](imgs/copy-header.png)

选择 `请求` 栏 `表单数据`，同样打开 `原始` 选项，复制全文，粘贴至粘贴至 `config.json` 中 `data` 字段

运行 `auto-auth.py`
