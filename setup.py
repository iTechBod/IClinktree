import os
import json
import subprocess
import sys

def get_principal():
    try:
        result = subprocess.run(['dfx', 'identity', 'get-principal'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except Exception:
        return "Unknown (Make sure dfx is installed and initialized)"

def main():
    print("🚀 ========================================================")
    print("      WEB3 CREATOR HUB - AUTOMATED SETUP WIZARD")
    print("======================================================== 🚀")
    
    principal = get_principal()
    print(f"\n🔑 Your DFINITY Principal ID: {principal}")
    print("⚠️  CRITICAL: Before deploying, make sure you add this Principal ID")
    print("    as a Controller to BOTH your Backend and Frontend canisters in the NNS!")
    
    input("\n👉 Press [Enter] once you have verified your canister controllers...")

    print("\n--- 1. Creator Profile Configuration ---")
    name = input("Enter your Creator Name (default: TechBod): ").strip() or "TechBod"
    bio = input("Enter your Bio / Subtitle (default: Exploring Technology & Web3 Architecture): ").strip() or "Exploring Technology & Web3 Architecture"
    yt_url = input("Enter your YouTube Channel Videos URL (default: https://www.youtube.com/@techbodam/videos):\n> ").strip() or "https://www.youtube.com/@techbodam/videos"

    print("\n--- 2. Social Media Links ---")
    socials = {
        "youtube": yt_url,
        "openchat": input("OpenChat Community URL:\n> ").strip() or "https://oc.app/community/vvj5y-nqaaa-aaaac-a77uq-cai/?ref=4voc2-7yaaa-aaaaf-bsado-pca",
        "telegram": input("Telegram Channel URL:\n> ").strip() or "https://t.me/techbod",
        "x": input("X (Twitter) URL:\n> ").strip() or "https://x.com/techbodam?s=21",
        "instagram": input("Instagram URL:\n> ").strip() or "https://www.instagram.com/techb0d?igsh=MWl0d3lvNmFpZjJrYw%3D%3D&utm_source=qr",
        "facebook": input("Facebook URL:\n> ").strip() or "https://www.facebook.com/share/12KCtgU5whP/?mibextid=wwXIfr",
        "discord": input("Discord Invite URL:\n> ").strip() or "https://discord.com/invite/PyWPGedY",
        "github": input("GitHub Profile URL:\n> ").strip() or "https://github.com/iTechBod",
        "tiktok": input("TikTok URL:\n> ").strip() or "https://www.tiktok.com/@techbod?_t=ZT-8tcJI3V27ZO&_r=1",
        "truthsocial": input("TruthSocial URL:\n> ").strip() or "https://truthsocial.com/@mahbod",
        "tumblr": input("Tumblr URL:\n> ").strip() or "https://www.tumblr.com/techbodam",
        "bluesky": input("Bluesky Profile URL:\n> ").strip() or "https://bsky.app/profile/techbod.bsky.social"
    }

    print("\n--- 3. Crypto Addresses & Coffee Support Setup ---")
    use_custom_crypto = input("Do you need to add your own crypto addresses for your website? (y/n) [default: n]: ").strip().lower()

    default_crypto = {
        "icp": {
            "id": "icp", "name": "ICP", "icon": "./images/$icp.svg",
            "addresses": [
                { "id": "icp-wallet", "label": "ICP Wallet / Account ID", "value": "4CvB6Yg68brVXv1JtkhV2jopMe7xDPKiEQm3WjutQn9j" },
                { "id": "icp-principal", "label": "Principal ID", "value": "57fkl-hfo3q-4sije-2dfvt-ikhqe-ti54q-ysccf-555lf-zc4bm-nykce-lae" }
            ]
        },
        "btc": {
            "id": "btc", "name": "BTC", "icon": "./images/btc.svg",
            "addresses": [{ "id": "btc-addr", "label": "Bitcoin", "value": "bc1qe57v3x9hkcz6z0ysmavnw2qh7lcy0jk82t3922" }]
        },
        "eth": {
            "id": "eth", "name": "ETH", "icon": "./images/eth.svg",
            "addresses": [{ "id": "eth-addr", "label": "Ethereum", "value": "0xCA3776676D5C787635beB5a6D3ceBEe3851E2F98" }]
        },
        "sol": {
            "id": "sol", "name": "SOL", "icon": "./images/sol.svg",
            "addresses": [{ "id": "sol-addr", "label": "Solana", "value": "4CvB6Yg68brVXv1JtkhV2jopMe7xDPKiEQm3WjutQn9j" }]
        },
        "xrp": {
            "id": "xrp", "name": "XRP", "icon": "./images/xrp.svg",
            "addresses": [{ "id": "xrp-addr", "label": "XRP", "value": "rHsxzgRzRPY7BVbdBo2Fdzs2p4QjiMPTwn" }]
        }
    }

    crypto_config = {}

    if use_custom_crypto == 'y':
        print("\nEnter your addresses below (press [Enter] on any prompt to leave blank / skip):")
        cust_icp_principal = input("  -> ICP Principal ID: ").strip()
        cust_icp_account = input("  -> ICP Account ID / Wallet ID: ").strip()
        cust_btc = input("  -> BTC Address: ").strip()
        cust_eth = input("  -> ETH Address: ").strip()
        cust_sol = input("  -> SOL Address: ").strip()
        cust_xrp = input("  -> XRP Address: ").strip()

        support_orig = input("\nDo you want to support the original website creator for any addresses you left blank? (y/n) [default: y]: ").strip().lower() != 'n'

        # Build ICP config
        icp_addrs = []
        if cust_icp_account:
            icp_addrs.append({ "id": "icp-wallet", "label": "ICP Wallet / Account ID", "value": cust_icp_account })
        elif support_orig:
            icp_addrs.append({ "id": "icp-wallet", "label": "ICP Wallet (Original Creator)", "value": default_crypto["icp"]["addresses"][0]["value"] })

        if cust_icp_principal:
            icp_addrs.append({ "id": "icp-principal", "label": "Principal ID", "value": cust_icp_principal })
        elif support_orig:
            icp_addrs.append({ "id": "icp-principal", "label": "Principal ID (Original Creator)", "value": default_crypto["icp"]["addresses"][1]["value"] })

        if icp_addrs:
            crypto_config["icp"] = { "id": "icp", "name": "ICP", "icon": "./images/$icp.svg", "addresses": icp_addrs }

        # Build BTC config
        if cust_btc:
            crypto_config["btc"] = { "id": "btc", "name": "BTC", "icon": "./images/btc.svg", "addresses": [{ "id": "btc-addr", "label": "Bitcoin", "value": cust_btc }] }
        elif support_orig:
            crypto_config["btc"] = { "id": "btc", "name": "BTC", "icon": "./images/btc.svg", "addresses": [{ "id": "btc-addr", "label": "Bitcoin (Original Creator)", "value": default_crypto["btc"]["addresses"][0]["value"] }] }

        # Build ETH config
        if cust_eth:
            crypto_config["eth"] = { "id": "eth", "name": "ETH", "icon": "./images/eth.svg", "addresses": [{ "id": "eth-addr", "label": "Ethereum", "value": cust_eth }] }
        elif support_orig:
            crypto_config["eth"] = { "id": "eth", "name": "ETH", "icon": "./images/eth.svg", "addresses": [{ "id": "eth-addr", "label": "Ethereum (Original Creator)", "value": default_crypto["eth"]["addresses"][0]["value"] }] }

        # Build SOL config
        if cust_sol:
            crypto_config["sol"] = { "id": "sol", "name": "SOL", "icon": "./images/sol.svg", "addresses": [{ "id": "sol-addr", "label": "Solana", "value": cust_sol }] }
        elif support_orig:
            crypto_config["sol"] = { "id": "sol", "name": "SOL", "icon": "./images/sol.svg", "addresses": [{ "id": "sol-addr", "label": "Solana (Original Creator)", "value": default_crypto["sol"]["addresses"][0]["value"] }] }

        # Build XRP config
        if cust_xrp:
            crypto_config["xrp"] = { "id": "xrp", "name": "XRP", "icon": "./images/xrp.svg", "addresses": [{ "id": "xrp-addr", "label": "XRP", "value": cust_xrp }] }
        elif support_orig:
            crypto_config["xrp"] = { "id": "xrp", "name": "XRP", "icon": "./images/xrp.svg", "addresses": [{ "id": "xrp-addr", "label": "XRP (Original Creator)", "value": default_crypto["xrp"]["addresses"][0]["value"] }] }
    else:
        # Use original creator addresses and label them accordingly
        crypto_config = default_crypto
        for coin in crypto_config:
            for addr in crypto_config[coin]["addresses"]:
                addr["label"] += " (Original Website Creator)"

    print("\n--- 4. Canister IDs ---")
    backend_id = input("Enter Backend Canister ID (default: v7c4r-xqaaa-aaaam-ad2ga-cai):\n> ").strip() or "v7c4r-xqaaa-aaaam-ad2ga-cai"
    frontend_id = input("Enter Frontend Canister ID (default: 2n2uw-uaaaa-aaaag-at2hq-cai):\n> ").strip() or "2n2uw-uaaaa-aaaag-at2hq-cai"

    # Create directories including assets/images
    os.makedirs("backend", exist_ok=True)
    os.makedirs("assets/images", exist_ok=True)

    # 1. Generate dfx.json
    print("\n📁 Generating dfx.json...")
    dfx_config = {
      "canisters": {
        "website": {
          "type": "assets",
          "source": ["assets"]
        },
        "backend": {
          "type": "motoko",
          "main": "backend/main.mo"
        }
      },
      "networks": {
        "local": {
          "bind": "127.0.0.1:4943"
        },
        "ic": {
          "providers": ["https://ic0.app"]
        }
      },
      "version": 1
    }
    with open("dfx.json", "w", encoding="utf-8") as f:
        json.dump(dfx_config, f, indent=2)

    # 2. Generate canister_ids.json
    print("📁 Generating canister_ids.json...")
    canister_ids = {
      "website": { "ic": frontend_id },
      "backend": { "ic": backend_id }
    }
    with open("canister_ids.json", "w", encoding="utf-8") as f:
        json.dump(canister_ids, f, indent=2)

    # 3. Generate backend/main.mo
    print("📁 Generating backend/main.mo...")
    main_mo_code = '''import Text "mo:base/Text";
import Array "mo:base/Array";
import Iter "mo:base/Iter";
import Nat "mo:base/Nat";
import Buffer "mo:base/Buffer";
import Timer "mo:base/Timer";
import Blob "mo:base/Blob";
import Time "mo:base/Time";

actor {
    public type VideoRecord = {
        title : Text;
        url : Text;
        description : Text;
        searchableText : Text;
    };

    public type ResponseItem = {
        title : Text;
        url : Text;
        description : Text;
    };

    public type DetailedVisitRecord = {
        timestamp : Time.Time;
        deviceId : Text;
        consent : Text;
        country : Text;
        device : Text;
        browser : Text;
        eventAction : ?Text;
    };

    public type TrafficStats = {
        totalVisits : Nat;
        uniqueVisitors : Nat;
        buttonClicks : Nat;
        countries : [Text];
        devices : [Text];
        browsers : [Text];
    };

    stable var videoLibrary : [VideoRecord] = [];
    stable var visitLogs : [DetailedVisitRecord] = [];

    let SEVEN_DAYS_NS : Time.Time = 604_800_000_000_000;

    func pruneOldVisits() {
        let now = Time.now();
        var validLogs = Buffer.Buffer<DetailedVisitRecord>(visitLogs.size());
        
        for (log in Iter.fromArray(visitLogs)) {
            if (now >= log.timestamp and (now - log.timestamp) <= SEVEN_DAYS_NS) {
                validLogs.add(log);
            }
        };
        visitLogs := Buffer.toArray(validLogs);
    };

    public shared func logVisit(
        deviceId : Text,
        consent : Text,
        country : Text,
        device : Text,
        browser : Text,
        eventAction : ?Text
    ) : async () {
        pruneOldVisits();
        let newRecord : DetailedVisitRecord = {
            timestamp = Time.now();
            deviceId = deviceId;
            consent = consent;
            country = country;
            device = device;
            browser = browser;
            eventAction = eventAction;
        };
        visitLogs := Array.append(visitLogs, [newRecord]);
    };

    public shared query func getTrafficStats() : async TrafficStats {
        pruneOldVisits();
        let now = Time.now();
        var activeLogs = Buffer.Buffer<DetailedVisitRecord>(20);
        var uniqueDevices = Buffer.Buffer<Text>(20);
        var countriesBuf = Buffer.Buffer<Text>(20);
        var devicesBuf = Buffer.Buffer<Text>(20);
        var browsersBuf = Buffer.Buffer<Text>(20);
        var clickCount : Nat = 0;

        for (log in Iter.fromArray(visitLogs)) {
            if (now >= log.timestamp and (now - log.timestamp) <= SEVEN_DAYS_NS) {
                activeLogs.add(log);

                var exists = false;
                for (dev in Iter.fromArray(Buffer.toArray(uniqueDevices))) {
                    if (dev == log.deviceId) { exists := true; };
                };
                if (not exists) {
                    uniqueDevices.add(log.deviceId);
                };

                countriesBuf.add(log.country);
                devicesBuf.add(log.device);
                browsersBuf.add(log.browser);

                switch (log.eventAction) {
                    case (?act) {
                        if (Text.startsWith(act, #text("click:"))) {
                            clickCount += 1;
                        };
                    };
                    case null {};
                };
            }
        };

        {
            totalVisits = activeLogs.size();
            uniqueVisitors = uniqueDevices.size();
            buttonClicks = clickCount;
            countries = Buffer.toArray(countriesBuf);
            devices = Buffer.toArray(devicesBuf);
            browsers = Buffer.toArray(browsersBuf);
        };
    };

    let synonymMap = [
        ("apple", ["mac", "macbook", "iphone", "ios", "اپل", "shortcuts"]),
        ("اپل", ["mac", "macbook", "iphone", "ios", "apple", "shortcuts"]),
        ("crypto", ["bitcoin", "ethereum", "blockchain", "بلاکچین", "کریپتو"]),
        ("icp", ["internet computer", "dfinity", "motoko", "sns", "nns", "canister"])
    ];

    func getSearchTargets(userText : Text) : [Text] {
        var targets = Buffer.Buffer<Text>(5);
        targets.add(userText);

        for (mapping in Iter.fromArray(synonymMap)) {
            if (Text.contains(userText, #text(mapping.0))) {
                for (synonym in Iter.fromArray(mapping.1)) {
                    targets.add(synonym);
                }
            }
        };
        return Buffer.toArray(targets);
    };

    public query func askBot(searchQuery : Text) : async [ResponseItem] {
        if (searchQuery == "") {
            return [];
        };

        let normalizedQuery = Text.toLowercase(searchQuery);
        let searchTargets = getSearchTargets(normalizedQuery);
        
        var matches = Buffer.Buffer<ResponseItem>(20);

        for (video in Iter.fromArray(videoLibrary)) {
            var isMatch = false;

            let fullText = Text.toLowercase(
                video.title # " " # video.description # " " # video.searchableText
            );

            for (target in Iter.fromArray(searchTargets)) {
                if (Text.contains(fullText, #text(target))) {
                    isMatch := true;
                }
            };

            if (isMatch) {
                matches.add({ 
                    title = video.title; 
                    url = video.url;
                    description = video.description;
                });
            }
        };

        let results = Buffer.toArray(matches);
        
        if (results.size() == 0) {
            return [{
                title = "Check out the latest on my channel!";
                url = "https://www.youtube.com/@techbodam";
                description = "I couldn't find a specific tutorial for that query, but you can browse all my videos directly on my channel."
            }];
        };

        if (results.size() > 6) {
            Array.tabulate<ResponseItem>(6, func(i) { results[i] })
        } else {
            results
        }
    };

    public shared func seedVideos(newVideos: [VideoRecord]) : async Nat {
        videoLibrary := Array.append(videoLibrary, newVideos);
        videoLibrary.size()
    };

    public shared func clearLibrary() : async () {
        videoLibrary := [];
    };

    public query func getAllVideos() : async [VideoRecord] {
        videoLibrary
    };

    ignore Timer.recurringTimer<system>(#seconds(21600), func() : async () {
        pruneOldVisits();
    });
}
'''
    with open("backend/main.mo", "w", encoding="utf-8") as f:
        f.write(main_mo_code)

    # 4. Generate assets/styles.css
    print("📁 Generating assets/styles.css...")
    styles_css_code = '''
:root {
  --bg-color: #030305;
  --text-primary: rgba(255, 255, 255, 0.98);
  --text-secondary: rgba(255, 255, 255, 0.6);
  --glass-bg: rgba(255, 255, 255, 0.05);
  --glass-border: rgba(255, 255, 255, 0.1);
  --safe-top: env(safe-area-inset-top, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  -webkit-tap-highlight-color: transparent;
}

body {
  background-color: var(--bg-color);
  color: var(--text-primary);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-x: hidden;
}

.ambient-glow, .ambient-glow-secondary {
  position: fixed;
  width: 350px;
  height: 350px;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.15;
  pointer-events: none;
  z-index: 0;
  transition: transform 0.3s cubic-bezier(0.25, 1, 0.5, 1);
}
.ambient-glow { top: -100px; left: -100px; background: #00bfff; }
.ambient-glow-secondary { bottom: -100px; right: -100px; background: #7928ca; }

#content-wrapper {
  width: 100%;
  max-width: 600px;
  padding: calc(80px + var(--safe-top)) 16px calc(80px + var(--safe-bottom));
  display: flex;
  flex-direction: column;
  gap: 24px;
  z-index: 1;
}

#icp-badge {
  position: fixed;
  top: max(16px, var(--safe-top));
  left: 50%;
  transform: translateX(-50%);
  z-index: 100;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 30px;
  text-decoration: none;
  color: var(--text-primary);
  font-size: 0.85rem;
  font-weight: 600;
  background: rgba(20, 20, 24, 0.9);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid var(--glass-border);
  cursor: pointer;
  touch-action: manipulation;
}

.icp-svg { width: 16px; height: 16px; }

#intro {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin: 0 auto;
}

.profile-container {
  width: 110px;
  height: 110px;
  margin: 0 auto 16px auto;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(255, 255, 255, 0.2);
  background: #111;
  display: flex;
  align-items: center;
  justify-content: center;
}

#techbod-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 25% center;
  transform: scale(1.45);
  display: block;
  margin: 0 auto;
}

h1 { font-size: 2rem; font-weight: 700; margin-bottom: 6px; text-align: center; }
.subtitle { font-size: 0.95rem; color: var(--text-secondary); text-align: center; }

.glass-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  padding: 16px;
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  cursor: pointer;
  touch-action: manipulation;
  transition: background 0.2s ease, transform 0.2s ease;
}
.glass-button:active { background: rgba(255, 255, 255, 0.18); }

.filter-pills {
  display: flex;
  gap: 6px;
  background: rgba(20, 20, 24, 0.8);
  padding: 4px;
  border-radius: 24px;
  border: 1px solid var(--glass-border);
  width: 100%;
}

.filter-btn {
  flex: 1;
  padding: 10px;
  border: none;
  background: transparent;
  color: var(--text-secondary);
  font-size: 0.85rem;
  font-weight: 500;
  border-radius: 20px;
  cursor: pointer;
  touch-action: manipulation;
  transition: all 0.2s ease;
}

.filter-btn.active {
  background: rgba(255, 255, 255, 0.15);
  color: var(--text-primary);
  font-weight: 600;
}

.grid-layout {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.glass-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px;
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  text-decoration: none;
  color: var(--text-primary);
  cursor: pointer;
  touch-action: manipulation;
  transition: transform 0.2s cubic-bezier(0.25, 1, 0.5, 1), background 0.2s ease;
}

.glass-card.filtered-out { display: none !important; }
.glass-card:active { background: rgba(255, 255, 255, 0.15); }

.card-left {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
}

.glass-card .icon, .tiktok-icon-wrap {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tiktok-icon-wrap svg { width: 28px; height: 28px; display: block; }
.glass-card .text { font-size: 0.9rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

.glass-banner {
  position: fixed;
  bottom: calc(80px + var(--safe-bottom));
  left: 16px;
  right: 16px;
  max-width: 500px;
  margin: 0 auto;
  background: rgba(20, 20, 24, 0.95);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  padding: 14px 18px;
  z-index: 1500;
  display: none;
}

.banner-content { display: flex; flex-direction: column; gap: 10px; font-size: 0.8rem; color: var(--text-secondary); }
.banner-actions { display: flex; gap: 10px; }
.btn-accept, .btn-decline { flex: 1; padding: 8px; border-radius: 8px; border: none; font-size: 0.8rem; font-weight: 600; cursor: pointer; }
.btn-accept { background: #00bfff; color: #000; }
.btn-decline { background: rgba(255, 255, 255, 0.1); color: var(--text-primary); }

.analytics-card {
  background: rgba(0, 0, 0, 0.45);
  border: 1px solid var(--glass-border);
  border-radius: 14px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 4px;
}

.analytics-header { font-weight: 700; font-size: 0.85rem; color: var(--text-primary); border-bottom: 1px solid var(--glass-border); padding-bottom: 6px; }
.analytics-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; text-align: center; }
.stat-item { background: rgba(255, 255, 255, 0.04); padding: 8px 4px; border-radius: 10px; border: 1px solid var(--glass-border); display: flex; flex-direction: column; }
.stat-val { font-size: 1.1rem; font-weight: 700; color: #00bfff; }
.stat-lbl { font-size: 0.6rem; color: var(--text-secondary); text-transform: uppercase; }
.analytics-breakdown { display: flex; flex-direction: column; gap: 4px; font-size: 0.75rem; color: var(--text-secondary); background: rgba(255, 255, 255, 0.02); padding: 8px 10px; border-radius: 8px; }

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  z-index: 2000;
  display: flex;
  align-items: flex-end;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
}
.modal-overlay.active { opacity: 1; pointer-events: all; }

.modal-content {
  width: 100%;
  background: #141418;
  border-top: 1px solid var(--glass-border);
  border-top-left-radius: 24px;
  border-top-right-radius: 24px;
  padding: 20px 16px calc(30px + var(--safe-bottom));
  max-height: 85vh;
  overflow-y: auto;
}

.modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
.close-btn { background: none; border: none; color: var(--text-secondary); font-size: 1.8rem; cursor: pointer; }

.crypto-tabs { display: flex; gap: 6px; margin-bottom: 16px; background: rgba(0,0,0,0.4); padding: 4px; border-radius: 12px; overflow-x: auto; }
.tab-btn { flex: 1; min-width: 70px; background: none; border: none; color: var(--text-secondary); padding: 10px 0; font-size: 0.85rem; font-weight: 600; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 6px; }
.tab-btn.active { background: rgba(255, 255, 255, 0.15); color: var(--text-primary); }
.tab-icon { width: 16px; height: 16px; border-radius: 50%; }

.crypto-card { background: rgba(255, 255, 255, 0.03); border: 1px solid var(--glass-border); border-radius: 14px; padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.qr-container { background: #fff; padding: 10px; border-radius: 10px; width: max-content; margin: 0 auto; }
.qr-box { width: 120px; height: 120px; }
.address-details { width: 100%; }
.address-label { font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 4px; }
.address-value { font-family: monospace; font-size: 0.8rem; word-break: break-all; background: rgba(0,0,0,0.5); padding: 10px; border-radius: 8px; margin-bottom: 10px; }
.copy-btn { width: 100%; padding: 12px; border-radius: 10px; border: 1px solid var(--glass-border); background: rgba(255, 255, 255, 0.1); color: var(--text-primary); font-weight: 600; cursor: pointer; }

#ai-chat-widget { position: fixed; bottom: calc(16px + var(--safe-bottom)); right: 16px; z-index: 1000; }
#ai-fab { width: 52px; height: 52px; border-radius: 50%; background: #141418; border: 1px solid var(--glass-border); color: var(--text-primary); font-size: 1.2rem; cursor: pointer; box-shadow: 0 4px 16px rgba(0,0,0,0.5); }

#ai-chat-panel {
  position: fixed;
  bottom: calc(80px + var(--safe-bottom));
  right: 16px; left: 16px; max-width: 400px; margin: 0 auto;
  background: #121215; border: 1px solid var(--glass-border); border-radius: 20px;
  display: flex; flex-direction: column; opacity: 0; pointer-events: none;
  transform: translateY(10px); transition: all 0.2s ease; box-shadow: 0 10px 30px rgba(0,0,0,0.7);
}
#ai-chat-panel.open { opacity: 1; pointer-events: all; transform: translateY(0); }

.chat-header { padding: 14px 16px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--glass-border); }
.chat-history { height: 250px; overflow-y: auto; padding: 12px; display: flex; flex-direction: column; gap: 10px; }
.chat-msg { padding: 10px 12px; border-radius: 12px; font-size: 0.85rem; max-width: 85%; word-break: break-word; }
.chat-msg.bot { background: rgba(255,255,255,0.08); align-self: flex-start; }
.chat-msg.user { background: rgba(0,191,255,0.2); align-self: flex-end; }

.chat-input-area { padding: 10px; display: flex; gap: 8px; border-top: 1px solid var(--glass-border); }
.chat-input-area input { flex: 1; background: none; border: none; color: var(--text-primary); padding: 8px; font-size: 0.9rem; outline: none; }
.chat-input-area button { background: rgba(255,255,255,0.1); border: 1px solid var(--glass-border); color: var(--text-primary); padding: 0 14px; border-radius: 10px; font-weight: 600; cursor: pointer; }

.video-card { background: rgba(0,0,0,0.3); border: 1px solid var(--glass-border); border-radius: 10px; padding: 10px; margin-top: 8px; }
.video-card h3 { font-size: 0.85rem; margin-bottom: 6px; }

.gradient-btn { display: block; background: #0A84FF; color: #fff; padding: 6px 12px; border-radius: 8px; text-decoration: none; font-size: 0.8rem; font-weight: 600; text-align: center; }

.toast-notification {
  position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%) translateY(50px);
  background: #2ed573; color: #000; padding: 10px 20px; border-radius: 20px;
  font-weight: 600; font-size: 0.85rem; opacity: 0; pointer-events: none; transition: all 0.2s ease; z-index: 3000;
}
.toast-notification.show { transform: translateX(-50%) translateY(0); opacity: 1; }
'''
    with open("assets/styles.css", "w", encoding="utf-8") as f:
        f.write(styles_css_code)

    # 5. Generate assets/script.js (injecting dynamic crypto_config JSON)
    print("📁 Generating assets/script.js...")
    script_js_template = '''const BACKEND_CANISTER_ID = '__BACKEND_ID__';

const CONFIG = {
  crypto: __CRYPTO_CONFIG__
};

function getOrCreateDeviceId() {
  let id = localStorage.getItem('tb_device_id');
  if (!id) {
    id = 'dev_' + Math.random().toString(36).substring(2, 11) + Date.now().toString(36);
    localStorage.setItem('tb_device_id', id);
  }
  return id;
}

function parseUserAgent() {
  const ua = navigator.userAgent;
  let device = 'Desktop';
  if (/mobile/i.test(ua)) device = 'Mobile';
  if (/iPad|Tablet/i.test(ua)) device = 'Tablet';

  let os = 'Unknown OS';
  if (ua.includes('Macintosh')) os = 'macOS';
  else if (ua.includes('iPhone') || ua.includes('iPad')) os = 'iOS';
  else if (ua.includes('Windows')) os = 'Windows';
  else if (ua.includes('Android')) os = 'Android';
  else if (ua.includes('Linux')) os = 'Linux';

  let browser = 'Unknown Browser';
  if (ua.includes('Chrome') && !ua.includes('Edg')) browser = 'Chrome';
  else if (ua.includes('Safari') && !ua.includes('Chrome')) browser = 'Safari';
  else if (ua.includes('Firefox')) browser = 'Firefox';
  else if (ua.includes('Edg')) browser = 'Edge';

  return { device: `${device} (${os})`, browser };
}

async function getCountryCode() {
  try {
    const cached = sessionStorage.getItem('tb_country');
    if (cached) return cached;
    const res = await fetch('https://ipapi.co/json/', { cache: 'force-cache', signal: AbortSignal.timeout(3000) });
    const data = await res.json();
    const country = data.country_name || data.country_code || 'Unknown';
    sessionStorage.setItem('tb_country', country);
    return country;
  } catch (e) {
    return 'Unknown';
  }
}

window.filterLinks = function(category, btn) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');

  document.querySelectorAll('.glass-card').forEach(card => {
    const cat = card.getAttribute('data-category');
    if (category === 'all' || cat === category) {
      card.classList.remove('filtered-out');
    } else {
      card.classList.add('filtered-out');
    }
  });
};

window.cryptoModal = {
  currentTab: Object.keys(CONFIG.crypto)[0] || 'icp',
  init() { this.renderTabs(); },
  open() {
    trackEvent('click:buy_coffee');
    document.getElementById('crypto-modal')?.classList.add('active');
    document.body.style.overflow = 'hidden';
    this.switchTab(this.currentTab);
  },
  close() {
    document.getElementById('crypto-modal')?.classList.remove('active');
    document.body.style.overflow = '';
  },
  renderTabs() {
    const container = document.getElementById('crypto-tabs');
    if (!container) return;
    container.innerHTML = '';
    Object.values(CONFIG.crypto).forEach(coin => {
      const btn = document.createElement('button');
      btn.className = `tab-btn ${coin.id === this.currentTab ? 'active' : ''}`;
      btn.onclick = () => this.switchTab(coin.id);
      btn.innerHTML = `<img src="${coin.icon}" class="tab-icon" onerror="this.style.display='none'"><span>${coin.name}</span>`;
      container.appendChild(btn);
    });
  },
  switchTab(coinId) {
    this.currentTab = coinId;
    this.renderTabs();
    const coinData = CONFIG.crypto[coinId];
    const body = document.getElementById('crypto-body');
    if (!body || !coinData) return;

    body.innerHTML = '';
    coinData.addresses.forEach((addr, i) => {
      const card = document.createElement('div');
      const qrId = `qr-${coinId}-${i}`;
      card.className = 'crypto-card';
      card.innerHTML = `
        <div class="qr-container"><div id="${qrId}" class="qr-box"></div></div>
        <div class="address-details">
          <div class="address-label">${addr.label}</div>
          <div class="address-value">${addr.value}</div>
          <button class="copy-btn" onclick="cryptoModal.copy('${addr.value}', '${addr.label}')">Copy Address</button>
        </div>
      `;
      body.appendChild(card);
      setTimeout(() => {
        const el = document.getElementById(qrId);
        if (el && typeof QRCode !== 'undefined') {
          new QRCode(el, { text: addr.value, width: 120, height: 120 });
        }
      }, 20);
    });
  },
  async copy(text, label) {
    try {
      await navigator.clipboard.writeText(text);
      trackEvent(`copy:${label}`);
      showToast(`${label} Copied!`);
    } catch {
      showToast('Failed to copy');
    }
  }
};

function showToast(msg) {
  const t = document.getElementById('toast');
  if (!t) return;
  t.innerText = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2000);
}

window.toggleChat = () => document.getElementById('ai-chat-panel')?.classList.toggle('open');
window.handleChatEnter = (e) => { if (e.key === 'Enter') window.sendQuery(); };

let backendActor = null;

async function getBackend() {
  if (backendActor) return backendActor;
  try {
    const mod = await import('https://esm.sh/@dfinity/agent?bundle');
    const agent = new mod.HttpAgent({ host: 'https://icp0.io' });
    backendActor = mod.Actor.createActor(({ IDL }) => IDL.Service({
      'askBot': IDL.Func([IDL.Text], [IDL.Vec(IDL.Record({ 'url' : IDL.Text, 'title' : IDL.Text, 'description' : IDL.Text }))], ['query']),
      'logVisit': IDL.Func([
        IDL.Text, IDL.Text, IDL.Text, IDL.Text, IDL.Text, IDL.Opt(IDL.Text)
      ], [], []),
      'getTrafficStats': IDL.Func([], [IDL.Record({
        'totalVisits' : IDL.Nat,
        'uniqueVisitors' : IDL.Nat,
        'buttonClicks' : IDL.Nat,
        'countries' : IDL.Vec(IDL.Text),
        'devices' : IDL.Vec(IDL.Text),
        'browsers' : IDL.Vec(IDL.Text)
      })], ['query'])
    }), { agent, canisterId: BACKEND_CANISTER_ID });
    return backendActor;
  } catch (e) {
    console.error("Backend connection error", e);
    return null;
  }
}

async function trackEvent(eventAction = 'pageview') {
  try {
    const backend = await getBackend();
    if (!backend) return;
    const deviceId = getOrCreateDeviceId();
    const consent = localStorage.getItem('traffic_consent') || 'ignored';
    const country = await getCountryCode();
    const meta = parseUserAgent();

    await backend.logVisit(
      deviceId,
      consent,
      country,
      meta.device,
      meta.browser,
      eventAction ? [eventAction] : []
    );
  } catch (err) {
    console.error("Traffic logging error", err);
  }
}

window.handleConsent = function(choice) {
  const banner = document.getElementById('traffic-consent-banner');
  if (banner) banner.style.display = 'none';
  localStorage.setItem('traffic_consent', choice);
  trackEvent('consent:' + choice);
};

function getTopItem(arr) {
  if (!arr || arr.length === 0) return 'None recorded';
  const counts = arr.reduce((acc, val) => { acc[val] = (acc[val] || 0) + 1; return acc; }, {});
  return Object.keys(counts).reduce((a, b) => counts[a] > counts[b] ? a : b);
}

window.sendQuery = async function() {
  const input = document.getElementById('chat-input');
  const history = document.getElementById('chat-history');
  if (!input || !history) return;
  const text = input.value.trim();
  if (!text) return;

  const userMsg = document.createElement('div');
  userMsg.className = 'chat-msg user';
  userMsg.innerText = text;
  history.appendChild(userMsg);
  input.value = '';
  history.scrollTop = history.scrollHeight;

  const botMsg = document.createElement('div');
  botMsg.className = 'chat-msg bot';
  botMsg.innerText = 'Searching...';
  history.appendChild(botMsg);
  history.scrollTop = history.scrollHeight;

  const lower = text.toLowerCase();
  
  if (lower.includes("how many people visited") || lower.includes("traffic") || lower.includes("stats") || lower.includes("visitor count")) {
    try {
      const backend = await getBackend();
      const stats = await backend.getTrafficStats();
      
      const topCountry = getTopItem(stats.countries);
      const topDevice = getTopItem(stats.devices);
      const topBrowser = getTopItem(stats.browsers);
      
      botMsg.innerHTML = `
        <div class="analytics-card">
          <div class="analytics-header">📊 7-Day Live Analytics</div>
          <div class="analytics-grid">
            <div class="stat-item">
              <span class="stat-val">${stats.totalVisits.toString()}</span>
              <span class="stat-lbl">Pageviews</span>
            </div>
            <div class="stat-item">
              <span class="stat-val">${stats.uniqueVisitors.toString()}</span>
              <span class="stat-lbl">Unique Users</span>
            </div>
            <div class="stat-item">
              <span class="stat-val">${stats.buttonClicks.toString()}</span>
              <span class="stat-lbl">Clicks</span>
            </div>
          </div>
          <div class="analytics-breakdown">
            <div>🌍 <strong>Top Country:</strong> ${topCountry}</div>
            <div>💻 <strong>Top Device/OS:</strong> ${topDevice}</div>
            <div>🌐 <strong>Top Browser:</strong> ${topBrowser}</div>
          </div>
        </div>
      `;
    } catch (e) {
      botMsg.innerText = "Couldn't fetch traffic stats right now.";
    }
    history.scrollTop = history.scrollHeight;
    return;
  }

  try {
    const backend = await getBackend();
    trackEvent(`search:${text}`);
    
    const results = await backend.askBot(text);
    botMsg.innerHTML = '';
    if (results && results.length > 0) {
      botMsg.innerHTML = '<div>Here are the best matching tutorials:</div>';
      results.forEach(item => {
        const card = document.createElement('div');
        card.className = 'video-card';
        card.innerHTML = `<h3>${item.title}</h3><p style="font-size:0.75rem; color:rgba(255,255,255,0.6); margin:4px 0 8px;">${item.description || ''}</p><a href="${item.url}" target="_blank" class="gradient-btn" onclick="trackEvent('click:watch_video')">Watch Video ↗</a>`;
        botMsg.appendChild(card);
      });
    } else {
      botMsg.innerText = 'No results found.';
    }
  } catch (err) {
    botMsg.innerText = 'Error loading results.';
  }
  history.scrollTop = history.scrollHeight;
};

document.addEventListener('DOMContentLoaded', () => {
  window.cryptoModal.init();
  trackEvent('pageview');

  const consent = localStorage.getItem('traffic_consent');
  if (!consent) {
    const banner = document.getElementById('traffic-consent-banner');
    if (banner) banner.style.display = 'block';
  }

  document.querySelectorAll('a.glass-card').forEach(link => {
    link.addEventListener('click', () => {
      const linkName = link.querySelector('.text')?.innerText || 'link';
      trackEvent(`click:${linkName.toLowerCase()}`);
    });
  });

  const glow1 = document.getElementById('glow-1');
  const glow2 = document.getElementById('glow-2');

  document.addEventListener('mousemove', (e) => {
    if (!glow1 || !glow2) return;
    const x = e.clientX / window.innerWidth;
    const y = e.clientY / window.innerHeight;
    glow1.style.transform = `translate(${x * 40}px, ${y * 40}px)`;
    glow2.style.transform = `translate(${-x * 40}px, ${-y * 40}px)`;
  });

  document.querySelectorAll('.magnetic-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      card.style.transform = `translate(${x * 0.08}px, ${y * 0.08}px) scale(1.015)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'translate(0px, 0px) scale(1)';
    });
  });
});
'''
    script_js_code = script_js_template.replace("__BACKEND_ID__", backend_id).replace("__CRYPTO_CONFIG__", json.dumps(crypto_config, indent=2))
    with open("assets/script.js", "w", encoding="utf-8") as f:
        f.write(script_js_code)

    # 6. Generate assets/index.html
    print("📁 Generating assets/index.html...")
    index_html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>__NAME__ | Creator Hub</title>
  <meta name="description" content="__BIO__">
  <meta name="theme-color" content="#030305">

  <link rel="shortcut icon" href="./images/techbod.png?v=4" type="image/png">
  <link rel="icon" type="image/png" sizes="32x32" href="./images/techbod.png?v=4">
  <link rel="icon" type="image/png" sizes="16x16" href="./images/techbod.png?v=4">
  <link rel="apple-touch-icon" sizes="180x180" href="./images/techbod.png?v=4">
  <link rel="apple-touch-icon" href="./images/techbod.png?v=4">

  <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <div class="ambient-glow" id="glow-1"></div>
  <div class="ambient-glow-secondary" id="glow-2"></div>

  <a href="https://internetcomputer.org/" target="_blank" rel="noopener noreferrer" id="icp-badge" class="glass-pill magnetic-card" aria-label="Built on the Internet Computer Protocol">
    <img src="./images/$icp.svg" alt="ICP" class="icp-svg">
    <span class="badge-text">Built on the Internet Computer Protocol</span>
  </a>

  <main id="content-wrapper">
    <header id="intro" class="reveal">
      <div class="profile-container">
        <div class="profile-crop">
          <img src="./images/techbod.png" alt="__NAME__ Profile" id="techbod-image" onerror="this.style.display='none'">
        </div>
        <div class="profile-ring"></div>
      </div>
      <h1>__NAME__</h1>
      <p class="subtitle">__BIO__</p>
    </header>

    <section class="reveal action-section">
      <button id="coffee-btn" class="glass-button primary magnetic-card" onclick="cryptoModal.open()">
        <span class="icon">☕</span>
        <span class="text">Buy Me a Coffee</span>
      </button>
    </section>

    <section class="reveal filter-section">
      <div class="filter-pills" role="tablist" aria-label="Category Filters">
        <button class="filter-btn active" data-filter="all" onclick="filterLinks('all', this)" role="tab" aria-selected="true">All Links</button>
        <button class="filter-btn" data-filter="social" onclick="filterLinks('social', this)" role="tab" aria-selected="false">Socials</button>
      </div>
    </section>

    <section class="reveal">
      <div id="unified-grid" class="grid-layout">
        <a href="__YOUTUBE__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/yt.png" alt="YouTube" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">YouTube</span>
          </div>
        </a>

        <a href="__OPENCHAT__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/oc.jpeg" alt="OpenChat" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">OpenChat</span>
          </div>
        </a>

        <a href="__TELEGRAM__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/tg.png" alt="Telegram" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">Telegram</span>
          </div>
        </a>

        <a href="__X__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/X.png" alt="X" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">X</span>
          </div>
        </a>

        <a href="__INSTAGRAM__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/ig.png" alt="Instagram" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">Instagram</span>
          </div>
        </a>

        <a href="__FACEBOOK__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/fb.png" alt="Facebook" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">Facebook</span>
          </div>
        </a>

        <a href="__DISCORD__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/discord.png" alt="Discord" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">Discord</span>
          </div>
        </a>

        <a href="__GITHUB__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/github.svg" alt="GitHub" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">GitHub</span>
          </div>
        </a>

        <a href="__TIKTOK__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <div class="icon tiktok-icon-wrap">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="12" fill="#000000"/>
                <path d="M16.6 8.2a4.5 4.5 0 0 1-2.8-1V4h-2.3v10.3a2.3 2.3 0 1 1-2.3-2.3c.3 0 .6 0 .9.1V9.8a4.6 4.6 0 1 0 3.7 4.5V9.4a6.8 6.8 0 0 0 4.2 1.4V8.5a4.5 4.5 0 0 1-1.4-.3z" fill="#25F4EE"/>
                <path d="M16.1 7.7a4.5 4.5 0 0 1-2.8-1V4h-2.3v10.3a2.3 2.3 0 1 1-2.3-2.3c.3 0 .6 0 .9.1V9.8a4.6 4.6 0 1 0 3.7 4.5V9.4a6.8 6.8 0 0 0 4.2 1.4V8.5a4.5 4.5 0 0 1-1.4-.3z" fill="#FE2C55"/>
              </svg>
            </div>
            <span class="text">TikTok</span>
          </div>
        </a>

        <a href="__TRUTHSOCIAL__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/ts.png" alt="TruthSocial" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">TruthSocial</span>
          </div>
        </a>

        <a href="__TUMBLR__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/tumblr.png" alt="Tumblr" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">Tumblr</span>
          </div>
        </a>

        <a href="__BLUESKY__" target="_blank" rel="noopener noreferrer" class="glass-card magnetic-card" data-category="social">
          <div class="card-left">
            <img src="./images/BS.png" alt="Bluesky" class="icon" onerror="this.src='./images/techbod.png'">
            <span class="text">Bluesky</span>
          </div>
        </a>
      </div>
    </section>
  </main>

  <footer class="reveal">
    <p>&copy; 2026 __NAME__. All rights reserved.</p>
  </footer>

  <div id="traffic-consent-banner" class="glass-banner">
    <div class="banner-content">
      <p>We use lightweight analytics to improve your experience. Data automatically expires in 7 days.</p>
      <div class="banner-actions">
        <button onclick="handleConsent('accepted')" class="btn-accept">Accept</button>
        <button onclick="handleConsent('declined')" class="btn-decline">Decline</button>
      </div>
    </div>
  </div>

  <div id="ai-chat-widget">
    <button id="ai-fab" class="glass-button magnetic-card" aria-label="Ask AI" onclick="toggleChat()">
      <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
    </button>
    
    <div id="ai-chat-panel" class="glass-panel" aria-hidden="true">
      <div class="chat-header">
        <h4>__NAME__ Assistant</h4>
        <button class="close-btn" onclick="toggleChat()">&times;</button>
      </div>
      <div id="chat-history" class="chat-history">
        <div class="chat-msg bot">Hi! Ask me anything about channel tutorials or type "traffic" for live metrics!</div>
      </div>
      <div class="chat-input-area">
        <input type="text" id="chat-input" dir="auto" placeholder="Search videos or type traffic..." onkeypress="handleChatEnter(event)">
        <button onclick="sendQuery()">
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M2 21l21-9L2 3v7l15 2-15 2v7z"/></svg>
        </button>
      </div>
    </div>
  </div>

  <div id="crypto-modal" class="modal-overlay" aria-hidden="true">
    <div class="modal-content glass-panel">
      <div class="modal-drag-handle"></div>
      <header class="modal-header">
        <h3>☕ Support __NAME__</h3>
        <button class="close-btn" onclick="cryptoModal.close()" aria-label="Close modal">&times;</button>
      </header>

      <div class="crypto-tabs" id="crypto-tabs"></div>
      <div id="crypto-body" class="crypto-body"></div>
    </div>
  </div>

  <div id="toast" class="toast-notification" aria-live="polite"></div>

  <script type="module" src="script.js"></script>
</body>
</html>
'''
    index_html_code = index_html_template.replace("__NAME__", name).replace("__BIO__", bio)
    for key, val in socials.items():
        index_html_code = index_html_code.replace(f"__{key.upper()}__", val)
    with open("assets/index.html", "w", encoding="utf-8") as f:
        f.write(index_html_code)

    # 7. Generate push.py
    print("📁 Generating push.py...")
    push_py_template = '''import json
import subprocess
import yt_dlp

def sanitize(text):
    if not text:
        return ""
    t = text.replace('\\\\', '\\\\\\\\')
    t = t.replace('"', '\\\\"')
    t = t.replace('\\n', ' ').replace('\\r', ' ')
    return t

channel_url = '__YOUTUBE_URL__'

ydl_opts = {
    'extract_flat': 'in_playlist',
    'skip_download': True,
    'ignoreerrors': True
}

print("Scraping all individual videos from your channel...")
video_database = []

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(channel_url, download=False)
    entries = info.get('entries', [])
    print(f"Found {len(entries)} video entries.")

    for entry in entries:
        if entry:
            vid_id = entry.get('id')
            title = sanitize(entry.get('title', ''))
            url = entry.get('url') if entry.get('url') else f"https://www.youtube.com/watch?v={vid_id}"
            description = sanitize(entry.get('description', ''))
            
            tags = entry.get('tags', []) or []
            tags_str = sanitize(" ".join(tags))

            searchable = f"{title} {tags_str} {description}".lower()

            video_database.append(
                f'record {{ title = "{title}"; url = "{url}"; description = "{description}"; searchableText = "{searchable}" }}'
            )

print(f"Formatted {len(video_database)} real videos.")

print("Clearing old canister library...")
subprocess.run(['dfx', 'canister', 'call', '--network', 'ic', 'backend', 'clearLibrary'], check=True)

chunk_size = 20
total_batches = (len(video_database) + chunk_size - 1) // chunk_size

for i in range(0, len(video_database), chunk_size):
    chunk = video_database[i:i + chunk_size]
    vec_content = "; ".join(chunk)
    candid_arg = f"(vec {{ {vec_content} }})"

    cmd = ['dfx', 'canister', 'call', '--network', 'ic', 'backend', 'seedVideos', candid_arg]

    print(f"Uploading batch {i // chunk_size + 1} of {total_batches}...")
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print("Batch uploaded successfully.")

print("All real videos successfully synced to your canister!")
'''
    push_py_code = push_py_template.replace("__YOUTUBE_URL__", socials['youtube'])
    with open("push.py", "w", encoding="utf-8") as f:
        f.write(push_py_code)

    print("\n✅ All project files successfully generated!")
    
    # 8. Run push.py
    print("\n🎥 Running push.py to scrape YouTube videos and seed canister...")
    subprocess.run([sys.executable, "push.py"], check=True)

    # 9. Run dfx deploy --network ic
    print("\n🚀 Deploying website assets and backend canister to Internet Computer Mainnet...")
    subprocess.run(["dfx", "deploy", "--network", "ic"], check=True)

    print("\n🎉 Setup Complete! Your Web3 Creator Hub is live on the Internet Computer!")

if __name__ == "__main__":
    main()
