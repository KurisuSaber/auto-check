# auto-check

自动打卡脚本

### 使用方法

#### 单次打卡

```shell
$ python3 check.py
```

#### 定时任务

以centos为例

```shell
$ crontab -e
```

进入任务列表编辑

每天17:05自动执行`python3 /root/Desktop/check.py`指令

```
05 17 * * * python3 /root/Desktop/check.py
```

:wq保存退出

```shell
$ crontab -l #查看任务是否被添加进来
$ service crond restart #重启服务
$ service crond status #查看服务状态 active代表正常
```

### 代码修改说明

```python
info = {
    "统一认证登录用户名":{
        "password":"统一认证登录密码","name":"真实姓名","number":"学号"
    }
}
```

"统一认证登录用户名"：**修改为** 登录统一认证时候的账号

"统一认证登录密码"： **修改为** 即登录统一认证时候的密码

"真实姓名"：**修改为** 真实姓名 如王大力

"学号"：**修改为** 学号  如21212121