🌐 IClinktree (Web3 Creator Hub) <img width="170" height="20" alt="image" src="https://github.com/user-attachments/assets/34ca1631-e1b7-4c42-8ff3-8952baf19064" />
<img width="114" height="20" alt="image" src="https://github.com/user-attachments/assets/577c08d5-74e0-41a3-a19e-754bfccf8f40" />
<img width="82" height="20" alt="image" src="https://github.com/user-attachments/assets/b11dce54-35e6-4537-8bcf-85b25bcb2c6a" />


IClinktree is an open-source creator-hub starter project for the Internet Computer (ICP). It includes a Python setup wizard, a Motoko backend generator, browser-side JavaScript for the canister connection and creator tools, and a collection of image assets.

- **Network:** Internet Computer mainnet
- **License:** MIT (see [`LICENSE`](LICENSE))
- **Repository:** https://github.com/iTechBod/IClinktree
- **Language:** English setup flow (no Persian-language setup mode)
- **Third-party analytics tags:** None are added by this setup wizard.

> **Important repository note:** The source archive supplied for this update contains `setup.py`, `README.md`, `LICENSE`, and `assets/images/`. It does not contain `assets/index.html`, `assets/styles.css`, or a `push.py` uploader. The wizard generates `backend/main.mo`, `assets/script.js`, and the DFX/package configuration, but it does not generate the missing HTML/CSS template or upload the scraped YouTube entries. A complete website deployment therefore requires those frontend template files and a video-seeding workflow to be supplied separately. Do not interpret a successful setup.py run as proof that the website has been deployed.

## Features represented by the current setup generator

- Motoko backend scaffold with video-search methods, traffic-event storage, and an encrypted visitor-ticket interface.
- Browser JavaScript scaffold for Internet Identity authentication, canister calls, ticket handling, traffic statistics, tutorial search, and crypto-address display.
- Config generation for `dfx.json`, `canister_ids.json`, `mops.toml`, and `package.json`.
- Creator profile, social-link, dApp referral, and cryptocurrency-address prompts.
- YouTube playlist metadata inspection through `yt-dlp` (the current wizard does not upload those entries to the canister).
- Local source/configuration ZIP backup after setup generation.
- Optional recording of two already-existing backup canister IDs after the website has been deployed.

## Architecture and canister cost

The standard deployment uses **two canisters**:

1. **Backend** — Motoko application logic and on-chain data.
2. **Website** — static frontend assets.

The two optional backup canister IDs are **not required**. The setup wizard does not create or deploy them, and it does not install backup-vault code, automatically copy canister state, synchronize data, or provide a restore operation. It only records IDs supplied by the user in a local `backup_canisters.json` file for a future/manual workflow. Do not pay for extra canisters on the assumption that ID registration itself creates a backup.

The wizard also creates a local ZIP archive of the project files in `local_backups/`. This is a **source-code/configuration backup**, not a backup of live canister stable memory, visitor tickets, analytics, or other on-chain state. Keep a copy somewhere separate from your computer.

## Prerequisites

Install and initialize:

- DFINITY Canister SDK (`dfx`): https://internetcomputer.org/docs/building-apps/getting-started/install
- Python 3.9 or newer
- `yt-dlp`: `python3 -m pip install yt-dlp`
- Motoko package manager (`mops`) if you use the generated `mops.toml`

Check that DFX is available:

```bash
dfx --version
dfx identity whoami
dfx identity get-principal
```

## Quick start

```bash
git clone https://github.com/iTechBod/IClinktree.git
cd IClinktree
python3 -m pip install -r requirements.txt
python3 setup.py
```

The wizard asks for the owner principal, ticket-retention preference, creator profile, social links, dApp referrals, crypto addresses, and existing frontend/backend canister IDs. It then writes the generated configuration and source files and creates a timestamped local source backup under `local_backups/`.

### Before deploying

1. Review the generated `backend/main.mo` and `assets/script.js`.
2. Confirm that the required frontend files exist. In this repository snapshot, `assets/index.html` and `assets/styles.css` are not included and must be added before deploying a working website.
3. Confirm that the backend and website canisters exist and that your deploying DFX identity has the required controller permissions.
4. Review the generated canister IDs and network configuration.
5. Build and deploy using your own verified DFX workflow. The current `setup.py` does **not** run `dfx deploy`.

Example commands, after the missing frontend template and all required project files have been supplied:

```bash
mops install
dfx build --network ic
dfx deploy --network ic
```

These commands are examples, not a guarantee that the incomplete source archive is deployable as-is.

## Optional backup canister IDs — after deployment

Only after your normal website deployment is complete, you can run:

```bash
python3 setup.py --configure-backups
```

The wizard asks whether you want to record two existing backup canister IDs. If you answer yes, it writes:

```text
backup_canisters.json
```

If you answer no, the standard two-canister setup remains unchanged. The optional IDs are simply recorded locally; no extra canister is created, charged, deployed, or synchronized by this command.

## Local source backup

Every normal setup run creates an archive similar to:

```text
local_backups/iclinktree-source-YYYYMMDD-HHMMSS.zip
```

It includes project source/configuration and image assets while excluding `.git`, `.dfx`, `.mops`, virtual environments, dependency folders, and previous local backup archives. It does not include live canister state. Copy this ZIP to another drive or secure storage location.

## Image assets

The repository already includes an `assets/images/` directory with the current profile image, social icons, crypto icons, and `og-cover.png`. You do not need to add another OG cover just to run the setup generator. Replace the profile image with your own while preserving the filename expected by your frontend template, or update that template's image path. Review the social/crypto icon filenames before changing them.

## Files generated by setup.py

| File | Purpose |
|---|---|
| `backend/main.mo` | Generated Motoko backend source |
| `assets/script.js` | Generated browser-side application logic |
| `dfx.json` | DFX canister/network configuration |
| `canister_ids.json` | Mainnet canister ID mapping |
| `mops.toml` | Motoko dependencies |
| `package.json` | JavaScript dependency metadata |
| `local_backups/*.zip` | Local source/configuration snapshots |
| `backup_canisters.json` | Created only if optional backup IDs are recorded |
| `requirements.txt` | Python dependency for YouTube metadata inspection |
| `.gitignore` | Excludes local backups, DFX build output, and optional local backup IDs |

## Security and operational notes

- Never publish private keys, recovery phrases, access tokens, or other secrets in this repository.
- Treat `backup_canisters.json` as local infrastructure configuration; do not commit it unless you intentionally want those canister IDs public.
- Canister IDs are not credentials, but public registration does not provide backup functionality.
- The local ZIP is not a substitute for exporting or otherwise backing up important live canister data.
- Test changes on a local replica or a disposable canister before upgrading a production canister.

## License

IClinktree is distributed under the MIT License. See [`LICENSE`](LICENSE).

Built with passion on the Internet Computer Protocol.
