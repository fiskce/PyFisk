import time
from consolemenu import *
from consolemenu.items import *
import consolemenu


# COLORS START
class headercolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BackgroundDefault      = "\033[49m"
    BackgroundBlack        = "\033[40m"
    BackgroundRed          = "\033[41m"
    BackgroundGreen        = "\033[42m"
    BackgroundYellow       = "\033[43m"
    BackgroundBlue         = "\033[44m"
    BackgroundMagenta      = "\033[45m"
    BackgroundCyan         = "\033[46m"
    BackgroundLightGray    = "\033[47m"
    BackgroundDarkGray     = "\033[100m"
    BackgroundLightRed     = "\033[101m"
    BackgroundLightGreen   = "\033[102m"
    BackgroundLightYellow  = "\033[103m"
    BackgroundLightBlue    = "\033[104m"
    BackgroundLightMagenta = "\033[105m"
    BackgroundLightCyan    = "\033[106m"
    BackgroundWhite        = "\033[107m"
    HEADER2 = "\33[7m"
# COLORS END


EmptyBorderType = "disable"
    

# MENU START
menu = ConsoleMenu(f"""{headercolors.OKGREEN}
                 ██████╗ ██╗   ██╗███████╗██╗███████╗██╗  ██╗
                 ██╔══██╗╚██╗ ██╔╝██╔════╝██║██╔════╝██║ ██╔╝
                 ██████╔╝ ╚████╔╝ █████╗  ██║███████╗█████╔╝ 
                 ██╔═══╝   ╚██╔╝  ██╔══╝  ██║╚════██║██╔═██╗ 
                 ██║        ██║   ██║     ██║███████║██║  ██╗
                 ╚═╝        ╚═╝   ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                      CREATED BY @FISKCE & @BERIFFAGROUP                  {headercolors.ENDC}""",)

menu_item = MenuItem("NMAP [In Development]")

function_item = FunctionItem("RAID BOT [In Development]", input, ["Enter Discord Invite Link > "])

command_item = CommandItem("Run a custom command [In Development]",  "touch hello.txt")

raid_toolbox_menu_item = CommandItem("RaidToolBox [In Development]",  "touch RTB.py")

menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(raid_toolbox_menu_item)

menu.show(False)


