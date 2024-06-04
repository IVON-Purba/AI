# -*- coding: utf-8 -*-

import openai
import json

openai.api_key = 'gpt key'

path = 'OCR result path'

with open(path, 'r', encoding='utf-8') as f:
    ocr_text = f.read()

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "user",
            "content": ocr_text
        },
        {
            "role": "system",
            "content": "결과는 json 형식으로 반환한다. 제시하는 모든 태그를 표시해야하며, 각 태그 아래 또 다른 후속 태그를 지정하지 않고, 해당 태그에 대한 내용이 일치하는 것이 없는 경우 해당 필드의 항목은 null 값으로 대체한다. 결과에 표시해야하는 태그는 1. 텍스트 한줄 요약 title, 2. 날짜와 관련된 start_day / end_day, 3. 장소나 지역과 관련된 location, 4. 가격이나 금액같은 금전적인 것은 합계 항목만 price에 나타내고, 5. 행사 시간과 같은 시간과 관련된 항목은 time 태그로, 6. 전체적인 2~5줄 요약 내용은 summary에, 7. 기타 중요한 항목은 etc 항목에 나타내며, 제시된 7개의 태그를 결과 항목으로 모두 출력해야 하며 만약, 특별하게 일치하는 정보가 없다면 해당 필드의 값을 null 값으로 처리한다." 
        }
    ]
)

json_result = completion.choices[0].message.content
json_string = json.dumps(json_result)

print(json_string)