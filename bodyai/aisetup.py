
from apis import chatgpt
import openai

ccp=''' Your role is a top-tier coach, nutritionist, physiologist, personal trainer.
Generate a personalized bodybuilding program based on the user's physical data, training experience, goals, and preferences.
The program must:
- Be science-based and up-to-date with current best practices.
- Aim for strength, hypertrophy, and overall fitness improvement.
- Include detailed workout splits, exercise selection, rep ranges, sets, rest times, and progression strategies.
- Align with criteria for program evaluation, including balance, volume, recovery, and progression.
  '''

ccp2=''' Your role is a top-tier coach, nutritionist, physiologist, personal trainer.
Based on the science of bodybuilding and current research, analyze the given program. 
Rate it on a scale of 1 to 10, explaining strengths, areas for improvement, and detailed suggestions.
Be constructive in your feedback and avoid being overly critical unless the program has significant flaws
explain how to fix those flaws.
  '''




openai.api_key = chatgpt


def create_prg(input):
    messages = [{'role': 'system', 'content':ccp}]    
    messages.append({'role': 'user', 'content':f'{input}'})
    chat = openai.ChatCompletion.create(model='gpt-4', messages=messages)
    reply = chat.choices[0].message.content
    print(reply)
    return reply



def rate_prg(data):
    messages = [{'role': 'system', 'content':ccp2}]    
    messages.append({'role': 'user', 'content':f'{data}'})
    chat = openai.ChatCompletion.create(model='gpt-4', messages=messages)
    reply = chat.choices[0].message.content
    print(reply)
    return reply