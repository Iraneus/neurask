from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
#add_routes(app, NotImplemented)

from openai_functions_tool_retrieval_agent import agent_executor as openai_functions_tool_retrieval_agent_chain

add_routes(app, openai_functions_tool_retrieval_agent_chain, path="/openai-functions-tool-retrieval-agent")

#from rag_multi_index_fusion import chain as rag_multi_index_fusion_chain

#add_routes(app, rag_multi_index_fusion_chain, path="/rag-multi-index-fusion")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
