@REM 用于设置GitHub以及v2ray的一键代理设置
@REM 在当前文件夹下的相对路径执行即可
@REM     会忽略SSL错误
@REM     同时添加代理

git config --global http.sslVerify "false"

git config --global http.proxy
git config --global https.proxy

git config --global --unset http.proxy
git config --global --unset https.proxy

git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy http://127.0.0.1:1080

git config --global -l