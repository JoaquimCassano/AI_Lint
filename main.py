import openai, rich.console
from sys import argv
openai.api_key = ''

file_name = argv[1]
with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

def get_gpt_response(log:list = []) -> str:
    output = openai.ChatCompletion.create(
        messages = log,
        model = 'gpt-3.5-turbo-0613',
    )

    return output.messages[0].message.content

sideA = [{'role':'system', 'content':'Você é um debuggador de IA, que irá ler o código, e apontar os erros para o usuário. Não invente erros. Tenha embasamento em todos os erros.'}]
sideB = [{'role':'system', 'content':'Você receberá um código-fonte, e os erros apontados por uma AI dela. Agora, reescreva a resposta da IA somente com os erros que fazem sentido.'}]

sideA.append({"role":'user', 'content':f'Here is the code named {file_name}: {content}'})
sideB.append({"role":"user", 'content':f'Código fonte do cód. {file_name}: {content} | \n Erros apontados: {get_gpt_response(sideA)}'})
shell = rich.Console()
errors_declared = get_gpt_response(sideB)
shell.print(f'[reverse green] Errors: [/reverse green]')
print(errors_declared)