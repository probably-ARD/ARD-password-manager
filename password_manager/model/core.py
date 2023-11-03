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
        
        logger.info(f'start core\npath: {external_storage_path}')

        # check parameters
        self.__check_params(
            [external_storage_path],
            [str]
        )

        # reading storage
        try:
            with open(external_storage_path, 'r', encoding='utf-8') as f:
                storage = dict(json.load(f))
        except Exception as e:
            logger.fatal(f'error with reading storage (__init__)\n{e}', stack_info=True)
        
        self.__logger = logger
        self.__external_storage_path = external_storage_path
        self.__storage = storage


    def __save_storage(self, storage: dict) -> None:
        '''
        simple writing storage
        '''
        try:
            with open(self.__external_storage_path, 'w', encoding='utf-8') as f:
                json.dump(storage, f)
        except Exception as e:
            self.__logger.fatal(f'error with writing storge\nstorage: {storage}\n{e}', stack_info=True)


    def __check_params(self,
            params: list,
            params_types: list
    ):
        '''
        func to simple params cheking
        '''
        for i in range(len(params)):
            if not isinstance(params[i], params_types[i]):
                raise TypeError(f'{params[i]} must be of the {params_types[i]} type')


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
        self.__check_params(
            [app, login, password, add_info],
            [str, str, (str, type(None)), (str, type(None))]
        )
        
        storage = self.__storage

        # adding storage
        try:
            storage[f'{app}-{login}'] = {
                "app": app,
                "login": login,
                "password": password,
                "add_info": add_info
            }
        except Exception as e:
            self.__logger.fatal(f'error with adding storage (add_app)\n{e}', stack_info=True)

        # write storage
        self.__save_storage(storage)
        self.__storage = storage

        return storage


    def get_storage(self) -> dict:
        '''
        get dict with storage
        '''
        storage = self.__storage
        
        self.__logger.info(f'getting storage {storage}')
        return storage

    
    def edit_storage(self,
            app_name: str,
            **kwargs: str
    ) -> None:
        '''
        edit storage\n
        **kwargs: app, login, password, add_info: all str type
        '''
        # check parameter
        self.__check_params([app_name], [str])
        
        # create editing app and check kwargs with adding it in editing app
        editing_app = {'app': '', 'login': '', 'password': '', 'add_inf': ''}
        
        if 'app' in kwargs:
            self.__check_params([kwargs['app']], [str])
            editing_app['app'] = kwargs['app']
        else:
            editing_app['app'] = ''
        
        if 'login' in kwargs:
            self.__check_params([kwargs['login']], [str])
            editing_app['login'] = kwargs['login']
        else:
            editing_app['login'] = ''
        
        if 'password' in kwargs:
            self.__check_params([kwargs['password']], [str])
            editing_app['password'] = kwargs['password']
        else:
            editing_app['password'] = ''

        if 'add_info' in kwargs:
            self.__check_params([kwargs['add_info']], [str])
            editing_app['add_info'] = kwargs['add_info']
        else:
            editing_app['add_info'] = ''
                
        # reading storage
        old_storage = self.__storage

        # edited storage
        edited_app = old_storage[app_name]
        # delete old app
        old_storage.pop(app_name)

        for key, data in editing_app:
            if data != '':
                edited_app[key] = data
        
        self.add_app(
            app=edited_app['app'], 
            login=edited_app['login'],
            password=edited_app['password'],
            add_info=edited_app['add_info']
        )
        

    def del_app(self, app_name: str) -> None:
        '''
        delete app from storage
        '''
        self.__check_params([app_name], [str])
        storage = self.__storage

        storage.pop(app_name)

        self.__save_storage(storage)
