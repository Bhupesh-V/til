# Seamlessly Exporting Environment Variables for both Shell & VS Code Debugger
**_Posted on 08 Jan, 2025_**

## The Problem

`.env` is a common pattern to store environment variables in a project.

If you are directly executing your project from the shell, you would expect the environment variables to be exported to the shell, in that case the `.env` file would look like this:

```shell
export VAR1=value1
export VAR2=value2
```

Which can later be sourced by the shell using `source .env`.

However, this file format is not compatible with the VS Code debugger `launch.json` file, which expects the `.env` file to look like this:

```shell
VAR1=value1
VAR2=value2
```

> Tip: Sample `launch.json` configuration for Go projects which uses `.env` file:

```json
{
  "configurations": [
    {
      "name": "Launch file",
      "type": "go",
      "request": "launch",
      "mode": "debug",
      "program": "main.go",
      "envFile": "${workspaceFolder}/.env",
    }
  ]
}
```

This calls for creating 2 different versions of the `.env` file, one for the shell & one for the debugger, which is of-course not ideal.

## The solution

We can create a single `.env` file that can be sourced by both the shell and the debugger.

```shell
VAR1=value1
VAR2=value2
```

Since this format is already compatible with VS Code, all we need to do is to export the environment variables to the shell and its child processes.

```shell
export $(grep --color=never -v '^#' .env | xargs)

# Makefile safe version

$(shell export $$(grep --color=never -v '^#' .env | xargs))
```

The above command dynamically exports the environment variables to the shell & to any child processes.

In the library approach to load the variables dynamically in your app, you will always need the `.env` file to be present in the directory, whereas in the dynamic approach we rely on the shell to export the variables, the vanilla way!
