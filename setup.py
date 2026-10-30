#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import time
import yt_dlp

def get_principal():
    try:
        result = subprocess.run(['dfx', 'identity', 'get-principal'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except Exception:
        return "Unknown (Make sure dfx is installed and initialized)"

def sanitize(text):
    if not text:
        return ''
    t = text.replace('\\', '\\\\')
    t = t.replace('"', '\\"')
    t = t.replace('\n', ' ').replace('\r', ' ')
    return t

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

    publisher_principal = terminal_pid if not terminal_pid.startswith("Unknown") else owner_principal

    print("\n--- 1. Ticket System & Expiration Configuration ---")
    enable_tickets = input("Do you want to enable the encrypted visitor ticket/messaging system? (y/n) [default: y]: ").strip().lower() != 'n'
    
    ticket_retention_days = 7
    if enable_tickets:
        days_input = input("How many days should the canister hold encrypted tickets before deleting them automatically? (default: 7):\n> ").strip()
        if days_input.isdigit():
            ticket_retention_days = int(days_input)

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

    print("\n📁 Generating mops.toml...")
    mops_toml_content = '''[dependencies]
base = "0.11.0"
ic-vetkeys = "0.6.0"
'''
    with open("mops.toml", "w", encoding="utf-8") as f:
        f.write(mops_toml_content)

    print("📁 Generating package.json...")
    package_json_content = {
        "name": name.lower().replace(" ", "-") + "-creator-hub",
        "version": "3.0.0",
        "description": "Decentralized Web3 Creator Hub on ICP",
        "scripts": {
            "build": "echo 'No extra build steps needed for static assets'"
        },
        "dependencies": {
            "@dfinity/agent": "^0.21.4",
            "@dfinity/auth-client": "^0.21.4",
            "@icp-sdk/vetkeys": "^0.1.0"
        },
        "devDependencies": {},
        "private": True
    }
    with open("package.json", "w", encoding="utf-8") as f:
        json.dump(package_json_content, f, indent=2)

    print("📁 Generating dfx.json...")
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

    print("📁 Generating canister_ids.json...")
    canister_ids = {
      "website": { "ic": frontend_id },
      "backend": { "ic": backend_id }
    }
    with open("canister_ids.json", "w", encoding="utf-8") as f:
        json.dump(canister_ids, f, indent=2)

    print("📁 Generating backend/main.mo (with vetKeys + full ticket system)...")
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
        let now = Time.now();
        if (now - lastSubmitTime < 5_000_000_000) {{
            return null;
        }};
        lastSubmitTime := now;

        if (Text.size(ciphertextPayload) == 0 or Text.size(ciphertextPayload) > MAX_CIPHER_LEN) {{
            return null;
        }};
        
        pruneOldTickets();

        if (tickets.size() >= MAX_TICKETS) {{
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

    public shared (msg) func getUnreadCount() : async Nat {{
        if (not Principal.equal(msg.caller, OWNER)) {{
            return 0;
        }};
        pruneOldTickets();
        var count : Nat = 0;
        var i = 0;
        while (i < tickets.size()) {{
            let t = tickets[i];
            if (not t.read and not t.archived) {{
                count += 1;
            }};
            i += 1;
        }};
        count
    }};

    public shared query (msg) func getMyPrincipal() : async Text {{
        Principal.toText(msg.caller)
    }};

    public shared (msg) func clearTickets() : async Bool {{
        if (not Principal.equal(msg.caller, OWNER)) return false;
        tickets := [];
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

    public shared (msg) func archiveTicket(id : Nat, archivedStatus : Bool) : async Bool {{
        if (not Principal.equal(msg.caller, OWNER)) return false;
        pruneOldTickets();
        var found = false;
        var updatedTickets = Buffer.Buffer<Ticket>(tickets.size());
        var i = 0;
        while (i < tickets.size()) {{
            let t = tickets[i];
            if (t.id == id) {{
                found := true;
                let modified : Ticket = {{ id = t.id; message = t.message; created = t.created; read = t.read; archived = archivedStatus }};
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
import Nat "mo:base/Nat";
import Buffer "mo:base/Buffer";
import Timer "mo:base/Timer";
import Time "mo:base/Time";
import Principal "mo:base/Principal";
import Error "mo:base/Error";
import ExperimentalCycles "mo:base/ExperimentalCycles";

actor {{
    let OWNER : Principal = Principal.fromText("{owner_principal}");
    let PUBLISHER : Principal = Principal.fromText("{publisher_principal}");

    let SEVEN_DAYS_NS : Time.Time = 604_800_000_000_000;
    let MAX_VISIT_LOGS : Nat = 50_000;
    let MAX_TICKETS : Nat = 200;
    let MAX_CIPHER_LEN : Nat = 2048;

    let KEY_NAME : Text = "key_1";
    let DOMAIN_SEPARATOR : Text = "techbod_tickets_v1";

    type IC = actor {{
        vetkd_public_key : ({{
            canister_id : ?Principal;
            context : Blob;
            key_id : {{ curve : {{ #bls12_381_g2; #bls12_381_g1 }}; name : Text }};
        }}) -> async {{ public_key : Blob }};

        vetkd_derive_key : ({{
            input : Blob;
            context : Blob;
            transport_public_key : Blob;
            key_id : {{ curve : {{ #bls12_381_g2; #bls12_381_g1 }}; name : Text }};
        }}) -> async {{ encrypted_key : Blob }};
    }};

    let ic : IC = actor ("aaaaa-aa");

    public type VideoRecord = {{
        title : Text;
        url : Text;
        description : Text;
        searchableText : Text;
        timestamp : Time.Time;
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
        topSearches : [CountedItem];
    }};

    stable var videoLibrary : [VideoRecord] = [];
    stable var visitLogs : [DetailedVisitRecord] = [];
    stable var searchQueriesBuffer : [Text] = [];
    stable var lastSubmitTime : Time.Time = 0;

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

    public shared func getPublicKey() : async Blob {{
        let result = await ic.vetkd_public_key({{
            canister_id = null;
            context = Text.encodeUtf8(DOMAIN_SEPARATOR);
            key_id = {{ curve = #bls12_381_g2; name = KEY_NAME }};
        }});
        result.public_key
    }};

    public shared ({{ caller }}) func deriveKey(transportPublicKey : Blob) : async Blob {{
        if (not Principal.equal(caller, OWNER)) {{
            throw Error.reject("Unauthorized: Only owner can derive keys");
        }};
        let input = Principal.toBlob(caller);
        ExperimentalCycles.add(26_000_000_000);
        let result = await ic.vetkd_derive_key({{
            input = input;
            context = Text.encodeUtf8(DOMAIN_SEPARATOR);
            transport_public_key = transportPublicKey;
            key_id = {{ curve = #bls12_381_g2; name = KEY_NAME }};
        }});
        result.encrypted_key
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
            case (?act) {{ 
                if (Text.size(act) > 128) return;
                if (Text.startsWith(act, #text("search:"))) {{
                    let stripped = Text.replace(act, #text("search:"), "");
                    let term = Text.trim(stripped, #text(" "));
                    if (Text.size(term) > 2 and Text.size(term) < 60) {{
                        if (searchQueriesBuffer.size() < 500) {{
                            searchQueriesBuffer := Array.append(searchQueriesBuffer, [term]);
                        }};
                    }};
                }};
            }};
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
                            countriesBuf.add(log.country);
                            devicesBuf.add(log.device);
                            browsersBuf.add(log.browser);
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
            topSearches  = tallyValues(searchQueriesBuffer, 5);
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

        var scoredMatches = Buffer.Buffer<{{ score : Nat; item : ResponseItem }}>(20);

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
        var sortedBuffer = Buffer.Buffer<{{ score : Nat; item : ResponseItem }}>(allMatches.size());
        var remainingMatches = Buffer.Buffer<{{ score : Nat; item : ResponseItem }}>(allMatches.size());
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
                    var newRem = Buffer.Buffer<{{ score : Nat; item : ResponseItem }}>(currentRem.size() - 1);
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
        }})
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

    print("📁 Generating assets/script.js (dynamic imports + vetKeys + full ticket UI)...")
    script_js_content = r'''// --- Immediate Global Fallbacks & UI Handlers ---
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
      card.style.display = 'flex';
    } else {
      card.classList.add('filtered-out');
      card.style.display = 'none';
    }
  });
};

function showToast(msg) {
  const t = document.getElementById('toast');
  if (!t) return;
  t.innerText = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2000);
}
window.showToast = showToast;

function renderQRCode(elementId, text, size = 120) {
  const el = document.getElementById(elementId);
  if (!el) return;
  el.innerHTML = '';
  if (typeof QRCode !== 'undefined') {
    try {
      new QRCode(el, {
        text: text,
        width: size,
        height: size,
        colorDark: "#000000",
        colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.M
      });
      return;
    } catch (e) {
      console.warn("QRCode gen error:", e);
    }
  }
  const img = document.createElement('img');
  img.src = `https://api.qrserver.com/v1/create-qr-code/?size=${size}x${size}&data=${encodeURIComponent(text)}`;
  img.width = size;
  img.height = size;
  el.appendChild(img);
}

const CONFIG = {
  crypto: __CRYPTO_CONFIG__
};

window.cryptoModal = {
  currentTab: localStorage.getItem('tb_crypto_tab') || Object.keys(CONFIG.crypto)[0] || 'icp',
  init() { this.renderTabs(); },
  open() {
    window.trackEvent?.('click:buy_coffee');
    const modal = document.getElementById('crypto-modal');
    if (modal) {
      modal.classList.add('active');
      modal.setAttribute('aria-hidden', 'false');
    }
    document.body.style.overflow = 'hidden';
    this.switchTab(this.currentTab);
  },
  close() {
    const modal = document.getElementById('crypto-modal');
    if (modal) {
      modal.classList.remove('active');
      modal.setAttribute('aria-hidden', 'true');
    }
    document.body.style.overflow = '';
  },
  renderTabs() {
    const container = document.getElementById('crypto-tabs');
    if (!container) return;
    container.innerHTML = '';
    Object.values(CONFIG.crypto).forEach(coin => {
      const btn = document.createElement('button');
      btn.className = `tab-btn ${coin.id === this.currentTab ? 'active' : ''}`;
      btn.onclick = () => window.cryptoModal.switchTab(coin.id);
      
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
      qrContainer.title = "Click to view full screen QR";
      qrContainer.onclick = () => window.openFullscreenQR(addr.value, addr.label);

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
      valDiv.onclick = () => window.cryptoModal.copy(addr.value, addr.label);

      const copyBtn = document.createElement('button');
      copyBtn.className = 'copy-btn';
      copyBtn.textContent = 'Copy Address';
      copyBtn.onclick = () => window.cryptoModal.copy(addr.value, addr.label);

      details.appendChild(labelDiv);
      details.appendChild(valDiv);
      details.appendChild(copyBtn);

      card.appendChild(qrContainer);
      card.appendChild(details);
      body.appendChild(card);

      setTimeout(() => {
        renderQRCode(qrId, addr.value, 120);
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
      window.trackEvent?.(`copy:${label}`);
      showToast(`${label} Copied!`);
    } catch {
      showToast('Failed to copy. Please select manually.');
    }
  }
};

window.openFullscreenQR = function(address, label) {
  const modal = document.getElementById('qr-fullscreen-modal');
  const container = document.getElementById('qr-fullscreen-container');
  const lbl = document.getElementById('qr-fullscreen-label');
  if (!modal || !container || !lbl) return;

  container.innerHTML = '';
  const innerBox = document.createElement('div');
  innerBox.id = 'qr-fullscreen-box';
  container.appendChild(innerBox);

  renderQRCode('qr-fullscreen-box', address, 220);
  lbl.textContent = label;
  modal.classList.add('active');
  modal.setAttribute('aria-hidden', 'false');
};

window.closeFullscreenQR = function() {
  const modal = document.getElementById('qr-fullscreen-modal');
  if (modal) {
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
  }
};

window.toggleChat = function() {
  const panel = document.getElementById('ai-chat-panel');
  if (!panel) return;
  const isOpen = panel.classList.toggle('open');
  panel.setAttribute('aria-hidden', isOpen ? 'false' : 'true');
  if (isOpen) {
    document.getElementById('chat-input')?.focus();
    updateUnreadBadge();
  }
};

window.handleChatKeyDown = function(e) {
  if (e.key === 'Enter') window.sendQuery();
};

document.addEventListener('DOMContentLoaded', () => {
  window.cryptoModal.init();

  const consent = localStorage.getItem('traffic_consent');
  if (!consent) {
    const banner = document.getElementById('traffic-consent-banner');
    if (banner) banner.style.display = 'block';
  }
  updateUnreadBadge();
});

let Actor, HttpAgent, AuthClient, Principal;
const BACKEND_CANISTER_ID = '__BACKEND_ID__';
const OWNER_PRINCIPAL = '__OWNER_PRINCIPAL__';
let authClient = null;
let lastTrackTime = 0;
let isSending = false;
let cachedAgent = null;
let cachedAgentIdentity = null;

(async function initWeb3() {
  try {
    const agentMod = await import('https://esm.sh/@dfinity/agent@0.21.4?bundle');
    const authMod = await import('https://esm.sh/@dfinity/auth-client@0.21.4?bundle');
    const princMod = await import('https://esm.sh/@dfinity/principal@0.21.4?bundle');
    
    Actor = agentMod.Actor;
    HttpAgent = agentMod.HttpAgent;
    AuthClient = authMod.AuthClient;
    Principal = princMod.Principal;

    if (shouldTrack()) trackEvent('pageview');
  } catch (err) {
    console.warn("Web3 canister connection modules unavailable or offline:", err);
  }
})();

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

async function getAuthClient() {
  if (!AuthClient) {
    const authMod = await import('https://esm.sh/@dfinity/auth-client@0.21.4?bundle').catch(() => null);
    if (authMod) AuthClient = authMod.AuthClient;
  }
  if (!AuthClient) return null;
  if (!authClient) {
    authClient = await AuthClient.create({
      idleOptions: {
        disableIdle: true,
        disableDefaultIdleCallback: true
      }
    });
  }
  return authClient;
}

async function getBackend(isAuthenticated = false) {
  if (!Actor || !HttpAgent) {
    const agentMod = await import('https://esm.sh/@dfinity/agent@0.21.4?bundle').catch(() => null);
    if (agentMod) {
      Actor = agentMod.Actor;
      HttpAgent = agentMod.HttpAgent;
    }
  }
  if (!Actor || !HttpAgent) return null;

  try {
    const client = isAuthenticated ? await getAuthClient() : null;
    const identity = client && await client.isAuthenticated() ? client.getIdentity() : null;
    const identityKey = identity ? identity.getPrincipal().toText() : 'anon';

    if (cachedAgent && cachedAgentIdentity === identityKey) {
      return cachedAgent;
    }

    const host = window.location.origin.includes('localhost') ? 'http://127.0.0.1:4943' : 'https://icp0.io';
    const agentOptions = { host };
    if (identity) {
      agentOptions.identity = identity;
    }
    
    const agent = new HttpAgent(agentOptions);
    if (host.includes('localhost') || host.includes('127.0.0.1')) {
      await agent.fetchRootKey().catch(() => {});
    }

    cachedAgent = Actor.createActor(({ IDL }) => {
      const CountedItem = IDL.Record({ 'name': IDL.Text, 'count': IDL.Nat });
      const Ticket = IDL.Record({
        'id': IDL.Nat,
        'message': IDL.Text,
        'created': IDL.Int,
        'read': IDL.Bool,
        'archived': IDL.Bool
      });
      const ResponseItem = IDL.Record({
        'title': IDL.Text,
        'url': IDL.Text,
        'description': IDL.Text
      });
      return IDL.Service({
        'askBot': IDL.Func([IDL.Text], [IDL.Vec(ResponseItem)], ['query']),
        'getLatestVideos': IDL.Func([], [IDL.Vec(ResponseItem)], ['query']),
        'logVisit': IDL.Func([IDL.Text, IDL.Text, IDL.Text, IDL.Text, IDL.Text, IDL.Opt(IDL.Text)], [], []),
        'getTrafficStats': IDL.Func([], [IDL.Record({
          'pageViews' : IDL.Nat,
          'totalEvents' : IDL.Nat,
          'uniqueDevices' : IDL.Nat,
          'buttonClicks' : IDL.Nat,
          'topCountries' : IDL.Vec(CountedItem),
          'topDevices' : IDL.Vec(CountedItem),
          'topBrowsers' : IDL.Vec(CountedItem),
          'topLinks' : IDL.Vec(CountedItem),
          'topSearches' : IDL.Vec(CountedItem)
        })], ['query']),
        'submitTicket': IDL.Func([IDL.Text], [IDL.Opt(IDL.Nat)], []),
        'getTickets': IDL.Func([], [IDL.Opt(IDL.Vec(Ticket))], []),
        'getUnreadCount': IDL.Func([], [IDL.Nat], []),
        'clearTickets': IDL.Func([], [IDL.Bool], []),
        'markAllRead': IDL.Func([], [IDL.Bool], []),
        'getMyPrincipal': IDL.Func([], [IDL.Text], ['query']),
        'markTicketRead': IDL.Func([IDL.Nat, IDL.Bool], [IDL.Bool], []),
        'archiveTicket': IDL.Func([IDL.Nat, IDL.Bool], [IDL.Bool], []),
        'deleteTicket': IDL.Func([IDL.Nat], [IDL.Bool], []),
        'getPublicKey': IDL.Func([], [IDL.Vec(IDL.Nat8)], []),
        'deriveKey': IDL.Func([IDL.Vec(IDL.Nat8)], [IDL.Vec(IDL.Nat8)], [])
      });
    }, { agent, canisterId: BACKEND_CANISTER_ID });

    cachedAgentIdentity = identityKey;
    return cachedAgent;
  } catch (e) {
    console.error("Backend connection error", e);
    return null;
  }
}

async function encryptMessage(plaintext, ownerPrincipalText) {
  try {
    const vetkeysMod = await import('https://esm.sh/@icp-sdk/vetkeys@0.5.0?bundle').catch(() => null);
    if (!vetkeysMod) return btoa(unescape(encodeURIComponent(plaintext)));
    const { DerivedPublicKey, IbeCiphertext, IbeIdentity, IbeSeed } = vetkeysMod;
    const princMod = await import('https://esm.sh/@dfinity/principal@0.21.4?bundle').catch(() => null);
    if (princMod) Principal = princMod.Principal;

    const backend = await getBackend(false);
    if (!backend) return btoa(unescape(encodeURIComponent(plaintext)));
    const publicKeyBytes = await backend.getPublicKey();
    const publicKey = DerivedPublicKey.deserialize(new Uint8Array(publicKeyBytes));
    
    const ownerPrincipal = Principal.fromText(ownerPrincipalText);
    const identity = IbeIdentity.fromBytes(ownerPrincipal.toUint8Array());
    const seed = IbeSeed.fromBytes(crypto.getRandomValues(new Uint8Array(32)));
    
    const ciphertext = IbeCiphertext.encrypt(
      publicKey, 
      identity, 
      seed, 
      new TextEncoder().encode(plaintext)
    );
    return btoa(String.fromCharCode(...ciphertext.serialize()));
  } catch (e) {
    return btoa(unescape(encodeURIComponent(plaintext)));
  }
}

async function decryptMessage(payloadB64, identity) {
  try {
    const vetkeysMod = await import('https://esm.sh/@icp-sdk/vetkeys@0.5.0?bundle').catch(() => null);
    if (!vetkeysMod) {
      try { return decodeURIComponent(escape(atob(payloadB64))); } catch { return payloadB64; }
    }
    const { TransportSecretKey, DerivedPublicKey, EncryptedVetKey, IbeCiphertext } = vetkeysMod;

    const backend = await getBackend(true);
    if (!backend) {
      try { return decodeURIComponent(escape(atob(payloadB64))); } catch { return payloadB64; }
    }
    const seed = crypto.getRandomValues(new Uint8Array(32));
    const transportSecretKey = TransportSecretKey.fromSeed(seed);
    const transportPublicKey = transportSecretKey.publicKey();

    const [encryptedKeyBytes, publicKeyBytes] = await Promise.all([
      backend.deriveKey(transportPublicKey),
      backend.getPublicKey()
    ]);

    const verificationKey = DerivedPublicKey.deserialize(new Uint8Array(publicKeyBytes));
    const encryptedVetKey = EncryptedVetKey.deserialize(new Uint8Array(encryptedKeyBytes));
    
    const vetKey = encryptedVetKey.decryptAndVerify(
      transportSecretKey, 
      verificationKey, 
      new Uint8Array(identity.getPrincipal().toUint8Array())
    );

    const rawCiphertext = Uint8Array.from(atob(payloadB64), c => c.charCodeAt(0));
    const plaintext = IbeCiphertext.deserialize(rawCiphertext).decrypt(vetKey);
    return new TextDecoder().decode(plaintext);
  } catch (e) {
    try { return decodeURIComponent(escape(atob(payloadB64))); } catch { return payloadB64; }
  }
}

async function trackEvent(eventAction = 'pageview') {
  if (!shouldTrack()) return;
  if (Date.now() - lastTrackTime < 2000 && eventAction === 'pageview') return;
  lastTrackTime = Date.now();
  try {
    const backend = await getBackend(false);
    if (!backend) return;
    const deviceId = getOrCreateDeviceId();
    if (!deviceId) return;
    const consent = localStorage.getItem('traffic_consent') || 'ignored';
    const country = await getCountryCode();
    const meta = parseUserAgent();

    await backend.logVisit(deviceId, consent, country, meta.device, meta.browser, eventAction ? [eventAction] : []);
  } catch (err) {
    console.error("Traffic logging error", err);
  }
}
window.trackEvent = trackEvent;

window.handleConsent = function(choice) {
  const banner = document.getElementById('traffic-consent-banner');
  if (banner) banner.style.display = 'none';
  localStorage.setItem('traffic_consent', choice);
  if (choice === 'accepted') trackEvent('pageview');
  else {
    localStorage.removeItem('tb_device_id');
    localStorage.removeItem('tb_country');
  }
};

window.triggerIILogin = async function() {
  const history = document.getElementById('chat-history');
  if (!history) return;

  const botMsg = document.createElement('div');
  botMsg.className = 'chat-msg bot';
  history.appendChild(botMsg);
  history.scrollTop = history.scrollHeight;

  try {
    const client = await getAuthClient();
    if (!client) {
      botMsg.textContent = 'Auth client offline.';
      return;
    }
    if (await client.isAuthenticated()) {
      await client.logout();
      cachedAgent = null;
      cachedAgentIdentity = null;
    }

    botMsg.textContent = 'Connecting to Internet Identity...';

    await client.login({
      identityProvider: 'https://identity.ic0.app/#authorize',
      maxTimeToLive: BigInt(8) * BigInt(24) * BigInt(60) * BigInt(60) * BigInt(1000) * BigInt(1000) * BigInt(1000),
      windowOpenerFeatures: 'toolbar=0,location=0,menubar=0,width=525,height=705,left=400,top=100',
      onSuccess: async () => {
        cachedAgent = null;
        cachedAgentIdentity = null;
        const identity = client.getIdentity();
        const principalText = identity.getPrincipal().toText();
        
        botMsg.textContent = '';
        const authDiv = document.createElement('div');
        authDiv.style.cssText = 'display:flex; flex-direction:column; gap:8px;';
        authDiv.innerHTML = `<strong>✅ Logged in successfully! Session remembered for 8 days.</strong><br>Your Principal ID:`;
        
        const inputPid = document.createElement('input');
        inputPid.type = 'text';
        inputPid.readOnly = true;
        inputPid.value = principalText;
        inputPid.style.cssText = 'font-family:monospace; font-size:0.75rem; padding:8px; background:rgba(0,0,0,0.5); border:1px solid var(--glass-border); border-radius:8px; color:#00bfff; width:100%; cursor:pointer;';
        inputPid.onclick = () => { inputPid.select(); navigator.clipboard.writeText(principalText); showToast('PID Copied!'); };
        
        authDiv.appendChild(inputPid);
        botMsg.appendChild(authDiv);
        history.scrollTop = history.scrollHeight;
        updateUnreadBadge();
      },
      onError: (err) => {
        botMsg.textContent = `Login failed or cancelled: ${err || 'Unknown error'}`;
      }
    });
  } catch (e) {
    botMsg.textContent = `Auth error: ${e.message || e}`;
  }
};

async function updateUnreadBadge() {
  const badge = document.getElementById('ai-unread-badge');
  if (!badge) return;
  try {
    const client = await getAuthClient();
    if (!client || !await client.isAuthenticated()) {
      badge.classList.remove('active');
      return;
    }
    const identity = client.getIdentity();
    if (identity.getPrincipal().toText() !== OWNER_PRINCIPAL) {
      badge.classList.remove('active');
      return;
    }
    const backend = await getBackend(true);
    if (!backend) return;
    const count = await backend.getUnreadCount();
    const num = Number(count);
    if (num > 0) {
      badge.textContent = num > 99 ? '99+' : num.toString();
      badge.classList.add('active');
    } else {
      badge.classList.remove('active');
    }
  } catch (e) {
    badge.classList.remove('active');
  }
}

function formatReadableLink(linkName) {
  if (!linkName) return '';
  const clean = linkName.replace('click:', '');
  const mapping = {
    'youtube': 'YouTube',
    'openchat': 'OpenChat',
    'telegram': 'Telegram',
    'x': 'X (Twitter)',
    'instagram': 'Instagram',
    'facebook': 'Facebook',
    'discord': 'Discord',
    'github': 'GitHub',
    'tiktok': 'TikTok',
    'truthsocial': 'Truth Social',
    'tumblr': 'Tumblr',
    'bluesky': 'Bluesky',
    'openchat_dapp': 'OpenChat dApp',
    'clown': 'Clown dApp',
    'oisy': 'Oisy Wallet',
    'randseed': 'Randseed',
    'buy_coffee': 'Buy Me a Coffee'
  };
  return mapping[clean] || clean.charAt(0).toUpperCase() + clean.slice(1).replace(/_/g, ' ');
}

function formatCountryName(code) {
  if (!code || code === 'Unknown') return 'Unknown Region';
  const names = {
    'DE': 'Germany (DE)', 'US': 'United States (US)', 'GB': 'United Kingdom (GB)',
    'FR': 'France (FR)', 'CA': 'Canada (CA)', 'IR': 'Iran (IR)', 'NL': 'Netherlands (NL)'
  };
  return names[code.toUpperCase()] || code.toUpperCase();
}

window.sendQuery = async function(presetText) {
  if (isSending) return;
  const input = document.getElementById('chat-input');
  const history = document.getElementById('chat-history');
  if (!history) return;
  const text = presetText !== undefined && presetText !== null ? presetText : (input ? input.value.trim() : '');
  if (!text) return;

  isSending = true;
  const sendBtn = document.querySelector('.chat-input-area button');
  if (sendBtn) sendBtn.disabled = true;

  const userMsg = document.createElement('div');
  userMsg.className = 'chat-msg user';
  userMsg.textContent = text;
  history.appendChild(userMsg);
  if (input && (presetText === undefined || presetText === null)) input.value = '';
  history.scrollTop = history.scrollHeight;

  const botMsg = document.createElement('div');
  botMsg.className = 'chat-msg bot';
  botMsg.textContent = 'Connecting to IC Canister...';
  history.appendChild(botMsg);
  history.scrollTop = history.scrollHeight;

  const lower = text.toLowerCase().trim();

  if (lower.startsWith('ticket ') || lower.startsWith('تیکت ')) {
    const messageContent = text.replace(/^(ticket|تیکت)\s+/i, '').trim();
    if (!messageContent) {
      botMsg.textContent = "Please include a message after 'ticket'. Example: ticket Hello!";
      isSending = false;
      if (sendBtn) sendBtn.disabled = false;
      return;
    }
    try {
      botMsg.textContent = 'Encrypting & submitting note...';
      const encryptedPayload = await encryptMessage(messageContent, OWNER_PRINCIPAL);
      const backend = await getBackend(false);
      if (!backend) throw new Error("Canister connection offline");
      const resId = await backend.submitTicket(encryptedPayload);
      if (resId !== null && resId !== undefined) {
        botMsg.textContent = `📬 Note submitted! Ticket ID: #${resId.toString()}`;
        updateUnreadBadge();
      } else {
        botMsg.textContent = "❌ Failed to send ticket. Server cooldown active.";
      }
    } catch (e) {
      botMsg.textContent = `Error sending ticket: ${e.message || 'Network error'}`;
    }
    history.scrollTop = history.scrollHeight;
    isSending = false;
    if (sendBtn) sendBtn.disabled = false;
    return;
  }

  if (lower === 'show tickets' || lower === 'show unread' || lower === 'tickets') {
    try {
      const client = await getAuthClient();
      if (!client || !await client.isAuthenticated()) {
        botMsg.textContent = '';
        const authDiv = document.createElement('div');
        authDiv.innerHTML = `🔒 Owner access requires Internet Identity login.<br><br>`;
        const loginBtn = document.createElement('button');
        loginBtn.className = 'gradient-btn';
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
      if (identity.getPrincipal().toText() !== OWNER_PRINCIPAL) {
        botMsg.textContent = `⛔ Unauthorized: Logged-in identity is not the canister owner.`;
        isSending = false;
        if (sendBtn) sendBtn.disabled = false;
        return;
      }

      botMsg.textContent = 'Fetching and decrypting tickets...';
      const ticketsOpt = await backend.getTickets();
      if (!ticketsOpt) {
        botMsg.textContent = "No tickets returned.";
      } else {
        const rawTickets = Array.isArray(ticketsOpt) ? (ticketsOpt[0] || []) : ticketsOpt;
        const tickets = Array.isArray(rawTickets) ? rawTickets : [];
        
        botMsg.textContent = '';
        const headerWrap = document.createElement('div');
        headerWrap.style.cssText = 'display:flex; flex-direction:column; gap:8px; margin-bottom:8px;';

        const topRow = document.createElement('div');
        topRow.style.cssText = 'display:flex; justify-content:space-between; align-items:center;';
        topRow.innerHTML = `<strong>📬 Inbox (${tickets.length})</strong>`;

        if (tickets.length > 0) {
          const actionRow = document.createElement('div');
          actionRow.style.cssText = 'display:flex; gap:6px;';

          const markAllBtn = document.createElement('button');
          markAllBtn.className = 'ticket-action-btn';
          markAllBtn.textContent = '✓ Mark All Read';
          markAllBtn.onclick = async () => {
            await backend.markAllRead();
            window.sendQuery('show tickets');
          };

          const deleteAllBtn = document.createElement('button');
          deleteAllBtn.className = 'ticket-action-btn danger';
          deleteAllBtn.textContent = '🗑️ Delete All';
          deleteAllBtn.onclick = async () => {
            if (confirm('Delete all tickets?')) {
              await backend.clearTickets();
              window.sendQuery('show tickets');
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
          empty.style.cssText = 'font-size:0.8rem; color:var(--text-secondary); margin-top:6px;';
          empty.textContent = 'No tickets in inbox.';
          botMsg.appendChild(empty);
        } else {
          for (const t of tickets) {
            if (lower === 'show unread' && (t.read || t.archived)) continue;
            const decryptedText = await decryptMessage(t.message, identity);
            const card = document.createElement('div');
            card.className = 'ticket-item';
            const dateStr = new Date(Number(t.created) / 1_000_000).toLocaleString();
            const unreadBadge = t.read ? '' : ' <span style="color:#00bfff; font-size:0.65rem;">● UNREAD</span>';
            const archivedBadge = t.archived ? ' <span style="color:#ffa500; font-size:0.65rem;">[ARCHIVED]</span>' : '';
            
            card.innerHTML = `<div><strong>#${t.id.toString()}</strong>${unreadBadge}${archivedBadge} <span style="font-size:0.65rem; color:var(--text-secondary);">${dateStr}</span></div><div style="margin:4px 0; color:#2ed573;">🔒 </div>`;
            card.lastChild.appendChild(document.createTextNode(decryptedText));

            const btnRow = document.createElement('div');
            btnRow.className = 'ticket-actions-row';

            const readBtn = document.createElement('button');
            readBtn.className = 'ticket-action-btn';
            readBtn.textContent = t.read ? 'Mark Unread' : 'Mark Read';
            readBtn.onclick = async () => {
              await backend.markTicketRead(t.id, !t.read);
              window.sendQuery('show tickets');
              updateUnreadBadge();
            };

            const archiveBtn = document.createElement('button');
            archiveBtn.className = 'ticket-action-btn';
            archiveBtn.textContent = t.archived ? 'Unarchive' : 'Archive';
            archiveBtn.onclick = async () => {
              await backend.archiveTicket(t.id, !t.archived);
              window.sendQuery('show tickets');
              updateUnreadBadge();
            };

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'ticket-action-btn danger';
            deleteBtn.textContent = 'Delete';
            deleteBtn.onclick = async () => {
              await backend.deleteTicket(t.id);
              window.sendQuery('show tickets');
              updateUnreadBadge();
            };

            btnRow.appendChild(readBtn);
            btnRow.appendChild(archiveBtn);
            btnRow.appendChild(deleteBtn);
            card.appendChild(btnRow);
            botMsg.appendChild(card);
          }
        }
      }
    } catch (e) {
      botMsg.textContent = `Error: ${e.message || e}`;
    }
    history.scrollTop = history.scrollHeight;
    isSending = false;
    if (sendBtn) sendBtn.disabled = false;
    return;
  }

  if (lower.includes("traffic") || lower.includes("stats") || lower.includes("analytics")) {
    try {
      const backend = await getBackend(false);
      if (!backend) throw new Error("Canister offline");
      const stats = await backend.getTrafficStats();

      const topCountriesStr = stats.topCountries && stats.topCountries.length > 0
        ? stats.topCountries.map(c => `${formatCountryName(c.name)}: <b>${c.count.toString()}</b>`).join('<br>')
        : 'No country data yet';

      const topDevicesStr = stats.topDevices && stats.topDevices.length > 0
        ? stats.topDevices.map(d => `${escapeHtml(d.name)}: <b>${d.count.toString()}</b>`).join('<br>')
        : 'No device data yet';

      const topBrowsersStr = stats.topBrowsers && stats.topBrowsers.length > 0
        ? stats.topBrowsers.map(b => `${escapeHtml(b.name)}: <b>${b.count.toString()}</b>`).join('<br>')
        : 'No browser data yet';

      const topLinksStr = stats.topLinks && stats.topLinks.length > 0
        ? stats.topLinks.map(l => `${formatReadableLink(l.name)}: <b>${l.count.toString()}</b>`).join('<br>')
        : 'No button/link clicks recorded yet';

      const topSearchesStr = stats.topSearches && stats.topSearches.length > 0
        ? stats.topSearches.map(s => `"${escapeHtml(s.name)}": <b>${s.count.toString()}</b>`).join('<br>')
        : 'No searches logged yet';

      const card = document.createElement('div');
      card.className = 'analytics-card';

      card.innerHTML = `
        <div class="analytics-header"><span>📊 7-Day Live Analytics</span><span class="live-dot"></span></div>
        <div class="analytics-grid">
          <div class="stat-item"><span class="stat-val">${stats.pageViews.toString()}</span><span class="stat-lbl">Pageviews</span></div>
          <div class="stat-item"><span class="stat-val">${stats.uniqueDevices.toString()}</span><span class="stat-lbl">Unique Devices</span></div>
          <div class="stat-item"><span class="stat-val">${stats.buttonClicks.toString()}</span><span class="stat-lbl">Clicks</span></div>
        </div>
        <div class="analytics-breakdown">
          <div class="analytics-row"><span class="analytics-label-title">🌍 Top Country</span><span class="analytics-val-box">${topCountriesStr}</span></div>
          <div class="analytics-row"><span class="analytics-label-title">💻 Top Device</span><span class="analytics-val-box">${topDevicesStr}</span></div>
          <div class="analytics-row"><span class="analytics-label-title">🌐 Top Browser</span><span class="analytics-val-box">${topBrowsersStr}</span></div>
          <div class="analytics-row"><span class="analytics-label-title">🖱️ Top Clicked Links</span><span class="analytics-val-box">${topLinksStr}</span></div>
          <div class="analytics-row"><span class="analytics-label-title">🔍 Top Searches</span><span class="analytics-val-box" style="color:#00bfff;">${topSearchesStr}</span></div>
        </div>
      `;

      botMsg.textContent = '';
      botMsg.appendChild(card);
    } catch (e) {
      botMsg.textContent = `Error fetching canister stats: ${e.message || e}`;
    }
    history.scrollTop = history.scrollHeight;
    isSending = false;
    if (sendBtn) sendBtn.disabled = false;
    return;
  }

  try {
    const backend = await getBackend(false);
    if (!backend) throw new Error("Canister offline");
    trackEvent(`search:${text}`);
    const results = await backend.askBot(text);
    botMsg.textContent = '';
    if (results && results.length > 0) {
      const introDiv = document.createElement('div');
      introDiv.textContent = 'Matching tutorials:';
      botMsg.appendChild(introDiv);

      results.forEach(item => {
        const safeUrl = item.url && item.url.startsWith('https://') ? item.url : '#';
        const card = document.createElement('div');
        card.className = 'video-card';
        card.innerHTML = `<h3>${escapeHtml(item.title || '')}</h3><p style="font-size:0.75rem; color:rgba(255,255,255,0.6); margin:4px 0 8px;">${escapeHtml(item.description || '')}</p><a href="${escapeHtml(safeUrl)}" target="_blank" rel="noopener" class="gradient-btn">Watch Video ↗</a>`;
        botMsg.appendChild(card);
      });
    } else {
      botMsg.textContent = 'No matching tutorials found in library.';
    }
  } catch (err) {
    botMsg.textContent = `Error: ${err.message || 'Canister query failed'}`;
  }
  history.scrollTop = history.scrollHeight;
  isSending = false;
  if (sendBtn) sendBtn.disabled = false;
};

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
}
'''
    script_js_content = script_js_content.replace("__BACKEND_ID__", backend_id).replace("__OWNER_PRINCIPAL__", owner_principal).replace("__CRYPTO_CONFIG__", json.dumps(crypto_config, indent=2))
    os.makedirs("assets", exist_ok=True)
    with open("assets/script.js", "w", encoding="utf-8") as f:
        f.write(script_js_content)

    if yt_url:
        print(f"\n🔍 Scraping videos from {yt_url} using yt-dlp...")
        ydl_opts = {'extract_flat': 'in_playlist', 'skip_download': True, 'ignoreerrors': True}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(yt_url, download=False)
                entries = info.get('entries', [])
                print(f"Found {len(entries)} video entries.")
        except Exception as e:
            print(f"⚠️ Warning during YouTube scraping: {e}")

    print("\n==================================================")
    print("🎉 Full setup and code generation completed successfully!")
    print("==================================================")

if __name__ == '__main__':
    main()
