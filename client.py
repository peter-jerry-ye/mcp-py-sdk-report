import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class MCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_server(self):
        """
        Connect to an MCP Server
        """
        command = "python"
        server_params = StdioServerParameters(
            command=command,
            args=["./server.py"],
            env=None,
        )
        stdio_transport = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(
            ClientSession(self.stdio, self.write)
        )
        await self.session.initialize()
        response = await self.session.list_tools()
        
        tools = response.tools
        print("\nConnected to MCP Server. Available tools:", [tool.name for tool in tools])

    async def cleanup(self):
        """
        Cleanup resources
        """
        await self.exit_stack.aclose()

async def main():
    client = MCPClient()
    try:
        await client.connect_to_server()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())