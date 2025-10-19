
# AkshitBaliyan-langgraph-mat496

https://academy.langchain.com/courses/intro-to-langgraph

Roll No. : 2310110029 

## Module 1 

### Video 1 : 

**Learnings :** 

I learned  Lang Graph limitations as well as how it make it useful.                                                                                          
Then the difference between chain and agent architecture where chains follow fixed steps and agents can decide their own.
Then we see how LangGraph balances control and reliability, while also allowing persistence, streaming, and human involvement in workflows.

### Video 2 :

**Learnings :** 

In this part, I learned how to build a basic graph that makes a decision. The exercise involved using a simple dictionary input and a single condition to form a sentence.built the graph, visualized it to see the logic, and then tested it to make sure it worked as expected.

original file link : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/original/module-1/simple-graph.ipynb

**Tweaks I made:**

I expanded the graph from three to five nodes, each representing a different mood or outcome.
I updated the conditional edge logic so that after the first node, the graph randomly chooses one of four possible end nodes.
I adjusted the markdown and code to match the new structure, making sure the documentation and outputs reflect the five-node setup.

<img width="500" height="333" alt="image" src="https://github.com/user-attachments/assets/4dd33438-daae-486b-a918-ce82b572f74a" />

<img width="1286" height="402" alt="image" src="https://github.com/user-attachments/assets/45b7e38f-d877-4283-85f6-9e15818a26e9" />


Modified work : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/Module1/simple-graph.ipynb

### Video 3 :

The graph that is done in Video 2, we did it same but on studio this time, 
but to do it on studio i have made changes in .py file also the same change done in video2.

<img width="1148" height="802" alt="Screenshot1" src="https://github.com/user-attachments/assets/568ab207-9197-4a77-a37d-cd696602417e" />

### Video 4 :

In this I moved from simple graphs toChains by linking different components together. concept was to take a conversation history which is stored as a list of messages, create a custom tool, and then bind them with an LLM inside a graph.

original file link : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/original/module-1/chain.ipynb

Tweaking: Changes convo to How to play Uno and its related conversation. make my translational tool and replaced it in the code with the given one. also done tweaking in MessageState graph task, randomly ask about topic like contribution of Bhagat Singh for India.

Modified work : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/Module1/chain.ipynb

### Video 5 : 

In this video learned how to build a router that lets the LLM choose its own path. It can either use a specific tool if needed or just answer the question directly.
like it will give answer based on the condition met but if unrelated thing is asked then it will give answer according to it only.

original file link : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/original/module-1/router.ipynb

changes : made the division thing just like multiply func, it lets now to take two integer input and divide them to get answer. same thing is updated in router.py and checked on studio also and found out it give same result.
also checked on studio giving random question to know the diff result.

modified file link : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/Module1/router.ipynb

![WhatsApp Image 2025-10-16 at 20 23 01_d5b0debe](https://github.com/user-attachments/assets/4eb4022f-df06-4411-87fa-c4a31d224002) 

### Video 6 : 

Make a agent with diff tools that can soolve many maths problem. We used React Architecture which used loop until the answer is found, they used a tool then forward it to another tool as per the req basically using multiple tools until answer is found.

original link: https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/original/module-1/agent.ipynb

tweaking : add more function/tools for solving maths problem. changed input make them complex and test with all diff tools whether they are working or not.

modified link : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/Module1/agent.ipynb


![WhatsApp Image 2025-10-16 at 23 05 28_1a2c0819](https://github.com/user-attachments/assets/f00dc7e7-07e8-422d-83e4-952899725456)


### Video 7 :

**Learnings :** 
Learnt how agent keep track of memory using threads nd results is obtained. 

original link : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/original/module-1/agent-memory.ipynb

**tweaking:** 
added some tools first, then performa a operation using one of the tool and then again perform a operation on that result to check memory is being kept by agent or not.

modified link : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/Module1/agent-memory.ipynb

![WhatsApp Image 2025-10-16 at 23 16 00_47cbc30e](https://github.com/user-attachments/assets/d73a9020-6a12-49c5-8e59-f8166fb88240)



## Module 2 

### Video 1 :

Learnt about the structure of the graph its schema. In this structure we defin the types and allowed values. but we found that in case of typedict and dataclass it is not strictly followed andd we can assign a invalid value also . to prevet this we noticed and learnt about the pydantic which prevents from happening this and throw error if no values is found.

Original file link : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/original/module-2/state-schema.ipynb

Tweaking : 
Change the entrire code from 2 node split strucure to 5 node split strucure with equal chances , previousely it was based on the mood but i modified it one the basis of sports i plays.

Modified file Link : https://github.com/AkshitBaliyan/AkshitBaliyan-langgraph-mat496/blob/main/Module2/state-schema.ipynb

