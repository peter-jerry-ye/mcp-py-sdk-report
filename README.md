This repository is used to report two issues that I found in mcp python sdk

1. The client hangs when the server send a log notification after the initialization phase.
2. The client hangs when the server sends a response having the id as string.

Both of the actions operations are valid as per specification.

They are recorded in `server.py` where two lines are commented out:

- Line 10 corresponds to problem 1
- Line 17 corresponds to problem 2

For reference, the equivalent version in TypeScript is added, which works fine.

TypeScript version:

```bash
deno run -A client.ts
```

Python version:

```bash
uv run client.py
```