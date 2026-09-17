# ChatterVia 💬

A minimal, real-time public chat room built with [Streamlit](https://streamlit.io/) and [Firebase Realtime Database](https://firebase.google.com/docs/database).

**Live app:** https://minulsandith-chattervia-chat-room-8mfa07.streamlit.app/

## Features

- Global, public chat room — no sign-up required, just enter a display name.
- Messages are stored in Firebase Realtime Database and shared with every visitor.
- Manual refresh button to pull the latest messages.
- A themed, mobile-friendly UI via custom CSS (`style.css`).
- Extra pages (Streamlit multipage app):
  - **Chat with Minul** — placeholder for a future 1:1 chat feature.
  - **Information** — about page describing the app.

## Tech stack

| Layer      | Technology                          |
|------------|--------------------------------------|
| UI         | [Streamlit](https://streamlit.io/)   |
| Backend    | [Firebase Realtime Database](https://firebase.google.com/docs/database) |
| DB client  | [Pyrebase4](https://github.com/nhorvath/Pyrebase4) |
| Hosting    | [Streamlit Community Cloud](https://streamlit.io/cloud) |

## Project structure

```
ChatterVia/
├── Chat_room.py            # Main entry point — the chat room page
├── pages/
│   ├── 1_Chat_with_Minul.py   # Placeholder page for a future direct chat
│   └── 2_Information.py       # About / info page
├── style.css                  # Custom styling injected into the app
├── requirements.txt            # Python dependencies
└── README.md
```

## Getting started

### Prerequisites

- Python 3.9+
- A Firebase project with Realtime Database enabled (only needed if you want to point the app at your own backend instead of the shared demo database)

### Installation

```bash
git clone https://github.com/MinulSandith/ChatterVia.git
cd ChatterVia
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run locally

```bash
streamlit run Chat_room.py
```

The app will open at `http://localhost:8501`.

### Using your own Firebase backend

The Firebase config currently lives directly in `Chat_room.py`. To point the app at your own project, replace the `config` dictionary with your Firebase web app credentials (found in Firebase Console → Project settings → General → Your apps), and make sure your Realtime Database rules allow read/write for this use case. For anything beyond a demo, prefer loading these values from [`st.secrets`](https://docs.streamlit.io/develop/concepts/connections/secrets-management) instead of hardcoding them in source.

## Known limitations

- The chat has no authentication or moderation — anyone can post as anyone.
- Message ordering relies on an incrementing counter stored in the database (`info/last`); concurrent writers can race and overwrite each other's counter update.
- The database schema and security rules are permissive by design (public demo project), so treat the shared instance as a scratchpad, not a place for sensitive data.

## Troubleshooting

**`ModuleNotFoundError: No module named 'requests.packages.urllib3.contrib.appengine'` (or a similar `requests_toolbelt` import error) when running the app.**
This comes from `Pyrebase4` depending on older internals of `requests`/`urllib3`/`requests-toolbelt` that were removed in recent releases. Reinstalling from the pinned `requirements.txt` in this repo (which constrains `urllib3<2` and `requests-toolbelt==0.10.1`) resolves it.

## Roadmap

- [ ] Implement the "Chat with Minul" direct-message page.
- [ ] Move Firebase credentials into `st.secrets`.
- [ ] Add basic message validation/moderation.

## Contributing

Bug reports and pull requests are welcome — this project is a good first-timer-friendly Streamlit codebase. Please open an issue describing the bug or feature before submitting a large PR.

## Author

**Minul Sandith**
GitHub: [@MinulSandith](https://github.com/MinulSandith)

### Other projects

| Project | Description |
|---|---|
| [Text-encrypter](https://github.com/MinulSandith/Text-encrypter) | A text encrypter using both built-in and custom Python encryption methods. |
| [Marks-collector](https://github.com/MinulSandith/Marks-collector) | Helps teachers total up marks across exam papers. |
| [Web-app-on-Geography-E-learning-](https://github.com/MinulSandith/Web-app-on-Geography-E-learning-) | A small Flask-based e-learning GUI. |
| [YouTube-Video-Downloader](https://github.com/MinulSandith/YouTube-Video-Downloader) | A Python script/GUI for downloading YouTube videos. |
| [Currency-Converter](https://github.com/MinulSandith/Currency-Converter) | A simple currency conversion tool. |
| [Language-Converter](https://github.com/MinulSandith/Language-Converter) | A language translation utility. |
| [Number-system-converter](https://github.com/MinulSandith/Number-system-converter) | Converts numbers between binary, octal, decimal and hex. |
| [The-Calc](https://github.com/MinulSandith/The-Calc) | A calculator app. |
| [Photo-Viewer](https://github.com/MinulSandith/Photo-Viewer) | A simple photo viewer app. |

See the full list at [github.com/MinulSandith?tab=repositories](https://github.com/MinulSandith?tab=repositories).
