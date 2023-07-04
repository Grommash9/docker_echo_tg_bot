
# docker echo tg bot

A minimal example of launching a telegram bot in a docker container with the output of the bot token to environment variables

## Run

To create a container, use the command

```bash
  docker build -t docker_echo_tg_bot .
```

When starting the container, please pass in the parameters the environment variable for the bot token

```bash
  docker run -e BOT_TOKEN=<your_token> docker_echo_tg_bot

```
