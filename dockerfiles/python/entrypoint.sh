#!/bin/sh

# Ensure bot.py has the correct executable permissions
chmod +x /usr/src/app/bot.py

# Execute the command passed to the entrypoint (start cron and tail the log)
exec "$@"
