# Auto-correct Git commands
**_Posted on 24 Jun, 2021_** 


> [**help.autocorrect**](https://git-scm.com/docs/git-config#Documentation/git-config.txt-helpautoCorrect) docs

Git offers correcting misspelled git commands within a timed interval

```bash
# run the correct command after 0.7 seconds
git config --global help.autocorrect 7
```

Or in your global `.gitconfig`

```gitconfig
[help]
        # default 0
        # negative value to run correct command immediately
	autocorrect = 7
```

Now test it by running `git sttus`

![git-auto-correct-demo](https://user-images.githubusercontent.com/34342551/123370921-599de080-d59e-11eb-84fa-375c399fa61f.gif)

