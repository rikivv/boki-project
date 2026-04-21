from chat_instance import ChatInstance
from llm.client import LLMClient

chatInstance = ChatInstance()
llmClient = LLMClient()

if __name__ == "__main__":
    while True:
        message = input("\nUser Prompt: ")
        print()
        response = chatInstance.send(message)
        if response != None:
            print("\n"+response)

    