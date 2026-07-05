import os
import cognee
from dotenv import load_dotenv

# 1. Load the environment file explicitly
load_dotenv()

# Read values from .env
GROQ_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")

# Configure Cognee
cognee.config.set("llm_provider", "custom")
cognee.config.set("llm_model", LLM_MODEL)
cognee.config.set("llm_api_key", GROQ_KEY)

cognee.config.set("embedding_provider", "fastembed")
cognee.config.set("embedding_model", "BAAI/bge-small-en-v1.5")

async def store_memory(text_content: str, dataset_name: str = "user_memory"):
    try:
        await cognee.remember(text_content, dataset_name=dataset_name)
        return {"status": "success", "message": "Memory stored successfully."}
    except Exception as e:
        return {"status": "error", "message": f"Cognee Memory Error: {str(e)}"}

async def retrieve_memory(query: str):
    try:
        search_results = await cognee.recall(query)
        formatted_results = [result.text for result in search_results] if search_results else []
        return {"status": "success", "results": formatted_results}
    except Exception as e:
        return {"status": "error", "message": f"Cognee Recall Error: {str(e)}"}
    
async def forget_memory(dataset: str = "user_memory", everything: bool = False):
    try:
        print("Deleting dataset:", dataset)
        print("Everything:", everything)

        await cognee.forget(
            dataset=dataset,
            everything=everything
        )

        return {
            "status": "success",
            "message": "Memory deleted successfully."
        }

    except Exception as e:
        print("Forget Error:", e)
        return {
            "status": "error",
            "message": f"Cognee Forget Error: {str(e)}"
        }
    
async def improve_memory(dataset: str = "user_memory"):
    try:
        await cognee.improve(dataset=dataset)

        return {
            "status": "success",
            "message": "Memory improved successfully."
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Cognee Improve Error: {str(e)}"
        }