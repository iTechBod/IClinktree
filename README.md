🌐 IClinktree (Web3 Creator Hub) <img width="170" height="20" alt="image" src="https://github.com/user-attachments/assets/34ca1631-e1b7-4c42-8ff3-8952baf19064" />
<img width="114" height="20" alt="image" src="https://github.com/user-attachments/assets/577c08d5-74e0-41a3-a19e-754bfccf8f40" />
<img width="82" height="20" alt="image" src="https://github.com/user-attachments/assets/b11dce54-35e6-4537-8bcf-85b25bcb2c6a" />

Platform: ICP

https://internetcomputer.org

License: MIT

IClinktree is a lightning-fast, fully decentralized, and self-hosted Creator Hub & AI-Powered Video Knowledge Base running 100% on-chain on the Internet Computer Protocol (ICP).
Say goodbye to centralized link-in-bio services. With IClinktree, you own your data entirely: your analytics are logged privately on-chain, supporters can tip you in multiple cryptocurrencies via dynamic QR codes, visitors can query your entire YouTube video history using an on-chain AI assistant, and fans can send secure direct messages/tickets straight to your canister inbox.
✨ Key Features
⚬ ⚡ 100% On-Chain Deployment: Hosted directly on Internet Computer canister smart contracts—no traditional cloud servers (AWS, Vercel, Heroku) required.
⚬ 🤖 On-Chain AI Assistant & Search: Integrated chat widget powered by your Motoko backend that instantly indexes and retrieves relevant YouTube tutorials based on user queries.
⚬ 📬 Secure Visitor Ticket System: Allows visitors to submit anonymous direct messages/tickets via the chat interface (e.g., typing ticket Can you cover Oisy wallet?). Protected by Internet Identity authentication so only the master owner principal can view, mark read, or delete inbox messages.
⚬ ⏳ Customizable Ticket Retention & Auto-Pruning: Set your preferred auto-deletion lifespan for incoming tickets during setup to optimize canister cycles and storage.
⚬ 📊 Privacy-First Live 7-Day Analytics: Tracks rolling visitor stats (pageviews, unique devices, button clicks, top country, device/OS, and browser) on-chain with automatic 7-day data pruning and zero third-party cookies.
⚬ ☕ Multi-Chain Crypto Tipping: Interactive "Buy Me a Coffee" modal featuring reliable, high-speed generated QR codes for ICP, BTC, ETH, SOL, and XRP with customizable wallet addresses and developer support fallbacks.
⚬ 🚀 Automated Setup & Deployment Wizard (setup.py): Interactive Python script that scaffolds your workspace, configures profiles, maps your Master Principal ID, sets up ticket retention parameters, scrapes YouTube, and deploys to ICP mainnet.
⚬ 🔗 Dynamic ICP Ecosystem & dApp Referrals: Integrated filter tabs and dedicated cards for top ICP dApps (OpenChat, Clown, Oisy, Randseed) with customizable referral support. If unused, the section dynamically hides itself.
🏗️ Project Architecture
IClinktree/
├── backend/
│   └── main.mo           # Motoko smart contract (Search index, AI assistant, traffic logs, & secured tickets)
├── assets/
│   ├── index.html        # Apple-inspired glassmorphism frontend (Dynamically rendered)
│   ├── styles.css        # Clean minimalist dark-mode styling & responsive grid layouts
│   ├── script.js         # Frontend router, crypto modal, analytics logger, chat handler, & II auth
│   └── images/           # Social media icons, profile photo, crypto logos, and dApp badges
├── setup.py              # Interactive Python configuration & mainnet deployment wizard
├── push.py               # Automated YouTube scraper & canister synchronization script
├── dfx.json              # DFINITY SDK canister compilation and network configuration
└── canister_ids.json     # Mainnet/local canister ID registry mapping

💡 How It Works
1. AI Assistant & Keyword Search Engine (backend/main.mo)
Indexing: When you run push.py, your YouTube channel's public playlist is scraped using yt-dlp. Every video's title, description, and tags are cleaned, lowercased, and combined into a searchable index string.
Batch Uploading: Video records are chunked and pushed securely onto your Motoko backend canister via Candid interface calls.
Smart Synonym Mapping: The backend features a built-in dictionary (mapping keywords like "apple" to "mac", "macbook", "iphone", "ios", or "crypto" to "bitcoin", "ethereum", "blockchain").
Query Execution: When a visitor types a query into the chat widget, types traffic for live metrics, or types ticket <message> to send feedback, the frontend routes requests directly to canister endpoints (askBot, getTrafficStats, or submitTicket).
2. Secure Ticket & Inbox Manager
Visitor Submission: Visitors can submit direct feedback or questions straight to the blockchain by typing ticket <your message> into the assistant chat.
Owner Authentication: Creators login securely using Internet Identity (II). The canister matches the caller's principal against the hardcoded OWNER principal (masterpid) defined during setup.
Inbox Commands: Once authenticated as the owner, typing show tickets or show unread in the chat reveals your private inbox with options to toggle read status, delete individual items, or batch clear/mark-read.
3. Automated Setup Wizard (setup.py)
Instead of manually editing JSON files or writing Candid arguments, setup.py guides you through an interactive terminal wizard:
Master Principal & II Mapping: Prompts for your Master Principal ID (PID) so only you can access the secure ticket inbox.
Ticket Preferences: Lets you decide whether to enable tickets and configure how many days the canister retains them before automatic deletion.
Principal Detection: Runs dfx identity get-principal to fetch your DFINITY Principal ID and reminds you to assign controller permissions in the NNS.
Profile Personalization: Prompts for your display name, bio, and YouTube channel URL.
Social & Crypto Configuration: Collects social profile links and custom cryptocurrency wallet addresses (ICP, BTC, ETH, SOL, XRP) with developer fallback options.
Scaffolding & Deployment: Auto-generates your directory tree, builds configuration files, executes push.py to seed video metadata, and deploys live via dfx deploy --network ic.
🚀 Deployment Guide
Prerequisites
Make sure your environment (macOS / Linux / WSL) has the following installed:
https://cli.internetcomputer.org/1.6/ (v3.x+)
Python 3 and yt-dlp: pip install yt-dlp
Step 1: Clone the Repository
git clone https://github.com/iTechBod/IClinktree.git
cd IClinktree

Step 2: Run the Setup Wizard
Execute the setup script:
python3 setup.py

Follow the prompts in your terminal:
Enter your Master Principal ID (PID) for secure owner ticket access.
Choose whether to enable the ticket system and specify auto-deletion retention days (e.g., 7 days).
Verify your DFINITY Principal ID and confirm canister ownership in the NNS.
Enter your custom Creator Name, Bio, and YouTube URL.
Provide your social media profile links and dApp referrals (or use developer fallbacks).
Set up your custom crypto wallet addresses.
Input your Backend and Frontend Canister IDs.
The script will automatically build all configuration files, sync your YouTube catalog, upload metadata on-chain, and deploy your creator hub live to the Internet Computer mainnet!
📜 License
Distributed under the MIT License. See LICENSE for more information. Feel free to fork, adapt for your creator brand, and build upon it!
Built with passion on the Internet Computer Protocol.
