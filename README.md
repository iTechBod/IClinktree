🌐 IClinktree (Web3 Creator Hub) 

<img width="114" height="20" alt="image" src="https://github.com/user-attachments/assets/577c08d5-74e0-41a3-a19e-754bfccf8f40" />
<img width="82" height="20" alt="image" src="https://github.com/user-attachments/assets/b11dce54-35e6-4537-8bcf-85b25bcb2c6a" />

IClinktree is an open-source creator-hub starter project for the Internet Computer (ICP). It includes a Python setup wizard, a generated Motoko backend, browser-side JavaScript for canister connectivity and creator tools, and a collection of image assets.

* Network: Internet Computer mainnet (the generated configuration targets ICP; review it before deployment).
* License: MIT (see LICENSE).
* Repository: https://github.com/iTechBod/IClinktree
* Setup language: English.
* Analytics: First-party on-chain analytics. The setup wizard does not add Google Analytics or other third-party analytics tags.
* AI integration: Generates ICP service-discovery assets for compatibility with DFINITY’s ICP MCP ecosystem, allowing authorized AI clients to discover and interact with supported canister methods.

Important source-layout note: The setup wizard generates backend/main.mo, assets/script.js, DFX configuration, Motoko package configuration, JavaScript package configuration, and ICP MCP discovery assets. It does not generate the HTML/CSS page templates. A working deployment also needs the frontend files expected by the generated JavaScript, including assets/index.html and assets/styles.css, plus the image assets referenced by that page. The wizard prepares YouTube metadata for import but does not automatically upload it to the canister. A successful setup run is not proof that the project has built or deployed successfully.

Features

Creator hub and profile configuration

* Creator name and biography/subtitle configuration.
* Social profile links for YouTube, OpenChat, Telegram, X, Instagram, Facebook, Discord, GitHub, TikTok, Truth Social, Tumblr, and Bluesky.
* Optional fallback to the starter project’s default social links for fields left blank.
* ICP ecosystem dApp referral links for OpenChat, Clown, Oisy, and Randseed, with optional starter-project fallback links.
* Cryptocurrency address configuration and display support for configured assets.
* Creator-facing frontend JavaScript scaffold and canister connection logic.
* Internet Identity integration for owner authentication and protected dashboard functionality.

AI integration through ICP MCP

IClinktree generates the service-discovery configuration required for integration with DFINITY’s ICP MCP ecosystem.

This allows compatible AI clients, including supported Claude and ChatGPT MCP integrations, to discover the application’s frontend and backend canisters and access documented functionality.

Generated discovery assets

The setup wizard creates:

assets/
├── .well-known/
│   └── ic-architecture
└── .ic-assets.json5

assets/.well-known/ic-architecture

Contains the application’s service-discovery manifest, including:

* Frontend canister ID.
* Backend canister ID.
* Canister names and roles.
* Descriptions of the available application services.
* Information about public and authenticated backend functionality.

assets/.ic-assets.json5

Configures the legacy DFX asset canister to include the hidden .well-known directory when deploying the frontend.

It also configures the correct JSON content type for the extensionless ic-architecture manifest.

Without this configuration, the asset canister may omit the hidden discovery directory.

AI-accessible backend methods

The generated backend includes a documentation method:

getApiDoc()

This method describes the backend API, its read methods, owner identity requirements, and security restrictions.

The documented methods include:

Method	Access	Purpose
getApiDoc()	Public read	Explains available API functionality and permissions.
getAllVideos()	Public read	Retrieves the creator’s video library.
getTrafficStats()	Owner/publisher only	Retrieves protected website analytics.
getMyPrincipal()	Public query	Returns the caller’s Internet Computer principal.

The backend also has protected management methods, including video-library management and ticket/key-management operations.

These are not intended to be exposed as unrestricted AI operations.

Owner authentication with Internet Identity

The setup wizard asks for a Master/Owner Principal ID.

This principal is used by the generated backend to protect owner-specific functionality.

For AI access to private owner data:

