# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\brian\\PycharmProjects\\specCheckWIthGui\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\brian\\PycharmProjects\\specCheckWIthGui\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\brian\\pycharmprojects\\speccheckwithgui\\venv\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\brian\\PycharmProjects\\specCheckWIthGui\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='SpecChecker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , version='C:\\Users\\brian\\PycharmProjects\\specCheckWIthGui\\target\\PyInstaller\\version_info.py', icon='C:\\Users\\brian\\PycharmProjects\\specCheckWIthGui\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='SpecChecker')
