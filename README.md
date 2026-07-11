Create a Python Telegram bot using python-telegram-bot.

Requirements:
- Use Python 3.12.
- Store configuration in a .env file.
- Organize the project into multiple files:
  - bot.py
  - config.py
  - sms_service.py
  - database.py
  - requirements.txt
  - README.md
- Integrate with a legitimate SMS provider's official API (the provider API key should be read from environment variables).
- Commands:
  /start - Welcome message
  /balance - Show API balance
  /countries - List supported countries
  /services - List available services
  /getnumber <country> <service> - Purchase a temporary phone number through the provider API
  /status - Check activation status
  /cancel - Cancel activation if supported
- Automatically poll the provider API every 5 seconds for incoming SMS.
- When an SMS arrives, send the OTP/message to the Telegram user.
- Handle API errors gracefully.
- Use async programming.
- Include logging.
- Add retry logic for network failures.
- Use SQLite to store user sessions and activation IDs.
- Include complete GitHub-ready project structure.
- Provide a detailed README explaining setup, installation, environment variables, and running the bot.
- Follow clean code principles with comments and type hints.
