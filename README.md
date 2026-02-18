# Wayback Machine Telegram Bot

A Telegram bot that helps you find archived versions of web pages using the Internet Archive (Wayback Machine). Send a URL and a date, and the bot will return a link to the closest archived snapshot.

## Features

- **URL + Date Input:** Users send a website URL and a target date (year, month, day).
- **Wayback Machine Integration:** Queries the Internet Archive API to find the closest snapshot.
- **Direct Link Output:** Returns a direct link to the archived page on `archive.org`.
- **Error Handling:** Gracefully handles invalid URLs, dates, or missing archives.
- **User‑Friendly Format:** Displays results in a clean, readable format in the chat.
- **Date Validation:** Ensures the date is in the past and formatted correctly.

## Technologies Used

- **Language:** `Python`
- **Telegram Bot Framework:** `telebot` (pyTelegramBotAPI)
- **HTTP Client:** `requests` library (for API calls)
- **Archive Service:** Internet Archive / Wayback Machine (https://archive.org)

### Prerequisites

- Python 3.8 or higher
- A Telegram account
- Telegram Bot API token (from @BotFather)

### Step‑by‑Step Guide

**Create a Telegram Bot:**
  - Message `@BotFather` on Telegram.
  - Use the `/newbot` command to create a new bot.
  - Copy the **API Token** provided by BotFather.
