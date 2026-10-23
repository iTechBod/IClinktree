# IClinktree
a Web3 (icp) alternative to Linktree!
# 🌐 Web3 Creator Hub

A high-performance, decentralized **Creator Hub & AI-Powered Video Knowledge Base** hosted 100% on-chain on the **Internet Computer Protocol (ICP)**. 

Featuring an Apple-inspired glassmorphism UI, real-time 7-day visitor analytics stored securely in a Motoko canister, an integrated cryptocurrency tipping modal with dynamic QR codes, and an on-chain semantic search assistant that indexes and retrieves YouTube tutorials instantly.

---

## ✨ Features

* **⚡ Fully On-Chain & Decentralized:** Hosted on Internet Computer asset and canister smart contracts with no centralized servers.
* **🤖 AI Tutorial Assistant:** Built-in semantic search query engine (`backend/main.mo`) that indexes your YouTube video library and answers user queries on-chain.
* **📊 Privacy-First Live Analytics:** Tracks 7-day rolling traffic stats (pageviews, unique visitors, button clicks, country, device, and browser breakdown) with automatic expiration and zero third-party cookies.
* **☕ Multi-Chain Crypto Tipping:** Support modal featuring dynamic QR generation for ICP, BTC, ETH, SOL, and XRP with customizable creator wallets.
* **🚀 Automated Setup & Deployment Wizard:** One script (`setup.py`) that scaffolds your entire project, scrapes your YouTube channel via `yt-dlp`, seeds your canister, and deploys to the ICP mainnet.

---

## 🛠️ Tech Stack

* **Blockchain:** Internet Computer Protocol (ICP)
* **Smart Contracts:** Motoko
* **Frontend:** HTML5, CSS3 (Glassmorphism), Vanilla JavaScript, QRious / QRCode.js
* **Automation & Scraping:** Python, `yt-dlp`, DFINITY `dfx` SDK

---

## 🚀 Getting Started & Deployment

Prerequisites:
* [DFINITY Dfx SDK](https://internetcomputer.org/docs/current/developer-docs/getting-started/install/) installed.
* Python 3 and `yt-dlp` (`pip install yt-dlp`) installed.

### 1. Clone the Repository
```bash