1. Deploy the generated frontend and backend.
2. Make the discovery manifest publicly accessible through the deployed frontend.
3. Configure a compatible AI client to use DFINITY’s ICP MCP integration.
4. Authenticate using the owner’s Internet Identity.
5. Authorize the requested access.
6. Ask the AI to retrieve supported information from the backend.

Important Internet Identity consideration:

Internet Identity generates application-specific principals based on the application origin.

The principal used by the AI connector must match the configured owner principal.

Use the same canonical frontend origin that was used when registering or obtaining the owner’s application-specific principal. Using a different domain or frontend origin may produce a different principal and cause owner authorization to fail.

Example AI queries

After successful authentication and authorization, the owner can ask supported AI clients questions such as:

* How many visitors did my website receive?
* Which countries generate the most traffic?
* What are my most popular tutorials?
* Show me my website’s traffic statistics.
* Retrieve my video library.
* Analyze the available creator-hub data.
* Explain my backend API and its available functionality.

The AI can only retrieve information exposed by the backend and permitted to the authenticated principal.

Permissions and security

* Public video-library queries remain publicly accessible.
* Traffic analytics require the configured owner or publisher principal.
* Ticket and key-management operations remain access-controlled.
* The AI connector should use read-only or Questions-only permissions when the owner only needs data retrieval.
* Do not authorize state-changing operations unless they are explicitly required and reviewed.
* Never expose private keys, recovery phrases, vetKeys material, or authentication secrets to an AI client.

Important: Generating the discovery manifest does not automatically connect Claude or ChatGPT, create an Internet Identity session, or grant permissions. The owner must configure a compatible MCP client and complete its authentication and authorization process.

Publishing the discovery manifest also opts the application into DFINITY’s ICP MCP ecosystem and constitutes acceptance of the applicable App Operator Terms. Review those terms before deployment.

Documentation:

* https://docs.internetcomputer.org/guides/frontends/service-discoverability/
* https://internetcomputer.org/icp-mcp/

30-day on-chain traffic analytics

The generated backend retains eligible analytics events for a rolling 30-day window and periodically prunes older records.

The generated analytics view can report:

* Pageviews during the retention window.
* Unique visitor/device identifiers.
* Button/link click totals and most-clicked links.
* Daily pageview counts across the 30-day window, including the daily total and peak day in the frontend display.
* Top countries, device types, and browsers.
* Most frequent tutorial searches.
* Searches that returned no matching videos.

Analytics access is restricted in the backend to the configured owner and publisher principals. Other callers do not receive the analytics result.

Analytics can also be retrieved by a properly authenticated AI client through the ICP MCP integration.

Visitor consent and collection

* The generated frontend presents a traffic-consent choice and stores the choice in browser local storage.
* The browser sends analytics events only when the visitor has accepted.
* The backend independently rejects events unless the consent value is accepted.
* Visitors who do not accept are not included in the analytics event log.
* The backend validates the lengths of submitted fields and applies a global request-throttling mechanism to reduce event flooding.
* Analytics data is stored in the application canister; it is not sent to Google Analytics by this setup wizard.

The analytics system is first-party application functionality, not a replacement for a formal privacy notice or a legal compliance review. Explain the collection and retention practices to visitors in your own privacy notice.

Encrypted visitor tickets and messaging

* Optional encrypted visitor ticket/messaging feature.
* Ticket payload encryption/decryption support using the Internet Computer vetKeys SDK.
* Ticket management methods for the configured owner.
* Owner-side inbox actions include viewing, marking read/unread, archiving, and deleting tickets, including clearing the inbox.
* Ticket retention is configurable in the setup wizard from 1 to 3,650 days; the default is 7 days.
* The backend periodically prunes expired tickets.
* Ticket storage and management methods are omitted from the generated backend when the ticket feature is disabled.

The setup wizard asks for a Master/Owner Principal ID. The terminal’s active DFX identity is used as the publisher principal when it can be read; otherwise, the owner principal is used as the publisher fallback.

Review both generated principal values before deployment.

vetKeys controls

