import pyvts
import asyncio

async def connect_auth(myvts):
    await myvts.connect()
    await myvts.request_authenticate_token()
    await myvts.request_authenticate()
    await myvts.close()

async def trigger(myvts):
    await myvts.connect()
    await myvts.request_authenticate()
    response_data = await myvts.request(myvts.vts_request.requestHotKeyList())
    print(response_data)
    hotkey_list = []
    for hotkey in response_data['data']['availableHotkeys']:
        hotkey_list.append(hotkey['name'])
    command = int(input(f'Action(0-{int(len(hotkey_list)) - 1}):'))
    send_hotkey_request = myvts.vts_request.requestTriggerHotKey(hotkey_list[command])
    await myvts.request(send_hotkey_request)
    await myvts.close()

if __name__ == "__main__":
    myvts = pyvts.vts()
    myvtsRQ = pyvts.VTSRequest()
    asyncio.run(connect_auth(myvts))
    while True:
        try:    
            asyncio.run(trigger(myvts))
        except IndexError:
            print('Error: Index out of range')