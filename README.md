# jarvis

![pr test workflow](https://github.com/tonghs/jarvis/actions/workflows/pr_test.yml/badge.svg)
![master test](https://github.com/tonghs/jarvis/actions/workflows/push_to_master.yml/badge.svg)


my telegram bot

## dev

Python 3.7


```shell
pip install -r requirements.dev.txt
```

Google Auth
```shell
cd libs/google/ python google_auth.py
```

```shell
python manager.py bot.py
```


## 目录结构

* bot.py  启动文件
* view.py message handler 文件
