import PySimpleGUI as sg
import json

quests = ["", "", "", "", ""]
ods_quests = [
    "What is the proportion of employees in your company who receive a decent minimum wage?",
    "What types of products or services does your company offer to improve the quality of life of people in poverty?",
    "Does your company adopt practices to promote the inclusion of people in economically vulnerable situations?",
    "Does your company have donation or philanthropy policies to support organizations working to eradicate poverty?",
    "How does your company measure and monitor the impact of its activities on poverty reduction?",

    "Does your company use sustainable and locally produced ingredients in its products or services?",
    "Does your company support sustainable agriculture through policies of purchasing organic products or products from local small-scale producers?",
    "Does your company adopt practices to avoid food waste in its operations?",
    "Does your company implement food education programs for its employees or customers?",
    "Does your company support projects or organizations working to improve food security and nutrition in vulnerable communities?",

    "Does your company offer wellness programs for its employees, such as physical activities, nutrition, or disease prevention programs?",
    "Does your company promote an organizational culture that values the mental and emotional health of employees?",
    "Does your company produce or sell products that promote the health and well-being of people?",
    "Does your company implement practices to ensure a safe and healthy work environment for its employees?",
    "Does your company support initiatives or organizations working to improve access to health and well-being in vulnerable communities?",

    "Does your company offer training and development programs for its employees?",
    "Does your company develop or produce products or services that help improve the quality of education?",
    "Does your company have partnerships with educational institutions or organizations working to improve the quality of education?",
    "Does your company implement policies to ensure equal educational opportunities for all?",
    "Does your company support projects or organizations working to improve access to and quality of education in vulnerable communities?",

    "Does your company adopt policies to ensure equal pay and opportunities for men and women?",
    "Does your company promote gender diversity in leadership and decision-making positions?",
    "Does your company adopt practices to combat gender harassment and violence in the workplace?",
    "Does your company promote gender equality through its products, services, or advertising campaigns?",
    "Does your company support initiatives or organizations working to promote gender equality and women's rights?",

    "Does your company adopt practices to minimize water pollution in its operations?",
    "Does your company support projects or organizations working to improve access to clean water and sanitation in vulnerable communities?",
    "Does your company implement measures to reduce water consumption in its operations?",
    "Does your company develop or produce products or services that help promote sustainable water use?",
    "Does your company measure and monitor the water footprint of its operations?",

    "Does your company adopt practices to reduce energy consumption in its operations?",
    "Does your company use renewable energy sources in its operations?",
    "Does your company support projects or organizations working to improve access to clean and affordable energy in vulnerable communities?",
    "Does your company develop or produce products or services that help promote the transition to a low-carbon economy?",
    "Does your company measure and monitor its greenhouse gas emissions?",

    "Does your company adopt policies to ensure decent work and fair compensation for its employees?",
    "Does your company promote diversity and inclusion in its hiring and promotions?",
    "Does your company adopt practices to ensure a safe and healthy work environment for its employees?",
    "Does your company support entrepreneurship and the economic growth of small businesses and startups?",
    "Does your company measure and monitor the impact of its activities on job creation and economic growth?",

    "Does your company invest in innovation and research to improve its products and services?",
    "Does your company adopt practices to minimize the environmental impact of its industrial processes?",
    "Does your company support the development of sustainable infrastructure in vulnerable communities?",
    "Does your company promote partnerships and collaboration among different sectors to promote innovation and sustainability?",
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
    "Does your company adopt policies to ensure its suppliers adopt responsible practices?",
    "Does your company promote consumer education and awareness of responsible consumption?",
    "Does your company measure and monitor the impact of its activities on responsible consumption and production?",

    "Does your company adopt practices to reduce its greenhouse gas emissions?",
    "Does your company use renewable energy sources in its operations?",
    "Does your company support projects or organizations working to mitigate the effects of climate change on vulnerable communities?",
    "Does your company develop or produce products or services that help promote adaptation to climate change?",
    "Does your company measure and monitor the impact of its activities on action against global climate change?",

    "Does your company adopt practices to minimize water pollution in its operations?",
    "Does your company support projects or organizations working to preserve marine life and aquatic ecosystems?",
    "Does your company develop or produce products or services that help promote the conservation of life in water?",
    "Does your company adopt practices to reduce water consumption in its operations?",
    "Does your company measure and monitor the impact of its activities on life in water?",

    "Does your company adopt practices to minimize the environmental impact of its operations on terrestrial ecosystems?",
    "Does your company support projects or organizations working to preserve biodiversity in terrestrial ecosystems?",
    "Does your company develop or produce products or services that help promote the conservation of life on land?",
    "Does your company adopt practices to reduce natural resource consumption in its operations?",
    "Does your company measure and monitor the impact of its activities on life on land?",

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
sg.theme('DarkBlue')

ods_list = [
    "1. Eradication of poverty",
    "2. Zero hunger and sustainable agriculture",
    "3. Health and well-being",
    "4. Quality education",
    "5. Gender equality",
    "6. Clean water and sanitation",
    "7. Affordable and clean energy",
    "8. Decent work and economic growth",
    "9. Industry, innovation and infrastructure",
    "10. Reduced inequalities",
    "11. Sustainable cities and communities",
    "12. Responsible consumption and production",
    "13. Climate action",
    "14. Life below water",
    "15. Life on land",
    "16. Peace, justice and strong institutions",
    "17. Partnerships for the goals"]

uri = {
    "1. Eradication of poverty": "QmdASsat2fzMV8Acir6byXiQ7CyRVyJH5prqftSvHta9wZ",
    "2. Zero hunger and sustainable agriculture": "Qmd2eLiowtrx2CSR4dZMjATuzzLigGfXzZwpcruSKi82gZ",
    "3. Health and well-being": "QmR5jSkBVcN4NknJxyJ7ErGBsmXf5n8iw7mDLUNAPkhcF7",
    "4. Quality education": "QmPtXu1HWTh3zMhqh6yhqRk1iqUVvcj74GABQkZiNEBKeu",
    "5. Gender equality": "QmYgwZeeUcw2vwTqCYky2iwrRXSDjKmaFoBfquZwAMJ1K7",
    "6. Clean Water and sanitation": "QmdcAuUYJbAwYzAV6QwrTS7j564tVD8WHDKCKMCWbb8eo8",
    "7. Affordable and clean energy": "QmcB1TWZdGHCwZGRhBnnpL9Kijr9Xr2xquFzn8ma43CBKz",
    "8. Decent work and economic growth": "QmdZbCrF4UdaoPB8tiyLdnHv7Zv1zgGPURxcx8q9t5WQrv",
    "9. Industry, innovation and infrastructure": "QmWV5NGDhboSVVUEWy5m5SmPiomT8pNFVSoaNz7LFXQdKo",
    "10. Reduced inequalities": "Qmcugn9wYTvY5DG9X57Sgcp9pXCKfaGG2ybjqgdJpyWVUL",
    "11. Sustainable cities and communities": "QmXKRaP9V47NbVcqL35PwQEJEPhGCqCaqmuiaTknNhhBMF",
    "12. Responsible consumption and production": "QmcVFz857NfuvQuJqExWVrMH4N3ETeBnk1YF66XNwumaq1",
    "13. Climate action": "QmYxN4iNNztaKjSN4cnghffmeeUv8Med4mrCYyMohUga97",
    "14. Life below water": "QmT5bsJCW3t658b8cjEvfDaXfQhGyWTjE7fJqo6PbyihiR",
    "15. Life on land":"QmWypB3ZN6ze7ZAm5c6NEecA35og21emE7QMnfdBcZurTJ",
    "16. Peace, justice and strong institutions":"QmejvA3o6zu39jY1kHnZCx97cMbW1QW2b51e9gaJnN4ynj",
    "17. Partnerships for the goals":"QmRuYGZpfPR5qLp1ubVtMB7Dk7DqUiuxeY3cwzSUZrtRDL"
    }


company_response = []
BASE_URL = "https://api.opensea.io/v2/orders/mumbai/seaport/listings"

layout = [[sg.Text('Company Name:')],
          [sg.Input(key='-COMPANY_NAME-', size=(30, 1))],
          [sg.Text('Type of Sustainable Development Goal (SDG):')],
          [sg.Listbox(values=ods_list, size=(30, 5), key='-ODS_TYPE-')],
          [sg.Button("Confirm")],
          [sg.Text(f'Question 1: {quests[0]}', key="quest1")],
          [sg.Input(key="answer1")],
          [sg.Text(f'Question 2: {quests[1]}', key="quest2")],
          [sg.Input(key="answer2")],
          [sg.Text(f'Question 3: {quests[2]}', key="quest3")],
          [sg.Input(key="answer3")],
          [sg.Text(f'Question 4: {quests[3]}', key="quest4")],
          [sg.Input(key="answer4")],
          [sg.Text(f'Question 5: {quests[4]}', key="quest5")],
          [sg.Input(key="answer5")],
          [sg.Button('Save'), sg.Button('Cancel')]]

window = sg.Window('Company Registration', layout)
p1 = window["quest1"]
p2 = window["quest2"]
p3 = window["quest3"]
p4 = window["quest4"]
p5 = window["quest5"]
print(len(ods_quests))
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Confirm':
        ods_type = values['-ODS_TYPE-'][0]
        if ods_type == ods_list[0]:
            p1.Update(f"Question 1: {ods_quests[0]}")
            p2.Update(f"Question 2: {ods_quests[1]}")
            p3.Update(f"Question 3: {ods_quests[2]}")
            p4.Update(f"Question 4: {ods_quests[3]}")
            p5.Update(f"Question 5: {ods_quests[4]}")
        elif ods_type == ods_list[1]:
            p1.Update(f"Question 1: {ods_quests[5]}")
            p2.Update(f"Question 2: {ods_quests[6]}")
            p3.Update(f"Question 3: {ods_quests[7]}")
            p4.Update(f"Question 4: {ods_quests[8]}")
            p5.Update(f"Question 5: {ods_quests[9]}")
        elif ods_type == ods_list[2]:
            p1.Update(f"Question 1: {ods_quests[10]}")
            p2.Update(f"Question 2: {ods_quests[11]}")
            p3.Update(f"Question 3: {ods_quests[12]}")
            p4.Update(f"Question 4: {ods_quests[13]}")
            p5.Update(f"Question 5: {ods_quests[14]}")
        elif ods_type == ods_list[3]:
            p1.Update(f"Question 1: {ods_quests[15]}")
            p2.Update(f"Question 2: {ods_quests[15]}")
            p3.Update(f"Question 3: {ods_quests[17]}")
            p4.Update(f"Question 4: {ods_quests[18]}")
            p5.Update(f"Question 5: {ods_quests[19]}")
        elif ods_type == ods_list[4]:
            p1.Update(f"Question 1: {ods_quests[20]}")
            p2.Update(f"Question 2: {ods_quests[21]}")
            p3.Update(f"Question 3: {ods_quests[22]}")
            p4.Update(f"Question 4: {ods_quests[23]}")
            p5.Update(f"Question 5: {ods_quests[24]}")
        elif ods_type == ods_list[5]:
            p1.Update(f"Question 1: {ods_quests[25]}")
            p2.Update(f"Question 2: {ods_quests[26]}")
            p3.Update(f"Question 3: {ods_quests[27]}")
            p4.Update(f"Question 4: {ods_quests[28]}")
            p5.Update(f"Question 5: {ods_quests[29]}")
        elif ods_type == ods_list[6]:
            p1.Update(f"Question 1: {ods_quests[30]}")
            p2.Update(f"Question 2: {ods_quests[31]}")
            p3.Update(f"Question 3: {ods_quests[32]}")
            p4.Update(f"Question 4: {ods_quests[33]}")
            p5.Update(f"Question 5: {ods_quests[34]}")
        elif ods_type == ods_list[7]:
            p1.Update(f"Question 1: {ods_quests[35]}")
            p2.Update(f"Question 2: {ods_quests[36]}")
            p3.Update(f"Question 3: {ods_quests[37]}")
            p4.Update(f"Question 4: {ods_quests[38]}")
            p5.Update(f"Question 5: {ods_quests[39]}")
        elif ods_type == ods_list[8]:
            p1.Update(f"Question 1: {ods_quests[40]}")
            p2.Update(f"Question 2: {ods_quests[41]}")
            p3.Update(f"Question 3: {ods_quests[42]}")
            p4.Update(f"Question 4: {ods_quests[43]}")
            p5.Update(f"Question 5: {ods_quests[44]}")
        elif ods_type == ods_list[9]:
            p1.Update(f"Question 1: {ods_quests[45]}")
            p2.Update(f"Question 2: {ods_quests[46]}")
            p3.Update(f"Question 3: {ods_quests[47]}")
            p4.Update(f"Question 4: {ods_quests[48]}")
            p5.Update(f"Question 5: {ods_quests[49]}")
        elif ods_type == ods_list[10]:
            p1.Update(f"Question 1: {ods_quests[50]}")
            p2.Update(f"Question 2: {ods_quests[51]}")
            p3.Update(f"Question 3: {ods_quests[52]}")
            p4.Update(f"Question 4: {ods_quests[53]}")
            p5.Update(f"Question 5: {ods_quests[54]}")
        elif ods_type == ods_list[11]:
            p1.Update(f"Question 1: {ods_quests[55]}")
            p2.Update(f"Question 2: {ods_quests[56]}")
            p3.Update(f"Question 3: {ods_quests[57]}")
            p4.Update(f"Question 4: {ods_quests[58]}")
            p5.Update(f"Question 5: {ods_quests[59]}")
        elif ods_type == ods_list[12]:
            p1.Update(f"Question 1: {ods_quests[60]}")
            p2.Update(f"Question 2: {ods_quests[61]}")
            p3.Update(f"Question 3: {ods_quests[62]}")
            p4.Update(f"Question 4: {ods_quests[63]}")
            p5.Update(f"Question 5: {ods_quests[64]}")
        elif ods_type == ods_list[13]:
            p1.Update(f"Question 1: {ods_quests[65]}")
            p2.Update(f"Question 2: {ods_quests[66]}")
            p3.Update(f"Question 3: {ods_quests[67]}")
            p4.Update(f"Question 4: {ods_quests[68]}")
            p5.Update(f"Question 5: {ods_quests[69]}")
        elif ods_type == ods_list[14]:
            p1.Update(f"Question 1: {ods_quests[70]}")
            p2.Update(f"Question 2: {ods_quests[71]}")
            p3.Update(f"Question 3: {ods_quests[72]}")
            p4.Update(f"Question 4: {ods_quests[73]}")
            p5.Update(f"Question 5: {ods_quests[74]}")
        elif ods_type == ods_list[15]:
            p1.Update(f"Question 1: {ods_quests[75]}")
            p2.Update(f"Question 2: {ods_quests[76]}")
            p3.Update(f"Question 3: {ods_quests[77]}")
            p4.Update(f"Question 4: {ods_quests[78]}")
            p5.Update(f"Question 5: {ods_quests[79]}")
        elif ods_type == ods_list[16]:
            p1.Update(f"Question 1: {ods_quests[80]}")
            p2.Update(f"Question 2: {ods_quests[81]}")
            p3.Update(f"Question 3: {ods_quests[82]}")
            p4.Update(f"Question 4: {ods_quests[83]}")
            p5.Update(f"Question 5: {ods_quests[84]}")
        elif ods_type == ods_list[17]:
            p1.Update(f"Question 1: {ods_quests[85]}")
            p2.Update(f"Question 2: {ods_quests[86]}")
            p3.Update(f"Question 3: {ods_quests[87]}")
            p4.Update(f"Question 4: {ods_quests[88]}")
            p5.Update(f"Question 5: {ods_quests[89]}")


    elif event == 'Save':
        company_name = values['-COMPANY_NAME-']
        ods_type = values['-ODS_TYPE-'][0]
        data = {
            "name": company_name,
            "ods": ods_type,
            "image": f"ipfs://ipfs/{uri[ods_type]}",
            "attributes": [
                {
                    "type": "answer1",
                    "value": values["answer1"]
                },

                {
                    "type": "answer2",
                    "value": values["answer2"]
                },

                {
                    "type": "answer3",
                    "value": values["answer3"]
                },

                {
                    "type": "answer4",
                    "value": values["answer4"]
                },

                {
                    "type": "answer5",
                    "value": values["answer5"]
                }

            ]

        }
        break

# for info in data:
# print(info)
for k, v in data.items():
    with open(f"{company_name}.json", "w+") as file:
        json.dump(data, file)
x = 0
for y in range(-1, len(data)):
    with open(f"{company_name}.txt", "a+") as file:
        file.write(f"answer {x + 1}: {data['attributes'][x]['value']}\n")
    x += 1
window.close()
