# To Enable Custom Rich Presence, Please Make Sure "RPC_BOOL" is True in env file.

# Custom Rich Presence (Edit as you like.)

ENABLE_CUSTOM_RICH_PRESENCE=False

                                # ⚠ RP_Prority_Order Number should not be same for other RPs.
SHOW_RECO_RP=(True,15,2)        # (True/False, Interval=15, RP_Prority_Order=2) ⚠ Interval should not be less than 10 seconds.
SHOW_CPU_USAGE_RP= (True,15,3)  # (True/False, Interval=15, RP_Prority_Order=3) ⚠ Interval should not be less than 10 seconds.


CUSTOM_RP_ACTIVITY = ({   
                "details": "Arvinth Krishna G",             # Remove this entire line if you don't need details key.
                "state"  : "Programmer | Mechanical Engg",  # Remove this entire line if you don't need state key.
                "assets" : {                                # Remove entire "Assests" dictionary if you don't need assets key.
                       "large_text" : "GAK",
                       "large_image": "https://i.imgur.com/lsB7P1k.png",
                    },
                "buttons" : [                               # Remove entire "Buttons" list if you don't want to add buttons.
                        {"label": 'YouTube',   "url": "https://www.youtube.com/channel/UCKU73B2c4FBl8o4b1qBBPxA"}, 
                        {"label": 'Instagram', "url": "https://bit.ly/GAKinstagram" }  # Remove this entire line if you need only one button.
                    ],
                "instance": False
            }, 15,1)            # (Custom_Activity, Interval=15, RP_Prority_Order=1 ) ⚠ Interval should not be less than 10 seconds.
