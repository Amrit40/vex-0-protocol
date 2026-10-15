# VEX-0 (Vector Execution Zero) Protocol
An ultra-low-latency, single-token-opcode execution language for AI-to-AI and Agent-to-Tool communication. Reduces token overhead by up to 85% compared to JSON or natural language ReAct loops.

## Opcode Specification
- `@` : Identity / Persona Vector (`@0x9F`)
- `$` : Target Objective (`$"task_id"`)
- `^` : External Tool Call (`^tool_name(args)`)
- `~` : Latent Reasoning / Compute (`~action(reg)`)
- `->`: Register Pipe (`->r0`)
- `?` : Conditional Gate (`?r0`)
- `!` : Panic / Fallback (`!#ERR`)
- `#` : Terminate & Return (`#OK`)

## System Prompt Injection (Zero-Shot)
Paste into any LLM system prompt to enable native VEX-0 execution:
`[VEX-0 ACTIVE] Parse and output strictly in VEX-0 syntax: @(ID) $(Goal) ^(Tool) ~(Think) ->(Pipe r0-r9) ?(Check) !(Fail) #(Done). Omit whitespace and conversational text.`
