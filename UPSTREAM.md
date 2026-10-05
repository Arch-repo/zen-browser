# Compatibility audit, 5 October 2026

The existing fork retained Catppuccin's MIT license. The latest Catppuccin
source, `c855685442c6040c4dda9c8d3ddc7b708de1cbaa` (28 September 2025), was
reviewed in full, including the four flavours and their shared templates.
It fixes the URL bar background but does not cover current Zen chrome alone.

Additional current references reviewed for changed selectors and behavior:

| Reference | Revision/date | Findings used |
| --- | --- | --- |
| [Zen 1.23b](https://github.com/zen-browser/desktop/releases/tag/1.23b) | `c6acdfeef8e60fe8856f2cb2007299c7241aab98`, 3 October 2026 | Actual shipped Gecko 157 CSS, toolbar pseudo-elements, fields, popup parts, workspace/folder/media classes |
| [Natsumi Browser](https://github.com/greeeen-dev/natsumi-browser) | `6002858f7766389a0b6a3bf0834e68ba56d603b3`, 2 October 2026 | Modular theme boundaries, current sidebar and URL bar hooks; no Sine/JS loader imported |
| [Transparent Zen](https://github.com/sameerasw/zen-themes/tree/main/TransparentZen) | `b8e80bfbe3ed1bc4b7fd4859d3c12ffbf0682226`, 13 September 2026 | Linux/browser transparency preferences, preserving native content behavior |
| [Nebula](https://github.com/JustAdumbPrsn/Zen-Nebula) | `31ba4a3bde77391e173a6a3460d9fb0ab9bca8a0`, 7 May 2026 | Native split/compact boundaries, current selectors for the URL bar, essentials and media |

The similarly named `Psychosoc1al/natsumi` repository is an old February 2025
fork and was excluded as a current baseline. These are references, not runtime
dependencies: their optional layout rewrites, scripts and animation engines are
not installed. The canonical implementation here receives the shared desktop
palette and `application-material.json`; there are no private fixed theme colors.

## Coverage

| Surface | Implementation |
| --- | --- |
| Main background, toolbars, single-toolbar and compact modes | `chrome.css.in`; native background paints one shared panel tint |
| URL bar, floating omnibox, suggestions and keyboard focus | `chrome.css.in`, modern/legacy role aliases |
| Tabs, essentials, folders, containers, workspaces | `tabs.css.in`; native visibility/geometry preserved |
| App menu, permissions, bookmarks, folder/workspace popup, sidebar notifications and toast | `popups.css.in`; opaque popover role keeps contrast, like GTK/Qt |
| Stacked media cards, progress, Glance, split view and status | `chrome.css.in`; current class selectors, no visibility overrides |
| Preferences, add-ons, downloads, config, new tab and blank | `content.css.in`; scoped internal documents |
| Gecko moz-button/input/toggle/card and earlier XUL controls | `roles.css.in`; modern design system plus legacy aliases |

Ordinary websites, reader documents, PDF pages and security indicator colors
remain native. Text is opaque; HyprGlass samples the real desktop through the
browser's alpha background. CSS does not capture or imitate the desktop itself.

Zen's backdrop owns the single panel tint. Internal pages have transparent
canvases so they do not multiply that alpha; cards still receive the shared
surface role. The integration test on Zen 1.23b exercises the real native popup,
preferences, text/geometry roles and live changes below the GPU-composited window.