* Uses the Internet Computer vetKeys interface for the ticket-encryption key workflow.
* Restricts key derivation to the configured owner and publisher principals.
* Applies a five-second minimum interval between key-derivation requests.
* Validates the submitted transport public-key size.
* The generated backend adds cycles to the vetKD derivation call; ensure the canister has sufficient cycles and test the workflow on a non-production canister first.

Video library and tutorial search

* Generated Motoko video-library storage and search methods.
* askBot searches the seeded video library and returns matching tutorial records.
* Search matching includes title, description, and searchableText.
* Includes a small synonym map for selected Apple, crypto, and ICP-related terms.
* Authorized owner/publisher methods support seeding and clearing the video library.
* Public query access to the video-library records is exposed by the generated backend.
* getAllVideos() provides a public read-only method for retrieving the video library.
* AI clients can use the public video-library query when supported by their ICP MCP integration.

YouTube metadata import preparation

The wizard can inspect the configured YouTube channel/videos URL using yt-dlp and write normalized records to:

video_library_import.json

Each record contains a title, video URL, description, searchable text, and timestamp.

This step:

* Does not download the video files.
* Does not upload the records to the canister.
* Does not automatically call seedVideos.

Use a separate, reviewed seeding workflow to import the JSON records into the deployed backend. Install yt-dlp as described below if you want the wizard to perform metadata extraction.

Architecture and canister cost

The standard website architecture uses two canisters:

1. Backend canister — Motoko application logic, video library, analytics event storage, and (if enabled) encrypted visitor tickets.
2. Frontend/website canister — serves the static website assets, including the ICP MCP discovery manifest.

The ICP MCP integration does not require a separate AI canister.

The wizard does not require two additional backup canisters. It does not create, deploy, synchronize, or restore backup canisters.

Optional registration of existing backup canister IDs

After your normal website deployment, you may optionally run:

python3 setup.py --configure-backups

This asks whether you want to record two existing backup canister IDs in:

backup_canisters.json

This is only local configuration. It does not:

* Create or deploy backup canisters.
* Install backup-vault code.
* Copy live canister state.
* Synchronize data between canisters.
* Provide an automatic restore operation.

Registering IDs does not itself create a backup or add a canister cost. Do not create or fund extra canisters on the assumption that this option provides automatic redundancy.

Prerequisites

Install and initialize:

* DFINITY Canister SDK (dfx): https://internetcomputer.org/docs/building-apps/getting-started/install
* Python 3.9 or newer
* yt-dlp for YouTube playlist metadata extraction: python3 -m pip install yt-dlp
* Motoko package manager (mops) if you use the generated mops.toml
* A valid Internet Identity account for owner authentication.
* A compatible MCP client and access to DFINITY’s ICP MCP integration if you intend to use AI-assisted canister access.

Check your DFX installation and active identity:

dfx --version
dfx identity whoami
dfx identity get-principal

The active DFX identity is used as the publisher principal when available. Make sure the principals configured by the wizard have the intended permissions on the canisters.

Quick start

git clone https://github.com/iTechBod/IClinktree.git
cd IClinktree
python3 setup.py

If you want YouTube metadata extraction, install yt-dlp first:

python3 -m pip install yt-dlp

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

The wizard also generates:

* ICP MCP service-discovery manifest.
* Legacy asset-canister configuration for serving the discovery manifest.
* Backend API documentation for compatible AI clients.

Review every generated file and configured principal before building or deploying.

Before deploying

1. Confirm that the required frontend template files exist. The setup wizard does not create assets/index.html or assets/styles.css.
2. Confirm that all image files referenced by the frontend are present in assets/images/.
3. Review backend/main.mo, especially owner/publisher authorization, ticket settings, analytics retention, and vetKeys calls.
4. Review assets/script.js, including the consent interface, canister IDs, and frontend behavior.
5. Inspect assets/.well-known/ic-architecture and confirm that both canister IDs and descriptions are correct.
6. Confirm that assets/.ic-assets.json5 includes the discovery manifest and that the frontend asset canister will serve it correctly.
7. Confirm that your deploying DFX identity has the required controller permissions for both the backend and frontend canisters.
8. Confirm that the generated canister IDs and network settings are correct.
9. Review DFINITY’s applicable ICP MCP App Operator Terms before publishing the discovery manifest.
10. Build and test before upgrading or deploying to production.

