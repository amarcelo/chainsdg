from requests import get
from datetime import datetime
import PySimpleGUI as sg
import tkinter as tk
from time import sleep

# API KEY criada na polygon
API_KEY = 'V9DB1JSDW3YCT2XGVSK7URWGPW41J84VGB'
BASE_URl = "https://api-testnet.polygonscan.com/api"
yy = mm = dd = h = min = seg = 0
date4 = [yy, mm, dd, h, min, seg]
MATIC_VALUE = 10**18
blockchain_normal_tx = blockchain_internal_tx = blockchain_out_of_gas_tx = blockchain_account_transfer = []
address = "0x09C65b58633d139e2C26B89B975240b1FFBAEd6E"
file_name_extension = "default"
# Side Defs



def make_api_url(module, action, **kwargs):
    url = BASE_URl + f'?module={module}&action={action}&apikey={API_KEY}'
    for k, v in kwargs.items():
        url += f'&{k}={v}'
    #url += f"&apikey={API_KEY}"
    return url



def get_last_block():
    BLOCK_NUMBER = make_api_url("proxy", "eth_blockNumber")
    response4 = get(BLOCK_NUMBER)
    data4 = response4.json()
    latest_block = data4["result"]
    return int(latest_block, base=16)


# Getting block by timeStamp
def get_block_byTimeStamp(get_timestamp):
    call_block_no = make_api_url("block", "getblocknobytime", timestamp=get_timestamp, closest="before")
    api_call = get(call_block_no)
    block_no = api_call.json()
    return block_no["result"]

# Getting the block date by using get_block_by_TimeStamp method
def get_block_by_date(input_data):
    date = input_data.split()
    date_in_datetime = datetime(*map(int, date))
    timeStamp = datetime.timestamp(date_in_datetime).__trunc__()
    block = get_block_byTimeStamp(timeStamp)
    return block


def get_time_by_block(block):
    get_time_api = make_api_url("block","getblockreward",blockno=block)
    request_time_api = get(get_time_api)
    time_api_json = request_time_api.json()
    date_in_timeStamp = time_api_json["result"]["timeStamp"]
    current_date = datetime.fromtimestamp(date_in_timeStamp)
    return current_date

def open_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    window = tk.Toplevel()
    text = tk.Text(window)
    text.insert('end', content)
    text.pack()


def save_file(data):
    file_path = sg.SaveFileDialog(title="Salvar arquivo", file_types=(("Arquivo de texto", "*.txt"),))
    if file_path == '':
        return  # usuário cancelou o diálogo de arquivo
    if not file_path.endswith(".txt"):
        file_path += ".txt"
    with open(file_path, 'w') as file:
        file.write(data)

#getting the analyzed block time


def initialize(start_date, end_date,address_given):
    start = get_block_by_date(start_date)
    end = get_block_by_date(end_date)
    address = str(address_given) if len(address_given) > 0 else "0x09C65b58633d139e2C26B89B975240b1FFBAEd6E"
    return start, end, address


sg.theme('DarkPurple4')  # tema da janela

layout = [[sg.Image(filename='polygon.png')],
    [sg.Text('SDGAudit Mumbai', font=('Helvetica', 20, 'bold'))],
    [sg.Text('Initial date:', font=('Helvetica', 12)), sg.InputText(key='start_date', font=('Helvetica', 12))],
    [sg.Text('Final date:', font=('Helvetica', 12)), sg.InputText(key='end_date', font=('Helvetica', 12))],
    [sg.Text("address:", font=('Helvetica', 12)), sg.InputText(key="address", font=('Helvetica', 12))],
    [sg.Button('Option 1', key='option1', font=('Helvetica', 12)),
     sg.Button('Option 2', key='option2', font=('Helvetica', 12)),
     sg.Button('Option 3', key='option3', font=('Helvetica', 12)),
     sg.Button('Option 4', key='option4', font=('Helvetica', 12)),
     sg.Button('Option 5', key='option5', font=('Helvetica', 12))],
    [sg.Text("Option 1: Get all Address's normal transactions\nOption 2: Get all Address's internal transactions\nOption 3: Get all Address's ERC721 transaction event\n    (default: contractaddress = 0xd6f9e7defa52ac67cdfd6a9a352ce6e0a9684b0a\n    address=0xbb282ced765a2a2573747f04101cabd2adab8f45) \nOption 4: Get Account balance \n  (default: contractAddress ='0x0000000000000000000000000000000000001010)'\nOption 5: Get all Address's ERC20 transaction event", font=('Black', 12))],
    [sg.Button('Open file', font=('Helvetica', 12)), sg.Button("Save file", font=('Helvetica', 12)),     sg.Button("Parar", font=('Helvetica', 12))]
]
# Criação da janela
window = sg.Window('Menu', layout)


# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Parar":
        break
    # Getting all Address's normal transactions
    if event == 'option1':
        file_name_extension = "normalTx"
        start, end, address = initialize(values["start_date"], values["end_date"], values["address"])
        total_blocks = int(end) - int(start)
        try:
            LIST_NORMAL_TX = make_api_url("account", "txlist", address=address,
                                          startblock=start, endblock=end,
                                          page=1, offset=10000, sort="asc")
            request1 = get(LIST_NORMAL_TX)
            data1 = request1.json()
            normal_tx_result = data1["result"]
            # Address's last activity block
            last_block1 = int(normal_tx_result[-1]["blockNumber"])
            # Address's last transaction
            last_transaction1 = normal_tx_result[-1]["hash"]
            # Address's last transaction date
            last_transaction_date1 = int(normal_tx_result[-1]["timeStamp"])
            #print(f'Stopped in block:{last_block1} hash: {last_transaction1} date: {datetime.fromtimestamp(last_transaction_date1)}')
        except:
            #print("cant reach API's information.")
            sg.popup("Cant reach API's information.")
        blockchain_normal_tx.extend(transaction for transaction in normal_tx_result)
        sleep(1)
        # Creating .txt file
        for item in blockchain_normal_tx:
            with open(f"{address}_{file_name_extension}.txt", "a+") as f:
                f.write("----------------------------------------------\n")
                f.write(
                    f"block: {item['blockNumber']}\n"
                    f"date: {datetime.fromtimestamp(int(item['timeStamp']))}\n"
                    f"hash: {item['hash']}\n"
                    f"nonce: {item['nonce']}\n"
                    f"blockHash:{item['blockHash']}\n"
                    f"transactionIndex:{item['transactionIndex']}\n"
                    f"from:{item['from']}\n"
                    f"to: {item['to'] if len(item['to']) > 0 else 'Contract creation'}\n"
                    f"value: {item['value']}\n"
                    f"gas : {item['gas']}\n"
                    f"gasPrice:{item['gasPrice']}\n"
                    f"isError : {item['isError']}\n"
                    f"txreceipt_status: {item['txreceipt_status']}\n"
                    # f"input: {item['input']}\n"
                    # f"contractAddress: {item['contractAddress']}\n"
                    # f"cumulativeGasUsed: {item['cumulativeGasUsed']}\n"
                    f"gasUsed:{item['gasUsed']}\n"
                    f"confirmations:{item['confirmations']}\n"
                )
    # Getting all Address's internal transactions
    elif event == 'option2':
        file_name_extension = "internalTx"
        start, end, address = initialize(values["start_date"], values["end_date"],values["address"])
        try:
            LIST_INTERNAL_TX = make_api_url("account", "txlistinternal", address=address, startblock=start, endblock=end,
                                            page=1, offset=10000, sort="asc")
            request2 = get(LIST_INTERNAL_TX)
            data2 = request2.json()
            internal_tx_result = data2["result"]
            # Address's last activity block
            last_block_in_list2 = internal_tx_result[-1]["blockNumber"]
            # Address's last transaction
            last_transaction2 = internal_tx_result[-1]["hash"]
            # Address's last transaction date
            last_transaction_date2 = int(internal_tx_result[-1]["timeStamp"])

            print(
                f'Stopped in block:{last_block_in_list2} hash: {last_transaction2} date: {datetime.fromtimestamp(last_transaction_date2)}')
        except:
            print("cant reach API's information.")

        blockchain_internal_tx.extend(transaction for transaction in internal_tx_result)#float(transaction["value"]) / MATIC_VALUE >= float(min_value)
        sleep(1)
        for item in blockchain_internal_tx:
            with open(f"{address}_{file_name_extension}.txt", "a+") as f:
                f.write("----------------------------------------------\n")
                f.write(
                f"blockNumber: {item['blockNumber']}\n"
                f"timeStamp: {item['timeStamp']}\n"
                f"hash: {item['hash']}\n"
                f"from: {item['from']}\n"
                f"to: {item['to']}\n"
                f"value: {item['value']}\n"
                f"contractAddress: {item['contractAddress']}\n"
                #f"input: {item['input']}\n"
                #f"type: {item['type']}\n"
                f"gas: {item['gas']}\n"
                f"gasUsed: {item['gasUsed']}\n"
                f"traceId: {item['traceId']}\n"
                f"isError: {item['isError']}\n"
                #f"errCode: {item['errCode']}"
                )
    elif event == 'option3':
        file_name_extension = "accountERC721Transfer"
        start, end, address = initialize(values["start_date"], values["end_date"], values["address"])
        try:
            GET_ERC20_ACCOUNT_TRANSFER = make_api_url("account", "tokennfttx",
                                                      contractaddress="0xd6f9e7defa52ac67cdfd6a9a352ce6e0a9684b0a",
                                                      address="0xbb282ced765a2a2573747f04101cabd2adab8f45", page=1, offset=10000, sort="asc")
            request3 = get(GET_ERC20_ACCOUNT_TRANSFER)
            data3 = request3.json()
            account_ERC721_transfer_result = data3['result']
        except:
            print("cant reach API's information.")
        blockchain_account_transfer.extend(transaction for transaction in account_ERC721_transfer_result)
        sleep(1)
        # print(f"FILE: {address}_{file_name_extension}.txt")
        for item in account_ERC721_transfer_result:
            with open(f"{address}_{file_name_extension}.txt", "a+") as f:
                f.write("-------------------------------------\n")
                f.write(
                    f"blockNumber: {item['blockNumber']}\n"
                    f"timeStamp: {item['timeStamp']}\n"
                    f"hash: {item['hash']}\n"
                    f"nonce: {item['nonce']}\n"
                    f"blockHash: {item['blockHash']}\n"
                    f"from: {item['from']}\n"
                    f"contractAddress: {item['contractAddress']}\n"
                    f"to: {item['to']}\n"
                    f"tokenID:{item['tokenID']}\n"
                    f"tokenName: {item['tokenName']}\n"
                    f"tokenSymbol: {item['tokenSymbol']}\n"
                    f"tokenDecimal: {item['tokenDecimal']}\n"
                    f"transactionIndex: {item['transactionIndex']}\n"
                    f"gas: {item['gas']}\n"
                    f"gasPrice: {item['gasPrice']}\n"
                    f"gasUsed: {item['gasUsed']}\n"
                    f"cumulativeGasUsed: {item['cumulativeGasUsed']}\n"
                    f"input: {item['input']}\n"
                    f"confirmations: {item['confirmations']}\n"
                        )
    elif event == 'option4':
        address = values["address"]
        #contract_address = values["contract_address"] for future
        try:
            GET_ERC20_ACCOUNT_BALANCE = make_api_url("account", "tokenbalance",
                                                     contractaddress="0x0000000000000000000000000000000000001010",
                                                     address=address, tag="latest")

            request4 = get(GET_ERC20_ACCOUNT_BALANCE)
            data4 = request4.json()
            account_balance_result = float(data4["result"])
        except:
            print("cant reach API's information.")

        sleep(1)
        try:
            sg.popup(f"{account_balance_result/MATIC_VALUE:.5f} MATIC")
        except:
            sg.popup("Address invalid")
    # Getting all Address's ERC20 transaction event
    elif event == 'option5':
        file_name_extension = "accountERC20Transfer"
        start, end, address = initialize(values["start_date"], values["end_date"], values["address"])
        try:
            GET_ERC20_ACCOUNT_TRANSFER = make_api_url("account", "tokentx",contractaddress="0x0000000000000000000000000000000000001010",
                                                      address=address, page=1, offset=10000, sort="asc")
            request5 = get(GET_ERC20_ACCOUNT_TRANSFER)
            data5 = request5.json()
            account_ERC20_transfer_result = data5['result']
        except:
            print("cant reach API's information.")
        blockchain_account_transfer.extend(transaction for transaction in account_ERC20_transfer_result)
        sleep(1)
        #print(f"FILE: {address}_{file_name_extension}.txt")
        for item in blockchain_account_transfer:
            with open(f"{address}_{file_name_extension}.txt", "a+") as f:
                f.write("-------------------------------------\n")
                f.write(
                f"blockNumber: {item['blockNumber']}\n"
                f"timeStamp: {item['timeStamp']}\n"
                f"hash: {item['hash']}\n"
                f"nonce: {item['nonce']}\n"
                f"blockHash: {item['blockHash']}\n"
                f"from: {item['from']}\n"
                f"contractAddress: {item['contractAddress']}\n"
                f"to: {item['to']}\n"
                f"value: {item['value']}\n"
                f"tokenName: {item['tokenName']}\n"
                f"tokenSymbol: {item['tokenSymbol']}\n"
                f"tokenDecimal: {item['tokenDecimal']}\n"
                f"transactionIndex: {item['transactionIndex']}\n"
                f"gas: {item['gas']}\n"
                f"gasPrice: {item['gasPrice']}\n"
                f"gasUsed: {item['gasUsed']}\n"
                f"cumulativeGasUsed: {item['cumulativeGasUsed']}\n"
                f"input: {item['input']}\n"
                f"confirmations: {item['confirmations']}\n"
                )
    # Opening the file
    elif event == 'Open file':
        try:
            with open(f"{address}_{file_name_extension}.txt", 'r') as f:
                contents = f.read()
                sg.popup_scrolled(contents, title=f'{address}_{file_name_extension} file information')
        except:
            sg.popup('Not found')
        file_name_extension = ""
    # Saving the file
    elif event == 'Save file':
        filename = sg.popup_get_file("Salvar arquivo", save_as=True, file_types=(("Arquivos de texto", "*.txt"),))
        try:
            with open(f"{address}_{file_name_extension}.txt", "w") as f:
                f.write("--------------------------------------------")
                f.write(
                    f"{address}_{file_name_extension} information:\n"
                    f"block: {item['blockNumber']}\n"
                    f"date: {datetime.fromtimestamp(int(item['timeStamp']))}\n"
                    f"hash: {item['hash']}\n"
                    f"nonce: {item['nonce']}\n"
                    f"blockHash:{item['blockHash']}\n"
                    f"transactionIndex:{item['transactionIndex']}\n"
                    f"from:{item['from']}\n"
                    f"to: {item['to'] if len(item['to']) > 0 else 'Contract creation'}\n"
                    f"value: {item['value']}\n"
                    f"gas : {item['gas']}\n"
                    f"gasPrice:{item['gasPrice']}\n"
                    f"isError : {item['isError']}\n"
                    f"txreceipt_status: {item['txreceipt_status']}\n"
                    # f"input: {item['input']}\n"
                    # f"contractAddress: {item['contractAddress']}\n"
                    # f"cumulativeGasUsed: {item['cumulativeGasUsed']}\n"
                    f"gasUsed:{item['gasUsed']}\n"
                    f"confirmations:{item['confirmations']}\n"
                )
            sg.popup("Arquivo salvo com sucesso!")
        except:
            sg.popup('Not found')
# Close window
window.close()
