# Anto426 Monet for Zen Browser

A wallpaper palette and shared glass material for Zen 1.23b / Gecko 157.
The existing repository and legacy `Anto426-Rofi-Dynamic` directory remain
compatible; the maintained implementation is in `palette/`.

```sh
python3 palette/render.py --palette palette/default.json --material palette/material.json --output themes/Anto426-Rofi-Dynamic
python3 scripts/verify-palette.py
```

Copy the generated `anto426/` folder and the two `user*.css` import files into
profile `chrome/`. Enable `toolkit.legacyUserProfileCustomizations.stylesheets`,
`zen.widget.linux.transparency` and `browser.tabs.allow_transparent_browser`,
then restart Zen. Existing CSS can retain a managed import rather than being
replaced. The dotfiles installer uses `profiles.ini`, preserves personal CSS and
preferences, and applies the generated roles at every wallpaper change.

`roles.css.in` owns current Gecko design-system aliases and older names;
`chrome.css.in`, `tabs.css.in`, `popups.css.in` and `content.css.in` share those
roles and the shell's radii/spacing/material. Popovers keep a readable surface.
Websites and document colors remain native. CSS palette changes require a
normal browser restart; no remote-debugging preference or JS loader is installed.

See [UPSTREAM.md](UPSTREAM.md) for dated source comparisons and coverage.
The real-browser verification is maintained by the dotfiles integration.
