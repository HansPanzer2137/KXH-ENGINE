import py_compile
import sys
from bib.gui.base.engine_config_editor_gui import engine_config_get, engine_run
from bib.gui.config_editor import create_config

def init_engine():
    create_config()
    engine_config_get()
    engine_run()
