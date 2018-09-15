# -*- mode: python -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Python36\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Python36\\Lib\\site-packages\\PyQt5\\Qt\\plugins', 'F:\\atom\\eric\\mytools\\test_tool'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='app',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False , icon='audio.ico')
