🌐 IClinktree (Web3 Creator Hub)
<img width="170" height="20" alt="image" src="https://github.com/user-attachments/assets/34ca1631-e1b7-4c42-8ff3-8952baf19064" />
<img width="114" height="20" alt="image" src="https://github.com/user-attachments/assets/577c08d5-74e0-41a3-a19e-754bfccf8f40" />
<img width="82" height="20" alt="image" src="https://github.com/user-attachments/assets/b11dce54-35e6-4537-8bcf-85b25bcb2c6a" />

Platform: ICP

https://internetcomputer.org

License: MIT

Live Mainnet Canister: https://2n2uw-uaaaa-aaaag-at2hq-cai.icp.net

IClinktree is a lightning-fast, fully decentralized, and self-hosted Creator Hub & AI-Powered Video Knowledge Base running 100% on-chain on the Internet Computer Protocol (ICP).

Say goodbye to centralized link-in-bio services. With IClinktree, you own your data entirely: your analytics are logged privately on-chain, your supporters can tip you in multiple cryptocurrencies via dynamic QR codes, and your visitors can query your entire YouTube video history using an on-chain AI assistant.

✨ Key Features

⚬ ⚡ 100% On-Chain Deployment: Hosted directly on Internet Computer canister smart contracts—no traditional cloud servers (AWS, Vercel, Heroku) required.
⚬ 🤖 On-Chain AI Assistant & Search: Integrated chat widget powered by your Motoko backend that instantly indexes and retrieves relevant YouTube tutorials based on user queries.
⚬ 📊 Privacy-First Live 7-Day Analytics: Tracks rolling visitor stats (pageviews, unique devices, button clicks, top country, device/OS, and browser) on-chain with automatic 7-day data pruning and zero third-party cookies.
⚬ ☕ Multi-Chain Crypto Tipping: Interactive "Buy Me a Coffee" modal featuring dynamic QR codes for ICP, BTC, ETH, SOL, and XRP with customizable wallet addresses and developer support fallbacks.
⚬ 🚀 Automated Setup & Deployment Wizard (setup.py): Interactive Python script that scaffolds your workspace, configures profiles, handles fallback permissions, scrapes YouTube, and deploys to ICP mainnet.
⚬ 🔗 Dynamic ICP Ecosystem & dApp Referrals: Integrated filter tabs and dedicated cards for top ICP dApps (OpenChat, Clown, Oisy, Randseed) with customizable referral support. If unused, the section dynamically hides itself.

🏗️ Project Architecture

IClinktree/
├── backend/
│   └── main.mo          # Motoko smart contract (Search index, AI assistant, & traffic logs)
├── assets/
│   ├── index.html       # Apple-inspired glassmorphism frontend (Dynamically rendered)
│   ├── styles.css       # Clean minimalist dark-mode styling & responsive grid layouts
│   ├── script.js        # Frontend router, crypto modal, analytics logger, & chat handler
│   └── images/          # Social media icons, profile photo, crypto logos, and dApp badges
├── setup.py             # Interactive Python configuration & mainnet deployment wizard
├── push.py              # Automated YouTube scraper & canister synchronization script
├── dfx.json             # DFINITY SDK canister compilation and network configuration
└── canister_ids.json    # Mainnet/local canister ID registry mapping


💡 How It Works

1. AI Assistant & Keyword Search Engine (backend/main.mo)

How does the assistant widget return matching video links?

1. Indexing: When you run push.py, your YouTube channel's public playlist is scraped using yt-dlp. Every video's title, description, and tags are cleaned, lowercased, and combined into a searchable index string.
2. Batch Uploading: Video records are chunked and pushed securely onto your Motoko backend canister (backend/main.mo) via Candid interface calls.
3. Smart Synonym Mapping: The backend features a built-in dictionary (mapping keywords like "apple" to "mac", "macbook", "iphone", "ios", or "crypto" to "bitcoin", "ethereum", "blockchain").
4. Query Execution: When a visitor types a query into the chat widget (e.g., "How do I build a canister?" or types "traffic" to view live 7-day analytics), the frontend queries askBot or getTrafficStats on your canister to rank matches and render interactive video cards.

2. Automated Setup Wizard (setup.py)

Instead of manually editing JSON files or writing Candid arguments, setup.py guides you through an interactive terminal wizard:

⚬ 🔑 Principal Detection: Runs dfx identity get-principal to fetch your Principal ID and reminds you to assign controller permissions in the NNS.
⚬ 👤 Profile Personalization: Prompts for your display name, bio, and YouTube channel URL.
⚬ 🌐 Social & Fallback Permissions: Collects your social media URLs (YouTube, OpenChat, Telegram, X, Instagram, TikTok, etc.). If any fields are skipped, it asks for permission to use original developer fallbacks.
⚬ 🔗 dApp Referrals: Collects referral links for top ICP dApps (OpenChat, Clown, Oisy, Randseed). If left blank and fallbacks are declined, the section dynamically omits itself from the frontend.
⚬ 💳 Crypto & Tipping Setup: Configures custom wallet addresses for ICP, BTC, ETH, SOL, and XRP.
⚬ 📦 Scaffolding & Deployment: Auto-generates your directory tree, builds configuration files, executes push.py to seed video metadata, and deploys live via dfx deploy --network ic.

3. YouTube Synchronization (push.py)

Maintains your video knowledge base by fetching fresh metadata from your YouTube channel URL, sanitizing special characters to prevent Motoko syntax crashes, and batch-uploading records directly into on-chain canister storage.

🚀 Deployment Guide

Prerequisites

Make sure your environment (macOS / Linux / WSL) has the following installed:

⚬ [suspicious link removed] (v3.x+)
⚬ Python 3 and yt-dlp:
  pip install yt-dlp
  

Step 1: Clone the Repository

git clone https://github.com/iTechBod/IClinktree.git
cd IClinktree


Step 2: Run the Setup Wizard

Execute the setup script:

python3 setup.py


Follow the prompts in your terminal:

1. Verify your DFINITY Principal ID and confirm canister ownership in NNS.
2. Enter your custom Creator Name and Bio.
3. Provide your social media profile links (or allow developer fallbacks).
4. Input your dApp referral links (or choose to omit/support fallbacks).
5. Set up your custom crypto wallet addresses for tips.
6. Input your Backend and Frontend Canister IDs.

The script will automatically build all files, sync your YouTube catalog, upload metadata on-chain, and deploy your creator hub live to the Internet Computer mainnet!

📜 License

Distributed under the MIT License. See LICENSE for more information. Feel free to fork, adapt for your creator brand, and build upon it!

Built with passion on the Internet Computer Protocol.
