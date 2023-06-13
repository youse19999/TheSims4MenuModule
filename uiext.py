from ui.ui_dialog_notification import UiDialogNotification
from distributor.shared_messages import IconInfoData
from sims4.localization import TunableLocalizedString, LocalizationHelperTuning
import services
import sims4
from ui.ui_dialog_picker import ObjectPickerRow
from ui.ui_dialog_picker import UiObjectPicker
from interactions.utils.tunable_icon import TunableIconFactory
import sims4.commands
import services
from alarms import add_alarm, cancel_alarm
from date_and_time import TimeSpan
from sims4.directory_watcher_handler import DirectoryWatcherHandler
from ui.ui_text_input import UiTextInput
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory
from sims4.collections import AttributeDict
from ui.ui_dialog_generic import UiDialogTextInputOkCancel
class Notification:
        def show(self,sim,title,text,icon=None):
            if icon is None:
                notification = UiDialogNotification.TunableFactory().default(services.get_active_sim() or sim,
                                                    title=lambda **_: LocalizationHelperTuning.get_raw_text(title),
                                                    text=lambda **_: LocalizationHelperTuning.get_raw_text(text))
                notification.show_dialog()
            else:
                notification = UiDialogNotification.TunableFactory().default(services.get_active_sim() or sim,
                                                                             title=lambda
                                                                                 **_: LocalizationHelperTuning.get_raw_text(title),
                                                                             text=lambda
                                                                                 **_: LocalizationHelperTuning.get_raw_text(text))
            notification.show_dialog(icon_override=icon)
class Object:
        def show(self,sim,_title,_text, _min_selectable, _max_selectable,row):
            uidialog = UiObjectPicker.TunableFactory().default(services.get_active_sim() or sim,
                                                               text=lambda **_: LocalizationHelperTuning.get_raw_text(
                                                                   _text),
                                                               title=lambda **_: LocalizationHelperTuning.get_raw_text(
                                                                   _title),
                                                               min_selectable=_min_selectable,
                                                               max_selectable=_max_selectable,
                                                               picker_type=UiObjectPicker.UiObjectPickerObjectPickerType.OBJECT)
            for x in row:
                uidialog.add_row(x)
            return uidialog
        def createpickerrow(self,_name,_description,icon,tag):
            return ObjectPickerRow(name=LocalizationHelperTuning.get_raw_text(_name), icon=icon,row_description=LocalizationHelperTuning.get_raw_text(_description), tag=tag)
class Image:
        def getimage(self,instance):
            return IconInfoData(sims4.resources.Key(0x00B2D882, instance, 0))
        def getobjectimage(self,sim):
            return IconInfoData(obj_instance=sim)
        def getImagekey(self,instance):
            return sims4.resources.Key(0x00B2D882, instance, 0)
class TextInputLengthName(HasTunableSingletonFactory, AutoFactoryInit):
    __qualname__ = 'Ebimonaca_TextInputLengthName'

    def build_msg(self, dialog, msg, *additional_tokens):
        msg.max_length = 100
        msg.min_length = 1
        msg.input_too_short_tooltip = LocalizationHelperTuning.get_raw_text("You must enter at least one character!")
class TextInput:
     def show(self,title,text,default_text,IsNumberOnly,callback):
        try:
            localized_text = lambda **_: LocalizationHelperTuning.get_raw_text(text)
            localized_title = lambda **_: LocalizationHelperTuning.get_raw_text(title)
            localized_default_text = lambda **_: LocalizationHelperTuning.get_raw_text(default_text)
            localized_initial_value = lambda **_: LocalizationHelperTuning.get_raw_text(default_text)
            if IsNumberOnly == True:
                localized_restricted_characters = lambda **_: LocalizationHelperTuning.get_raw_text("1234567890")
            text_input_1 = UiTextInput(sort_order=0)
            text_input_1.default_text = localized_default_text
            text_input_1.initial_value = localized_initial_value
            text_input_1.title = None
            text_input_1.max_length = 15
            text_input_1.length_restriction = TextInputLengthName()
            text_input_1.restricted_characters = localized_restricted_characters
            text_input_1.check_profanity = IsNumberOnly
            text_input_1.height = 1
            inputs = AttributeDict({'dialog': text_input_1})
            dialog = UiDialogTextInputOkCancel.TunableFactory().default(services.get_active_sim(), text=localized_text, title=localized_title, text_inputs=inputs, is_special_dialog=True)
            dialog.add_listener(callback)
            dialog.show_dialog()
        except Exception as ex:
            pass