import json
import logging
from random import randint
from password_manager.model.core_config import *


class passwordStorage:
    def __init__(self, external_storage_path: str):
        # make logger
        logger = logging.getLogger('core-logger')
        logger.setLevel(LOG_LVL)

        formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        handler = logging.FileHandler(LOG_PATH, encoding='utf-8')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        
        logger.info(f'start __init__')
        logger.debug(f'(__init__) params\n\tstorage path: {external_storage_path}')

        self.__logger = logger

        # check parameters
        self.__check_params(
            [external_storage_path],
            [str]
        )

        # reading storage
        try:
            with open(external_storage_path, 'r', encoding='utf-8') as f:
                storage = dict(json.load(f))
            logger.debug(f'(__init__) reading storage\n\tstorage: {storage}')
        except Exception as e:
            logger.warning(f'(__init__) Error with reading storage\n{e}', stack_info=True)
        
        self.__external_storage_path = external_storage_path
        self.__storage = storage


    def __save_storage(self) -> None:
        '''
        func to fast and simple writing storage\n
        !!! storage writing from self.__storage !!!
        '''
        self.__logger.info('start __save_storage')
        self.__logger.debug(f'(__save_storage) params\n\tstorage: {self.__storage}')
        
        try:
            with open(self.__external_storage_path, 'w', encoding='utf-8') as f:
                json.dump(self.__storage, f)
            self.__logger.debug(f'(__save_storage) writing storage DONE\n')
        except Exception as e:
            self.__logger.warning(f'(__save_storage) Error with writing storge\n{e}', stack_info=True)

    
    def __gen_password(self,
        numbs: bool = True,
        spec_symbs: bool = True,
        alph_lower: bool = True,
        alph_upper: bool = True,
        password_len: int = 12,
        add_symbs: str = None
    ) -> str:
        '''
        generate random password
        '''
        self.__logger.info('start __gen_password')
        self.__logger.debug(f'(__gen_password) params\n\tnumbs: {numbs}\n\tspec_symbs: {spec_symbs}\n\talph_lower: {alph_lower}\n\talph_upper: {alph_upper}\n\tpassword_len: {password_len}\n\tadd_symbs: {add_symbs}')
        # check parameters
        self.__check_params(
            [numbs, spec_symbs, alph_lower, alph_upper, password_len, add_symbs],
            [bool, bool, bool, bool, int, (str, type(None))]
        )
        if password_len <= 0:
            self.__logger.warning('ValueError password_len must be > 0')
            raise ValueError('password_len must be > 0')


        # generate alphabet of allowed symbols
        symbs = []
        if numbs == True:
            symbs.append('1234567890')
        
        if spec_symbs == True:
            symbs.append('!$%()?*[]^@')
        
        if alph_lower == True:
            symbs.append('abcdefghijklmnopqrstuvwxyz')
        
        if alph_upper == True:
            symbs.append('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
        if add_symbs is not None:
            symbs.append(add_symbs)

        # password generation
        password = ''
        for i in range(password_len):
            alph = randint(0, len(symbs)-1)
            alph_sym = randint(0, len(symbs[alph])-1)
            password += symbs[alph][alph_sym]
        
        self.__logger.debug(f'password generation is DONE\n\tpassword: {password}')
        return password


    def __check_params(self,
            params: list,
            params_types: list
    ) -> None:
        '''
        func to simple params cheking\n
        it must checking all others methods parameters\n
        raising TypeError if param doesn't match the stated
        '''
        self.__logger.info('start __check_params')
        self.__logger.debug(f'(__check_params)\n\tparams: {params}\n\tparams_types: {params_types}\n')
        
        for i in range(len(params)):
            if not isinstance(params[i], params_types[i]):
                raise TypeError(f'{params[i]} must be of the {params_types[i]} type')


    def add_app(self, 
                app: str, 
                login: str, 
                password: str = None, 
                add_info: str = None
    ) -> None:
        '''
        adding app in storage\n
        if the app and login is already in the storage,\n
        then they are overwritten on top of the old ones\n
        !!! ^there not checks^ !!!
        '''
        
        self.__logger.info('start add_app')
        self.__logger.debug(f'(add_app) params:\n\tapp: {app}\n\tlogin: {login}\n\tpassword: {password}\n\tadd_info: {add_info}')

        # check parameters
        self.__check_params(
            [app, login, password, add_info],
            [str, str, (str, type(None)), (str, type(None))]
        )
        
        # adding storage
        try:
            self.__storage[f'{app}-{login}'] = {
                "app": app,
                "login": login,
                "password": password,
                "add_info": add_info
            }
            self.__logger.debug(f'(add_app) adding storage DONE\n')
        except Exception as e:
            self.__logger.warning(f'(add_app) Error with adding storage\n{e}', stack_info=True)

        # write storage
        self.__save_storage()


    def get_storage(self) -> dict:
        '''
        get dict with storage
        '''
        self.__logger.info('start get_storage')
        self.__logger.debug(f'(get_storage)\n\tstorage: {self.__storage}\n')
        # dict() need to make copy storage
        return dict(self.__storage)

    
    def del_app(self, app_name: str) -> None:
        '''
        delete app from storage
        '''
        self.__logger.info('start del_app')
        self.__logger.debug(f'(del_app) params:\n\tapp_name: {app_name}')
        self.__check_params([app_name], [str])
        
        try:
            self.__storage.pop(app_name)
            self.__logger.debug(f'(del_app) deliting DONE\n')
            self.__save_storage()
        except Exception as e:
            self.__logger.warning(f'(del_app) Error with adding storage\n{e}', stack_info=True)
    
    def edit_app(self,
            app_name: str,
            **kwargs: str
    ) -> None:
        '''
        edit storage\n
        **kwargs: app: str, login: str, password: str, add_info: str
        '''
        self.__logger.info('start edit_app')
        self.__logger.debug(f'(edit_app) params:\n\tapp_name: {app_name}\n\tkwargs: {kwargs}')
        
        # check parameter
        self.__check_params([app_name], [str])
        
        # create new_app and check kwargs with adding it in new_app
        new_app = dict(APP_STRUCT)
        
        if 'app' in kwargs:
            self.__check_params([kwargs['app']], [str])
            new_app['app'] = kwargs['app']
        else:
            new_app['app'] = ''
        
        if 'login' in kwargs:
            self.__check_params([kwargs['login']], [str])
            new_app['login'] = kwargs['login']
        else:
            new_app['login'] = ''
        
        if 'password' in kwargs:
            self.__check_params([kwargs['password']], [str])
            new_app['password'] = kwargs['password']
        else:
            new_app['password'] = ''

        if 'add_info' in kwargs:
            self.__check_params([kwargs['add_info']], [str])
            new_app['add_info'] = kwargs['add_info']
        else:
            new_app['add_info'] = ''
                
        # get old app inf
        try:
            old_app = self.__storage[app_name]
            self.__logger.debug(f'(edit_app) get old_app DONE')
        except KeyError:
            self.__logger.debug(f"(edit_app) KeyError storage haven't app with {app_name} app_name", stack_info=True)
            raise KeyError(f"storage haven't app with {app_name} app_name")
        
        # get new + old app
        for key in new_app.keys():
            if new_app[key] == '':
                new_app[key] = old_app[key]
        
        # removing old app
        self.del_app(app_name)
        self.__logger.debug(f'(edit_app) removing old app DONE')
        # writing new app
        self.add_app(
            app=new_app['app'],
            login=new_app['login'],
            password=new_app['password'],
            add_info=new_app['add_info']
        )
        self.__logger.debug(f'(edit_app) writing new app DONE\n')
