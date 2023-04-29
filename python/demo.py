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
"Qual é a proporção de funcionários em sua empresa que recebem um salário mínimo digno?",
"Que tipos de produtos ou serviços a sua empresa oferece para melhorar a qualidade de vida das pessoas em situação de pobreza?",
"Sua empresa adota práticas para promover a inclusão de pessoas em situação de vulnerabilidade econômica?",
"Sua empresa tem políticas de doação ou filantropia para apoiar organizações que trabalham na erradicação da pobreza?",
"Como a sua empresa mede e monitora o impacto de suas atividades na redução da pobreza?",

"Sua empresa usa ingredientes sustentáveis e produzidos localmente em seus produtos ou serviços?",
"Sua empresa apoia a agricultura sustentável por meio de políticas de compras de produtos orgânicos ou de pequenos produtores locais?",
"Sua empresa adota práticas para evitar o desperdício de alimentos em suas operações?",
"Sua empresa implementa programas de educação alimentar para seus funcionários ou clientes?",
"Sua empresa apoia projetos ou organizações que trabalham para melhorar a segurança alimentar e nutricional em comunidades vulneráveis?",

"Sua empresa oferece programas de bem-estar para seus funcionários, como atividades físicas, nutrição ou programas de prevenção de doenças?",
"Sua empresa promove uma cultura organizacional que valoriza a saúde mental e emocional dos funcionários?",
"Sua empresa produz ou vende produtos que promovem a saúde e o bem-estar das pessoas?",
"Sua empresa implementa práticas para garantir um ambiente de trabalho seguro e saudável para seus funcionários?",
"Sua empresa apoia iniciativas ou organizações que trabalham para melhorar o acesso à saúde e ao bem-estar em comunidades vulneráveis?",

"Sua empresa oferece programas de capacitação e treinamento para seus funcionários?",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a melhorar a qualidade da educação?",
"Sua empresa tem parcerias com instituições de ensino ou organizações que trabalham para melhorar a qualidade da educação?",
"Sua empresa implementa políticas para garantir a igualdade de oportunidades de educação para todos?",
"Sua empresa apoia projetos ou organizações que trabalham para melhorar o acesso e a qualidade da educação em comunidades vulneráveis?",


"Sua empresa adota políticas para garantir a igualdade de remuneração e oportunidades para homens e mulheres?",
"Sua empresa promove a diversidade de gênero em cargos de liderança e tomada de decisão?",
"Sua empresa adota práticas para combater o assédio e a violência de gênero no ambiente de trabalho?",
"Sua empresa promove a igualdade de gênero por meio de seus produtos, serviços ou campanhas publicitárias?",
"Sua empresa apoia iniciativas ou organizações que trabalham para promover a igualdade de gênero e os direitos das mulheres?",

"Sua empresa adota práticas para minimizar a poluição da água em suas operações?",
"Sua empresa apoia projetos ou organizações que trabalham para melhorar o acesso à água limpa e ao saneamento em comunidades vulneráveis?",
"Sua empresa implementa medidas para reduzir o consumo de água em suas operações?",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a promover o uso sustentável da água?",
"Sua empresa mede e monitora a pegada hídrica de suas operações?",

"Sua empresa adota práticas para reduzir o consumo de energia em suas operações?",
"Sua empresa usa fontes de energia renovável em suas operações?",
"Sua empresa apoia projetos ou organizações que trabalham para melhorar o acesso à energia limpa e acessível em comunidades vulneráveis?",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a promover a transição para uma economia de baixo carbono?",
"Sua empresa mede e monitora suas emissões de gases de efeito estufa?",

"Sua empresa adota políticas para garantir o trabalho decente e a remuneração justa de seus funcionários?",
"Sua empresa promove a diversidade e a inclusão em suas contratações e promoções?",
"Sua empresa adota práticas para garantir um ambiente de trabalho seguro e saudável para seus funcionários?",
"Sua empresa apoia o empreendedorismo e o crescimento econômico de pequenas empresas e startups?",
"Sua empresa mede e monitora o impacto de suas atividades na geração de empregos e no crescimento econômico?",

