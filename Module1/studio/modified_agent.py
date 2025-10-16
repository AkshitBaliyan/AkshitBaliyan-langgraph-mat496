from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode



def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

# This will be a tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b

# New Tools : 

def mod(a: int, b: int) -> float:
    """Divide a and b and return reminder.

    Args:
        a: first int
        b: second int
    """
    return a % b

def convert_to_binary(number: int, bits: int = 8) -> str:
    """Converts a decimal integer to its two's complement binary representation.

    Args:
        number: The decimal integer to convert.
        bits: The number of bits for the binary representation.
    """
    if number >= 0:
        # For positive numbers, use standard binary conversion
        return bin(number)[2:].zfill(bits)
    else:
        # For negative numbers, calculate two's complement
        return bin((1 << bits) + number)[2:]

def power(a: int, b: int) -> float:
    """Get a to the power b.

    Args:
        a: first int
        b: second int
    """
    return a ** b

tools = [add, multiply, divide, mod, convert_to_binary, power]
llm = ChatOpenAI(model="gpt-4o")

# For this ipynb we set parallel tool calling to false as math generally is done sequentially, and this time we have 3 tools that can do math
# the OpenAI model specifically defaults to parallel tool calling for efficiency, see https://python.langchain.com/docs/how_to/tool_calling_parallel/
# play around with it and see how the model behaves with math equations!
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)

# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with writing performing arithmetic on a set of inputs.")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")

# Compile graph
graph = builder.compile()
