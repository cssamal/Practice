#!/usr/bin/env python3


class ModuleConnectProcess:

    def __init__(self):
        pass

    def echo(self, input_string):
        return input_string + input_string

    def reverse(self, input_string):
        return input_string[::-1]

    def noop(self, input_string):
        return input_string

    def delay(self, input_string):
        word_list = input_string.split(" ")
        if len(word_list) >= 1:
            return word_list[0]
        else:
            return None

    def process(self, input_string, module_list, module_dict):
        for module in module_list:
            if module_dict[module] == 'echo':
                input_string = module_connect_process.echo(input_string)
            elif module_dict[module] == 'reverse':
                input_string = module_connect_process.reverse(input_string)
            elif module_dict[module] == 'noop':
                input_string = module_connect_process.noop(input_string)
            elif module_dict[module] == 'delay':
                input_string = module_connect_process.delay(input_string)
        print(input_string)

    def main(self):
        print("Input provided as such:"
              "\n module <module_name> <module_operation>"
              "\n <module_operation> allowed 'echo', 'reverse', 'delay', 'noop'"
              "\n connect <module_name1> <module_name2>..."
              "\n process <input string>")
        module_list = []
        module_dict = {}
        no_of_connect = 0
        while True:
            options = input("Provide command inputs:")
            options_list = options.split(" ")
            if options_list[0] == 'module':
                if len(options_list) < 2:
                    print("Please provide in this order module <module_name> <module_operation>")
                elif options_list[2] not in ['echo', 'reverse', 'delay', 'noop']:
                    print("Module operation not supported!")
                else:
                    module_dict[options_list[1]] = options_list[2]
            elif options_list[0] == 'connect':
                if not module_dict:
                    print("Please provide module before connect")
                else:
                    no_of_connect += 1
                    for i in range(1, len(options_list)):
                        if options_list[i] in module_dict:
                            module_list.append(options_list[i])
                        else:
                            print('It seems, module name not declared')
            elif options_list[0] == 'process':
                if not module_dict:
                    print("No module present to process the input.")
                    break
                elif no_of_connect == 0 or no_of_connect > 1:
                    print("I am confused as None or more than one connect defined.")
                    break
                else:
                    input_string = " ".join(word for word in options_list[1:])
                    module_connect_process.process(input_string, module_list, module_dict)
                    break


if __name__ == '__main__':
    module_connect_process = ModuleConnectProcess()
    module_connect_process.main()

