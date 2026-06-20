
<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=24&duration=3000&pause=1000&color=8cb8e4&center=true&vCenter=true&width=500&height=80&lines=Zen+Browser+Theme;Anto426+Rofi+Style;Wallpaper+Accent+Sync" alt="Typing SVG" /></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/divider.gif" width="440" height="40" />
</p>

# <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/icon.gif" width="60px" /> About;

```sh
root@anto426: ~/zen-browser (main⚡)$ cat details.txt

A custom Zen Browser theme designed to mirror the rofi control menu palette:
  - Translucent glassmorphism surfaces
  - Perfectly integrated about:preferences (searchbox & managed notice)
  - Dynamically updated wallpaper-driven highlight accent
```

> [!NOTE]
> The dotfiles color engine (`~/.config/anto426/wallpaper_effects.sh`) automatically updates the stylesheets (`userChrome.css` and `userContent.css`) inside all active Zen Browser profiles whenever you change your wallpaper.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/divider.gif" width="440" height="40" />
</p>

# <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/icon2.gif" width="70px" /> Usage;

```sh
root@anto426: ~/zen-browser (main⚡)$ cat usage.txt

To use this theme on Zen Browser:
```

1. Copy the `userChrome.css` and `userContent.css` files from the [`themes/Anto426-Rofi-Dynamic`](themes/Anto426-Rofi-Dynamic) directory to your Zen Browser profile's `chrome` directory.
2. Enable stylesheets in your profile's `user.js` or via `about:config`:
   - Set `toolkit.legacyUserProfileCustomizations.stylesheets` to `true`.
   - Set `zen.widget.linux.transparency` to `true`.
   - Set `browser.tabs.allow_transparent_browser` to `true`.
   - Set `widget.transparent-windows` to `true`.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/divider.gif" width="440" height="40" />
</p>

# <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/icon3.gif" width="70px" /> FAQ;

- **Q:** What if I already have custom styling?
  
  **A:** You can copy and paste the generated content into your existing `userChrome.css` and/or `userContent.css` files. This way, you can keep your configurations while enjoying the dynamic colors.

- **Q:** Do I need to manually configure transparency?
  
  **A:** The `app_theme.sh` script automatically sets up the required transparency settings in all detected profiles' `user.js`.

<p align="center">
  <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/divider.gif" width="440" height="40" />
</p>

<div align="center">
  <i>Configured by anto426</i>
</div>
