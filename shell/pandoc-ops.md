# Pandoc Ops

## Images to PDF

Each image as new page in PDF.

```
ls *.jpg | sort -V | awk '{print "![](" $0 "){width=\\paperwidth}\n\\newpage"}' | pandoc -f markdown -o output.pdf -V geometry:margin=0in
```

Problem: There's un-ncessary padding on the right side of the page.