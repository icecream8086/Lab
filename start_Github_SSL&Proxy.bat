@REM 用于设置GitHub以及v2ray的一键代理设置
@REM 执行前在当前文件夹下的路径执行即可
@REM     会忽略SSL错误
@REM     同时添加代理

git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy http://127.0.0.1:1080
git config --global http.sslVerify "false"
