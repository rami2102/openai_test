import os
import openai
openai.organization = "org-IaDdGaKWO3C8jW0RZ7oQw4Up"
#openai.organization = "org-rami"
openai.api_key = "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"

#os.getenv("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")
#openai.Model.list()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
#        {"role" : "system", "content" : "You are helpful assistant that helps to write highly converting landing page copies"},
            {"role": "user", "content": '''You will help me write website landing page copies. You will be my helpful assistant that helps to write highly converting landing page copies. There are some rules to follow that I will explain to you:
1. Subject: Qi gong VOD course
2. You will generate at least 6 sub-titles for at least 6 paragraphs ordered by logical way of the landing page copy
3. You will expand each sub-title in a descriptive way to help you understand what to generate.
4. You will write the subject of website's landing page followed by at least 6 paragraphs, each paragraph will begin with its sub-title 
5. This landing page should be high quality lead magnet to convert incoming people for subscription
6. The lenght of each paragraph should be at least 300 words, and the total length of the generated copy at least 2000 words
7. The copy should be personalized and very persuasive
8. The copy should be high quality lead magnet to convert incoming people for subscription
9. The following words mustn't appear in the generated text: paragraph, title, section
10. At the end you should write highly converting CTA to convert leads for subscription
11. You will not use any numbers in the text
'''
}
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(response)
print(result)





