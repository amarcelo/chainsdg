import PySimpleGUI as sg
from requests import get



"""{
    "name": "BRAZUCANFT",
    "description": "Primeiro NFT do Codigo Brazuca na Hathor",
    "image": "ipfs://ipfs/QmQYjix1mPpHKSHiu2m1tkjnbpNsx9MTUim8LWj9B7ssLe",
    "attributes": [
        {
            "type": "rarity",
            "value": "super rare"
        },
        {
            "type": "Nome",
            "value": "Brazuca NFT"
        }
    ]
}"""

"""{
  "name": "Minha Obra de Arte",
  "description": "Uma linda obra de arte",
  "image": "https://www.exemplo.com/obrasdearte/1.jpg",
  "attributes": [
    {
      "trait_type": "Autor",
      "value": "João da Silva"
    },
    {
      "trait_type": "Técnica",
      "value": "Aquarela"
    },
    {
      "trait_type": "Ano",
      "value": "2022"
    },
    {
      "trait_type": "Edição",
      "value": "1 de 10"
    }
  ]
}"""

perguntas=["","","","",""]

perguntas_ods=[
"What is the proportion of employees in your company who receive a decent minimum wage?",
"What types of products or services does your company offer to improve the quality of life of people in poverty?",
"Does your company adopt practices to promote the inclusion of people in economic vulnerability?",
"Does your company have donation or philanthropy policies to support organizations working to eradicate poverty?",
"How does your company measure and monitor the impact of its activities on poverty reduction?",

"Does your company use sustainable and locally produced ingredients in its products or services?",
"Does your company support sustainable agriculture through policies of purchasing organic products or from small local producers?",
"Does your company adopt practices to avoid food waste in its operations?",
"Does your company implement food education programs for its employees or customers?",
"Does your company support projects or organizations that work to improve food security and nutrition in vulnerable communities?",

"Does your company offer wellness programs for its employees, such as physical activities, nutrition or disease prevention programs?",
"Does your company promote an organizational culture that values the mental and emotional health of employees?",
"Does your company produce or sell products that promote people's health and well-being?",
"Does your company implement practices to ensure a safe and healthy work environment for its employees?",
"Does your company support initiatives or organizations that work to improve access to health and well-being in vulnerable communities?",

"Does your company offer training and development programs for its employees?",
"Does your company develop or produce products or services that help improve the quality of education?",
"Does your company have partnerships with educational institutions or organizations working to improve the quality of education?",
"Does your company implement policies to ensure equal educational opportunities for all?",
"Does your company support projects or organizations working to improve access and quality of education in vulnerable communities?",


"Does your company adopt policies to ensure equal pay and opportunities for men and women?",
"Does your company promote gender diversity in leadership positions and decision-making?",
"Does your company adopt practices to combat gender harassment and violence in the workplace?",
"Does your company promote gender equality through its products, services or advertising campaigns?",
"Does your company support initiatives or organizations that work to promote gender equality and women's rights?",

"Does your company adopt practices to minimize water pollution in its operations?",
"Does your company support projects or organizations that work to improve access to clean water and sanitation in vulnerable communities?",
"Does your company implement measures to reduce water consumption in its operations?",
"Does your company develop or produce products or services that help promote sustainable water use?",
"Does your company measure and monitor the water footprint of its operations?",

"Does your company adopt practices to reduce energy consumption in its operations?",
"Does your company use renewable energy sources in its operations?",
"Does your company support projects or organizations that work to improve access to clean and affordable energy in vulnerable communities?",
"Does your company develop or produce products or services that help promote the transition to a low-carbon economy?",
"Does your company measure and monitor its greenhouse gas emissions?",

"Does your company adopt policies to ensure decent work and fair pay for its employees?",
"Does your company promote diversity and inclusion in its hiring and promotions?",
"Does your company adopt practices to ensure a safe and healthy work environment for its employees?",
"Does your company support entrepreneurship and economic growth of small businesses and startups?",
"Does your company measure and monitor the impact of its activities on job creation and economic growth?",

"Does your company invest in innovation and research to improve its products and services?",
"Does your company adopt practices to minimize the environmental impact of its industrial processes?",
"Does your company support the development of sustainable infrastructure in vulnerable communities?",
"Does your company promote partnerships and collaboration between different sectors to promote innovation and sustainability?",
"Does your company measure and monitor the impact of its activities on sustainable industry, innovation, and infrastructure?",


"Does your company adopt policies to ensure equal opportunities and inclusion of marginalized groups?",
"Does your company support projects or organizations working to reduce inequalities?",
"Does your company develop or produce products or services that help reduce social and economic inequalities?",
"Does your company adopt practices to combat prejudice and discrimination in its operations?",
"Does your company measure and monitor the impact of its activities on reducing inequalities?",

"Does your company adopt practices to reduce the environmental impact of its buildings and facilities?",
"Does your company support projects or organizations working to improve the quality of life in vulnerable communities?",
"Does your company develop or produce products or services that help promote sustainable transportation and urban planning?",
"Does your company adopt practices to promote cultural diversity and historical heritage in its operations?",
"Does your company measure and monitor the impact of its activities on promoting sustainable cities and communities?",

"Does your company adopt practices to minimize waste and pollution in its operations?",
"Does your company develop or produce products or services that help promote sustainable consumption and production?",
"Does your company adopt policies to ensure that its suppliers adopt responsible practices?",
"Does your company promote consumer education and awareness about responsible consumption?",
"Does your company measure and monitor the impact of its activities on responsible consumption and production?",

"Does your company adopt practices to reduce its greenhouse gas emissions?",
"Does your company use renewable energy sources in its operations?",
"Does your company support projects or organizations working to mitigate the effects of climate change in vulnerable communities?",
"Does your company develop or produce products or services that help promote adaptation to climate change?",
"Does your company measure and monitor the impact of its activities on taking action against global climate change?",

"Does your company adopt practices to minimize water pollution in its operations?",
"Does your company support projects or organizations working to preserve marine life and aquatic ecosystems?",
"Does your company develop or produce products or services that help promote the conservation of life in water?",
"Does your company adopt practices to reduce water consumption in its operations?",
"Does your company measure and monitor the impact of its activities on life in water?",

"Does your company adopt practices to minimize the environmental impact of its operations on terrestrial ecosystems?",
"Does your company support projects or organizations working to preserve biodiversity in terrestrial ecosystems?",
"Does your company develop or produce products or services that help promote the conservation of terrestrial life?",
"Does your company adopt practices to reduce natural resource consumption in its operations?",
"Does your company measure and monitor the impact of its activities on terrestrial life?",

"Does your company adopt practices to ensure transparency and ethics in its operations?",
"Does your company develop or produce products or services that help promote social justice and equality?",
"Does your company adopt policies to ensure respect for human rights in all its operations?",
"Does your company promote a culture of peace and peaceful conflict resolution?",
"Does your company measure and monitor the impact of its activities on peace, justice, and effective institutions?",

"Does your company seek to establish partnerships with other organizations to maximize its positive impact?",
"Does your company adopt practices to ensure transparency and accountability in its partnerships?",
"Does your company support projects or organizations working to promote the SDGs?",
"Does your company adopt practices to promote the empowerment and development of its employees?",
"Does your company measure and monitor the impact of its activities on partnerships and means of implementing the SDGs?"

]
import PySimpleGUI as sg
import json
sg.theme('DarkBlue')

