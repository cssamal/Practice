#!/usr/bin/env python3
from random import randint
from argparse import ArgumentParser


class StreamSampler:
    """Get a desired sample from a stream"""

    def __init__(self, size):
        self.size = size
        self.stream = None
        self.size_input = len(str(self.stream))

    def operate_stream(self, stream):
        """Operate on stream to get a sample output"""
        self.stream = stream
        self.sample = self.stream[0:self.size]

        for i in range(self.size+1, self.size_input):
            random_index = randint(0, i)
            if random_index < self.size:
                self.sample[random_index] = self.stream[i]
        return self.sample

    @staticmethod
    def read_in_chunks(file_object, chunk_size=1024):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data


def input_parser():
    """Generate the argparse object"""

    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('size',
                        help="The size of sample to be generated",
                        type=int)
    group.add_argument('-i', '--interactive',
                       default=False,
                       action='store_true',
                       help='For use with pipes')
    return parser


def main():
    parser = input_parser()
    args = parser.parse_args()
    stream_sampler = StreamSampler(size=args.size)

    if args.interactive:
        file_object = open('/dev/stdin', 'rb')
        stream_list = []
        try:
            for line in stream_sampler.read_in_chunks(file_object):
                stream_list.extend(line)
        except KeyboardInterrupt:
            print("Keyboard Interrupt detected")
        finally:
            output = stream_sampler.operate_stream(stream_list)
            print("The sample output is:" + str(output))


if __name__ == "__main__":
    main()

