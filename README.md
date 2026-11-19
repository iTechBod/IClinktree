# 🌐 IClinktree (Web3 Creator Hub) <img width="170" height="20" alt="image" src="https://github.com/user-attachments/assets/34ca1631-e1b7-4c42-8ff3-8952baf19064" />
<img width="114" height="20" alt="image" src="https://github.com/user-attachments/assets/577c08d5-74e0-41a3-a19e-754bfccf8f40" />
<img width="82" height="20" alt="image" src="https://github.com/user-attachments/assets/b11dce54-35e6-4537-8bcf-85b25bcb2c6a" />

IClinktree is an open-source creator-hub starter project for the Internet Computer (ICP). It includes a Python setup wizard, a generated Motoko backend, browser-side JavaScript for canister connectivity and creator tools, and a collection of image assets.

- **Network:** Internet Computer mainnet (the generated configuration targets ICP; review it before deployment)
- **License:** MIT (see [`LICENSE`](LICENSE))
- **Repository:** https://github.com/iTechBod/IClinktree
- **Setup language:** English
- **Third-party analytics tags:** The setup wizard does not add Google Analytics or other third-party analytics tags. Its analytics are implemented in the generated application and stored in the backend canister.

> **Important source-layout note:** The setup wizard generates `backend/main.mo` and `assets/script.js`, along with DFX, Motoko package, and JavaScript package configuration. It does **not** generate the HTML/CSS page templates. A working deployment also needs the frontend files expected by the generated JavaScript, including `assets/index.html` and `assets/styles.css`, plus the image assets referenced by that page. The wizard prepares YouTube metadata for import but does not automatically upload it to the canister. A successful setup run is not proof that the project has built or deployed successfully.

## Features

### Creator hub and profile configuration

- Creator name and biography/subtitle configuration.
- Social profile links for YouTube, OpenChat, Telegram, X, Instagram, Facebook, Discord, GitHub, TikTok, Truth Social, Tumblr, and Bluesky.
- Optional fallback to the starter project's default social links for fields left blank.
- ICP ecosystem dApp referral links for OpenChat, Clown, Oisy, and Randseed, with optional starter-project fallback links.
- Cryptocurrency address configuration and display support for the configured assets.
- Creator-facing frontend JavaScript scaffold and canister connection logic.

### 30-day on-chain traffic analytics

The generated backend retains eligible analytics events for a rolling **30-day window** and periodically prunes older records.

The generated analytics view can report:

- Pageviews during the retention window.
- Unique visitor/device identifiers.
- Button/link click totals and most-clicked links.
- Daily pageview counts across the 30-day window, including the daily total and peak day in the frontend display.
- Top countries, device types, and browsers.
- Most frequent tutorial searches.
- Searches that returned no matching videos.

Analytics access is restricted in the backend to the configured **owner** and **publisher** principals. Other callers do not receive the analytics result.

#### Visitor consent and collection

- The generated frontend presents a traffic-consent choice and stores the choice in browser local storage.
- The browser sends analytics events only when the visitor has accepted.
- The backend independently rejects events unless the consent value is `accepted`.
- Visitors who do not accept are not included in the analytics event log.
- The backend validates the lengths of submitted fields and applies a global request-throttling mechanism to reduce event flooding.
- Analytics data is stored in the application canister; it is not sent to Google Analytics by this setup wizard.

The analytics system is first-party application functionality, not a replacement for a formal privacy notice or a legal compliance review. Explain the collection and retention practices to visitors in your own privacy notice.

### Encrypted visitor tickets and messaging

- Optional encrypted visitor ticket/messaging feature.
- Ticket payload encryption/decryption support using the Internet Computer vetKeys SDK.
- Ticket management methods for the configured owner.
- Owner-side inbox actions include viewing, marking read/unread, archiving, and deleting tickets, including clearing the inbox.
- Ticket retention is configurable in the setup wizard from **1 to 3,650 days**; the default is **7 days**.
- The backend periodically prunes expired tickets.
- Ticket storage and management methods are omitted from the generated backend when the ticket feature is disabled.

The setup wizard asks for a **Master/Owner Principal ID**. The terminal's active DFX identity is used as the publisher principal when it can be read; otherwise, the owner principal is used as the publisher fallback. Review both generated principal values before deployment.

### vetKeys controls

- Uses the Internet Computer vetKeys interface for the ticket-encryption key workflow.
- Restricts key derivation to the configured owner and publisher principals.
- Applies a five-second minimum interval between key-derivation requests.
- Validates the submitted transport public-key size.
- The generated backend adds cycles to the vetKD derivation call; ensure the canister has sufficient cycles and test the workflow on a non-production canister first.

### Video library and tutorial search

- Generated Motoko video-library storage and search methods.
- `askBot` searches the seeded video library and returns matching tutorial records.
- Search matching includes title, description, and `searchableText`.
- Includes a small synonym map for selected Apple, crypto, and ICP-related terms.
- Authorized owner/publisher methods support seeding and clearing the video library.
- Public query access to the video-library records is exposed by the generated backend.

#### YouTube metadata import preparation

The wizard can inspect the configured YouTube channel/videos URL using `yt-dlp` and write normalized records to:

```text
video_library_import.json
```

Each record contains a title, video URL, description, searchable text, and timestamp. This step:

- Does not download the video files.
- Does not upload the records to the canister.
- Does not automatically call `seedVideos`.

Use a separate, reviewed seeding workflow to import the JSON records into the deployed backend. Install `yt-dlp` as described below if you want the wizard to perform metadata extraction.

## Architecture and canister cost

The standard website architecture uses **two canisters**:

