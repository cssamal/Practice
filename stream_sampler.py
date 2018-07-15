#!/usr/bin/env python3
from random import randint
from argparse import ArgumentParser
import sys


class StreamSampler:
    """Get a desired sample from a stream"""

    def __init__(self, size):
        self.size = size
        self.sample = []
        self.stream = None
        self.size_input = len(str(self.stream))

    def operate_stream(self, stream):
        """Operate on stream to get a sample output"""
        self.stream = stream
        for i in range(0, self.size):
            self.sample.append(self.stream[i])

        for i in range(self.size+1, self.size_input):
            random_index = randint(0, i)
            if random_index < self.size:
                self.sample[random_index] = self.stream[i]
        return self.sample


def input_parser():
    """Generate the argparse object"""

    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('size',
                        help="The size of sample to be generated",
                        type=int)
    group.add_argument('-i', '--interactive',
                       default=False,
                       help='For use with pipes')
    return parser


def main():
    parser = input_parser()
    args = parser.parse_args()
    stream_sampler = StreamSampler(size=args.size)

    if args.size:
        with open("/dev/random", 'rb') as random_string:
            output = stream_sampler.operate_stream(random_string.readline())
            print("The sample output is:" + str(output))
    if args.interactive:
        output = stream_sampler.operate_stream(args.interactive)
        print("The sample output is:" + str(output))


if __name__ == "__main__":
    sys.exit(main())
