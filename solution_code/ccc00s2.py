#Babbling Brooks ccc00s2

from math import floor
import sys

from typing import List


def split_strm(stream: int, perce: int) -> List[float]:

    return (stream * perce / 100), (stream * (1 - perce/ 100))

def join_strm(stream: int, stream_rt: int) -> List[float]:

    return stream + stream_rt

def gettinput():

    getting_input = []

    while True:

        reader = int(sys.stdin.readline().strip('\n'))

        if reader != 77:

            getting_input.append(reader)

        else:

            break

    streams = getting_input[0] + 1

    #print(f'streams, {streams}')

    ind_stream = getting_input[1: streams]

    #print(f'ind_stream, {ind_stream}')

    stream_data = getting_input[streams: ]

    #print(f'Stream data {stream_data}')

    return streams, ind_stream, stream_data

def calculate_babbling(streams, ind_stream, stream_data):
    ind = 0

    while True:

        if stream_data[ind] == 99:

            #print(f'{ind}')

            #print('entering split')

            result_str = split_strm(ind_stream[stream_data[ind + 1] - 1], stream_data[ind + 2])
            #print(f'result in 99 {result_str}')
            #get the result from the split_strm, use the idx value in the input and manipulate the ind_stream

            ind_stream[stream_data[ind + 1] - 1] = result_str[0]

            #insert the 1st result element at the existing stream location

            ind_stream.insert(stream_data[ind + 1], result_str[1])

            #insert the 2nd result after the existing result, that is to the left 

            ind = ind + 3

            if ind >= len(stream_data):

                break

        elif stream_data[ind] == 88:

            #print(f'{ind}')
            #print(f'len of stream {len(stream_data)}')
            #print(f'len of rivers {len(ind_stream)}')
            #print('entering join')

            #get the stream value in ind_stream array, and then add it to stream to right of it

            result_str = join_strm(ind_stream[stream_data[ind + 1] - 1], ind_stream[stream_data[ind + 1]])

            print(f"Result in join {result_str}")
            #remember to use the actual index value

            ind_stream[stream_data[ind + 1] - 1] = 0

            ind_stream[stream_data[ind + 1]] = result_str

            ind = ind + 2
            print(ind)
            if ind >= len(stream_data):

                break
    return ind_stream
    
def main():

    streams, ind_stream, stream_data = gettinput()
    print(streams, ind_stream, stream_data)

    get_result = calculate_babbling(streams, ind_stream, stream_data)
    
    for x in get_result:
        if x != 0:
            print(round(x),end=' ')

if __name__ == "__main__": main()