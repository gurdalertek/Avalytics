import pytz
import json
from datetime import datetime

TokenDetails = [
    {"symbol": "WETH.e", "address": "0x49d5c2bdffac6ce2bfdb6640f4f80f226bc10bab"},
    {"symbol": "USDT.e", "address": "0xc7198437980c041c805a1edcba50c1ce5db95118"},
    {"symbol": "WAVAX.e", "address": "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7"},
    {"symbol": "UNI.e", "address": "0x8ebaf22b6f053dffeaf46f4dd9efa95d89ba8580"},
    {"symbol": "LINK.e", "address": "0x5947bb275c521040051d82396192181b413227a3"},
    {"symbol": "AAVE.e", "address": "0x63a72806098bd3d9520cc43356dd78afe5d386d9"},
    {"symbol": "1INCH.e", "address": "0xd501281565bf7789224523144fe5d98e8b28f267"},
    {"symbol": "SUSHI.e", "address": "0x37b608519f91f70f2eeb0e5ed9af4061722e4f76"},
    {"symbol": "FRAX", "address": "0xd24c2ad096400b6fbcd2ad8b24e7acbc21a1da64"},
    {"symbol": "ANY", "address": "0xb44a9b6905af7c801311e8f4e76932ee959c663c"},
    {"symbol": "FXS", "address": "0x214db107654ff987ad859f34125307783fc8e387"},
    {"symbol": "JOE", "address": "0x6e84a6216ea6dacc71ee8e6b0a5b7322eebc0fdd"},
    {"symbol": "WALBT", "address": "0x9e037de681cafa6e661e6108ed9c2bd1aa567ecd"},
    {"symbol": "SWAP.e", "address": "0xc7b5d72c836e718cda8888eaf03707faef675079"},
    {"symbol": "BIFI", "address": "0xd6070ae98b8069de6b494332d1a1a81b6179d960"},
    {"symbol": "PNG", "address": "0x60781c2586d68229fde47564546784ab3faca982"},
    {"symbol": "QI", "address": "0x8729438eb15e2c8b576fcc6aecda6a148776c0f5"},
    {"symbol": "DYP", "address": "0x961c8c0b1aad0c0b10a51fef6a867e3091bcef17"},
    {"symbol": "SNOB", "address": "0xc38f41a296a4493ff429f1238e030924a1542e50"},
    {"symbol": "XAVA", "address": "0xd1c3f94de7e5b45fa4edbba472491a9f4b166fc4"},
    {"symbol": "YAK", "address": "0x59414b3089ce2af0010e7523dea7e2b35d776ec7"},
    {"symbol": "USDC.e", "address": "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664"},
    {"symbol": "DAI.e", "address": "0xd586e7f844cea2f87f50152665bcbc2c279d8d70"},
    {"symbol": "CRA", "address": "0xa32608e873f9ddef944b24798db69d80bbb4d1ed"},
    {"symbol": "OOE", "address": "0x0ebd9537a25f56713e34c45b38f421a1e7191469"},
    {"symbol": "MIM", "address": "0x130966628846bfd36ff31a822705796e8cb8c18d"},
    {"symbol": "HCT", "address": "0x45c13620b55c35a5f539d26e88247011eb10fdbd"},
    {"symbol": "CLY", "address": "0xec3492a2508ddf4fdc0cd76f31f340b30d1793e6"},
    {"symbol": "SMRTr", "address": "0x6d923f688c7ff287dc3a5943caeefc994f97b290"},
    {"symbol": "TIME", "address": "0xb54f16fb19478766a268f172c9480f8da1a7c9c3"},
    {"symbol": "xJOE", "address": "0x57319d41f71e81f3c65f2a47ca4e001ebafd4f33"},
    {"symbol": "WBTC.e", "address": "0x50b7545627a5162f82a992c33b87adc75187b218"},
]

TraderJoePairCreatedEventABI = json.dumps({
  "anonymous": False,
  "inputs": [
    {
      "indexed": True,
      "internalType": "address",
      "name": "token0",
      "type": "address"
    },
    {
      "indexed": True,
      "internalType": "address",
      "name": "token1",
      "type": "address"
    },
    {
      "indexed": False,
      "internalType": "address",
      "name": "pair",
      "type": "address"
    },
    {
      "indexed": False,
      "internalType": "uint256",
      "name": "",
      "type": "uint256"
    }
  ],
  "name": "PairCreated",
  "type": "event"
})


def get_next_timestamp(summary_type, ts):
    if summary_type == "Token1Day":
        _ts = ts + (24 * 60 * 60)
    elif summary_type == "Token4Hour":
        _ts = ts + (4 * 60 * 60)
    else:
        _ts = ts + (1 * 60 * 60)  # One Hour
    return _ts


def adjust_timestamp(timestamp, summary_type):
    if summary_type == "Token1Day":
        _ts = int(
            datetime.fromtimestamp(timestamp)
            .replace(hour=0, minute=0, second=0, tzinfo=pytz.utc)
            .timestamp()
        )
    elif summary_type == "Token4Hour":
        _hour = datetime.utcfromtimestamp(timestamp).hour
        _new_hour = int(_hour / 4) * 4
        _ts = int(
            datetime.fromtimestamp(timestamp)
            .replace(hour=_new_hour, minute=0, second=0, tzinfo=pytz.utc)
            .timestamp()
        )
    else:
        _ts = int(
            datetime.fromtimestamp(timestamp).replace(minute=0, second=0).timestamp()
        )

    return _ts


def make_dictionary(collection, primary_key_field, secondary_key_fields):
    results = collection.find({})

    primary_dict = {}
    for item in results:
        secondary_dict = {}
        for field in secondary_key_fields:
            secondary_dict[field] = item[field]
        
        primary_dict[item[primary_key_field]] = secondary_dict
    
    return primary_dict

