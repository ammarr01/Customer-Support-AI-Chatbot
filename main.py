from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tools import tools
from pydantic import BaseModel
from langgraph.checkpoint.memory import InMemorySaver
from tools import llm
from langgraph.prebuilt import create_react_agent


class Request(BaseModel):
    message : str 
    thread_id: str = "1"

app = FastAPI()
    
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

with open("system_prompt.txt", "r") as f:
    prompt = f.read()


agent = create_react_agent(llm, tools=tools, prompt=prompt, checkpointer=InMemorySaver())

MESSAGE_CAP = 15

session_counts: dict[str, int] = {}

@app.post("/chat")
def chat(request: Request):
    count = session_counts.get(request.thread_id, 0)

    if count >= MESSAGE_CAP:
          raise HTTPException(
              status_code=429,
              detail="Message limit reached for this session."
          )

    response = agent.invoke(
        {"messages": [{"role": "user", "content": request.message}]},
        {"configurable": {"thread_id": request.thread_id}}
    )
    
    session_counts[request.thread_id] = count + 1

    return {"response": response["messages"][-1].content}