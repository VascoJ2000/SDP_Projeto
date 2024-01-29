import threads
import Client


if __name__ == '__main__':
    print('Welcome to Notlar \n')
    if input('Do you wish to launch client? (y/n) \n') == 'y':
        try:
            client = Client.run()
        except Exception as e:
            print('Error: ' + str(e))
    elif input('Do you wish to launch server mode? (y/n) \n') == 'y':
        bl_server = None
        dl_server = None
        while True:
            try:
                bl_servers = int(input('How many business layer servers do u wish to launch? \n'))
            except ValueError:
                print('Invalid input! Please try again.')
            else:
                break
        while True:
            try:
                dl_servers = int(input('How many data layer servers do u wish to launch? \n'))
            except ValueError:
                print('Invalid input! Please try again.')
            else:
                break
        thread_list = threads.run_thread(bl_servers, dl_servers)
