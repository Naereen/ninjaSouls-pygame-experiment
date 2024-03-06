# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ( "./assets", "./assets" ),
        ( "./maps", "./maps" ),
        ( "./saves", "./saves" ),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,  # FIXME: check this parameter
)
print("Before first call to Tree(...) : a.datas =", a.datas)

# a.datas += Tree('assets', prefix='assets', typecode='DATA')
# print("After assets/ call to Tree(...) : a.datas =", a.datas)
# # a.datas += Tree('./assets', prefix='assets', typecode='DATA')
# # a.datas += Tree('assets', typecode='DATA')
# # a.datas += Tree('assets', prefix='.', typecode='DATA')
# # a.datas += Tree('./assets', typecode='DATA')
# # a.datas += Tree('./assets', prefix='.', typecode='DATA')

# a.datas += Tree('saves', prefix='saves', typecode='DATA')
# print("After saves/ call to Tree(...) : a.datas =", a.datas)
# # a.datas += Tree('./saves', prefix='saves', typecode='DATA')
# # a.datas += Tree('saves', typecode='DATA')
# # a.datas += Tree('saves', prefix='.', typecode='DATA')
# # a.datas += Tree('./saves', typecode='DATA')
# # a.datas += Tree('./saves', prefix='.', typecode='DATA')

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ninjaSouls',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
