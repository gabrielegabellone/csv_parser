import argparse
import csv
import asyncio


def csv_reader(file_path: str):
    """It takes care of yielding the rows of a csv file.

    :param file_path: the path of the csv file to read
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row


async def process_data(queue: asyncio.Queue):
    """Takes care of processing the objects that are put in the queue passed as a parameter.
    Processing ends when the object taken from the queue is `None`.

    :param queue: an Asyncio queue that will receive the objects to process
    """
    while True:
        row = await queue.get()
        if row is None:
            break
        print(f'Processing {row}')


async def main(file_path):
    queue = asyncio.Queue()

    # create and start the processing coroutine
    processor = asyncio.create_task(process_data(queue))

    # reads the CSV and inserts the rows into the queue
    for row in csv_reader(file_path):
        await queue.put(row)

    await queue.put(None)
    await processor  # wait for the processing coroutine to finish


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    asyncio.run(main(args.filename))
