Title: Regular expressions
Date: 2018-08-08 13:48
Authors: José Aniceto


## Regex for finding URLs

Regex if you want to ensure URL starts with HTTP/HTTPS:

```regex
https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)
```

If you do not require HTTP protocol:

```regex
[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)
```

#### Exemple usage in VSCode to find a URL and convert to Markdown link like, `[link](link)`:

Find: `(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))`

Replace: `[$1]($1)`

Use `()` to create a group and `$1` to reference that group.