Example commands, once the complete frontend templates and project files are present:

mops install
dfx build --network ic
dfx deploy --network ic

After deployment, verify that the discovery manifest is publicly accessible at:

https://YOUR-FRONTEND-CANISTER-ID.icp0.io/.well-known/ic-architecture

Confirm that the returned document contains the correct frontend and backend canister IDs.

For AI integration, configure a compatible client using DFINITY’s ICP MCP service and complete the owner’s Internet Identity authentication and authorization.

These are example deployment commands. The current setup.py generates project files but does not run dfx build or dfx deploy, and it does not guarantee that the supplied project is deployable without the missing frontend templates.

Generated and supporting files

File	Purpose
backend/main.mo	Generated Motoko backend, including video library, analytics, vetKeys integration, optional ticket methods, and AI-readable API documentation
assets/script.js	Generated browser-side application logic, canister connection, consent handling, analytics display, tutorial search, and ticket UI
assets/.well-known/ic-architecture	ICP MCP service-discovery manifest describing the frontend and backend canisters
assets/.ic-assets.json5	Configures the legacy asset canister to include and correctly serve the hidden discovery manifest
dfx.json	DFX canister and network configuration
canister_ids.json	Canister ID mapping/configuration
mops.toml	Motoko package configuration
package.json	JavaScript package/dependency metadata
video_library_import.json	YouTube metadata prepared for manual/separate canister seeding, when extraction succeeds
backup_canisters.json	Optional local record of two existing backup canister IDs; created only by --configure-backups
requirements.txt	Python dependency declarations supplied with the repository
LICENSE	MIT license text

The wizard may update or create configuration files as part of its run. Review the actual generated files in your checkout rather than assuming every optional file will always be present.

Image assets

The repository’s assets/images/ directory contains the starter project’s profile, social, cryptocurrency, and Open Graph image assets. The wizard prompts you to check that these assets are present; it does not create a replacement profile image.

To use your own profile photo, replace the expected profile image while preserving the filename used by your HTML template, or update the template’s image path. Check the icon filenames and paths before changing them.

Security and operational notes

* Never commit private keys, recovery phrases, access tokens, or other secrets.
* Treat backup_canisters.json as local infrastructure configuration. Do not commit it unless you deliberately intend to publish those canister IDs.
* Canister IDs are identifiers, not backups or authentication credentials.
* Analytics are retained for up to 30 days by the generated backend; ticket retention is separately configured in the wizard.
* Analytics collection requires visitor consent in the generated frontend and is also checked by the backend.
* Analytics queries and ticket/key-management operations are principal-restricted as described above.
* The generated rate limits are basic abuse controls, not a complete denial-of-service defense.
* vetKeys derivation consumes cycles. Monitor canister cycles and test the encryption/decryption flow before production use.
* The YouTube metadata JSON is not automatically uploaded. Validate it and use a separate seeding workflow.
* The ICP MCP discovery manifest makes service information publicly discoverable; it does not make private backend data public by itself.
* Owner-only analytics access depends on the caller’s principal matching the configured owner or publisher principal.
* Internet Identity application-specific principals can differ across frontend origins. Use the same canonical origin when authenticating through the AI connector.
* Prefer read-only AI permissions for analytics and data retrieval. Review any requested state-changing permissions carefully.
* Publishing the discovery manifest constitutes acceptance of the applicable DFINITY App Operator Terms.
* Test upgrades on a local replica or disposable canister before changing a production canister.
* Keep your own source-code and deployment-configuration copies in a secure location. This setup wizard does not back up live canister stable memory or application data.

License

IClinktree is distributed under the MIT License. See LICENSE.

Built with passion on the Internet Computer Protocol.