"Sua empresa investe em inovação e pesquisa para melhorar seus produtos e serviços?",
"Sua empresa adota práticas para minimizar o impacto ambiental de seus processos industriais?",
"Sua empresa apoia o desenvolvimento de infraestrutura sustentável em comunidades vulneráveis?",
"Sua empresa promove parcerias e colaboração entre diferentes setores para promover a inovação e a sustentabilidade?",
"Sua empresa mede e monitora o impacto de suas atividades na indústria, inovação e infraestrutura sustentáveis?",


"Sua empresa adota políticas para garantir a igualdade de oportunidades e a inclusão de grupos marginalizados?",
"Sua empresa apoia projetos ou organizações que trabalham para reduzir as des",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a reduzir as desigualdades sociais e econômicas?",
"Sua empresa adota práticas para combater o preconceito e a discriminação em suas operações?",
"Sua empresa mede e monitora o impacto de suas atividades na redução das desigualdades?",

"Sua empresa adota práticas para reduzir o impacto ambiental de seus prédios e instalações?",
"Sua empresa apoia projetos ou organizações que trabalham para melhorar a qualidade de vida em comunidades vulneráveis?",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a promover o transporte sustentável e o planejamento urbano?",
"Sua empresa adota práticas para promover a diversidade cultural e o patrimônio histórico em suas operações?",
"Sua empresa mede e monitora o impacto de suas atividades na promoção de cidades e comunidades sustentáveis?",

"Sua empresa adota práticas para minimizar o desperdício e a poluição em suas operações?",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a promover o consumo e a produção sustentáveis?",
"Sua empresa adota políticas para garantir que seus fornecedores adotem práticas responsáveis?",
"Sua empresa promove a educação e a conscientização do consumidor sobre o consumo responsável?",
"Sua empresa mede e monitora o impacto de suas atividades no consumo e produção responsáveis?",

"Sua empresa adota práticas para reduzir suas emissões de gases de efeito estufa?",
"Sua empresa usa fontes de energia renovável em suas operações?",
"Sua empresa apoia projetos ou organizações que trabalham para mitigar os efeitos da mudança climática em comunidades vulneráveis?",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a promover a adaptação à mudança climática?",
"Sua empresa mede e monitora o impacto de suas atividades na ação contra a mudança global do clima?",

"Sua empresa adota práticas para minimizar a poluição da água em suas operações?",
"Sua empresa apoia projetos ou organizações que trabalham para preservar a vida marinha e os ecossistemas aquáticos?",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a promover a conservação da vida na água?",
"Sua empresa adota práticas para reduzir o consumo de água em suas operações?",
"Sua empresa mede e monitora o impacto de suas atividades na vida na água?",

"Sua empresa adota práticas para minimizar o impacto ambiental de suas operações em ecossistemas terrestres?",
"Sua empresa apoia projetos ou organizações que trabalham para preservar a biodiversidade em ecossistemas terrestres?",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a promover a conservação da vida terrestre?",
"Sua empresa adota práticas para reduzir o consumo de recursos naturais em suas operações?",
"Sua empresa mede e monitora o impacto de suas atividades na vida terrestre?",

"Sua empresa adota práticas para garantir a transparência e a ética em suas operações?",
"Sua empresa desenvolve ou produz produtos ou serviços que ajudam a promover a justiça e a igualdade social?",
"Sua empresa adota políticas para garantir o respeito aos direitos humanos em todas as suas operações?",
"Sua empresa promove a cultura de paz e a resolução pacífica de conflitos?",
"Sua empresa mede e monitora o impacto de suas atividades na paz, justiça e instituições eficazes?",

"Sua empresa busca estabelecer parcerias com outras organizações para maximizar seu impacto positivo?",
"Sua empresa adota práticas para garantir a transparência e a responsabilidade em suas parcerias?",
"Sua empresa apoia projetos ou organizações que trabalham para promover as ODS?",
"Sua empresa adota práticas para promover a capacitação e o desenvolvimento de seus funcionários?",
"Sua empresa mede e monitora o impacto de suas atividades nas parcerias e meios de implementação das ODS?"

]
import PySimpleGUI as sg
import json
sg.theme('DarkBlue')

