from distutils.core import setup
import py2exe

# includes = ["encodings", "encodings.*", "sip"]#需要包含的文件，sip是 PyQt打包需要添加的
includes = ["encodings", "encodings.*"]
options = {"py2exe":
               {"compressed": 1,# 压缩文件
                 "optimize": 2,  # 优化级别，默认为 0
                "ascii": 1,  # 不自动包含 encodings 和 codecs
                "includes": includes,#需要包含的文件
                # "bundle_files": 1,#64 位的 py2exe 不要添加本句
                "zipfile" : None
}
}

setup(options=options,
      zipfile=None,
      windows=[{"script": "001.py",
                "icon_resources": [(1, "icon.ico")]
                }],
      # data_files=[("*",["#","#","#"]),]
      )
