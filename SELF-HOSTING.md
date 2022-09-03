# Self-hosting Tyger
Want to self-host Tyger? Just follow this tutorial!

## Requirements
```
Python 3.10
The following modules:
    git+https://github.com/EnokiUN/voltage (voltage)
    python-dotenv
    os
    ast
    random
    mcstatus
    pypixel-api
    mojang
    mcrcon
    datetime
    requests
```

## Setup

1. Clone Tyger using `git clone https://github.com/4444dogs/Tyger.git`
2. Open up Tyger's directory using `cd Tyger`
3. Create a configuration file using `cp .env.example .env` (`cp` is renamed to `copy` on Windows)
3. Open `.env` with your text editor of choice
4. Replace "YOUR BOT TOKEN HERE" with your Revolt bot's token (Do NOT remove the quotes in any of these steps)
5. Because Tyger is still in pre-alpha, you need to add servers that Tyger can join; do so by replacing "YOU SERVER ID HERE" with your server id (Note that to add another entry, you can add a comma, and then inside of two quotes, another server's id)
6. IF you plan on using the Hypixel command you must replace "YOUR HYPIXEL API KEY HERE" with a Hypixel API token (Do so by connecting to Hypixel and running `/api`)

If you want to setup an RCON console for your Minecrafter server, fill out it's entires in `.env`
