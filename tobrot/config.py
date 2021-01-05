from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1542901091:AAHywtiz-z07C0h41joDZ3H7Wm0NdRlNm8E"
    APP_ID = 2987116
    API_HASH = "d4fe61280b4fa7b2a55fdaae35d91248"
    OWNER_ID = 779581342
    AUTH_CHANNEL = [-355683257]
    DESTINATION_FOLDER = "TorrentDownloads" #Name of your folder read readme(not id of the folder)
    #fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    # Do not delete [DRIVE] #do not delete [DRIVE] but replace remaining part
    RCLONE_CONFIG = """
[DRIVE]
type = drive
client_id = 10414513063-gcdvqv7k6n0hao82j3um7trsapr5h3bs.apps.googleusercontent.com
client_secret = 5X60BW6O7fXm7tldsR6BQYSk
scope = drive
root_folder_id =
token = {"access_token":"ya29.a0AfH6SMBkJHeZr6ihzk8f7bGNRtVmYh3J8_6VuV5k1K3zMvnRS9As89JGnrG2stU05bIfq_Yh03tq0uN0r_hCHYFXFODNmo8VbUG7u0Tq1u7_kjg_0mIm-JFsAO-aXFV2Z0xL4duqeo5xAzoG87dTsNjjdmUmCJeXpkYJA-7ZKGE","token_type":"Bearer","refresh_token":"1//0gAS30nph5HyqCgYIARAAGBASNwF-L9IrliJi4UEq1VYfrSfNaQx7u4hMcx5Pxg_7yoNguphLVL_JPaBclyRIUEKHnYXKo7YrslA","expiry":"2021-01-04T22:02:48.443414422+05:30"}
team_drive = 0AM3W78woX9DoUk9PVA
"""
