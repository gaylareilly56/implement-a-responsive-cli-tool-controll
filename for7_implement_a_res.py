import argparse
import os
import sys

class ResponsiveCLIController:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Responsive CLI Tool Controller')
        self.parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
        self.parser.add_argument('command', choices=['start', 'stop', 'status'], help='Command to execute')
        self.args = self.parser.parse_args()

    def start(self):
        print('Starting the service...')
        # Add implementation for starting the service

    def stop(self):
        print('Stopping the service...')
        # Add implementation for stopping the service

    def status(self):
        print('Checking service status...')
        # Add implementation for checking service status

    def run(self):
        if self.args.verbose:
            print(f'Running in verbose mode')

        if self.args.command == 'start':
            self.start()
        elif self.args.command == 'stop':
            self.stop()
        elif self.args.command == 'status':
            self.status()

if __name__ == '__main__':
    controller = ResponsiveCLIController()
    controller.run()