ods_list = ["1. No Poverty",
            "2. Zero Hunger",
            "3. Good Health and Well-Being",
            "4. Quality Education",
            "5. Gender Equality",
            "6. Clean Water and Sanitation",
            "7. Affordable and Clean Energy",
            "8. Decent Work and Economic Growth",
            "9. Industry, Innovation and Infrastructure",
            "10. Reduced Inequalities",
            "11. Suistainable Cities and Communities",
            "12. Responsible Consuption and Production",
            "13. Climate Action",
            "14. Life Belllow Water",
            "15. Life on Land",
            "16. Peace, justice and Strong Insitutions",
            "17. Partneships for the Goals"]

uri = {"1. No Poverty": "QmdASsat2fzMV8Acir6byXiQ7CyRVyJH5prqftSvHta9wZ",
       "2. Zero Hunger":"Qmd2eLiowtrx2CSR4dZMjATuzzLigGfXzZwpcruSKi82gZ",
       "3. Good Health and Well-Being":"QmR5jSkBVcN4NknJxyJ7ErGBsmXf5n8iw7mDLUNAPkhcF7",
       "4. Quality Education":"QmPtXu1HWTh3zMhqh6yhqRk1iqUVvcj74GABQkZiNEBKeu",
       "5. Gender Equality":"QmYgwZeeUcw2vwTqCYky2iwrRXSDjKmaFoBfquZwAMJ1K7",
       "6. Clean Water and Sanitation":"QmdcAuUYJbAwYzAV6QwrTS7j564tVD8WHDKCKMCWbb8eo8",
       "7. Affordable and Clean Energy":"QmcB1TWZdGHCwZGRhBnnpL9Kijr9Xr2xquFzn8ma43CBKz",
       "8. Decent Work and Economic Growth":"QmdZbCrF4UdaoPB8tiyLdnHv7Zv1zgGPURxcx8q9t5WQrv",
       "9. Industry, Innovation and Infrastructure":"QmWV5NGDhboSVVUEWy5m5SmPiomT8pNFVSoaNz7LFXQdKo",
       "10. Reduced Inequalities":"Qmcugn9wYTvY5DG9X57Sgcp9pXCKfaGG2ybjqgdJpyWVUL",
       "11. Suistainable Cities and Communities":"QmXKRaP9V47NbVcqL35PwQEJEPhGCqCaqmuiaTknNhhBMF",
       "12. Responsible Consuption and Production":"QmcVFz857NfuvQuJqExWVrMH4N3ETeBnk1YF66XNwumaq1",
       "13. Climate Action":"QmYxN4iNNztaKjSN4cnghffmeeUv8Med4mrCYyMohUga97",
        "14. Life Belllow Water":"QmT5bsJCW3t658b8cjEvfDaXfQhGyWTjE7fJqo6PbyihiR",
        "15. Life on Land":"QmWypB3ZN6ze7ZAm5c6NEecA35og21emE7QMnfdBcZurTJ",
        "16. Peace, justice and Strong Insitutions":"QmejvA3o6zu39jY1kHnZCx97cMbW1QW2b51e9gaJnN4ynj",
        "17. Partneships for the Goals": "QmRuYGZpfPR5qLp1ubVtMB7Dk7DqUiuxeY3cwzSUZrtRDL"}
