# kooreelkah-telegram-bot

A simple bot for stupid things


## What is *kooreelkah*?

Russian word `курилка` means a room or another place for smoking.


## Pre

If you want to run it as dockerized daemon (I hope), don't forget to configure your Docker restart containers after reboot:

```sh
# emacs /etc/docker/daemon.json
-------------------------------
{
  "live-restore": true
}
```

And reload `docker` settings:

```sh
# systemctl reload docker.service 
```


## Installation

The ~~three~~ ~~eight~~ ~~ten~~ eleven easy steps:

1. Fork this project as a private repository.
1. Clone it.
1. Ask @BotFather for your own Bot token.
1. Find out `chat_id` of all chat room member using @userinfobot.
1. Also get `chat_id` of the chat room (if you want to use Scheduled Messages).
1. Copy `config.default.py` or `config.example.py` to `config.py`.
1. Configure `TOKEN`, `CHAT`, `MEMBERS`, `GROUPS` etc. as in `config.example.py`.
1. Commit-n-push back to your repository.
1. Clone to your server.
1. In the project directory build Docker image:
    ```sh
   $ docker build -t kooreelkah-bot:latest .
   ```
1. Run it as a daemon:
    ```sh
   $ docker run -d --restart unless-stopped kooreelkah-bot 
   ```  
   
Enjoy if you can.
