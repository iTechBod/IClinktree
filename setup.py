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
    
    terminal_pid = get_principal()
    print(f"\n🔑 Your Terminal DFINITY Principal ID (Publisher/Sync PID): {terminal_pid}")

    print("\n--- 0. Internet Identity & Master PID Configuration ---")
    print("ℹ️  To manage and view secure incoming messages/tickets, you need a Master Principal ID.")
    print("    If you already deployed once, you can login with Internet Identity on your live site")
    print("    to copy your Principal ID (PID).")
    
    default_owner = terminal_pid if not terminal_pid.startswith("Unknown") else "YOUR-PRINCIPAL-ID-HERE"
    owner_principal = input(f"Enter your Master Principal ID for owner ticket access (default: {default_owner}):\n> ").strip() or default_owner

    # Publisher PID for push.py script syncing
    publisher_principal = terminal_pid if not terminal_pid.startswith("Unknown") else owner_principal

    print("\n--- 1. Ticket System & Expiration Configuration ---")
    enable_tickets = input("Do you want to enable the encrypted visitor ticket/messaging system? (y/n) [default: y]: ").strip().lower() != 'n'
    
    ticket_retention_days = 7
    if enable_tickets:
        days_input = input("How many days should the canister hold encrypted tickets before deleting them automatically? (default: 7):\n> ").strip()
        if days_input.isdigit():
            ticket_retention_days = int(days_input)

    # Convert retention days to nanoseconds for Motoko backend
    retention_ns = ticket_retention_days * 24 * 60 * 60 * 1_000_000_000

    print("\n⚠️  CRITICAL: Before deploying, make sure you add your Principal ID")
    print("    as a Controller to BOTH your Backend and Frontend canisters in the NNS!")
    
    input("\n👉 Press [Enter] once you have verified your canister controllers...")

    print("\n--- 2. Asset & Image Instructions ---")
    print("🖼️  NOTE: Make sure you place your profile photo in the 'assets/images/'")
    print("    directory and name it strictly 'techbod.png'.")
    print("    Also, ensure all social and crypto icons exist inside your local 'assets/images/' folder!\n")

    input("👉 Press [Enter] after verifying your images are in 'assets/images/'...")

    print("\n--- 3. Creator Profile Configuration ---")
    name = input("Enter your Creator Name (default: Creator): ").strip() or "Creator"
    bio = input("Enter your Bio / Subtitle (default: Exploring Technology & Web3 Architecture): ").strip() or "Exploring Technology & Web3 Architecture"
    yt_url = input("Enter your YouTube Channel Videos URL (default: https://www.youtube.com/@techbodam/videos):\n> ").strip() or "https://www.youtube.com/@techbodam/videos"

    # Default developer fallbacks
    default_socials = {
        "youtube": "https://www.youtube.com/@techbodam/videos",
        "openchat": "https://oc.app/community/vvj5y-nqaaa-aaaac-a77uq-cai/?ref=4voc2-7yaaa-aaaaf-bsado-pca",
        "telegram": "https://t.me/techbod",
        "x": "https://x.com/techbodam?s=21",
        "instagram": "https://www.instagram.com/techb0d?igsh=MWl0d3lvNmFpZjJrYw%3D%3D&utm_source=qr",
        "facebook": "https://www.facebook.com/share/12KCtgU5whP/?mibextid=wwXIfr",
        "discord": "https://discord.com/invite/PyWPGedY",
        "github": "https://github.com/iTechBod",
        "tiktok": "https://www.tiktok.com/@techbod?_t=ZT-8tcJI3V27ZO&_r=1",
        "truthsocial": "https://truthsocial.com/@mahbod",
        "tumblr": "https://www.tumblr.com/techbodam",
        "bluesky": "https://bsky.app/profile/techbod.bsky.social"
    }

    print("\n--- 4. Social Media Links ---")
    print("Enter your links below (leave blank to skip or use fallback):")
    raw_socials = {
        "youtube": yt_url,
        "openchat": input("OpenChat Community URL:\n> ").strip(),
        "telegram": input("Telegram Channel URL:\n> ").strip(),
        "x": input("X (Twitter) URL:\n> ").strip(),
        "instagram": input("Instagram URL:\n> ").strip(),
        "facebook": input("Facebook URL:\n> ").strip(),
        "discord": input("Discord Invite URL:\n> ").strip(),
        "github": input("GitHub Profile URL:\n> ").strip(),
        "tiktok": input("TikTok URL:\n> ").strip(),
        "truthsocial": input("TruthSocial URL:\n> ").strip(),
        "tumblr": input("Tumblr URL:\n> ").strip(),
        "bluesky": input("Bluesky Profile URL:\n> ").strip()
    }

    has_blank_socials = any(v == "" for v in raw_socials.values())
    support_socials = True
    if has_blank_socials:
        ans = input("\nDo you give permission to use the original dev's links for any blank/skipped social media? (y/n) [default: y]: ").strip().lower()
        support_socials = (ans != 'n')

    socials = {}
    for key, val in raw_socials.items():
        if val != "":
            socials[key] = val
        elif support_socials:
            socials[key] = default_socials[key]

    print("\n--- 5. ICP Ecosystem dApp Referrals ---")
    default_dapps = {
        "openchat": "https://oc.app/?ref=4voc2-7yaaa-aaaaf-bsado-pca",
        "clown": "https://clown.it.com/?ref=RZDcXG75KtmrD5w6vRjE3A",
        "oisy": "https://oisy.com/?referrer=943439452",
        "randseed": "https://randseed.org/?invite=81FO3"
    }

    raw_dapps = {
        "openchat": input("OpenChat Referral Link (leave blank to skip): ").strip(),
        "clown": input("Clown Referral Link (leave blank to skip): ").strip(),
        "oisy": input("Oisy Referral Link (leave blank to skip): ").strip(),
        "randseed": input("Randseed Referral Link (leave blank to skip): ").strip()
    }

    has_blank_dapps = any(v == "" for v in raw_dapps.values())
    support_dapps = True
    if has_blank_dapps:
        ans = input("\nDo you want to support original dev's referral links for any blank dApp fields? (y/n) [default: y]: ").strip().lower()
        support_dapps = (ans != 'n')

    dapps = {}
    for key, val in raw_dapps.items():
        if val != "":
            dapps[key] = val
        elif support_dapps:
            dapps[key] = default_dapps[key]

    print("\n--- 6. Crypto Addresses & Coffee Support Setup ---")
    use_custom_crypto = input("Do you need to add your own crypto addresses for your website? (y/n) [default: n]: ").strip().lower()

    default_crypto = {
        "icp": {
            "id": "icp", "name": "ICP", "icon": "./images/$icp.svg",
            "addresses": [
                { "id": "icp-wallet", "label": "ICP Wallet / Account ID", "value": "4CvB6Yg68brVXv1JtkhV2jopMe7xDPKiEQm3WjutQn9j" },
                { "id": "icp-principal", "label": "Principal ID", "value": owner_principal }
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
        cust_icp_principal = input("  -> ICP Principal ID: ").strip()
        cust_icp_account = input("  -> ICP Account ID / Wallet ID: ").strip()
        cust_btc = input("  -> BTC Address: ").strip()
        cust_eth = input("  -> ETH Address: ").strip()
        cust_sol = input("  -> SOL Address: ").strip()
        cust_xrp = input("  -> XRP Address: ").strip()

        support_crypto = input("\nDo you want to support original creator for blank crypto fields? (y/n) [default: y]: ").strip().lower() != 'n'

        icp_addrs = []
        if cust_icp_account:
            icp_addrs.append({ "id": "icp-wallet", "label": "ICP Wallet / Account ID", "value": cust_icp_account })
        elif support_crypto:
            icp_addrs.append({ "id": "icp-wallet", "label": "ICP Wallet (Original Creator)", "value": default_crypto["icp"]["addresses"][0]["value"] })

        if cust_icp_principal:
            icp_addrs.append({ "id": "icp-principal", "label": "Principal ID", "value": cust_icp_principal })
        elif support_crypto:
            icp_addrs.append({ "id": "icp-principal", "label": "Principal ID (Original Creator)", "value": default_crypto["icp"]["addresses"][1]["value"] })

        if icp_addrs:
            crypto_config["icp"] = { "id": "icp", "name": "ICP", "icon": "./images/$icp.svg", "addresses": icp_addrs }

        if cust_btc:
            crypto_config["btc"] = { "id": "btc", "name": "BTC", "icon": "./images/btc.svg", "addresses": [{ "id": "btc-addr", "label": "Bitcoin", "value": cust_btc }] }
        elif support_crypto:
            crypto_config["btc"] = default_crypto["btc"]

        if cust_eth:
            crypto_config["eth"] = { "id": "eth", "name": "ETH", "icon": "./images/eth.svg", "addresses": [{ "id": "eth-addr", "label": "Ethereum", "value": cust_eth }] }
        elif support_crypto:
            crypto_config["eth"] = default_crypto["eth"]

        if cust_sol:
            crypto_config["sol"] = { "id": "sol", "name": "SOL", "icon": "./images/sol.svg", "addresses": [{ "id": "sol-addr", "label": "Solana", "value": cust_sol }] }
        elif support_crypto:
            crypto_config["sol"] = default_crypto["sol"]

        if cust_xrp:
            crypto_config["xrp"] = { "id": "xrp", "name": "XRP", "icon": "./images/xrp.svg", "addresses": [{ "id": "xrp-addr", "label": "XRP", "value": cust_xrp }] }
        elif support_crypto:
            crypto_config["xrp"] = default_crypto["xrp"]
    else:
        crypto_config = default_crypto

    print("\n--- 7. Canister IDs ---")
    backend_id = input("Enter Backend Canister ID (default: v7c4r-xqaaa-aaaam-ad2ga-cai):\n> ").strip() or "v7c4r-xqaaa-aaaam-ad2ga-cai"
    frontend_id = input("Enter Frontend Canister ID (default: 2n2uw-uaaaa-aaaag-at2hq-cai):\n> ").strip() or "2n2uw-uaaaa-aaaag-at2hq-cai"

    os.makedirs("backend", exist_ok=True)
    os.makedirs("assets/images", exist_ok=True)

    # 1. Generate dfx.json
    print("\n📁 Generating dfx.json...")
    dfx_config = {
      "canisters": {
        "website": { "type": "assets", "source": ["assets"] },
        "backend": { "type": "motoko", "main": "backend/main.mo" }
      },
      "networks": {
        "local": { "bind": "127.0.0.1:4943" },
        "ic": { "providers": ["https://ic0.app"] }
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

    # 3. Generate backend/main.mo with dual OWNER + PUBLISHER sync principals
    print("📁 Generating backend/main.mo...")
    
    ticket_methods_mo = f'''
    public type Ticket = {{
        id : Nat;
        message : Text;
        created : Time.Time;
        read : Bool;
        archived : Bool;
    }};

    stable var tickets : [Ticket] = [];
    stable var nextTicketId : Nat = 1;
    let TICKET_RETENTION_NS : Time.Time = {retention_ns};

    func pruneOldTickets() {{
        let now = Time.now();
        var validTickets = Buffer.Buffer<Ticket>(tickets.size());
        var i = 0;
        while (i < tickets.size()) {{
            let t = tickets[i];
            if (now >= t.created and (now - t.created) <= TICKET_RETENTION_NS) {{
                validTickets.add(t);
            }};
            i += 1;
        }};
        tickets := Buffer.toArray(validTickets);
    }};

    public shared func submitTicket(ciphertextPayload : Text) : async ?Nat {{
        if (Text.size(ciphertextPayload) == 0 or Text.size(ciphertextPayload) > 1024) {{
            return null;
        }};
        pruneOldTickets();
        if (tickets.size() >= 200) {{
            return null;
        }};
        let assignedId = nextTicketId;
        let newTicket : Ticket = {{
            id = assignedId;
            message = ciphertextPayload;
            created = Time.now();
            read = false;
            archived = false;
        }};
        tickets := Array.append(tickets, [newTicket]);
        nextTicketId += 1;
        return ?assignedId;
    }};

    public shared (msg) func getTickets() : async ?[Ticket] {{
        if (not Principal.equal(msg.caller, OWNER)) {{
            return null;
        }};
        pruneOldTickets();
        return ?tickets;
    }};

    public shared (msg) func clearTickets() : async Bool {{
        if (not Principal.equal(msg.caller, OWNER)) return false;
        tickets := [];
        nextTicketId := 1;
        true
    }};

    public shared (msg) func markAllRead() : async Bool {{
        if (not Principal.equal(msg.caller, OWNER)) return false;
        pruneOldTickets();
        var updatedTickets = Buffer.Buffer<Ticket>(tickets.size());
        var i = 0;
        while (i < tickets.size()) {{
            let t = tickets[i];
            let modified : Ticket = {{ id = t.id; message = t.message; created = t.created; read = true; archived = t.archived }};
            updatedTickets.add(modified);
            i += 1;
        }};
        tickets := Buffer.toArray(updatedTickets);
        true
    }};

    public shared (msg) func markTicketRead(id : Nat, readStatus : Bool) : async Bool {{
        if (not Principal.equal(msg.caller, OWNER)) return false;
        pruneOldTickets();
        var found = false;
        var updatedTickets = Buffer.Buffer<Ticket>(tickets.size());
        var i = 0;
        while (i < tickets.size()) {{
            let t = tickets[i];
            if (t.id == id) {{
                found := true;
                let modified : Ticket = {{ id = t.id; message = t.message; created = t.created; read = readStatus; archived = t.archived }};
                updatedTickets.add(modified);
            }} else {{
                updatedTickets.add(t);
            }};
            i += 1;
        }};
        tickets := Buffer.toArray(updatedTickets);
        found
    }};

    public shared (msg) func deleteTicket(id : Nat) : async Bool {{
        if (not Principal.equal(msg.caller, OWNER)) return false;
        pruneOldTickets();
        var remaining = Buffer.Buffer<Ticket>(tickets.size());
        var deleted = false;
        var i = 0;
        while (i < tickets.size()) {{
            let t = tickets[i];
            if (t.id == id) {{
                deleted := true;
            }} else {{
                remaining.add(t);
            }};
            i += 1;
        }};
        tickets := Buffer.toArray(remaining);
        deleted
    }};'''

    main_mo_code = f'''import Text "mo:base/Text";
import Array "mo:base/Array";
import Iter "mo:base/Iter";
import Nat "mo:base/Nat";
import Buffer "mo:base/Buffer";
import Timer "mo:base/Timer";
import Time "mo:base/Time";
import Principal "mo:base/Principal";

actor {{
    let OWNER : Principal = Principal.fromText("{owner_principal}");
    let PUBLISHER : Principal = Principal.fromText("{publisher_principal}");

    let SEVEN_DAYS_NS : Time.Time = 604_800_000_000_000;
    let MAX_VISIT_LOGS : Nat = 50_000;

    public type VideoRecord = {{
        title : Text;
        url : Text;
        description : Text;
        searchableText : Text;
    }};

    public type ResponseItem = {{
        title : Text;
        url : Text;
        description : Text;
    }};

    public type DetailedVisitRecord = {{
        timestamp : Time.Time;
        deviceId : Text;
        consent : Text;
        country : Text;
        device : Text;
        browser : Text;
        eventAction : ?Text;
    }};

    public type CountedItem = {{
        name : Text;
        count : Nat;
    }};

    public type TrafficStats = {{
        pageViews : Nat;
        totalEvents : Nat;
        uniqueDevices : Nat;
        buttonClicks : Nat;
        topCountries : [CountedItem];
        topDevices : [CountedItem];
        topBrowsers : [CountedItem];
        topLinks : [CountedItem];
    }};

    stable var videoLibrary : [VideoRecord] = [];
    stable var visitLogs : [DetailedVisitRecord] = [];

    func pruneOldVisits() {{
        let now = Time.now();
        var validLogs = Buffer.Buffer<DetailedVisitRecord>(visitLogs.size());
        var i = 0;
        while (i < visitLogs.size()) {{
            let log = visitLogs[i];
            if (now >= log.timestamp and (now - log.timestamp) <= SEVEN_DAYS_NS) {{
                validLogs.add(log);
            }};
            i += 1;
        }};
        visitLogs := Buffer.toArray(validLogs);
    }};

    public shared (_msg) func logVisit(
        deviceId : Text,
        consent : Text,
        country : Text,
        device : Text,
        browser : Text,
        eventAction : ?Text
    ) : async () {{
        if (Text.size(deviceId) > 64) return;
        if (Text.size(country) > 64) return;
        if (Text.size(device) > 128) return;
        if (Text.size(browser) > 128) return;
        switch (eventAction) {{
            case (?act) {{ if (Text.size(act) > 128) return; }};
            case null {{}};
        }};

        if (visitLogs.size() >= MAX_VISIT_LOGS) {{
            pruneOldVisits();
            if (visitLogs.size() >= MAX_VISIT_LOGS) return;
        }};

        let newRecord : DetailedVisitRecord = {{
            timestamp = Time.now();
            deviceId = deviceId;
            consent = consent;
            country = country;
            device = device;
            browser = browser;
            eventAction = eventAction;
        }};
        visitLogs := Array.append(visitLogs, [newRecord]);
    }}{ticket_methods_mo}

    func tallyValues(values : [Text], topN : Nat) : [CountedItem] {{
        var uniqueNames : [Text] = [];
        var uniqueCounts : [Nat] = [];

        var idx = 0;
        while (idx < values.size()) {{
            let v = values[idx];
            var found = false;
            var k = 0;
            while (k < uniqueNames.size()) {{
                if (uniqueNames[k] == v) {{ found := true; }};
                k += 1;
            }};
            if (found) {{
                uniqueCounts := Array.tabulate<Nat>(uniqueCounts.size(), func(i : Nat) : Nat {{
                    if (uniqueNames[i] == v) {{ uniqueCounts[i] + 1 }} else {{ uniqueCounts[i] }}
                }});
            }} else {{
                uniqueNames := Array.append(uniqueNames, [v]);
                uniqueCounts := Array.append(uniqueCounts, [1]);
            }};
            idx += 1;
        }};

        var remaining = Array.tabulate<Nat>(uniqueNames.size(), func(i : Nat) : Nat {{ i }});
        let result = Buffer.Buffer<CountedItem>(topN);
        var taken : Nat = 0;

        while (taken < topN and taken < remaining.size()) {{
            var bestPos : Nat = 0;
            var bestCount : Nat = 0;
            var p = 0;
            while (p < remaining.size()) {{
                let idxy = remaining[p];
                if (p == 0 or uniqueCounts[idxy] > bestCount) {{
                    bestCount := uniqueCounts[idxy];
                    bestPos := p;
                }};
                p += 1;
            }};
            let bestIdx = remaining[bestPos];
            result.add({{ name = uniqueNames[bestIdx]; count = uniqueCounts[bestIdx] }});

            let newRem = Array.tabulate<Nat>(remaining.size() - 1, func(i : Nat) : Nat {{
                if (i < bestPos) {{ remaining[i] }} else {{ remaining[i + 1] }}
            }});
            remaining := newRem;
            taken += 1;
        }};

        Buffer.toArray(result)
    }};

    public shared query func getTrafficStats() : async TrafficStats {{
        let now = Time.now();
        var pageViews : Nat = 0;
        var totalEvents : Nat = 0;
        var clickCount : Nat = 0;

        let uniqueDevices = Buffer.Buffer<Text>(20);
        let countriesBuf = Buffer.Buffer<Text>(20);
        let devicesBuf   = Buffer.Buffer<Text>(20);
        let browsersBuf  = Buffer.Buffer<Text>(20);
        let linksBuf     = Buffer.Buffer<Text>(20);

        var i = 0;
        while (i < visitLogs.size()) {{
            let log = visitLogs[i];
            if (now >= log.timestamp and (now - log.timestamp) <= SEVEN_DAYS_NS) {{
                totalEvents += 1;

                var exists = false;
                var d = 0;
                let uDevs = Buffer.toArray(uniqueDevices);
                while (d < uDevs.size()) {{
                    if (uDevs[d] == log.deviceId) {{ exists := true; }};
                    d += 1;
                }};
                if (not exists) {{ uniqueDevices.add(log.deviceId); }};

                switch (log.eventAction) {{
                    case null {{
                        pageViews += 1;
                        countriesBuf.add(log.country);
                        devicesBuf.add(log.device);
                        browsersBuf.add(log.browser);
                    }};
                    case (?act) {{
                        if (act == "pageview") {{
                            pageViews += 1;
                        }} else if (Text.startsWith(act, #text("click:"))) {{
                            clickCount += 1;
                            linksBuf.add(act);
                        }};
                    }};
                }};
            }};
            i += 1;
        }};

        {{
            pageViews = pageViews;
            totalEvents = totalEvents;
            uniqueDevices = uniqueDevices.size();
            buttonClicks = clickCount;
            topCountries = tallyValues(Buffer.toArray(countriesBuf), 5);
            topDevices   = tallyValues(Buffer.toArray(devicesBuf), 5);
            topBrowsers  = tallyValues(Buffer.toArray(browsersBuf), 5);
            topLinks     = tallyValues(Buffer.toArray(linksBuf), 5);
        }};
    }};

    let synonymMap : [(Text, [Text])] = [
        ("apple", ["mac", "macbook", "iphone", "ios", "shortcuts"]),
        ("اپل", ["mac", "macbook", "iphone", "ios", "apple", "shortcuts"]),
        ("crypto", ["bitcoin", "ethereum", "blockchain", "کریپتو"]),
        ("icp", ["internet computer", "dfinity", "motoko", "sns", "nns", "canister"])
    ];

    func getSearchTargets(userText : Text) : [Text] {{
        var targets = Buffer.Buffer<Text>(5);
        targets.add(userText);

        var i = 0;
        while (i < synonymMap.size()) {{
            let item = synonymMap[i];
            let key = item.0;
            let synonyms = item.1;
            if (Text.contains(userText, #text(key))) {{
                var s = 0;
                while (s < synonyms.size()) {{
                    targets.add(synonyms[s]);
                    s += 1;
                }};
            }};
            i += 1;
        }};
        return Buffer.toArray(targets);
    }};

    public query func askBot(searchQuery : Text) : async [ResponseItem] {{
        if (searchQuery == "") {{
            return [];
        }};

        let normalizedQuery = Text.toLowercase(searchQuery);
        let searchTargets = getSearchTargets(normalizedQuery);

        var scoredMatches = Buffer.Buffer<({{ score : Nat; item : ResponseItem }})>(20);

        var i = 0;
        while (i < videoLibrary.size()) {{
            let video = videoLibrary[i];
            var score : Nat = 0;
            let titleLower = Text.toLowercase(video.title);
            let descLower = Text.toLowercase(video.description);
            let fullText = titleLower # " " # descLower # " " # Text.toLowercase(video.searchableText);

            var tIdx = 0;
            while (tIdx < searchTargets.size()) {{
                let target = searchTargets[tIdx];
                if (Text.contains(titleLower, #text(target))) {{
                    score += 5;
                }} else if (Text.contains(descLower, #text(target))) {{
                    score += 2;
                }} else if (Text.contains(fullText, #text(target))) {{
                    score += 1;
                }};
                tIdx += 1;
            }};

            if (score > 0) {{
                scoredMatches.add({{
                    score = score;
                    item = {{
                        title = video.title;
                        url = video.url;
                        description = video.description;
                    }};
                }};
            }};
            i += 1;
        }};

        var allMatches = Buffer.toArray(scoredMatches);
        var sortedBuffer = Buffer.Buffer<({{ score : Nat; item : ResponseItem }})>(allMatches.size());
        var remainingMatches = Buffer.Buffer<({{ score : Nat; item : ResponseItem }})>(allMatches.size());
        var rIdx = 0;
        while (rIdx < allMatches.size()) {{
            remainingMatches.add(allMatches[rIdx]);
            rIdx += 1;
        }};

        label myloop while (sortedBuffer.size() < allMatches.size() and remainingMatches.size() > 0) {{
            var bestIdx : ?Nat = null;
            var bestScore : Nat = 0;
            var sIdx = 0;
            let currentRem = Buffer.toArray(remainingMatches);
            while (sIdx < currentRem.size()) {{
                let candidate = currentRem[sIdx];
                if (bestIdx == null or candidate.score > bestScore) {{
                    bestScore := candidate.score;
                    bestIdx := ?sIdx;
                }};
                sIdx += 1;
            }};

            switch (bestIdx) {{
                case (?bi) {{
                    let chosen = currentRem[bi];
                    sortedBuffer.add(chosen);
                    var newRem = Buffer.Buffer<({{ score : Nat; item : ResponseItem }})>(currentRem.size() - 1);
                    var skipIdx = 0;
                    while (skipIdx < currentRem.size()) {{
                        if (skipIdx != bi) {{
                            newRem.add(currentRem[skipIdx]);
                        }};
                        skipIdx += 1;
                    }};
                    remainingMatches := newRem;
                }};
                case null {{
                    break myloop;
                }};
            }};
        }};

        let finalSorted = Buffer.toArray(sortedBuffer);
        let limit = if (finalSorted.size() > 6) 6 else finalSorted.size();
        Array.tabulate<ResponseItem>(limit, func(idx : Nat) : ResponseItem {{
            finalSorted[idx].item
        }});
    }};

    public shared (msg) func seedVideos(newVideos: [VideoRecord]) : async Nat {{
        let isAuthorized = Principal.equal(msg.caller, OWNER) or Principal.equal(msg.caller, PUBLISHER);
        assert isAuthorized;
        videoLibrary := Array.append(videoLibrary, newVideos);
        videoLibrary.size()
    }};

    public shared (msg) func clearLibrary() : async () {{
        let isAuthorized = Principal.equal(msg.caller, OWNER) or Principal.equal(msg.caller, PUBLISHER);
        assert isAuthorized;
        videoLibrary := [];
    }};

    public query func getAllVideos() : async [VideoRecord] {{
        videoLibrary
    }};

    ignore Timer.recurringTimer<system>(#seconds(21600), func() : async () {{
        pruneOldVisits();
        pruneOldTickets();
    }};
}}
'''

    with open("backend/main.mo", "w", encoding="utf-8") as f:
        f.write(main_mo_code)

    print("\n📁 Generating assets/script.js with client-side E2EE tickets...")
    script_js_content = '''import { Actor, HttpAgent } from 'https://esm.sh/@dfinity/agent@0.21.4?bundle';
import { AuthClient } from 'https://esm.sh/@dfinity/auth-client@0.21.4?bundle';

const BACKEND_CANISTER_ID = '__BACKEND_ID__';
const OWNER_PRINCIPAL = '__OWNER_PRINCIPAL__';

const CONFIG = {
  crypto: __CRYPTO_CONFIG__
};

let authClient = null;
let lastTrackTime = 0;
let isSending = false;

async function encryptMessage(plaintext) {
  const enc = new TextEncoder();
  const key = await crypto.subtle.generateKey(
    { name: 'AES-GCM', length: 256 },
    true,
    ['encrypt', 'decrypt']
  );
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const ciphertext = await crypto.subtle.encrypt(
    { name: 'AES-GCM', iv },
    key,
    enc.encode(plaintext)
  );
  const exportedKey = await crypto.subtle.exportKey('raw', key);
  
  const combined = new Uint8Array(exportedKey.byteLength + iv.byteLength + ciphertext.byteLength);
  combined.set(new Uint8Array(exportedKey), 0);
  combined.set(iv, exportedKey.byteLength);
  combined.set(new Uint8Array(ciphertext), exportedKey.byteLength + iv.byteLength);
  
  return btoa(String.fromCharCode(...combined));
}

async function decryptMessage(payloadB64) {
  try {
    const raw = Uint8Array.from(atob(payloadB64), c => c.charCodeAt(0));
    const rawKey = raw.slice(0, 32);
    const iv = raw.slice(32, 44);
    const ciphertext = raw.slice(44);

    const key = await crypto.subtle.importKey(
      'raw',
      rawKey,
      { name: 'AES-GCM', length: 256 },
      false,
      ['decrypt']
    );

    const decrypted = await crypto.subtle.decrypt(
      { name: 'AES-GCM', iv },
      key,
      ciphertext
    );
    return new TextDecoder().decode(decrypted);
  } catch (e) {
    return "[Encrypted Ticket / Unable to Decrypt]";
  }
}

async function getAuthClient() {
  if (!authClient) {
    authClient = await AuthClient.create();
  }
  return authClient;
}

async function getBackend(isAuthenticated = false) {
  try {
    const agentOptions = { host: 'https://icp0.io' };
    if (isAuthenticated) {
      const client = await getAuthClient();
      if (await client.isAuthenticated()) {
        agentOptions.identity = client.getIdentity();
      }
    }
    const agent = new HttpAgent(agentOptions);
    await agent.fetchRootKey().catch(() => {});

    return Actor.createActor(({ IDL }) => {
      const CountedItem = IDL.Record({ 'name': IDL.Text, 'count': IDL.Nat });
      const Ticket = IDL.Record({
        'id': IDL.Nat,
        'message': IDL.Text,
        'created': IDL.Int,
        'read': IDL.Bool,
        'archived': IDL.Bool
      });
      return IDL.Service({
        'askBot': IDL.Func([IDL.Text], [IDL.Vec(IDL.Record({ 'url' : IDL.Text, 'title' : IDL.Text, 'description' : IDL.Text }))], ['query']),
        'logVisit': IDL.Func([IDL.Text, IDL.Text, IDL.Text, IDL.Text, IDL.Text, IDL.Opt(IDL.Text)], [], []),
        'getTrafficStats': IDL.Func([], [IDL.Record({
          'pageViews' : IDL.Nat,
          'totalEvents' : IDL.Nat,
          'uniqueDevices' : IDL.Nat,
          'buttonClicks' : IDL.Nat,
          'topCountries' : IDL.Vec(CountedItem),
          'topDevices' : IDL.Vec(CountedItem),
          'topBrowsers' : IDL.Vec(CountedItem),
          'topLinks' : IDL.Vec(CountedItem)
        })], ['query']),
        'submitTicket': IDL.Func([IDL.Text], [IDL.Opt(IDL.Nat)], []),
        'getTickets': IDL.Func([], [IDL.Opt(IDL.Vec(Ticket))], []),
        'clearTickets': IDL.Func([], [IDL.Bool], []),
        'markAllRead': IDL.Func([], [IDL.Bool], []),
        'getMyPrincipal': IDL.Func([], [IDL.Text], ['query']),
        'markTicketRead': IDL.Func([IDL.Nat, IDL.Bool], [IDL.Bool], []),
        'archiveTicket': IDL.Func([IDL.Nat, IDL.Bool], [IDL.Bool], []),
        'deleteTicket': IDL.Func([IDL.Nat], [IDL.Bool], [])
      });
    }, { agent, canisterId: BACKEND_CANISTER_ID });
  } catch (e) {
    console.error("Backend connection error", e);
    return null;
  }
}

function shouldTrack() {
  return localStorage.getItem('traffic_consent') === 'accepted';
}

function getOrCreateDeviceId() {
  if (!shouldTrack()) return null;
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
  if (/iPad|Tablet/i.test(ua) || (navigator.maxTouchPoints > 1 && /Macintosh/.test(ua))) device = 'Tablet';

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
  if (!shouldTrack()) return 'Unknown';
  try {
    const cached = localStorage.getItem('tb_country');
    if (cached) return cached;
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 3000);
    const res = await fetch('https://api.country.is/', { signal: controller.signal });
    clearTimeout(timeoutId);
    const data = await res.json();
    const country = data.country || 'Unknown';
    localStorage.setItem('tb_country', country);
    return country;
  } catch (e) {
    return 'Unknown';
  }
}

window.filterLinks = function(category, btn) {
  document.querySelectorAll('.filter-btn').forEach(b => {
    b.classList.remove('active');
    b.setAttribute('aria-selected', 'false');
  });
  if (btn) {
    btn.classList.add('active');
    btn.setAttribute('aria-selected', 'true');
  }

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
  currentTab: localStorage.getItem('tb_crypto_tab') || Object.keys(CONFIG.crypto)[0] || 'icp',
  init() { this.renderTabs(); },
  open() {
    trackEvent('click:buy_coffee');
    const modal = document.getElementById('crypto-modal');
    modal?.classList.add('active');
    modal?.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    this.switchTab(this.currentTab);
  },
  close() {
    const modal = document.getElementById('crypto-modal');
    modal?.classList.remove('active');
    modal?.setAttribute('aria-hidden', 'true');
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
      
      const img = document.createElement('img');
      img.src = coin.icon;
      img.className = 'tab-icon';
      img.onerror = function() { this.style.display = 'none'; };
      
      const span = document.createElement('span');
      span.textContent = coin.name;

      btn.appendChild(img);
      btn.appendChild(span);
      container.appendChild(btn);
    });
  },
  switchTab(coinId) {
    this.currentTab = coinId;
    localStorage.setItem('tb_crypto_tab', coinId);
    this.renderTabs();
    const coinData = CONFIG.crypto[coinId];
    const body = document.getElementById('crypto-body');
    if (!body || !coinData) return;

    body.innerHTML = '';
    coinData.addresses.forEach((addr, i) => {
      const card = document.createElement('div');
      const qrId = `qr-${coinId}-${i}`;
      card.className = 'crypto-card';
      
      const qrContainer = document.createElement('div');
      qrContainer.className = 'qr-container';
      const qrBox = document.createElement('div');
      qrBox.id = qrId;
      qrBox.className = 'qr-box';
      qrContainer.appendChild(qrBox);

      const details = document.createElement('div');
      details.className = 'address-details';

      const labelDiv = document.createElement('div');
      labelDiv.className = 'address-label';
      labelDiv.textContent = addr.label;

      const valDiv = document.createElement('div');
      valDiv.className = 'address-value';
      valDiv.textContent = addr.value;
      valDiv.title = 'Click to copy address';
      valDiv.onclick = () => cryptoModal.copy(addr.value, addr.label);

      const copyBtn = document.createElement('button');
      copyBtn.className = 'copy-btn';
      copyBtn.textContent = 'Copy Address';
      copyBtn.onclick = () => cryptoModal.copy(addr.value, addr.label);

      details.appendChild(labelDiv);
      details.appendChild(valDiv);
      details.appendChild(copyBtn);

      card.appendChild(qrContainer);
      card.appendChild(details);
      body.appendChild(card);

      setTimeout(() => {
        const el = document.getElementById(qrId);
        if (el) {
          el.innerHTML = '';
          const img = document.createElement('img');
          img.src = `https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=${encodeURIComponent(addr.value)}`;
          img.width = 120;
          img.height = 120;
          img.style.display = 'block';
          img.style.borderRadius = '4px';
          el.appendChild(img);
        }
      }, 20);
    });
  },
  async copy(text, label) {
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(text);
      } else {
        const textArea = document.createElement("textarea");
        textArea.value = text;
        textArea.style.position = "fixed";
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
      }
      trackEvent(`copy:${label}`);
      showToast(`${label} Copied!`);
    } catch {
      showToast('Failed to copy. Please select manually.');
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

window.toggleChat = () => {
  const panel = document.getElementById('ai-chat-panel');
  const isOpen = panel?.classList.toggle('open');
  panel?.setAttribute('aria-hidden', isOpen ? 'false' : 'true');
  if (isOpen) {
    document.getElementById('chat-input')?.focus();
  }
};

window.handleChatEnter = (e) => { if (e.key === 'Enter') window.sendQuery(); };

window.triggerIILogin = async function() {
  const history = document.getElementById('chat-history');
  if (!history) return;

  const botMsg = document.createElement('div');
  botMsg.className = 'chat-msg bot';
  history.appendChild(botMsg);
  history.scrollTop = history.scrollHeight;

  try {
    const client = await getAuthClient();
    
    if (await client.isAuthenticated()) {
      await client.logout();
    }

    botMsg.textContent = 'Connecting to Internet Identity...';

    await client.login({
      identityProvider: 'https://identity.ic0.app/#authorize',
      onSuccess: async () => {
        const identity = client.getIdentity();
        const principalText = identity.getPrincipal().toText();
        
        botMsg.textContent = '';
        const authDiv = document.createElement('div');
        authDiv.style.display = 'flex';
        authDiv.style.flexDirection = 'column';
        authDiv.style.gap = '8px';
        
        authDiv.innerHTML = `<strong>✅ Logged in successfully!</strong><br>Your Internet Identity Principal ID (PID):`;
        
        const inputPid = document.createElement('input');
        inputPid.type = 'text';
        inputPid.readOnly = true;
        inputPid.value = principalText;
        inputPid.style.cssText = 'font-family:monospace; font-size:0.75rem; padding:8px; background:rgba(0,0,0,0.5); border:1px solid var(--glass-border); border-radius:8px; color:#00bfff; width:100%; cursor:pointer;';
        inputPid.onclick = () => { inputPid.select(); navigator.clipboard.writeText(principalText); showToast('PID Copied to Clipboard!'); };
        
        authDiv.appendChild(inputPid);
        authDiv.appendChild(document.createTextNode('Click the box to copy your PID and send it over!'));
        botMsg.appendChild(authDiv);
        history.scrollTop = history.scrollHeight;
      },
      onError: (err) => {
        botMsg.textContent = `Login failed or cancelled: ${err || 'Unknown error'}`;
      }
    });
  } catch (e) {
    botMsg.textContent = `Auth error: ${e.message || e}`;
  }
};

window.sendQuery = async function(presetText = null) {
  if (isSending) return;
  const input = document.getElementById('chat-input');
  const history = document.getElementById('chat-history');
  if (!input || !history) return;
  const text = presetText !== null ? presetText : input.value.trim();
  if (!text) return;

  isSending = true;
  const sendBtn = document.querySelector('.chat-input-area button');
  if (sendBtn) sendBtn.disabled = true;

  const userMsg = document.createElement('div');
  userMsg.className = 'chat-msg user';
  userMsg.textContent = text;
  history.appendChild(userMsg);
  if (presetText === null) input.value = '';
  history.scrollTop = history.scrollHeight;

  const botMsg = document.createElement('div');
  botMsg.className = 'chat-msg bot';
  botMsg.textContent = 'Thinking...';
  history.appendChild(botMsg);
  history.scrollTop = history.scrollHeight;

  const lower = text.toLowerCase().trim();

  if (lower.startsWith('ticket ') || lower.startsWith('تیکت ')) {
    const messageContent = text.replace(/^(ticket|تیکت)\s+/i, '').trim();
    if (!messageContent) {
      botMsg.textContent = "Please include a message after 'ticket' or 'تیکت'. Example: ticket Can you cover Oisy wallet?";
      isSending = false;
      if (sendBtn) sendBtn.disabled = false;
      return;
    }
    try {
      botMsg.textContent = 'Encrypting message end-to-end...';
      const encryptedPayload = await encryptMessage(messageContent);
      const backend = await getBackend(false);
      const resId = await backend.submitTicket(encryptedPayload);
      if (resId !== null && resId !== undefined) {
        botMsg.textContent = `🔒 Encrypted anonymous ticket sent successfully! Reference ID: #${resId.toString()}`;
      } else {
        botMsg.textContent = "❌ Failed to send ticket. Message may be too long or inbox is full.";
      }
    } catch (e) {
      botMsg.textContent = `Error sending encrypted ticket: ${e.message || 'Network error'}`;
    }
    history.scrollTop = history.scrollHeight;
    isSending = false;
    if (sendBtn) sendBtn.disabled = false;
    setTimeout(() => { lastTrackTime = Date.now(); }, 1000);
    return;
  }

  if (lower === 'show tickets' || lower === 'show unread') {
    try {
      const client = await getAuthClient();
      if (!await client.isAuthenticated()) {
        botMsg.textContent = '';
        const authDiv = document.createElement('div');
        authDiv.innerHTML = `🔒 Owner access requires authentication.<br><br>`;
        const loginBtn = document.createElement('button');
        loginBtn.className = 'gradient-btn';
        loginBtn.style.marginTop = '6px';
        loginBtn.textContent = 'Login with Internet Identity';
        loginBtn.onclick = () => window.triggerIILogin();
        authDiv.appendChild(loginBtn);
        botMsg.appendChild(authDiv);
        isSending = false;
        if (sendBtn) sendBtn.disabled = false;
        return;
      }

      const backend = await getBackend(true);
      const identity = client.getIdentity();
      const currentPrincipal = identity.getPrincipal().toText();
      
      if (currentPrincipal !== OWNER_PRINCIPAL) {
        botMsg.textContent = `⛔ Unauthorized: Logged-in Principal (${currentPrincipal.substring(0, 8)}...) does not match the owner principal.`;
        isSending = false;
        if (sendBtn) sendBtn.disabled = false;
        return;
      }

      botMsg.textContent = 'Fetching and decrypting tickets...';
      const ticketsOpt = await backend.getTickets();
      if (ticketsOpt === null || ticketsOpt === undefined) {
        botMsg.textContent = "Unauthorized: Your current Internet Identity principal is not authorized as the owner.";
      } else {
        const rawTickets = Array.isArray(ticketsOpt) ? (ticketsOpt[0] || []) : ticketsOpt;
        const tickets = Array.isArray(rawTickets) ? rawTickets : [];
        
        botMsg.textContent = '';
        
        const headerWrap = document.createElement('div');
        headerWrap.style.cssText = 'display:flex; flex-direction:column; gap:8px; margin-bottom:8px;';

        const topRow = document.createElement('div');
        topRow.style.cssText = 'display:flex; justify-content:space-between; align-items:center;';
        
        const titleStrong = document.createElement('strong');
        titleStrong.innerHTML = `📬 Decrypted Inbox (${tickets.length})`;
        topRow.appendChild(titleStrong);

        if (tickets.length > 0) {
          const actionRow = document.createElement('div');
          actionRow.style.cssText = 'display:flex; gap:6px;';

          const markAllBtn = document.createElement('button');
          markAllBtn.className = 'ticket-action-btn';
          markAllBtn.textContent = '✓ Mark All Read';
          markAllBtn.onclick = async () => {
            await backend.markAllRead();
            window.sendQuery('show tickets');
            showToast('All tickets marked as read!');
          };

          const deleteAllBtn = document.createElement('button');
          markAllBtn.className = 'ticket-action-btn danger';
          deleteAllBtn.textContent = '🗑️ Delete All';
          deleteAllBtn.onclick = async () => {
            if (confirm('Are you sure you want to delete all tickets?')) {
              await backend.clearTickets();
              window.sendQuery('show tickets');
              showToast('All tickets cleared!');
            }
          };

          actionRow.appendChild(markAllBtn);
          actionRow.appendChild(deleteAllBtn);
          headerWrap.appendChild(topRow);
          headerWrap.appendChild(actionRow);
        } else {
          headerWrap.appendChild(topRow);
        }

        botMsg.appendChild(headerWrap);

        if (tickets.length === 0) {
          const empty = document.createElement('div');
          empty.style.fontSize = '0.8rem';
          empty.style.color = 'var(--text-secondary)';
          empty.style.marginTop = '6px';
          empty.textContent = 'No tickets in inbox.';
          botMsg.appendChild(empty);
        } else {
          for (const t of tickets) {
            if (lower === 'show unread' && t.read) continue;
            const decryptedText = await decryptMessage(t.message);
            const card = document.createElement('div');
            card.className = 'ticket-item';
            const dateStr = new Date(Number(t.created) / 1_000_000).toLocaleString();
            const unreadBadge = t.read ? '' : ' <span style="color:#00bfff; font-size:0.65rem;">● UNREAD</span>';
            card.innerHTML = `<div><strong>#${t.id.toString()}</strong>${unreadBadge} <span style="font-size:0.65rem; color:var(--text-secondary);">${dateStr}</span></div><div style="margin:4px 0; color:#2ed573;">🔒 ${escapeHtml(decryptedText)}</div>`;
            botMsg.appendChild(card);
          }
        }
      }
    } catch (e) {
      botMsg.textContent = `Authentication or decryption error: ${e.message || e}`;
    }
    history.scrollTop = history.scrollHeight;
    isSending = false;
    if (sendBtn) sendBtn.disabled = false;
    return;
  }

  if (lower.includes("how many people visited") || lower.includes("traffic") || lower.includes("stats") || lower.includes("visitor count")) {
    try {
      const backend = await getBackend(false);
      if (!backend) {
        botMsg.textContent = "Error: Unable to connect to backend canister.";
        isSending = false;
        if (sendBtn) sendBtn.disabled = false;
        return;
      }
      const stats = await backend.getTrafficStats();
      
      const topCountry = stats.topCountries[0] ? `${stats.topCountries[0].name} (${stats.topCountries[0].count.toString()})` : 'None';
      const topDevice = stats.topDevices[0] ? `${stats.topDevices[0].name} (${stats.topDevices[0].count.toString()})` : 'None';
      const topBrowser = stats.topBrowsers[0] ? `${stats.topBrowsers[0].name} (${stats.topBrowsers[0].count.toString()})` : 'None';
      
      const card = document.createElement('div');
      card.className = 'analytics-card';

      const header = document.createElement('div');
      header.className = 'analytics-header';
      
      const titleSpan = document.createElement('span');
      titleSpan.textContent = '📊 7-Day Live Analytics';
      const dot = document.createElement('span');
      dot.className = 'live-dot';
      header.appendChild(titleSpan);
      header.appendChild(dot);

      const grid = document.createElement('div');
      grid.className = 'analytics-grid';

      const items = [
        { val: stats.pageViews.toString(), lbl: 'Pageviews' },
        { val: stats.uniqueDevices.toString(), lbl: 'Unique Devices' },
        { val: stats.buttonClicks.toString(), lbl: 'Clicks' }
      ];

      items.forEach(it => {
        const sItem = document.createElement('div');
        sItem.className = 'stat-item';
        const sVal = document.createElement('span');
        sVal.className = 'stat-val';
        sVal.textContent = it.val;
        const sLbl = document.createElement('span');
        sLbl.className = 'stat-lbl';
        sLbl.textContent = it.lbl;
        sItem.appendChild(sVal);
        sItem.appendChild(sLbl);
        grid.appendChild(sItem);
      });

      const breakdown = document.createElement('div');
      breakdown.className = 'analytics-breakdown';
      
      const b1 = document.createElement('div');
      b1.appendChild(document.createTextNode(`🌍 Top Country: ${topCountry}`));
      const b2 = document.createElement('div');
      b2.appendChild(document.createTextNode(`💻 Top Device/OS: ${topDevice}`));
      const b3 = document.createElement('div');
      b3.appendChild(document.createTextNode(`🌐 Top Browser: ${topBrowser}`));

      breakdown.appendChild(b1);
      breakdown.appendChild(b2);
      breakdown.appendChild(b3);

      card.appendChild(header);
      card.appendChild(grid);
      card.appendChild(breakdown);

      botMsg.textContent = '';
      botMsg.appendChild(card);
    } catch (e) {
      console.error(e);
      botMsg.textContent = `Couldn't fetch traffic stats: ${e.message || 'Network error'}`;
    }
    history.scrollTop = history.scrollHeight;
    isSending = false;
    if (sendBtn) sendBtn.disabled = false;
    setTimeout(() => { lastTrackTime = Date.now(); }, 1000);
    return;
  }

  try {
    const backend = await getBackend(false);
    if (!backend) {
      botMsg.textContent = "Error: Backend connection failed.";
      isSending = false;
      if (sendBtn) sendBtn.disabled = false;
      return;
    }
    trackEvent(`search:${text}`);
    
    const results = await backend.askBot(text);
    botMsg.textContent = '';
    if (results && results.length > 0) {
      const introDiv = document.createElement('div');
      introDiv.textContent = 'Here are the best matching tutorials:';
      botMsg.appendChild(introDiv);

      results.forEach(item => {
        const card = document.createElement('div');
        card.className = 'video-card';
        
        const h3 = document.createElement('h3');
        h3.textContent = item.title;

        const p = document.createElement('p');
        p.style.cssText = 'font-size:0.75rem; color:rgba(255,255,255,0.6); margin:4px 0 8px;';
        p.textContent = item.description || '';

        const a = document.createElement('a');
        a.href = item.url;
        a.target = '_blank';
        a.rel = 'noopener';
        a.className = 'gradient-btn';
        a.textContent = 'Watch Video ↗';
        a.addEventListener('click', () => trackEvent('click:watch_video'));

        card.appendChild(h3);
        card.appendChild(p);
        card.appendChild(a);
        botMsg.appendChild(card);
      });
    } else {
      botMsg.textContent = 'No matching tutorials found. Browse all videos on the YouTube channel directly!';
    }
  } catch (err) {
    botMsg.textContent = `Error loading results: ${err.message || 'Unknown error'}`;
  }
  history.scrollTop = history.scrollHeight;
  isSending = false;
  if (sendBtn) sendBtn.disabled = false;
  setTimeout(() => { lastTrackTime = Date.now(); }, 1000);
};

function escapeHtml(str) {
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
}

async function trackEvent(eventAction = 'pageview') {
  if (!shouldTrack()) return;
  if (Date.now() - lastTrackTime < 2000 && eventAction === 'pageview') return;
  try {
    const backend = await getBackend(false);
    if (!backend) return;
    const deviceId = getOrCreateDeviceId();
    if (!deviceId) return;
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
    lastTrackTime = Date.now();
  } catch (err) {
    console.error("Traffic logging error", err);
  }
}
window.trackEvent = trackEvent;

window.handleConsent = function(choice) {
  const banner = document.getElementById('traffic-consent-banner');
  if (banner) banner.style.display = 'none';
  localStorage.setItem('traffic_consent', choice);
  if (choice === 'accepted') {
    trackEvent('pageview');
  } else {
    localStorage.removeItem('tb_device_id');
    localStorage.removeItem('tb_country');
  }
};

document.addEventListener('DOMContentLoaded', () => {
  window.cryptoModal.init();

  if (shouldTrack()) {
    trackEvent('pageview');
  }

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

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      window.cryptoModal.close();
      const chatPanel = document.getElementById('ai-chat-panel');
      if (chatPanel?.classList.contains('open')) {
        window.toggleChat();
      }
    }
  });
});
'''
    script_js_content = script_js_content.replace("__BACKEND_ID__", backend_id).replace("__OWNER_PRINCIPAL__", owner_principal).replace("__CRYPTO_CONFIG__", json.dumps(crypto_config, indent=2))
    os.makedirs("assets", exist_ok=True)
    with open("assets/script.js", "w", encoding="utf-8") as f:
        f.write(script_js_content)

    print("\n✅ Setup.py successfully updated! Terminal PID captured and set as PUBLISHER in backend/main.mo.")

if __name__ == "__main__":
    main()
