## A [PopClip](http://pilotmoon.com/popclip/extensions/) extension that converts USD/GBP/EUR/JPY to CNY

###Demo

![image](doc/before.png)

![image](doc/after.png)

###How to build

* Install PopClip
* Fill up your [open exchange rates](http://openexchangerates.org/) appid (`__apikey__` in `src/settings_local.py`)
* cd to `src` folder
* execute `./test.sh` to check if have any errors
* execute `./build.sh` to build and install

###Files

	├── README.md
	├── build
	│   └── CurrencyConvert.popclipextz
	└── src
 		├── Config.plist
		├── build.sh
    	├── currency.py
    	├── settings_local.py
    	├── currency_yuan.png
    	├── latest_rates.json
    	└── test.sh
    	
###Reference
* [PopClip-Extensions](https://github.com/pilotmoon/PopClip-Extensions)
* [Open Exchangerates](https://openexchangerates.org/quick-start)
