# Install dependencies: pip install mcp
from mcp.server.fastmcp import FastMCP
import re

mcp = FastMCP("VEX-0 Execution Engine")

@mcp.tool()
def execute_vex0(vex_script: str) -> dict:
    """Executes a compressed VEX-0 agent script and returns register states."""
    registers = {}
    log = []
    
    # Match opcodes and payloads
    steps = re.findall(r'([@$~^?!#])([^@$~^?!#]+)', vex_script)
    for op, payload in steps:
        if op == '^':
            # Execute external tool hook
            match = re.match(r'(\w+)\((.*?)\)->(r\d+)', payload)
            if match:
                tool, args, reg = match.groups()
                registers[reg] = f"Executed_{tool}({args})"
                log.append(f"Tool {tool} -> {reg}")
        elif op == '~':
            # Execute latent reasoning step
            match = re.match(r'(\w+)\((r\d+)\)->(r\d+)', payload)
            if match:
                fn, in_r, out_r = match.groups()
                registers[out_r] = f"{fn}({registers.get(in_r, '')})"
                log.append(f"Latent {fn} -> {out_r}")
        elif op == '#':
            log.append(f"Terminated: {payload}")
            break
            
    return {"status": "complete", "registers": registers, "trace": log}

if __name__ == "__main__":
    mcp.run()
