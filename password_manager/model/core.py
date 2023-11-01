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
                try:
                    storage = json.load(f)
                except Exception as e:
                    self.__logger.fatal('error with json loading storage', stack_info=True)
        except Exception as e:
            self.__logger.fatal('error with reading storage', stack_info=True)

        
        # adding storage
        storage[f'{app} - {login}'] = {
            "app": app,
            "login": login,
            "password": password,
            "add_info": add_info
        }

        # write storage
        try:
            with open(self.__external_storage_path, 'w', encoding='utf-8') as f:
                try:
                    json.dump(storage, f)
                except Exception as e:
                    self.__logger.fatal('error with json dumping storage', stack_info=True)
        except Exception as e:
            self.__logger.fatal('error with writing storage', stack_info=True)

        return storage[f'{app} - {login}']
