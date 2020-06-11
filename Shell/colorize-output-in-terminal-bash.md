# Colorize Output in Terminal
<!-- 31 Jan 2020 -->
The ANSI escape sequences help adding color to the terminal (Doesn't work on Windows I guess)

Here is the format:

`\033[<ForegroundColorCode>;<BackgroundColorCode>;<Style>mYour Text`

where

`<ForegroundColorCode>`, `<BackgroundColorCode>` & `<Style>` are integer Color Codes.
See [Resources](##Resources) for list of colors.

Example : 
```bash
echo -e "\033[92;1mHello\033[0m"
```
Hello will be bold & green in color

## Resources

- [List of ANSI color escape sequences](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences)
- [Bash tips: Colors and formatting (ANSI/VT100 Control sequences)](https://misc.flogisoft.com/bash/tip_colors_and_formatting)
