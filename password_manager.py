from password_manager.model.core import passwordStorage
from password_manager.view.wins.main import mainWin


def main():
    app = mainWin()
    app.mainloop()

if __name__ == '__main__':
    main()
