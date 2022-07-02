SERIAL_WRITE = "SERIAL_WRITE"
SERIAL_READ = "SERIAL_READ"

SERIAL_DRAW = "SERIAL_DRAW"

SERIAL_TEST = "test_serial"
CHECK_DISTANCE = "measure_dist"

ACTION_EXECUTE = "ACTION:EXECUTE"
ACTION_MOVEMENT = "ACTION:MOVEMENT"

SHUTDOWN = "SHUTDOWN"
REBOOT = "REBOOT"
LED_ON = "LED_ON"
LED_OFF = "LED_OFF"
LED_FLASH = "LED_TOGGLE"

LISTEN_STT = "LISTEN_STT"

TERMINATE = "TERMINATE"
PATROL = "PATROL"
TALK = "TALK"

TALK_SYSTEMS = "TALK_SYSTEMS"
LISTENING = "LISTENING"
STOPPED_LISTENING = "STOPPED_LISTENING"
INFERENCING_SPEECH = "INFERENCING_SPEECH"
STOPPED_INFERENCING_SPEECH = "STOPPED_INFERENCING_SPEECH"

HUMAN = "HUMAN"
OBJECT = "OBJECT"

OVERLAY_DRAW = "OVERLAY_DRAW"
IDENT_POSITIVE = "IDENT_POSITIVE"

PRI_MSN_STAND_ORD = "PRI_MSN:STAND_ORD"
SEC_MSN_STAND_ORD = "SEC_MSN:STAND_ORD"
TER_MSN_STAND_ORD = "TER_MSN:STAND_ORD"

PRIMARY = "PRIMARY"
SECONDARY = "SECONDARY"
TERTIARY = "TERTIARY"

HARDWARE_PI = "HARDWARE_PI"

ANY = [x for x in dir() if not x.startswith("__")]
