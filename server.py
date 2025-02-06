import sys

# Request from Client
print(sys.stdin.readline().strip(), file=sys.stderr)
print('{"jsonrpc":"2.0", "id": 0, "result": {"protocolVersion": "2024-11-05", "capabilities": {"logging": {}}, "serverInfo": {"name": "mcp-simple-server", "version": "0.1.0"}}}', flush=True)
# Notification from Client
print(sys.stdin.readline().strip(), file=sys.stderr)

# Problem 1: I want to log something after initialization
# print('{"jsonrpc": "2.0", "method": "notifications/message", params: {"level": "info", "data": {}"}}', flush=True)

# Request from Client
print(sys.stdin.readline().strip(), file=sys.stderr)

# Problem 2: I want to answer with id being string
print('{"jsonrpc": "2.0", "id": 1, "result": {"tools": []}}', flush=True)
# print('{"jsonrpc": "2.0", "id": "1", "result": {"tools": []}}', flush=True)