resposta_empresa = []
BASE_URL = "https://api.opensea.io/v2/orders/mumbai/seaport/listings"

layout = [[sg.Text('Nome da Empresa:')],
          [sg.Input(key='-NOME_EMPRESA-', size=(30,1))],
          [sg.Text('ODS:')],
          [sg.Listbox(values=ods_list, size=(30,5), key='-TIPO_ODS-')],
          [sg.Button("Confirma")],
          [sg. Text(f'Question 1: {perguntas[0]}',key="quest1")],
          [sg.Input(key="resposta1")],
          [sg. Text(f'Question 2: {perguntas[1]}',key="quest2")],
          [sg.Input(key="resposta2")],
          [sg. Text(f'Question 3: {perguntas[2]}',key="quest3")],
          [sg.Input(key="resposta3")],
          [sg. Text(f'Question 4: {perguntas[3]}',key="quest4")],
          [sg.Input(key="resposta4")],
          [sg. Text(f'Question 5: {perguntas[4]}',key="quest5")],
          [sg.Input(key="resposta5")],
          [sg.Button('Salvar'), sg.Button('Cancelar')]]

window = sg.Window('Company Name', layout)
p1 = window["quest1"]
p2 = window["quest2"]
p3= window["quest3"]
p4= window["quest4"]
p5= window["quest5"]
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    elif event == 'Confirmar':
        tipo_ods = values['-TIPO_ODS-'][0]
        if tipo_ods == ods_list[0]:
            p1.Update(f"Pergunta 1: {perguntas_ods[0]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[1]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[2]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[3]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[4]}")
        elif tipo_ods == ods_list[1]:
            p1.Update(f"Pergunta 1: {perguntas_ods[5]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[6]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[7]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[8]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[9]}")
        elif tipo_ods == ods_list[2]:
            p1.Update(f"Pergunta 1: {perguntas_ods[10]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[11]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[12]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[13]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[14]}")
        elif tipo_ods == ods_list[3]:
            p1.Update(f"Pergunta 1: {perguntas_ods[15]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[15]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[17]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[18]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[19]}")
        elif tipo_ods == ods_list[4]:
            p1.Update(f"Pergunta 1: {perguntas_ods[20]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[21]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[22]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[23]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[24]}")
        elif tipo_ods == ods_list[5]:
            p1.Update(f"Pergunta 1: {perguntas_ods[25]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[26]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[27]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[28]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[29]}")
        elif tipo_ods == ods_list[6]:
            p1.Update(f"Pergunta 1: {perguntas_ods[30]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[31]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[32]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[33]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[34]}")
        elif tipo_ods == ods_list[7]:
            p1.Update(f"Pergunta 1: {perguntas_ods[35]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[36]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[37]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[38]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[39]}")
        elif tipo_ods == ods_list[8]:
            p1.Update(f"Pergunta 1: {perguntas_ods[40]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[41]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[42]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[43]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[44]}")
        elif tipo_ods == ods_list[9]:
            p1.Update(f"Pergunta 1: {perguntas_ods[45]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[46]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[47]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[48]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[49]}")
        elif tipo_ods == ods_list[10]:
            p1.Update(f"Pergunta 1: {perguntas_ods[50]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[51]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[52]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[53]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[54]}")
        elif tipo_ods == ods_list[11]:
            p1.Update(f"Pergunta 1: {perguntas_ods[55]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[56]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[57]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[58]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[59]}")
        elif tipo_ods == ods_list[12]:
            p1.Update(f"Pergunta 1: {perguntas_ods[60]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[61]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[62]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[63]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[64]}")
        elif tipo_ods == ods_list[13]:
            p1.Update(f"Pergunta 1: {perguntas_ods[65]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[66]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[67]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[68]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[69]}")
        elif tipo_ods == ods_list[14]:
            p1.Update(f"Pergunta 1: {perguntas_ods[70]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[71]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[72]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[73]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[74]}")
        elif tipo_ods == ods_list[15]:
            p1.Update(f"Pergunta 1: {perguntas_ods[75]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[76]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[77]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[78]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[79]}")
        elif tipo_ods == ods_list[16]:
            p1.Update(f"Pergunta 1: {perguntas_ods[80]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[81]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[82]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[83]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[84]}")
        elif tipo_ods == ods_list[17]:
            p1.Update(f"Pergunta 1: {perguntas_ods[85]}")
            p2.Update(f"Pergunta 2: {perguntas_ods[86]}")
            p3.Update(f"Pergunta 3: {perguntas_ods[87]}")
            p4.Update(f"Pergunta 4: {perguntas_ods[88]}")
            p5.Update(f"Pergunta 5: {perguntas_ods[89]}")
    elif event == 'Salvar':
        print("foi")
        nome_empresa = values['-NOME_EMPRESA-']
        tipo_ods = values['-TIPO_ODS-'][0]
        data = {
            "name": nome_empresa,
            "ods":tipo_ods,
            "image": "ipfs://ipfs/"+uri[tipo_ods],
            "attributes": [
                {
                    "type": "resposta1",
                    "value": values["resposta1"]
                },
                {
                    "type": "resposta2",
                    "value": values["resposta2"]
                },
                {
                    "type": "resposta3",
                    "value": values["resposta3"]
                },
                {
                    "type": "resposta4",
                    "value": values["resposta4"]
                },
                {
                    "type": "resposta5",
                    "value": values["resposta5"]
                }
            ]
        }
        break
for info in data:
    print(info)
for k,v in data.items():
    with open(f"{nome_empresa}.json","w+") as file:
        json.dump(data,file)
x = 0
for y in range(-1,len(data)):
    with open(f"{nome_empresa}.txt","a+") as file:
        file.write(f"resposta {x+1}: {data['attributes'][x]['value']}\n")
    x +=1
window.close()
