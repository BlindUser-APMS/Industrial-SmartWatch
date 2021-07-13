
import sys
from swserver.mqtt_client import main

if len(sys.argv) > 1:
    main(sys.argv[1])
else:
    main()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
