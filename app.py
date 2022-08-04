#from https://www.youtube.com/watch?v=oDoFvpDftBA

import logging
import os
import re

from dotenv import load_dotenv
import pyjokes
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

SLACK_APP_TOKEN = "xapp-1-A03S92XELQ5-3895973811299-9c501fd720e54f17a220228c6fce1f39ca766ab54fb1a35f7e2685a75a45fd58"
SLACK_BOT_TOKEN = "xoxb-3881475683879-3881500756151-awDa886An4t8nY7ZgXPlN4LO"

app = App(token=SLACK_BOT_TOKEN, name="Joke Bot")
logger = logging.getLogger(__name__)


@app.message(re.compile("^joke$"))  # type: ignore
def show_random_joke(message, say):
    """Send a random pyjoke back"""
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    joke = pyjokes.get_joke()
    logger.info(f"Sent joke < {joke} > to user {user_id}")

    say(text=joke, channel=dm_channel)

@app.message("$")  # type: ignore
def show_random_joke(message, say):
    """Send a random pyjoke back"""
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    joke = "Fuck off!"
    logger.info(f"Sent joke < {joke} > to user {user_id}")

    say(text=joke, channel=dm_channel)

def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
