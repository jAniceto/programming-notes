# Pelican - Static Site Genarator

1) Create `.md` articles in the `content` directory.

2) To deploy the site it to production run:

```
cd programming-notes-blog\src
pelican content -s publishconf.py
```

3) Copy the files in the `output` directory to the root of `programming-notes-blog`.

4) Push to Github