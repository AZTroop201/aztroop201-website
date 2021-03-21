# aztroop201

Arizona Troop 201 Hugo Website content

## References

- https://gohugo.io/getting-started/quick-start/

## Commands

### Create new site

```bash
hugo new site home
```

1. Download a theme into the same-named folder.
   Choose a theme from https://themes.gohugo.io/ or
   create your own with the "hugo new theme <THEMENAME>" command.
2. Perhaps you want to add some content. You can add single files
   with "hugo new <SECTIONNAME>/<FILENAME>.<FORMAT>".
3. Start the built-in live server via "hugo server".

### Theme setup

Do this in each clone

```bash
git submodule add https://github.com/budparr/gohugo-theme-ananke.git home/themes/ananke
```

### Debug

```bash
hugo server -D --bind "0.0.0.0" -p 8080

#Crostini Shortcut
hugo server -D --bind "0.0.0.0" -b "http://penguin.termina.linux.test"
```

### Publish outside of actions

```bash
git worktree add -B gh-pages public upstream/gh-pages
```

Automatic with git actions

https://github.com/peaceiris/actions-gh-pages#options



### Setup local dev env

1. Install Hugo

   ```bash
   snap install hugo
   ```

2. Clone Repo
3. Init submodules

   ```bash
   git submodule update --init --recursive
   ```
4. hugo -D