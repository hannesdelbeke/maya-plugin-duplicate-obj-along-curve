import sys
import maya.api.OpenMaya as om
import maya.cmds as cmds


MENU_NAME = "ToolsMenu"  # no spaces in names, use CamelCase
MENU_LABEL = "Tools"  # spaces are fine in labels
MENU_ENTRY_LABEL = "Duplicate obj along curve"

MENU_PARENT = "MayaWindow"  # do not change

def maya_useNewAPI():  # noqa
    pass  # dummy method to tell Maya this plugin uses Maya Python API 2.0


# =============================== Menu ===========================================
def show(*args):
    import duplicateObjAloneCurve
    w = duplicateObjAloneCurve.GUI()
    w.show()


def loadMenu():
    if not cmds.menu(f"{MENU_PARENT}|{MENU_NAME}", exists=True):
        cmds.menu(MENU_NAME, label=MENU_LABEL, parent=MENU_PARENT)
    cmds.menuItem(label=MENU_ENTRY_LABEL, command=show, parent=MENU_NAME)  


def unloadMenuItem():
    if cmds.menu(f"{MENU_PARENT}|{MENU_NAME}", exists=True):
        menu_long_name = f"{MENU_PARENT}|{MENU_NAME}"
        menu_item_long_name = f"{menu_long_name}|{MENU_ENTRY_LABEL}"
        # Check if the menu item exists; if it does, delete it
        if cmds.menuItem(menu_item_long_name, exists=True):
            cmds.deleteUI(menu_item_long_name, menuItem=True)
        # Check if the menu is now empty; if it is, delete the menu
        if not cmds.menu(menu_long_name, query=True, itemArray=True):
            cmds.deleteUI(menu_long_name, menu=True)


# =============================== Plugin (un)load ===========================================
def initializePlugin(plugin):
    loadMenu()


def uninitializePlugin(plugin):
    unloadMenuItem()
    
