🌐 IClinktree (Web3 Creator Hub) live website: https://2n2uw-uaaaa-aaaag-at2hq-cai.icp.net
License: MIT | Built on ICP
IClinktree is a lightning-fast, fully decentralized, and self-hosted Creator Hub & AI-Powered Video Knowledge Base running 100% on-chain on the Internet Computer Protocol (ICP).
Say goodbye to centralized link-in-bio services. With IClinktree, you own your data, your analytics are logged privately on-chain, your supporters can tip you in multiple cryptocurrencies via dynamic QR codes, and your visitors can query your entire YouTube video history using an on-chain AI assistant.
✨ Key Features
⚡ 100% On-Chain Deployment: Hosted directly on Internet Computer canister smart contracts—no traditional cloud servers (AWS, Vercel, Heroku) required.
🤖 On-Chain AI Assistant & Keyword Search: An integrated chat widget powered by your Motoko backend that instantly indexes and retrieves relevant YouTube tutorials based on user queries.
📊 Privacy-First Live 7-Day Analytics: Tracks rolling visitor stats (total pageviews, unique devices, button clicks, country, device/OS, and browser) entirely on-chain with automatic rolling 7-day data pruning and zero third-party cookies.
☕ Multi-Chain Crypto Tipping: Interactive "Buy Me a Coffee" modal featuring dynamic QR codes for ICP, BTC, ETH, SOL, and XRP with customizable wallet addresses and optional developer support fallbacks.
🚀 Automated Setup & Deployment Wizard (setup.py): An all-in-one interactive Python script that scaffolds your workspace, configures your profiles, handles fallback permissions, scrapes your YouTube channel, and deploys everything to the ICP mainnet.
🔗 Dynamic ICP Ecosystem & dApp Referrals: Integrated filter tabs and dedicated cards for top ICP dApps (OpenChat, Clown, Oisy, Randseed) with customizable or fallback referral support. If unused, the section dynamically hides itself.
🏗️ Project Architecture & How It Works
IClinktree/
├── backend/
│   └── main.mo                  # Motoko smart contract (Handles search index, AI assistant, & traffic logs)
├── assets/
│   ├── index.html               # Apple-inspired glassmorphism frontend user interface (dynamically rendered)
│   ├── styles.css               # Clean minimalist dark-mode styling & responsive grid layouts
│   ├── script.js                # Frontend router, crypto modal renderer, analytics logger, & chat handler
│   └── images/                  # Social media icons, profile picture, crypto logos, and dApp badges
├── setup.py                     # Interactive Python configuration & mainnet deployment wizard
├── push.py                      # Automated YouTube scraper & canister video synchronization script
├── dfx.json                     # DFINITY SDK canister compilation and network configuration
└── canister_ids.json            # Mainnet/local canister ID registry mapping

The AI Assistant & Keyword Search Engine (backend/main.mo)
How does the assistant widget return matching video links?
Indexing: When you run push.py, your YouTube channel's public playlist is scraped using yt-dlp. Every video's title, description, and tags are cleaned, lowercased, and combined into a searchable text string.
Batch Uploading: These video records are chunked and pushed securely onto your Motoko backend canister (backend/main.mo) via Candid interface calls.
Smart Synonym Mapping: The backend features a built-in dictionary (mapping keywords like "apple" to "mac", "macbook", "iphone", "ios", or "crypto" to "bitcoin", "ethereum", "blockchain").
Query Execution: When a user types a question or keyword into the chat widget (e.g., "How do I build a canister?" or types "traffic" to view live 7-day analytics), the frontend queries the askBot or getTrafficStats query functions on your canister. The backend scans stored metadata, ranks matches, and dynamically renders clickable video cards with direct links back to your YouTube content.
The Automated Setup Wizard (setup.py)
Instead of manually editing JSON files or writing Candid arguments, setup.py handles the heavy lifting through a streamlined interactive flow:
Principal Detection: Automatically runs dfx identity get-principal to fetch your DFINITY Principal ID and reminds you to assign controller permissions in the NNS.
Profile Personalization: Prompts you for your creator name, bio, and YouTube channel video URL.
Social Media & Fallback Permissions: Prompts for your social media URLs (YouTube, OpenChat, Telegram, X, Instagram, TikTok, etc.). If any links are left blank, it asks for permission to use the original developer's links as a fallback.
ICP Ecosystem dApp Referrals: Prompts you for your referral links for top ICP dApps (OpenChat, Clown, Oisy, Randseed). If left blank, it asks if you'd like to support the original creator's referral links. If you decline and leave them blank, the entire ICP Ecosystem tab and card section are automatically omitted from the build.
Flexible Crypto & Tipping Setup: Asks if you want to use custom crypto addresses. If you choose Yes, you can enter your own addresses for ICP, BTC, ETH, SOL, and XRP, with options to support the original developer for any blank fields.
Scaffolding & Deployment: Automatically creates your folder structure (backend/, assets/images/), populates configuration files, executes push.py to seed your video library, and runs dfx deploy --network ic to push your site live.
YouTube Synchronization (push.py)
Maintains your video knowledge base by fetching fresh metadata from your YouTube channel URL, sanitizing special characters to prevent Motoko syntax crashes, and batch-uploading records into your backend canister storage.
🚀 Getting Started & Deployment Guide
Prerequisites
Make sure you have the following installed on your machine (macOS / Linux / WSL):
DFINITY Dfx SDK (v3.x+)
Python 3 and yt-dlp (pip install yt-dlp)
Step 1: Clone the Repository
git clone https://github.com/iTechBod/IClinktree.git
cd IClinktree

Step 2: Run the Setup Wizard
Execute the automated python script:
python3 setup.py

Follow the interactive prompts in your terminal:
Review your DFINITY Principal ID and verify canister controllers.
Enter your custom Display Name and Bio.
Provide your social media profile URLs (or grant fallback permissions for blank entries).
Provide your ICP Ecosystem dApp referral links (or grant support permissions).
Choose whether to configure your own crypto wallet addresses or support the original creator.
Provide your deployed Backend and Frontend Canister IDs (or press Enter to use default placeholders).
The script will automatically generate all files, scrape your YouTube channel, upload your video database to the blockchain, and deploy your site live to the Internet Computer mainnet!
📜 License
This project is open-source and released under the MIT License. Feel free to fork it, adapt it for your own creator brand, or contribute improvements!
Built with passion on the Internet Computer Protocol.
