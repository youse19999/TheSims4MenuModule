import sims4.commands
import services
from alarms import add_alarm, cancel_alarm
from date_and_time import TimeSpan
from sims4.directory_watcher_handler import DirectoryWatcherHandler
from uiext import Notification,Object,Image

class cheatmenu_module():
    def __init__(self,name,description,icon,rows,interactive=False):
        self.menurows = rows
        self.menutitle = name
        self.menudescription = description
        self.menuicon = icon
        self.back = None
        self.menuinteractive = interactive
    #レスポンスコールバック!
    def responce(self,dialog):
        try:
            #分岐√
            for x in dialog.get_result_tags():
                if x == "___back":
                        self.back.show()
                #自分のROWをforeachでかき回す。
                for row in self.menurows:
                    #メニュータイトル
                    if row.menutitle == x:
                        if row.menuinteractive == False:
                            row.show()
                        elif row.menuinteractive == True:
                            row.interact()
                    #バックタグ用の分岐
        except Exception as ex:
            pass
    def show(self):
        #ROWSの初期化
        rows = []
        #戻る追加！
        back_icon = Image.getImagekey(Image,0x9C8538E60CD2CD26)
        #ROWをいちいち展開しますここで。
        for row in self.menurows:
            #項目用のタイプでインスタンス化したものを、アペンド
            rows.append(Object.createpickerrow(Object,row.menutitle,row.menudescription,row.menuicon,row.menutitle))
            #以前のROWの情報を添付
            row.back = self
        #バックタグ用のROW
        rows.append(Object.createpickerrow(Object,"back","back me",back_icon,"___back"))
        #表示
        Object.show(Object,services.get_active_sim(),"CheatMenu","menu",1,1,rows).show_dialog(on_response=self.responce)
    def interact(self):
        Notification.show(Notification,services.get_active_sim(),"world","None Interaction",Image.getimage(Image,0x9C8538E60CD2CD26))