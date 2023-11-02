import os
import json
import logging


class passwordStorage:
    def __init__(self, external_storage_path: str):
        # make logger
        logger = logging.getLogger('core-logger')
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        handler = logging.FileHandler(r'password_manager_log.log', encoding='utf-8')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        
        logger.info('start core')

        # check parameters
        if not isinstance(external_storage_path, str):
            raise TypeError('external_storage_path must be of the str type')
        
        self.__logger = logger
        self.__external_storage_path = external_storage_path
    
    
    def add_app(self, 
                app: str, 
                login: str, 
                password: str = None, 
                add_info: str = None
    ) -> dict:
        '''
        adding app in storage
        '''
        self.__logger.info('adding app')

        # check parameters
        if not isinstance(app, str):
            raise TypeError('app must be of the STR type')
        
        if not isinstance(login, str):
            raise TypeError('login must be of the STR type')
        
        if not isinstance(password, (str, type(None))):
            raise TypeError('password must be of the STR type')
        
        if not isinstance(add_info, (str, type(None))):
            raise TypeError('add_info must be of the STR type')
        
        # read storage
        try:
            with open(self.__external_storage_path, 'r', encoding='utf-8') as f:
                storage = json.load(f)
        except Exception as e:
            self.__logger.fatal(f'error with reading storage (add_app)\n{e}', stack_info=True)

        # adding storage
        try:
            storage[f'{app} - {login}'] = {
                "app": app,
                "login": login,
                "password": password,
                "add_info": add_info
            }
        except Exception as e:
            self.__logger.fatal(f'error with adding storage (add_app)\n{e}', stack_info=True)

        # write storage
        try:
            with open(self.__external_storage_path, 'w', encoding='utf-8') as f:
                json.dump(storage, f)
        except Exception as e:
            self.__logger.fatal(f'error with writing storage (add_app)\ncheck the availability of the storage and the json dict written in it\n{e}', stack_info=True)

        return storage[f'{app} - {login}']


    def get_storage(self) -> dict:
        '''
        get dict with storage
        '''
        try:
            with open(self.__external_storage_path, 'r', encoding='utf-8') as f:
                storage = json.load(f)
        except Exception as e:
            self.__logger.fatal(f'error with reading storage (get_storage)\n{e}', stack_info=True)
        
        return storage

password_storage = passwordStorage(r'A:\password_storage.json')
password_storage.add_app('1app', 'login', add_info='1 add info')
password_storage.add_app('2app', 'login', add_info='2 add info')
print(password_storage.get_storage())