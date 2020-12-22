# tmux

* [Room - tmux](https://tryhackme.com/room/rptmux)

---

## Introduction

* `apt install tmux`

* `tmux` - Create unnamed session.

* `<Ctrl+b>` - Leader key.

---

## Sessions

* `<Ctrl+b> d` - Detach session.

* `tmux a -t 0` -0 attach to session 0.

* `nmap -sV -vv -sC 10.10.215.166`

* `<Ctrl+b> [` - Enter `copy mode`. Works like `less`.

    * `g` - Go to top.

    * `G` - Go to bottom.

    * `q` - Exit copy mode.

---

## Windows

* `<Ctrl+b> c` - Create new window.

* `<Ctrl+b> N` - Goto next window.

* `<Ctrl+b> P` - Goto previous window.

---

## Panes

* `<Ctrl+b> %` - Vertically split window into pane.

* `<Ctrl+b> "` - Horizontally split window into pane.

* `<Ctrl+b> <arrow-key>` - Navigate between panes.

* `<Ctrl+b>+<arrow-key>` - Resize panes. (Hold down leader whilst pressing arrow keys).

* `<Ctrl+b> x` - Kill pane.

* `exit` - Close pane.

---

## Resources

* [Cheat Sheet](https://imgur.com/bL9Dn3U)

* [Learning Tmux - Video](https://www.youtube.com/watch?v=Lqehvpe_djs)










