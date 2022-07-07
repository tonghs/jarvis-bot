# jarvis

![pr test workflow](https://github.com/tonghs/jarvis-bot/actions/workflows/pr_test.yml/badge.svg)
![main test](https://github.com/tonghs/jarvis-bot/actions/workflows/push_to_main.yml/badge.svg)


a telegram bot

## dev

Python 3.8


```shell
pip install -r requirements.dev.txt
```

```shell
python manager.py main.py
```

## run test
```shell
make build && make test
```

## run

```shell
make build && docker-compose up
```
