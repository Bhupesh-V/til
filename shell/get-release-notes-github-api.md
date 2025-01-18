# Get Release notes from Github API


Getting release notes for your favourite tool is a piece of cake using the [GitHub Releases API](https://docs.github.com/en/rest/reference/repos#releases)

```bash
REMOTE_REPO="Bhupesh-V/ugit"
curl -s -L https://api.github.com/repos/$REMOTE_REPO/releases | awk -F=":" '/body/ {print $1;exit}' | cut -d ':' -f 2 | tr -d "\""
```

Note that the curl to the `/releases` endpoint will give all the releases. But we only want the latest changelog here.
`awk -F=":" '/body/ {print $1;exit}'` will get the first release which is stored inside the _body_ property and exit immediately.