1. **Backend canister** — Motoko application logic, video library, analytics event storage, and (if enabled) encrypted visitor tickets.
2. **Frontend/website canister** — serves the static website assets.

The wizard does not require two additional backup canisters. It does not create, deploy, synchronize, or restore backup canisters.

### Optional registration of existing backup canister IDs

After your normal website deployment, you may optionally run:

```bash
python3 setup.py --configure-backups
```

This asks whether you want to record two existing backup canister IDs in:

```text
backup_canisters.json
```

This is only local configuration. It does **not**:

- Create or deploy backup canisters.
- Install backup-vault code.
- Copy live canister state.
- Synchronize data between canisters.
- Provide an automatic restore operation.

Registering IDs does not itself create a backup or add a canister cost. Do not create or fund extra canisters on the assumption that this option provides automatic redundancy.

## Prerequisites

Install and initialize:

- **DFINITY Canister SDK (`dfx`):** https://internetcomputer.org/docs/building-apps/getting-started/install
- **Python 3.9 or newer**
- **`yt-dlp`** for YouTube playlist metadata extraction: `python3 -m pip install yt-dlp`
- **Motoko package manager (`mops`)** if you use the generated `mops.toml`

Check your DFX installation and active identity:

```bash
dfx --version
dfx identity whoami
dfx identity get-principal
```

The active DFX identity is used as the publisher principal when available. Make sure the principals configured by the wizard have the intended permissions on the canisters.

## Quick start

```bash
git clone https://github.com/iTechBod/IClinktree.git
cd IClinktree
python3 setup.py
```

If you want YouTube metadata extraction, install `yt-dlp` first:

```bash
python3 -m pip install yt-dlp
```

The wizard prompts for:

1. Owner/Master Principal ID.
2. Whether to enable encrypted visitor tickets.
3. Ticket retention period, if tickets are enabled.
4. Creator name, biography, and YouTube channel/videos URL.
5. Social media links and whether to use fallback links for blank fields.
6. ICP ecosystem dApp referral links and optional fallback links.
7. Cryptocurrency address configuration.
8. Existing frontend and backend canister IDs and other deployment configuration requested by the wizard.
9. Confirmation that the relevant canister controller permissions and image assets have been checked.

Review every generated file and configured principal before building or deploying.

## Before deploying

1. Confirm that the required frontend template files exist. The setup wizard does not create `assets/index.html` or `assets/styles.css`.
2. Confirm that all image files referenced by the frontend are present in `assets/images/`.
3. Review `backend/main.mo`, especially owner/publisher authorization, ticket settings, analytics retention, and vetKeys calls.
4. Review `assets/script.js`, including the consent interface, canister IDs, and frontend behavior.
5. Confirm that your deploying DFX identity has the required controller permissions for both the backend and frontend canisters.
6. Confirm that the generated canister IDs and network settings are correct.
7. Build and test before upgrading or deploying to production.

Example commands, once the complete frontend templates and project files are present:

```bash
mops install
dfx build --network ic
dfx deploy --network ic
```

These are example deployment commands. The current `setup.py` generates project files but does **not** run `dfx build` or `dfx deploy`, and it does not guarantee that the supplied project is deployable without the missing frontend templates.

## Generated and supporting files

| File | Purpose |
|---|---|
| `backend/main.mo` | Generated Motoko backend, including video library, analytics, vetKeys integration, and optional ticket methods |
| `assets/script.js` | Generated browser-side application logic, canister connection, consent handling, analytics display, tutorial search, and ticket UI |
| `dfx.json` | DFX canister and network configuration |
| `canister_ids.json` | Canister ID mapping/configuration |
| `mops.toml` | Motoko package configuration |
| `package.json` | JavaScript package/dependency metadata |
| `video_library_import.json` | YouTube metadata prepared for manual/separate canister seeding, when extraction succeeds |
| `backup_canisters.json` | Optional local record of two existing backup canister IDs; created only by `--configure-backups` |
| `requirements.txt` | Python dependency declarations supplied with the repository |
| `LICENSE` | MIT license text |

The wizard may update or create configuration files as part of its run. Review the actual generated files in your checkout rather than assuming every optional file will always be present.

## Image assets

The repository's `assets/images/` directory contains the starter project's profile, social, cryptocurrency, and Open Graph image assets. The wizard prompts you to check that these assets are present; it does not create a replacement profile image.

To use your own profile photo, replace the expected profile image while preserving the filename used by your HTML template, or update the template's image path. Check the icon filenames and paths before changing them.

## Security and operational notes

- Never commit private keys, recovery phrases, access tokens, or other secrets.
- Treat `backup_canisters.json` as local infrastructure configuration. Do not commit it unless you deliberately intend to publish those canister IDs.
- Canister IDs are identifiers, not backups or authentication credentials.
- Analytics are retained for up to 30 days by the generated backend; ticket retention is separately configured in the wizard.
- Analytics collection requires visitor consent in the generated frontend and is also checked by the backend.
- Analytics queries and ticket/key-management operations are principal-restricted as described above.
- The generated rate limits are basic abuse controls, not a complete denial-of-service defense.
- vetKeys derivation consumes cycles. Monitor canister cycles and test the encryption/decryption flow before production use.
- The YouTube metadata JSON is not automatically uploaded. Validate it and use a separate seeding workflow.
- Test upgrades on a local replica or disposable canister before changing a production canister.
- Keep your own source-code and deployment-configuration copies in a secure location. This setup wizard does not back up live canister stable memory or application data.

## License

IClinktree is distributed under the MIT License. See [`LICENSE`](LICENSE).

Built with passion on the Internet Computer Protocol.
