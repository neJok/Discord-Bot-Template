# Discord Bot Template 🚀

This is a template for building a Discord bot using the `discord.py` and `motor` libraries.

## Prerequisites ✅

Before you begin, make sure you have the following installed on your system:

- Python ~3.12 or higher 🐍
- pip (Python package manager) 💻

## Setting up the bot ⚙️

1. Clone or download this repository. 📥
2. Navigate to the root directory of the project and create a file called `.env`. 📝
3. Follow the instructions below to get a Discord token and a MongoDB connection string. 🔑
4. **Rename `.env.example` to `.env`** and fill in the necessary values for your bot. 🛠️
5. Install the required packages by running the following command:

```
pip install -r requirements.txt
```

6. You can run the bot in two ways:
    - **Standard**: Run it using the following command:

    ```
    python bot.py
    ```

    - **Docker Compose**: Alternatively, you can use Docker to run the bot. Make sure Docker is installed and then use the following command to start the bot:

    ```
    docker-compose up --build
    ```

## Getting a Discord token 🎮

To use the Discord API, you need to create a Discord bot and get a token to authenticate your bot. Here's how to do that:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and log in with your Discord account. 🔑
2. Click on the "New Application" button. ➕
3. Give your application a name and click "Create". ✍️
4. On the left-hand side of the screen, click on the "Bot" tab. 🤖
5. Click on the "Add Bot" button. ➕
6. Enable all intents on the Discord Developer Portal:
    * Go to the **Discord Developer Portal**.
    * Click on your Discord application.
    * Go to the "Settings" tab.
    * Scroll down to the "Privileged Gateway Intents" section.
    * Enable all necessary intents. 🔐
7. Copy the token that is displayed on the screen. This is the token you will use to authenticate your bot. 🔑

## Getting a MongoDB connection string 🌐

To connect to a MongoDB database, you need a connection string that specifies the hostname and port of the MongoDB server, as well as the name of the database you want to connect to. Here's how to get a connection string:

1. Sign up for a [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account. 🌐
2. Create a new cluster and select the "Free Tier" option. 🆓
3. Click on the "Connect" button. 🔗
4. Follow the instructions to connect to your cluster using the MongoDB Compass GUI. 🔧
5. Click on the "Connect Your Application" button. 💻
6. Copy the connection string that is displayed on the screen. This is the connection string you will use to connect to your MongoDB database. 🔑

Now you're all set! 🎉