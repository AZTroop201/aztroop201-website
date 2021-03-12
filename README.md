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
cd home
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
```

### Debug

```bash
hugo server -D --bind "0.0.0.0" -p 8080

#Crostini Shortcut
hugo server -D --bind "0.0.0.0" -b "http://penguin.termina.linux.test"
```