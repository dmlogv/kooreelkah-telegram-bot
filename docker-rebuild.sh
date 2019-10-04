#!/usr/bin/env bash
docker stop $(docker ps -q --filter ancestor="kooreelkah-bot")
docker build -t kooreelkah-bot .
docker run -d --restart unless-stopped kooreelkah-bot