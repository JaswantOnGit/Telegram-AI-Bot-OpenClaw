——————————├──├──├──├──└──—·# Telegram AI Bot — OpenClaw

An intelligent Telegram chatbot powered by the OpenAI API (via OpenClaw). It handles natural language conversations in real time, enforces allowlist-based access control, and supports automated proactive messaging through cron job scheduling.

---

## Features

- **Real-time AI responses** — Uses OpenAI's `gpt-4o-mini` model to generate context-aware replies to user messages
- - **Allowlist access control** — Only pre-authorized Telegram user IDs can interact with the bot, preventing unauthorized API usage
  - - **Proactive cron messaging** — Configured via OpenClaw to send scheduled messages (e.g. motivational quotes, reminders) without user input
    - - **Environment-based configuration** — All secrets managed via `.env` file; no hardcoded credentials
      - - **Structured logging** — Timestamped logs for monitoring messages and unauthorized access attempts
       
        - ---

        ## Tech Stack

        - **Python 3.11+**
        - - [python-telegram-bot](https://python-telegram-bot.org/) — Telegram Bot API wrapper
          - - [OpenAI Python SDK](https://github.com/openai/openai-python) — AI response generation
            - - [python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management
              - - [OpenClaw](https://openclaw.dev/) — AI agent gateway and cron job scheduler
               
                - ---

                ## Project Structure

                ```
                Telegram-AI-Bot-OpenClaw/
                ├── bot.py              # Main bot logic (handlers, AI integration)
                ├── .env.example        # Example environment variable file
                ├── requirements.txt    # Python dependencies
                ├── .gitignore          # Git ignore rules
                └── README.md
                ```

                ---

                ## Getting Started

                ### Prerequisites

                - Python 3.11 or higher
                - - A Telegram Bot token (create one via [@BotFather](https://t.me/BotFather))
                  - - An OpenClaw / OpenAI API key
                    - - Node.js 22+ (for OpenClaw gateway)
                     
                      - ### Installation
                     
                      - 1. **Clone the repository**
                        2.    ```bash
                                 git clone https://github.com/JaswantOnGit/Telegram-AI-Bot-OpenClaw.git
                                 cd Telegram-AI-Bot-OpenClaw
                                 ```

                              2. **Create and activate a virtual environment**
                              3.    ```bash
                                       python -m venv venv
                                       source venv/bin/activate   # Windows: venv\Scripts\activate
                                       ```

                                    3. **Install dependencies**
                                    4.    ```bash
                                             pip install -r requirements.txt
                                             ```

                                          4. **Configure environment variables**
                                          5.    ```bash
                                                   cp .env.example .env
                                                   ```
                                                   Then edit `.env` and fill in your values:
                                               ```
                                               TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
                                               ALLOWED_USER_IDS=123456789,987654321
                                               OPENCLAW_API_KEY=your_openclaw_api_key_here
                                               ```

                                            5. **Run the bot**
                                            6.    ```bash
                                                     python bot.py
                                                     ```

                                                  ---

                                              ## Bot Commands

                                      | Command | Description |
                                |---------|-------------|
                                | `/start` | Initializes the bot and displays a welcome message |
                                | `/status` | Confirms the bot is active and running |

                                Any other text message will be sent to the AI model and responded to in real time.

                          ---

                        ## Security

                        Access is restricted to users listed in `ALLOWED_USER_IDS`. Unauthorized users receive an "Access denied" response, and the attempt is logged with a warning. Never commit your `.env` file — it is excluded by `.gitignore`.

                        ---

                        ## Author

                        **Jaswant Singh**
                        [jaswants022@gmail.com](mailto:jaswants022@gmail.com)
                        [GitHub](https://github.com/JaswantOnGit)

                        ---

                        ## License

                        This project is licensed under the [MIT License](LICENSE).
