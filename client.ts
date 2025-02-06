import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
    command: "python3",
    args: ["./server.py"],
    env: {}
})

const client = new Client({ name: "example-client", version: "0.1.0" });

await client.connect(transport);

const { tools } = await client.listTools();

console.log("Connected to MCP Server. Available tools: ", tools.map((v) => v.name));

client.close();