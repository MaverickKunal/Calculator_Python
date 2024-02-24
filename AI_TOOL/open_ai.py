import openai
from config import api_key

openai.api_key = api_key

response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write an email to boss for sick leavewrite an email to boss for sick leave\n\nSubject: Request for Sick Leave\n\nDear [Boss’s Name],\n\nI am writing to inform you that I am feeling unwell and would like to request a few days of sick leave. Due to high fever and severe body ache, my doctor has advised me to take rest and not to leave the house for at least [number of days] days.\n\nAs much as I understand the importance of my work and responsibilities towards the company, I believe that it is crucial for me to prioritize my health and recover fully before resuming my duties. I am confident that a few days of rest will help me to fully recuperate and come back stronger.\n\nIn the meantime, I have discussed my absence with my team and have delegated my tasks to [colleague’s name], who has agreed to cover for me during my absence. I have also ensured that all urgent projects are completed and there will be no delay in their timelines.\n\nI will keep you updated on my health and will be in touch with [colleague’s name] to ensure that everything is running smoothly in my absence. I am confident that the team will handle the situation with utmost efficiency.\n\nPlease let me know if you require any further information from my end. I would be happy to provide it at the earliest. I will",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)