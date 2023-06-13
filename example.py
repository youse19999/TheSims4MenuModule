import sims4.commands
import services
from uiext import Notification,Object,Image
from CheatModule import cheatmenu_module
from ui.ui_text_input import UiTextInput
from sims4.localization import TunableLocalizedString, LocalizationHelperTuning
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory
from sims4.collections import AttributeDict
from ui.ui_dialog_generic import UiDialogTextInputOkCancel
@sims4.commands.Command("startmenu",command_type=sims4.commands.CommandType.Live)
def start(_connection=None):
    sim = services.get_active_sim()
    output = sims4.commands.CheatOutput(_connection)
    rows = []
    example_icon = Image.getImagekey(Image,0x9C8538E60CD2CD26)
    #exampletab1 = cheatmenu_module(Title,Description,Icon,Rows,IsButton)
    button = cheatmenu_module("button","button",example_icon,[],True)
    
    def button_action():
        pass
    
    exampletab1 = cheatmenu_module("tab1","",example_icon,[button],False)
    exampletab2 = cheatmenu_module("tab2","",example_icon,[button],False)
    exampletab3 = cheatmenu_module("tab3","",example_icon,[button],False)
    maintab = cheatmenu_module("main","",example_icon,[exampletab1,exampletab2,exampletab3],False)
    
    button.interact = button_action

    maintab.back = None
    maintab.show()