from configparser import ConfigParser
import subprocess


def main():
    inifile = ConfigParser()
    inifile.read('settings.ini')

    mac_music_path = inifile.get('DEFAULT', 'mac_music_path')
    walkman_music_path = inifile.get('DEFAULT', 'walkman_music_path')

    subprocess.run(f'adb push {mac_music_path}/* {walkman_music_path}', shell=True)


if __name__ == '__main__':
    main()