ods_list = ["1. Erradicação da pobreza",
            "2. Fome zero e agricultura sustentável",
            "3. Saúde e bem-estar",
            "4. Educação de qualidade",
            "5. Igualdade de gênero",
            "6. Água potável e saneamento",
            "7. Energia limpa e acessível",
            "8. Trabalho decente e crescimento econômico",
            "9. Indústria, inovação e infraestrutura",
            "10. Redução das desigualdades",
            "11. Cidades e comunidades sustentáveis",
            "12. Consumo e produção responsáveis",
            "13. Ação contra a mudança global do clima",
            "14. Vida na água",
            "15. Vida terrestre",
            "16. Paz, justiça e instituições eficazes",
            "17. Parcerias e meios de implementação"]

uri = {"1. Erradicação da pobreza": "QmdASsat2fzMV8Acir6byXiQ7CyRVyJH5prqftSvHta9wZ",
       "2. Fome zero e agricultura sustentável":"Qmd2eLiowtrx2CSR4dZMjATuzzLigGfXzZwpcruSKi82gZ",
       "3. Saúde e bem-estar":"QmR5jSkBVcN4NknJxyJ7ErGBsmXf5n8iw7mDLUNAPkhcF7",
       "4. Educação de qualidade":"QmPtXu1HWTh3zMhqh6yhqRk1iqUVvcj74GABQkZiNEBKeu",
       "5. Igualdade de gênero":"QmYgwZeeUcw2vwTqCYky2iwrRXSDjKmaFoBfquZwAMJ1K7",
       "6. Água potável e saneamento":"QmdcAuUYJbAwYzAV6QwrTS7j564tVD8WHDKCKMCWbb8eo8",
       "7. Energia limpa e acessível":"QmcB1TWZdGHCwZGRhBnnpL9Kijr9Xr2xquFzn8ma43CBKz",
       "8. Trabalho decente e crescimento econômico":"QmdZbCrF4UdaoPB8tiyLdnHv7Zv1zgGPURxcx8q9t5WQrv",
       "9. Indústria, inovação e infraestrutura":"QmWV5NGDhboSVVUEWy5m5SmPiomT8pNFVSoaNz7LFXQdKo",
       "10. Redução das desigualdades":"Qmcugn9wYTvY5DG9X57Sgcp9pXCKfaGG2ybjqgdJpyWVUL",
       "11. Cidades e comunidades sustentáveis":"QmXKRaP9V47NbVcqL35PwQEJEPhGCqCaqmuiaTknNhhBMF",
       "12. Consumo e produção responsáveis":"QmcVFz857NfuvQuJqExWVrMH4N3ETeBnk1YF66XNwumaq1",
       "13. Ação contra a mudança global do clima":"QmYxN4iNNztaKjSN4cnghffmeeUv8Med4mrCYyMohUga97",
        "14. Vida na água":"QmT5bsJCW3t658b8cjEvfDaXfQhGyWTjE7fJqo6PbyihiR",
        "15. Vida terrestre":"QmWypB3ZN6ze7ZAm5c6NEecA35og21emE7QMnfdBcZurTJ",
        "16. Paz, justiça e instituições eficazes":"QmejvA3o6zu39jY1kHnZCx97cMbW1QW2b51e9gaJnN4ynj",
        "17. Parcerias e meios de implementação": "QmRuYGZpfPR5qLp1ubVtMB7Dk7DqUiuxeY3cwzSUZrtRDL"}
resposta_empresa = []
BASE_URL = "https://api.opensea.io/v2/orders/mumbai/seaport/listings"

layout = [[sg.Text('Nome da Empresa:')],
          [sg.Input(key='-NOME_EMPRESA-', size=(30,1))],
          [sg.Text('Tipo de ODS:')],
          [sg.Listbox(values=ods_list, size=(30,5), key='-TIPO_ODS-')],
          [sg.Button("Confirmar")],
          [sg. Text(f'Pergunta 1: {perguntas[0]}',key="quest1")],
          [sg.Input(key="resposta1")],
          [sg. Text(f'Pergunta 2: {perguntas[1]}',key="quest2")],
          [sg.Input(key="resposta2")],
          [sg. Text(f'Pergunta 3: {perguntas[2]}',key="quest3")],
          [sg.Input(key="resposta3")],
          [sg. Text(f'Pergunta 4: {perguntas[3]}',key="quest4")],
          [sg.Input(key="resposta4")],
          [sg. Text(f'Pergunta 5: {perguntas[4]}',key="quest5")],
          [sg.Input(key="resposta5")],
          [sg.Button('Salvar'), sg.Button('Cancelar')]]

window = sg.Window('Cadastro de Empresa', layout)
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