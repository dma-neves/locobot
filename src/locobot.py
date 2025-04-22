import ollama

from data_embedding import load_data, get_embedding_data, list_files

SYSTEM_PROMPT="""You are a helpful coding assistant. Try to respond to the user's requests in a professional and concise manner. Use code snippets when appropriate. Use markdown for text formatting."""
USER_PROMPT = SYSTEM_PROMPT

class Locobot:
    
    def __init__(self, directory, include_extensions=None, exclude_paths=None):
        self.file_list = list_files(directory, include_extensions, exclude_paths)
        self.collection = load_data(self.file_list)
        self.chat_history = [ {"role": "system", "content": SYSTEM_PROMPT, "user_prompt": USER_PROMPT} ]
        
        self.model = "llama3.2"
        self.context_size = 8192
        
    def submit_prompt(self, prompt):
        
        embedding_data = get_embedding_data(self.collection, prompt)
        contextualized_prompt = f"Respond the best you can to the user prompt given the context of the data. The data: {embedding_data}. The user prompt: {prompt}"
        self.chat_history.append( {"role": "user", "content": contextualized_prompt, "user_prompt": prompt} )
        
        response = ollama.chat(model=self.model, 
                           options={"context": self.context_size},
                           messages=self.chat_history, 
                           stream=True)
        
        full_response = ""
        for chunk in response:
            full_response += chunk['message']['content']
            yield chunk['message']['content']
            
        self.chat_history.append( {"role": "assistant", "content": full_response, "user_prompt": full_response} )
        
    
    def get_file_list(self):
        return self.file_list
    
    def get_last_response(self):
        return self.chat_history[-1]["content"]
    
    def get_conversation(self):
        
        convo = ""
        for message in self.chat_history:
            if message["role"] != "system":
                convo += "**locobot\\>** " if message["role"] == "assistant" else "**you\\>** "
                convo += message["user_prompt"]
                convo += "\n\n\n"
            
        return convo
            