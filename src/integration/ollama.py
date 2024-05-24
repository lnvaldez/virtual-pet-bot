from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Configuracion para el modelo Ollama Gemma
MODEL = 'gemma'
llm = Ollama(model=MODEL, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), temperature=0.2, num_predict=64)

# Definir la plantilla del prompt
prompt_template = PromptTemplate(
    input_variables=['input'],
    template='{input}'
)

# Crear la cadena LLMChain con el prompt template y modelo
chain = LLMChain(llm=llm, prompt=prompt_template, verbose=False)

# Funcion para generar una respuesta
def generate_response(user_input):
    response = chain.invoke({'input': user_input})
    return response['text']
