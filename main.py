import asyncio
import message_analyser.retriever.telegram as tg
import message_analyser.analyser


async def get_dialogs(loop):
    dialogs = await tg.get_str_dialogs(loop=loop)
    print(dialogs)

if __name__ == "__main__":
    aio_loop = asyncio.get_event_loop()

    key = input("For getting dialogs type d, for getting&analyzing type g, for analyzing from file a: ")

    if key == 'd':
        asyncio.get_event_loop().run_until_complete(get_dialogs(aio_loop))

    if key == 'g':
        asyncio.get_event_loop().run_until_complete(message_analyser.analyser.retrieve_and_analyse(aio_loop))

    if key == 'a':
        path = input("type path to file")
        message_analyser.analyser.analyse_from_file(path)